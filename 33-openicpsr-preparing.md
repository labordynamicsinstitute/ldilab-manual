(submitting-info-via-openicpsr)=
# Submitting deposit-related information via openICPSR 

## Decision point?

```{note}
If 

  - [`MCStatus`] contains `CA` and [`MCRecommendationV2`] = `Conditional Accept`, or
  - [`MCStatus`] contains `RR`

then proceed to [Request revisions](request-revisions).

Otherwise, if  [`MCStatus`] contains `CA` and [`MCRecommendationV2`] = `Accept` or `Accept with changes`
then proceed to [Preparing Deposit for Publication](preparing-deposit-for-publication).
```

(request-revisions)=
## Request revisions

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


```{admonition}  We call this 
the **"Request-revisions-RR" message**.

```

```
Revisions requested. Details in the full report, which you will receive via ScholarOne shortly.

> [NOTE] Starting July 1, 2021, we will start to publish replication packages as soon as all requested changes to the deposit have been made. Please process any requested changes as soon as possible.
```

4. Back in the Jira issue, transition the issue to `Done`.



(preparing-deposit-for-publication)=
## Preparing Deposit for Publication
 

### FOR ACCEPT WITH CHANGES

1. Open the issue on Jira
2. Click on the `Wait for response on openICPSR` transition to `Pending openICPSR changes`. 
  - In the pop-up, you should have all the necessary information.
     - Note: links in the pop-up window are not clickable: double-click, then use right-click to "Open in New Tab".
     - If not already done: `Replication package URL` should point to openICPSR. If not, go to the final step.
     - Make a note of the issue number (in the URL) and the `Manuscript Central identifier` again.

![Pop-up for transition to Pending openICSPR](images/jira-Wait-for-response-on-ICPSR.png)

3. On openICPSR, 
  - verify what the openICPSR `Deposit Status` is (top right corner) ![Deposit in Progress image](images/change-status-button.png).
4. On openICPSR, if `Deposit Status` = *`Deposit in Progress`*
   - start a message in the Communication log:
      - with subject line: `Please make the following changes (AEAREP-xxx)` (replace with appropriate numbers)
      - Message content: 
         - the contents of the portion of the report after "`Action Items (openICPSR)`"
         - then the following lines


```{admonition} We call this 
the **"Request-revisions-CA" message  when `Deposit in Progress`** is shown.

```
         
```
Details in the full report, which you will receive via ScholarOne shortly. Please provide your response to the items listed above via the openICPSR Project Communication log, specifying AEAREP-xxx. Other items in the report may need to be addressed via ScholarOne.

Once all changes have been made, please change the status of your deposit to "Submit to AEA".


> [NOTE] Starting July 1, 2021, we will start to publish replication packages as soon as all requested changes to the deposit have been made. Please process any requested changes as soon as possible.
```
(replace xxx with the issue number)

6. On openICPSR, if `Deposit Status` = *`Submitted`*:
  - click on `Change Status`, choose `Request revisions`
  - in the pop-up, 
    - paste the contents of the repository-specific portion of the report after "`Action Items (openICPSR)`"
    - then the following lines: 


```{admonition} We call this 
the **"Request-revisions-CA" message when `Submitted` is shown**.
```

```
Details in the full report, which you will receive via ScholarOne shortly. Please provide your response to the items listed above via the openICPSR Project Communication log, specifying AEAREP-xxx. Other items in the report may need to be addressed via ScholarOne.

> [NOTE] Starting July 1, 2021, we will start to publish replication packages as soon as all requested changes to the deposit have been made. Please process any requested changes as soon as possible.
```
(replace xxx with the issue number)
 
(submitting-info-via-openicpsr-for-accept)=
### FOR ACCEPT:

1. Open the issue on Jira
2. Click on the `Prepare for publication` transition
3. In the pop-up, you should have all the necessary information.
   - Note: links in the pop-up window are not clickable: double-click, then use right-click to "Open in New Tab".
   - If not already done: `Replication package URL` should point to openICPSR. If not, go to the final step.
   - Make a note of the issue number (in the URL) and the `Manuscript Central identifier` again.
4. On openICPSR,
   - remove any RAs from the Share list (leave anybody else who is on there!)
   - (new!) verify what the openICPSR `Deposit Status` is (top right corner) ![Deposit in Progress image](images/change-status-button.png).
5. On openICPSR, if `Deposit Status` = *`Deposit in Progress`*
   - start a message in the Communication log:
      - with subject line: `Data and Code Deposit accepted for MCNumberXXX AEAREP-xxx` (replace with appropriate numbers)
      - with body


```{admonition} We call this 
the **"Sign-off" message  when author needs to `Submit`**.
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


```{admonition} We call this 
the **"Final Sign-off" message**.
```

```
This data and code deposit is accepted.

Action items:

 - Author: no further action required
 - AEA Staff: update DOI, Vol, Iss, Year of related publication, then publish.
```

7. Back in the Jira popup, finalize by clicking `OK`. The issue will be moved to `Pending Publication`.
8. You are **not quite done** yet! 
   - You will receive an email from openICPSR.  
   - forward the email to *dataeditor-queue@aeapubs.org* , but **don't press send yet!**
   - manually add the **issue number** (AEAREP-xxx) into the subject line
   - delete anything in the body of the email before the "From:" 
   - Now send the email.
   - This will add the message to the Jira ticket.

> ICPSR does not always successfully send out a notification email for the posting of the comment. If you don't receive the email, as a last resort, simply copy and paste your ICPSR comment into the Jira ticket so that we have a record.
