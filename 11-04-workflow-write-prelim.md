
### Write Preliminary Report 

At this stage, you need to fill out the REPLICATION.md up to the "Replication steps" part. 

- There is sample language for commonly encountered problems in the [sample-language-report.md](`r config$url$templmd`sample-language-report.md), which is part of the replication package.
  - Select an appropriate tag, and copy-paste into the REPLICATION.md
- [ ] Commit this preliminary report to the Bitbucket repository.


This stage allows for earlier identification of  issues that might warrant changes to the procedure. 

- This is the stage where you might have identified that some, but not all data are not provided, and we can undertake steps there.
- You might also have concerns about the REQUIREMENTS - the code might require software that you do not know how to use, or that is not available.
- The authors might have identified computational requirements that you do not have access to, or do not have the time to run ("compute cluster with 100 nodes", "Fortran compiler").
  - You may want to identify packages that needs to be installed. To help you with this task, we provide a tool called "scan_packages.do" for STATA programs. Instruction for using this dofile is in [Appendix G](https://labordynamicsinstitute.github.io/replicability-training-curriculum/using-scan-packages-do.html).


> Commit!

```bash
git add REPLICATION.md
git commit -m "Preliminary report"
git push
```

> !! If you identify any of the elements above that prevent you from completing the issue on time, you should notify your supervisor. DO NOT ADVANCE THE TICKET!!

- Otherwise, advance the ticket to one of three options: `Verification`, `Code Review`, or `Incomplete`
  - `Verification`: at least some of the data is accessible. In order to progress to this state,
    - [ ] `Working location of data` has to be filled out
    - [ ] `Computing environment` has to be selected.
  - `Code Review`: none of the data is accessible
  - `Incomplete`: more information/action is required before you can proceed
