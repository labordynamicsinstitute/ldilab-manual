# Submitting to the JMS and openICPSR

:::{tip}
Reminder: for the AEA, the JMS is ScholarOne.
:::

## Submitting to JMS

1. Open the issue on JIRA. It must be `Approved`.
2. Click on the `Submit to MC` transition. A pop-up will be shown.

![Submit to MC pop-up](images/jira-Submit-to-MC.png)

3. In the pop-up, you should have all the necessary information
   - Note: links in the pop-up window are not clickable: double-click, then use right-click to `Open in New Tab`
   - `MCEntryURL`  has the link to Manuscript Central (MC) in order to submit
   - `Manuscript Central Identifier` to find the manuscript
   - Field [`MCRecommendationV2`] has the information about how the editorial office should proceed, to be selected in the JMS
      - In cases where `MCStatus` contains `RR`, the information will be in field [`MCRecommendation`]
   - Field [`Git working location`] has the information to clone the repository (and thus be able to access the report)
4. If necessary, clone the Bitbucket repository associated with the issue. You should find a `REPLICATION.pdf` there.

:::{admonition} If there is no `REPLICATION.pdf`...
... then the Approver probably forgot to create it. Contact the Approver to avoid any misunderstandings.
:::

6. Open the Manuscript Central link `MCEntryURL` (double-click, right-click, open in new tab)
   1. Enter your credentials to access Manuscript Central (let LastPass fill the information)
   2. Click on the review tab and identify the manuscript number (`Manuscript Central Identifier`) of the paper
   3. Select `Continue Review`
   4. Always click `Yes` when asked: Would you be willing to review a revision of this manuscript?
   5. Select the recommendation as noted in the Issue
      - If `MCStatus` contains `CA`: Look at the field [`MCRecommendationV2`]
      - If `MCStatus` contains `RR`: Look at the field [`MCRecommendation`]
   6. Copy-paste the "Summary" part from `REPLICATION.md` into the field `Comments to the Author`. 
   7. Select and upload the `REPLICATION.pdf`, click on `For author and  editor`.
   8. In some cases, the Data Editor will have put a note in the issue with a "for Editor only" file. The contents of that file should be copied and pasted into the field `Confidential Comments to the Coeditor`.
   8. Re-verify all information
   9. Click on `Submit`
7. Back in the pop-up, 
   1. Click on `Submit to MC`


## Processing openICPSR deposit after JMS

If 

  - [`MCStatus`] contains `CA` and [`MCRecommendationV2`] = `Conditional Accept`, or
  - [`MCStatus`] contains `RR`

then proceed to [Request revisions](request-revisions-jira).

Otherwise, if  [`MCStatus`] contains `CA` and [`MCRecommendationV2`] = `Accept` or `Accept with changes`
then proceed to [Preparing Deposit for Publication](preparing-deposit-for-publication-jira).

(request-revisions-jira)=
### Request revisions

In principle, once the report is uploaded, the author will get the report with the requested revisions via ScholarOne. However, under the post-August 2020 workflow on openICPSR, the project may need to be unlocked for the author to make changes.
To do so, proceed as follows:

1. Open the issue on Jira
2. Right-click on the [`Replication package URL`] field to open the openICPSR deposit.
3. On openICPSR, 
   - verify what the openICPSR `Deposit Status` is (top right corner) ![Deposit in Progress image](images/change-status-button.png).
   - if  `Deposit Status` = *`Deposit in Progress`*, you are done on openICPSR. Go back to the Jira issue
   - if `Deposit Status` = *`Submitted`*, then
      - click on `Change Status`, choose `Request revisions`
  - in the pop-up, paste and submit the following lines: 


```{admonition} We call this the
"Request-revisions-RR" message.
```

Use this template if the paper is in [`RR`] :

```
Revisions requested. Details in the full report, which you will receive via ScholarOne
or from the editor in charge of the paper.

> [NOTE] We may publish replication packages as soon as all requested changes
to the deposit have been made. Please process any requested changes as soon
as possible.
```

Use this template if the paper is in [`CA`] :

```
Revisions requested. Details in the full report, which you will receive via ScholarOne
in a few business days.

> [NOTE] We may publish replication packages as soon as all requested changes
to the deposit have been made. Please process any requested changes as soon
as possible.
```

4. Back in the Jira issue, transition the issue to `Done`.



(preparing-deposit-for-publication-jira)=
### Preparing Deposit for Publication
 

#### FOR ACCEPT WITH CHANGES

