# Request for External Reproducibility Check (general)

When we ask an external entity (person or institution) to verify reproduciblity, we initiate the process with an email, and follow the process with several tags within Jira.

## Jira stuff

### Create a new subtask 

- Type `Verify code and data` with title "External reproducibility check for (AEAREP-xxxx)"
- In the tab `External validation`, select `Yes` for `External validation` and choose or add `External party name` (try to remain consistent with existing entries).
- The subtask has status "open", "in progress", and "done". 
- Choose as `Assignee` the person who will follow the progress.

Back in the main issue,

- Duplicate the information in the tab `External validation`, select `Yes` for `External validation` and choose or add `External party name` (try to remain consistent with existing entries).

The main issue can 

- go from `Open` to `Waiting for external report`, which should be chosen when no preliminary report is or will be created (rare)
- go through the normal process up to `Write preliminary report`, and then can only go to `Waiting for external report` if the `External validation` field `=Yes`.

Now send the email.

## Email template

```

Dear [replicator],

I would like to ask if you are able to review a manuscript for us. [Brief description - 1 sentence]

If you are able to conduct the reproducibility check, please prepare a reproducibility report 
for the following manuscript, code, and data:

Manuscript: Attached.

README: In the ICPSR repository.

Code: https://www.openicpsr.org/openicpsr/workspace?goToPath=/openicpsr/172381

Please file your report via reply-all to this email,  as soon as possible, understanding that it 
might take a while to get access to the data.

Thank you very much in advance!

```

> NOTE: This needs more info, pointing to the Policy on Third-party replications, and explaining the report. The above example is a simplified example for communication with cascad.

The email should be sent from the `dataeditor@aeapubs.org` account, cc'ing the same, as well as the `dataeditor-queue@aeapubs.org` account. The subject line should hvae the `AEAREP-xxxx` number of the **subtask**.

## openICPSR

The openICPSR repository should be shared with the external replicator. All information should come from the openICPSR repository, and not from communication of any kind with the authors, other than to possibly obtain the data.

## Receipt of report

When the external report is received,

- If not already done, forward the report to `dataeditor-queue@aeapubs.org` with the subtask number in the subject line. If authors reply-all to the original email, this will already be done.
- Mark the subtask as `done`
- Move the main issue forward to `writing report` and assign a pre-approver to combine the two reports.

## Finalizing the report

During report writing, the salient facts should be summarized in the standard report. The third-party report will generally be appended. However, if  we need to keep the replicator "anonymous", the contents of the report, suitably edited, should be added into the standard report.

