# AEA: Monitoring Pending openICPSR Changes

## Background

Many cases which the Lab reviews receive a recommendation ([`MCRecommendationV2`] on Jira) of `Accept - with Changes.` What this means is that the changes which are requested do not constitute a complete revision from the authors. Instead of re-submitting a complete revision for review by the Lab, the authors will make any necessary changes to the deposit directly on ICPSR. Separately, any changes to the manuscript/appendix will be made at the copyediting stage by the editorial office, without further interaction with the Lab.

It is important to understand how the submission process works once the final report has been approved. The RAs responsible for this process are following the instructions in [Chapter 13](aea-interfacing-with-the-journal-management-system.html). If you are not yourself involved in that process, please review those instructions. Briefly, cases that are designated as `Accept - with Changes` will have the reproducibility report submitted to ScholarOne (aka Manuscript Central (MC)), the Jira ticket will be moved into status `Pending openICPSR changes`, and the ICPSR deposit will have been unlocked so that the authors can make changes, with comments to that extent in the "Project Communication Log." 

![partial process](images/pending_openicpsr.png)

The openICPSR deposit is subsequently regularly monitored. Authors may contact the Data Editor as well. When it is clear that edits have been made to the deposit, the Jira issue is moved to `Assess openICPSR changes`. The Data Editor then needs to verify that all of the `[REQUIRED]` tags have been completed. The RA conducting that check can review the required changes both in the full report on Bitbucket and in the Project Communication Log in ICPSR. 

The evaluation process usually does **NOT** require running any code. In most cases, these are minor changes, such as adding software dependencies or data access instructions to the README. Some cases will involve minor debugging issues, for which the Lab  only checks to see that edits to the code have been made as identified in the report. Unless specifically instructed to do so by the Data Editor, no code needs to be run.

## Process

As RA tasked with this, these are the instructions.

### Verifying if changes have been made

- A good place to start in this process is to go to the openICPSR deposit (fields [`Code Provenance`] or [`openICPSR alternate URL`]) 
- First, verify the data of the last request made to the author, in the "Project Communication Log" area. The Project Communication log always contains our request to the authors, and may contain subsequent responses from the author.

![Communication Log area](images/pending_openicpsr_com.png)

- Now open the project log:  click "View Log" under "Share Project" and "Change Owner." 

![Project log](images/pending_openicpsr_logbutton.png)

- This log will tell you all the changes that have been made to the deposit and when. From here we can tell whether or not the authors have made any changes since we originally requested the revisions. 
- Additionally, this is a great resource for checking which program files the authors have made changes to. 

### If changes have been made

Once you have ascertained that changes have been made, move the Jira ticket to `Assess openICPSR changes`. 

![partial process](images/pending_openicpsr.png)


### Verify Requested Changes

You should now open the report, and verify the changes made by the author. How to do this will vary. In some cases, you may be able to simply inspect the deposit, in others, you may need to download the deposit again, and verify the changes made, as you might do for a full revision (see [Revision Reports](aea-revision-reports-after-author-resubmission.html)).

- Open the report. You can do this by checking out the Bitbucket repo, or by clicking on the [`Report URL`] field.
  - Check the "Summary" (at the top), as well as the "Reason for incomplete reproducibility" (at the bottom, and in the Jira issue)
- Verify the changes.
- For each change, you should make a note of what problem was addressed. For instance, if the "Reason for incomplete reproducibiliy" notes that the code contained fixable bugs, and the authors have made the changes noted in the report, then you will want to  uncheck the box "Bugs in code"
  - You can find the "Reasons for incomplete reproducibility" in the "Repl.info" tab in the Jira ticket, or in the popup when moving from `Assess openICPSR changes` to `Pending publication` at the end of this process.
- If you have verified that all the required changes have been made, move forward with the acceptance process, by moving the issue to `Pending publication` (see [**Chapter 13.5.2**](aea-interfacing-with-the-journal-management-system.html#for-accept)).
  - You have another opportunity to uncheck any boxes here that have been addressed.
  - Check under "Other links" if "Non-compliant"  = yes, if so, **do not proceed** until you find clarification
  - - See if the reason for non-compliance (usually mentioned in the report, and at least in the comments) is resolved, then uncheck that box.




### Insufficient Changes

- If, in your review, you find that not all changes have been made, or it is unclear whether or not certain changes are acceptable/sufficient, please reach out to the Data Editor with a comment on the Jira ticket outlining your question. 
- These cases are not always cut and dry, please err on the side of caution and ask questions before posting a "final acceptance" message on the deposit.

### No Changes

- If no changes have been made to the deposit **four weeks** after requesting revisions, start a message in the Communication log:

    - with subject line: `AEAREP-xxx Data and Code Deposit Revisions Reminder` (replace with appropriate numbers)
    - with body
```{block, type="bbox"}
Authors,

Please make the revisions requested to the ICPSR deposit so that we may
move forward with publication of the deposit.

See our previous comment above and our full report for details. 
Feel free to contact us directly at dataeditor@aeapubs.org with any questions.


> [NOTE] Starting July 1, 2021, we will start to publish replication 
packages as soon as all requested changes to the deposit have been made. 
Please process any requested changes as soon as possible.

Thanks!
```
- Make a note in the Jira ticket that such a message has been posted.
- If after an additional **four weeks** still no changes have been made, make a note in the Jira ticket, tagging/ alerting the Data Editor.

## Notes

- **A note on [SUGGESTED] items**. We, of course, attempt to get authors to make their deposit as reproducible as possible. Which means suggesting improvements such as creating a `master.do` or including code to automatically export results. However, they are only suggestions. In other words, they do not impede reproducibility and thus we do not require that the authors make those changes. If the only changes not made to the deposit were [SUGGESTED], move forward with acceptance. 

- **A note on deposit status**. When an ICPSR deposit has a status of "Submitted" it is locked. This means that the authors will not be able to make any changes. If the deposit status is "Deposit in Progress" or "Revisions Requested" the deposit unlocked and changes may be made. Review the submission instructions above for information on how to unlock a deposit. 

- When authors ask if they need to re-submit the updated manuscript to ScholarOne/Manuscript Central. Paste the following within the acceptance (or reminder) post on ICPSR:

```{block, type="bbox"}
At this stage, any changes to the manuscript are handled directly with editorial office â another submission to Scholar One is not necessary. If you are not already in contact with the editorial office, please reach out to the managing editors via aejaccept@aeapubs.org or aeraccept@aeapubs.org.
```