1. Open the issue on Jira
2. Click on the `Wait for response on openICPSR` transition to `Pending openICPSR changes`. 
  - In the pop-up, you should have all the necessary information.
     - Note: links in the pop-up window are not clickable: double-click, then use right-click to "Open in New Tab".
     - If not already done: `Code provenance` should point to openICPSR. If not, go to the final step.
     - Make a note of the issue number (in the URL) and the `Manuscript Central identifier` again.

![Pop-up for transition to Pending openICSPR](images/jira-Wait-for-response-on-ICPSR.png)

3. On openICPSR, 
  - verify what the openICPSR `Deposit Status` is (top right corner) ![Deposit in Progress image](images/change-status-button.png).
4. On openICPSR, if `Deposit Status` = *`Deposit in Progress`*
   - start a message in the Communication log:
      - with subject line: `Please make the following changes (AEAREP-xxx)` (replace with appropriate numbers)
      - Message content: 
         - the contents of the portion of the report after "`Action Items (openICPSR)`", but ONLY the action items.
         - then the following lines


```{admonition} We call this the
"Request-revisions-CA" message when `Deposit in Progress` is shown.
```
         
```
Details in the full report, which you will receive via ScholarOne in a
few business days. Please provide your response to the items listed above
via the openICPSR Project Communication log, specifying AEAREP-xxx.
Other items in the report may need to be addressed via ScholarOne.

Once all changes have been made, please change the status of your deposit
to "Submit to AEA".


> [NOTE] We may publish replication packages as soon as all requested changes
to the deposit have been made. Please process any requested changes as soon
as possible.
```
(replace xxx with the issue number)

6. On openICPSR, if `Deposit Status` = *`Submitted`*:
  - click on `Change Status`, choose `Request revisions`
  - in the pop-up, 
    - paste the contents of the repository-specific portion of the report after "`Action Items (openICPSR)`", but ONLY the action items.
    - then the following lines: 


```{admonition} We call this the
"Request-revisions-CA" message when `Submitted` is shown.
```

```
Details in the full report, which you will receive via ScholarOne in a
few business days. Please provide your response to the items listed above
via the openICPSR Project Communication log, specifying AEAREP-xxx.
Other items in the report may need to be addressed via ScholarOne.

Once all changes have been made, please change the status of your deposit
to "Submit to AEA".


> [NOTE] We may publish replication packages as soon as all requested changes
to the deposit have been made. Please process any requested changes as soon
as possible.
```
(replace xxx with the issue number)
 

#### FOR ACCEPT:

1. Open the issue on Jira
2. Click on the `Prepare for publication` transition
3. In the pop-up, you should have all the necessary information.
   - Note: links in the pop-up window are not clickable: double-click, then use right-click to "Open in New Tab".
   - If not already done: `Code provenance` should point to openICPSR. If not, go to the final step.
   - Make a note of the issue number (in the URL) and the `Manuscript Central identifier` again.
4. On openICPSR,
   - remove any RAs from the Share list (leave anybody else who is on there!)
   - (new!) verify what the openICPSR `Deposit Status` is (top right corner) ![Deposit in Progress image](images/change-status-button.png).
5. On openICPSR, if `Deposit Status` = *`Deposit in Progress`*
   - start a message in the Communication log:
      - with subject line: `Data and Code Deposit accepted for MCNumberXXX AEAREP-xxx` (replace with appropriate numbers)
      - with body


```{admonition} We call this the
"Sign-off" message when author needs to `Submit`.
```
      
```
This data and code deposit is accepted.

Action items:

 - Author: Please change the status of your deposit to "Submit to AEA"
 - AEA Staff: update DOI, Vol, Iss, Year of related publication, then publish.
```

6. On openICPSR, if `Deposit Status` = *`Submitted`*:
  - start a message in the Communication log:
      - with subject line: `Data and Code Deposit accepted for MCNumberXXX AEAREP-xxx` (replace with appropriate numbers)
      - with body


```{admonition} We call this the
"Sign-off" message when author has `Submit`ted.
```

```
This data and code deposit is accepted.

Action items:

 - Author: no further action required
 - AEA Staff: update DOI, Vol, Iss, Year of related publication, then publish.
```

7. Back in the Jira popup, finalize by clicking `OK`. The issue will be moved to `Pending Publication`.

:::{note}

You will receive an email from openICPSR. This email should also have gone to *dataeditor@aeapubs.org*. Verify that it is the case. If yes, you're all done. If not, contact the Data Editor.

:::
