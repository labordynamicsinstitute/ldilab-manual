# AEA: Revision reports after author resubmission

Some pre-publication reproducibility checks require revisions from the authors. We will try to assign these revisions to the replicator for the original submission whenever possible.

## Generic Guidance 

- Most revisions will not take you much time, so please try to process them quickly!
- Revisions do not require you to repeat all of the same steps as the original replication (see below).
- **Do not create a new Bitbucket repo**. You will overwrite the original repo (the original contents will still be available -- this is why we use version control software like Bitbucket!)
- The original REPLICATION.md is a contract; if the authors fix what we ask them to fix, then they have completed their part of the agreement.
    - If new issues turn up as a result of additional materials provided, these are okay to include as [REQUIRED] changes in the revised report. 
    - If you are unsure about something, add it to the report. While reviewing your report, we can make a determination about whether or not it can be done after acceptance of the manuscript, be a suggested instead of required change, etc. 

- In particular, **do NOT create "update" or "new" directories** The current state of the repository should always correspond to the author's structure. Overwrite files, delete files. The previous state is preserved in Git. This will also tell you what files have changed.
- Please be sure to have the committed "REPLICATION.md" be accurate when you commit it - do not let it contain holdover data from a previous replication attempt, as this can lead to confusion.



## Writing the Revision Report 

Please be clear when writing the revision report. The report should make sense without having to refer to the previous report. 

- The body of the report should reflect the current status of the deposit. 
    - Example: if authors were missing a setup program before and now provide it, the `Code Description` section of the REPLICATION.md should be updated to reflect the inclusion of this program. 
- Replace all [REQUIRED] and [SUGGESTED] items with [We REQUESTED] and [We SUGGESTED], respectively. 
    - Note: in the summary, these tags are using bullets (`- [REQUIRED]`) - those should be changed to "quotes": `> [We REQUESTED]`
- Below each such tag, add a bullet point. Start the paragraph with "Done" if the issue was resolved, or "Not done" if not. Then explain what was done. 

