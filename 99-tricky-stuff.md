(tricky-stuff)=
# Technical issues

## File too big - rejection by Bitbucket

Bitbucket imposes a 100MB limit for files being pushed to the Git repo. This is similar to other Git services.

::::{admonition} Do not try to override this!
:class: warning

While in some cases, the right solution may be to use something like [Git LFS](https://support.atlassian.com/bitbucket-cloud/docs/manage-large-files-with-git-large-file-storage-lfs/), we do not need to use that here, except in very rare cases.

::::

### If the commit has not been pushed yet

Remove the file from the repository, and then "amend" the previous commit. This assumes that the immediately preceding commit is the offending one. Adjust if not.

```bash
git rm --cached path/to/VERYLARGEFILE
git commit --amend
```

### If the commit has been pushed

If the commit has been pushed, you will need to rewrite the history. This is a bit more complicated, but it can be done. The following steps will rewrite the history of the last 3 commits.

```bash
git rm --cached path/to/VERYLARGEFILE
git rebase -i HEAD~3
```

This will open an editor with the last 3 commits. Change the word `pick` to `squash` for the commits between when the large file was added, and when it was removed. Save and close the editor. You will then be prompted to edit the commit message. Save and close the editor. This will solve it on your local machine. You will then need to force push to the remote repository.

```bash
git push origin master --force
```

### File too big in history of repository

If there are various files scattered throughout the history of the repository, you will need to use a tool called `bfg-repo-cleaner`. This is a more advanced tool, and you should be careful when using it. It is not recommended to use this tool unless you are very comfortable with Git.

- [Instructions to migrate to LFS](https://support.atlassian.com/bitbucket-cloud/docs/use-bfg-to-migrate-a-repo-to-git-lfs/)

However, we do not want to migrate to LFS, rather, we want to delete the big files. See the command line option `-D` to `bfg`. 

:::{warning}

Danger! Do not proceed unless you **really** understand what you are doing!

:::

Sample session:

```bash
# In the original cloned repository for aearep-xxxx
xxxx=4406
git rm data/path/to/VERYLARGEFILE
git commit -m 'Removing big files' -a
git push
cd ..
# The "--bare" is very important here!
git clone --bare git@bitbucket.org:aeaverification/aearep-${xxxx}.git
# remove all rds files
java -jar bfg-1.14.0.jar -D "*.rds" aearep-${xxxx}.git/
# remove files based on size
java -jar bfg-1.14.0.jar --strip-blobs-bigger-than 50M aearep-${xxxx}.git/
# The report will detail what was removed
cd aearep-${xxxx}.git
git reflog expire --expire=now --all && git gc --prune=now --aggressive
git push origin master --force
```

After cleaning, if the repository size is still too big, then it may be necessary to

- delete the repository completely on Bitbucket
- create a new (empty) repository on Bitbucket
- redo `git push origin master --force` 

Sample report:

```
Cleaning
--------

Found 13 commits
Cleaning commits:       100% (13/13)
Cleaning commits completed in 90 ms.

Updating 3 Refs
---------------

	Ref                 Before     After   
	---------------------------------------
	refs/heads/master | bb7f0f55 | 6d879f82
	refs/tags/update1 | 2957723c | 644805e8
	refs/tags/update2 | dfe21158 | 95801e58

Updating references:    100% (3/3)
...Ref update completed in 17 ms.
...
	                        Before     After   
	-------------------------------------------
	First modified commit | 86b4bcc3 | 1098d6cb
	Last dirty commit     | f769cec6 | cfcaead8

Deleted files
-------------

	Filename                  Git id             
	---------------------------------------------
	aa_fc_m.rds             | f1c98be6 (56 B )   
	aa_fc_nr.rds            | 7b82b717 (63 B )   
	altmech.rds             | 9e02cdbc (2.9 KB)  
	arrests-aa-outcomes.rds | bb6b87ba (17.0 MB) 
	arrests_by_NUID.rds     | 12f4b2f2 (2.0 MB)  
	arrests_by_NUID180.rds  | 1d65d2c9 (2.5 MB)  
	base_cohorts.rds        | 03ac41c8 (80.0 KB) 
	cncomp.rds              | b1691139 (6.0 KB)  
	compare_gr.rds          | ed3a3380 (554 B )  
	error_df.rds            | 0874a70c (600.8 KB)
	extra_comps.rds         | 1bcd3f3d (299.5 KB)
	fe_list.rds             | 018ba52c (349 B )  
	fes_by_NUID.rds         | a7bd7f27 (3.7 MB)  
	fes_by_NUID180.rds      | 4cfb0bae (453.2 KB)
	full_cohorts.rds        | e44c10c3 (1.5 MB)  
	...


In total, 27 object ids were changed. Full details are logged here:
```

