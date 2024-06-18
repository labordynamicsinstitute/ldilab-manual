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


```bash