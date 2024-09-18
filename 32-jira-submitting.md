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

   ![ScholarOne Login](images/scholarone-login.png)

   2. Click on the review tab and identify the manuscript number (`Manuscript Central Identifier`) of the paper
   3. Select `Continue Review`

![ScholarOne Submission](images/scholarone-submissionpage.png)

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

