## Reproducibility Checks in Codeocean

The workflow should be the same up until the verification stage, at which point you will use [Codeocean](https://codeocean.com) to run the reproducibility check. You can access Codeocean from your personal computer or on CISER.

### Create a Capsule

- First, create your own account on Codeocean using your cornell.edu email address (it's free). 
- In Codeocean, create a new capsule. Name the compute capsule as "`AEAREP-xxxx Compute Capsule for: TITLE`"
Example:

> AEAREP-1974 Compute Capsule for: Waiting to Choose: The Role of Deliberation in Intertemporal Choice

- Share your CodeOcean capsule with `dataeditor@aeapubs.org` (make sure to give `ownership` permissions).

### Environment

- Set up the environment specified by the authors. This includes software, version of that software, and any dependencies (packages). 
Example: `Stata(16) with ssc packages estout and boottest`

![Environment](images/environment.png)

### Metadata

- Add a "Tag" in the metadata with the AEAREP number, and an additional tag with the manuscript number. These tags persist, even when we rename the deposit for publication, and thus allows us to keep track of things.

### Recording the environment in Jira

In Jira,

- record the URL for the CodeOcean capsule (e.g., `https://codeocean.com/capsule/1665863/tree`) in the field `Computing URL` (`Data Info`  tab)
- record the use of CodeOcean in the `Computing Environment` field (`Data Info` tab) (use the existing word `codeocean`)
- record the `Working location of the data` as "Codeocean"





### Files and Directories

- There are only three directories in the Codeocean environment: `/data`; `/code`; `/results`.
    - All paths in the code must refer to one of these directories.
    - If the authors set their own globals, you change the globals to reflect these directories.
    - If the authors do not use globals, you should use the `config.do` (see [instructions](stata-related-procedures.html#using-config.do-in-stata)) to make the code more reproducible by setting globals in the `config.do` and amending the paths in the authors' code. Example:
    `use "D:\Dropbox\Data for paper\x.dta"` becomes `use "$data/x.dta"`.
    - Modify the standard `config.do` as follows:
    ```{stata,eval=FALSE}
    local scenario "A"                      // line 35
    global logdir "${rootdir}/results/logs" // line 59
    // .... go to the very end 
    global data    "${rootdir}/data
    global results "${rootdir}/results
    ```
    Occasionally, other changes are also necessary, for instance, creating new directories.


- Upload the code  to the `/code` and the data files to the `/data` directories in Codeocean.

- Define the default `run` file using the right-click menu for the main do file. This will create a new file (called `run`) which is a Bash script that CodeOcean uses to run all of the other code. 

    ![run](images/run_file.png)

- Which file to use for the automatic creation of the `run` file depends on your manuscript:
    - If the manuscript has a single master file (e.g., `master.do`), use that. The `run` file will then look like 
    ```
    #!/usr/bin/env bash
    set -ex

    ## This is the master script for the capsule. When you click "Reproducible Run", the code in this file will execute.
    stata-mp -q do master.do "$@"
    ``` 
    - If the authors provide instructions on a specific order in which to individually execute programs, each program will need to be added to the "run" file in that order. In this case, you should be including the `config.do` at the top of each program instead of only the `Master.do`. 
    ```
    #!/usr/bin/env bash
    set -ex

    ## This is the master script for the capsule. When you click "Reproducible Run", the code in this file will execute.
    stata-mp -q do 01_step1.do "$@"
    stata-mp -q do 02_step2.do "$@"
    stata-mp -q do 03_step3.do "$@"
    stata-mp -q do 04_step4.do "$@"
    ``` 

### Log files

- Any code that generates logfiles (this includes the `config.do`) needs to be amended to write to the `results` directory (i.e. `global logdir "${rootdir}/results"`). 
- Note that CodeOcean automatically generates a capture of all screen output in a file called "`output`" in the `results` directory. In many cases, this will be sufficient.

### Output

- Nothing is captured unless it is *explicitly* exported to the `/results` directory.
    - For example, you will not see any graphics files saved by the code unless they are saved as something such as `${results}/figure1.gph`. 
    - You may not need to do this for intermediate data files. The program(s) should still run as long as the files are successfully created.
    - All tables and figures need to be adjusted to write to "`${results}`". The best way is to use a global (yet again defined in the `config.do`), e.g. `graph export "${results}/figure1.pdf"`.

### Notes

- Note that some features will not work on CodeOcean if they rely on graphical windows (see LINK TO CODEOCEAN SITE)
  - A particular feature missing from Stata 16.0 on CodeOcean is the ability to write PNG graphics. Write PDF instead.

### Recording edits 

- Once you have finished editing and running the code in Codeocean, you should download the edited code and commit it to the repository. The best way to do this is similar to the [steps taken during a revision](/replicability-training-curriculum/aea-revision-reports-after-author-resubmission.html):
  - Delete, by hand (**NOT** git rm), the code files as you downloaded them onto your workspace. 
  - Then, place the amended codes into that same directory. 
  - Git `add, commit, push`. 
  - We should then be able to identify the changes you made to the code in order to run it on Codeocean. See further guidance [here](/replicability-training-curriculum/aea-revision-reports-after-author-resubmission.html).

#### Expert tip

Instead of manually downloading CodeOcean results, in a (git) bash shell on your laptop or CISER, cd to the base directory of the reproducibility check (e.g., "aearep-xxxxx"), and run

```
tools/sync-codeocean.sh nnnnn
```

where `nnnnn` is the numerical capsule identifier from the CodeOcean URL: `https://codeocean.com/capsule/` **nnnnnn** `/tree`. You will be asked to authenticate using your CodeOcean (not Bitbucket!) login and password!

This will create two directories in your workspace: `codeocean-nnnnn-live` and `codeocean-nnnn`. The former will be "ignored", but the latter will be refreshed each time you run the `sync-codeocean.sh` command, and will be committed to the Bitbucket repository. This is a convenient way to synchronize the two.

Don't forget to `git add; git commit; git push` afterwards. This command can be run multiple times, as changes are made on CodeOcean.

### Recording results

- Download the `/results` directory as a ZIP file. Remember the "run" number from the CodeOcean interface (e.g. "Run 1234567").
- If not already present, create a "results" directory in the `codeocean-nnnnn` directory. 
- Create a directory for each run with the "run" number. 
- Unzip the ZIP file you just downloaded into the numerical directory you just created.

This should look like this:

```
aearep-1234/
    codeocean-nnnnn/
        code/
        metadata/
        results/
            2931206/
                output
                logfile_20220201-1201-root.log
                figure1.pdf
```

- Don't forget to add all results from the "results" directory, `git add; git commit; git push`.