An example: 

    > [REQUIRED] Please add a setup program that installs all packages as noted above. Please specify all necessary commands. An example of a setup file can be found at [https://github.com/gslab-econ/template/blob/master/config/config_stata.do](https://github.com/gslab-econ/template/blob/master/config/config_stata.do)

becomes 

    > [We REQUESTED] Please add a setup program that installs all packages as noted above. Please specify all necessary commands. An example of a setup file can be found at [https://github.com/gslab-econ/template/blob/master/config/config_stata.do](https://github.com/gslab-econ/template/blob/master/config/config_stata.do)

    - Done. A setup program has been added to the deposit, which installs all necessary packages. 

 

## Revision Workflow 

You should proceed through the [workflow](/replicability-training-curriculum/aea-jira-workflow-a-guide.html) as you would for an original case with some exceptions:

- You **should not** create a new Bitbucket repository. 
- You do not need to fill out a new Data Citation and Information Report.
- You _may_ not need to re-run any code.  
- All sections are potentially subject to updates, so pay attention.

### In Progress 

First, advance the ticket from `Assigned` to `In Progress`. 

- [ ] Identify previous issue. 
    - You should see the previous issue listed under **Linked Issues** on JIRA. 
    - Use the previous issue, to fill in the following JIRA fields (if not already filled): 
        - `Code provenance` 
        - `Journal` 
        - `Empirical Article`
        - `Bitbucket short name`. This should be the name of the original JIRA issue (e.g. `aearep-123)`.
        - `openICPSR project number`

        

- [ ] Download the materials attached to the JIRA issue. This will typically include 
  - an updated copy of the manuscript, 
  - a response to the editor addressing the requested changes from the prior replication attempt. 
  
- [ ] Remove obsolete files. In the root, this should be obvious (old manuscript), in the copy of the code, a bit trickier, but necessary.

- [ ] Add these to the root of the repository locally, and then `git add`, `git commit`, and `git push` them to the Bitbucket repository (e.g., `git add PDF_Proof.pdf readme.pdf reply_to_editor.pdf`)
  - The root of the repository should contain only our files (i.e., REPLICATION.md, etc.) and the manuscript files (main manuscript, any online appendices and README files provided through the JIRA ticket). Example:

```
code-check.xlsx
config.do
PDF_Proof.PDF
PII_stata_scan.do
readme.pdf
REPLICATION.md
reply_to_editor.pdf
```
  

- [ ] Open `REPLICATION.md` to review the requested changes from the prior replication attempt. Read the reply to the editor, if provided, to get a sense of what changes the authors made. Make a determination if the revision requires re-running code. 
    - If there were [REQUIRED] changes in the Code Description, Replication Steps, or Findings sections of the original report, you will likely have to re-run code. 
    - If the only [REQUIRED] changes were data citations or changes to the README, you should not need to re-run code. 


Change the status from `In Progress` to `Code`. 

### Code 

At this point, you may want to transition to CISER if you haven't already. You should `git pull` to ensure the changes you've made are reflected in the local version of the repository on CISER.  

- [ ] Download the updated openICPSR deposit and commit the materials to the **same Bitbucket repo as the original replication**, in the **same directory** (i.e., if the openICPSR deposit is `12345` then all updated materials will again go into the `12345` subdirectory. 
    - Example: if AEAREP-250 is a revision of AEAREP-123, then download the entire openICPSR deposit and commit it to the `aearep-123` repo on Bitbucket.
    - Overwrite any files, if requested. Pay attention to files that might have been deleted (you will have to `git rm` them). 
    - There are tricks to letting Git do much of the work: **Follow the detailed instructions for the process of updating the replication materials** in the [Appendix: Updating Replication Materials after Revision](/replicability-training-curriculum/updating-replication-materials-after-revisions.html).

- [ ] Update the Data Description section of the report.  
   
- [ ] Update the Code Description section of the report. 

- [ ] Fill out the required JIRA fields: 
    - `Data Provenance` 

Change the status from `Code` to `Data`. 

### Data 

- [ ] Update the Data Checks section of the report, if new data have been provided. 

- Fill out the required fields in JIRA:    
    - `Working location of the data` or
    - `Reason for non-accessibility` 

Change the status from `Data` to `Write Preliminary Report`. 

### Write Preliminary report

- [ ] Ensure all sections of the report up to Replication Steps have been updated. 

- [ ] Delete sections of the report. 


Change the status from `Writing preliminary report` to `Code Review` or `Verification`. 

### Code Review or Verification 

If you have previously determined that code needs to be re-run, you should select the  `Verification` stage. 

If you have determined that code does not need to be re-run (or code is unable to be run due to lack of data), select the `Code Review` option. 

#### Re-running code 

- You **do not** need to re-verify tables/figures that were successfully replicated the first time *unless* the new code also affects them. 
- If parts of the code take a long time to run and the [REQUIRED] changes do not involve those parts, you do not need to re-run that part of the code. 
- **Be careful!** Sometimes the code will produce intermediate outputs along the way that may be needed later on. So if you skip parts of the code and cannot replicate the result(s), go back and check to see if you actually need to run all of the code.

- [ ] Run relevant parts of code, including the config.do generating system. 

- [ ] Update the Replication Steps section of the report, accordingly. 

- [ ] Update the `code-check.xlsx` file. 

- [ ] Update the Findings section of the report. 

- [ ] `git add`, `git commit`, and `git push` any new results to the Bitbucket repository. 

Change the status from `Code Review` or `Verification` to `Writing Report`. 

### Writing Report 

In this stage, you will finalize the revision report. 

- [ ] Ensure all `[REQUIRED]` and `[SUGGESTED]` items from the original report have been changed to `[We REQUESTED]` and `[We SUGGESTED]` in the body of the report. 
    - The resolution (or lack thereof) should be included as a bullet point directly below the request. 
    - If using the scripts, you can use the `[aearevision](https://github.com/AEADataEditor/editor-scripts)` to change all the tags
    - If the resolution is incomplete (`Not done`  or `Partially done`), then repeat the usual `> [REQUIRED]` tag, as this will become an action item.

- [ ] Ensure any new issues found are tagged with the appropriate `> [REQUIRED]` and `> [SUGGESTED]` tags. 

- [ ] Delete/modify any comments of the report template that are no longer true:
    - e.g. if the previous report stated "Data not cited" and the author has now added citations, then that part should state "Data is cited" or "Data is now cited".

- [ ] Delete any parts of the report template that are no longer relevant:
    - e.g. if no code changes were `[REQUIRED]`, then delete the sections involving code, replication steps, and findings. 
    - careful however here, too: authors should only be making changes to parts that we requested changes for, but if they change things elsewhere, then you should, in fact, retain that section, and accurately describe it again. New errors *can* be introduced!

- [ ] Update the Classification. 
    - If you do not need to re-run code for the revision, keep the original classification.
    - If you do need to re-run code for the revision, update the classification appropriately.


- [ ] Incorporate all old/new requested changes and resolutions in the SUMMARY section of the report: 

    - Create a new sub-section `### Previously` and collect the **Unresolved**, and **Resolved** issues. 
      - Leave the existing `### Action Items (manuscript)` and `### Action Items (openICPSR)` sections!
    - Collect all the `> [We REQUESTED]` and `> [We SUGGESTED]` items from the rest of the report (this should correspond to the previous - [REQUIRED]` and `- [SUGGESTED]` items)
      - These should go under the `### Previously` section, appropriately classified.
      - Below each item, include the same resolution you listed in the body of the report. 
    - New and any unresolved issues should be collected with their `- [REQUIRED]` and `- [SUGGESTED]` tags under the `### Action Items` sections. 
      - If using the scripts, you can use the `[aeareq](https://github.com/AEADataEditor/editor-scripts)` as usual.
    

## An example

In the example below, the revision found bugs in the code that were not previously present (a **new action item**), and identified the continued lack of data citations (an **unresolved** action item). A setup program that was requested was provided by the authors, and is thus **resolved**.

```
SUMMARY
-------

### Action Items (openICPSR)

- [REQUIRED] Please provide debugged code, addressing the issues identified in 
  this report.
- [REQUIRED] Please add data citations to the article. 
  Guidance on how to cite data is provided in the 
  [AEA Sample References](https://www.aeaweb.org/journals/policies/sample-references) 
  and in [additional guidance](https://social-science-data-editors.github.io/guidance/addtl-data-citation-guidance.html#confidential-databases).

### Previously

#### Unresolved 

> [We REQUESTED] Please add data citations to the article. 
  Guidance on how to cite data is provided in the 
  [AEA Sample References](https://www.aeaweb.org/journals/policies/sample-references) 
  and in [additional guidance](https://social-science-data-editors.github.io/guidance/addtl-data-citation-guidance.html#confidential-databases).

- Not done. Please add data citations to the manuscript for the 
  following data sources: data source 1, data source 2. 

#### Resolved 

> [We REQUESTED] Please add a setup program that installs all 
  packages as noted above. Please specify all necessary commands. 
  An example of a setup file can be found at 
  [https://github.com/gslab-econ/template/blob/master/config/config_stata.do](https://github.com/gslab-econ/template/blob/master/config/config_stata.do)

- Done. A setup program has been added to the deposit, which 
  installs all necessary packages.
```





Finally, don't forget to `git add`, `git commit`, and `git push` the new report. Then, change the status in JIRA from `Writing Report` to `Report Under Review`.  
