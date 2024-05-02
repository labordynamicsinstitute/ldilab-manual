# Original Replication Report

:::{admonition} If this is a `RR` case, check for overlapping `CA` cases!
:class: warning dropdown

In some cases, we will have worked on a `RR` case (title says "Invitation to Review"), but the editor of the journal may have already issued a `CA`. 

- Usually, these cases should be linked - check if there is a `Is Revised By` link.
- If not, double-check by going to the `Other Links` tab in JIRA, and clicking on the `JiraSearchMC` field (is always pre-filled). This will show all cases that are tagged with the same `Manuscript Central Identifier`. Check if one of them is an incomplete or unassigned `CA` case.

If there is an overlapping `CA` case, the next steps depend on what updates the authors may have made:

> Check the openICPSR deposit to see if there have been any updates since the `RR` was originally submitted. 

- Often there are no updates. In that case, treat this report as if it were a `CA` report, and then contact the Data Editor.
- If there are no updates, this gets complicated. Contact the Data Editor immediately.

:::

1. Verify that the replicator has deleted all of the `INSTRUCTIONS` comments of the report; if not, please do so.
1. Verify if the replication requires **IRB approval/RCT registration**.  These are commonly found in papers that utilize **randomized experiments, lab experiments, or surveys** run by the authors, involving "human participants."  Ensure that the manuscript contains the necessary approval information (on the title footnote). If absent, insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments wherever necessary:
   - [Sample tags for IRB issues](https://github.com/AEADataEditor/replication-template/blob/master/sample-language-report.md?plain=1#L317)
   - [Sample tags for RCT issues](https://github.com/AEADataEditor/replication-template/blob/master/sample-language-report.md?plain=1#L308)
   - For surveys and experiments, also check if relevant "code" to run the survey or experiment is included. [Sample tags for survey/experiment issues](https://github.com/AEADataEditor/replication-template/blob/master/sample-language-report.md?plain=1#L328)
1. Read through the **Data Sources section** of the report and check for completeness.
   - Reports sometimes might be missing data sources.  Cross-check (scan) this with the manuscript and the README.  This is usually the most time-intensive part of the pre-approval. 
   - You are not expected to redo this section, but you should spot-check to see if it is complete and accurate.
   - When replicators mention "URL does not work" but provide no further information, verify the URL (if less than 5 URLs to check)
   - The report should accurately reflect whether the data source has been cited and whether its location/access modality has been provided. 
   - Verify/Insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
1. Check the **Data checks section** for completion.
   - Check if the PII scan output is present in the repository (should have been done automatically by the Pipelines)
   - Check if the Package scan output is present in the repository. (should have been done automatically by the Pipelines)
   - Verify/Insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
1. Check the **Code checks section** for completion.
   - Check if the completed Code check spreadsheet is present in the repository.
   - Verify/ Insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
1. Check the **Stated Requirements** and **Missing requirements** section for completion and insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
1. Carefully read through the **Replication steps section.**
   - Ensure that this report section is coherent in its description of the steps the replicator took to perform the entire replication. Can you follow the narrative/list of steps, and from it, do you think you understand what the replicator did?
   - If the replicator noted that the code contains bugs, the error message/error code should be explicitly listed.
   - **The pre-approver should not be rerunning any of the code!**
   - Communication between the pre-approver and replicator is encouraged so that any confusing/unclear language used in this section can be clarified. Use the Jira comments, and tag the Data Editor as necessary.
   - Verify/Insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
1. Check the **Computing Environment of the Replicator section** for completeness. (It should not include the description of the replicator's laptop unless it is clear that the replicator actually ran code on the laptop)
1. Verify: Format the results in the **Findings section** into tables by utilizing the the Excel-to-Markdown Extension in Visual Studio.
   - Check if the output/log files have been pushed to the Bitbucket repository.
   - If there are discrepancies between the replicated tables and figures and those of the manuscript, the report should contain images/screenshots to highlight the differences.
   - If there are numerous tables and figures that exhibit discrepancies, these should be put into a .zip file.  This action should be noted in the **Summary section** as well as mentioned in a JIRA comment.
1. Ensure the classification of the replication fits the degree of reproducibility.
1. Fill out the **Action Items** of the report.
   - These are separated into "Manuscript" and "openICPSR" (these sections are pre-existent in the template)
   - Use a script or manually copy-paste all of the `[REQUIRED]` tags to this list.
      - [`aeareq`](https://github.com/AEADataEditor/editor-scripts) extracts the `[REQUIRED]` tags and places them at the top of the REPLICATION.md 
   - Split the action items according to where they can be addressed. Some may be addressable in both sections (for instance, correcting figures and tables, and/or data citations). Others belong only into the "Manuscript" part (IRB, RCT), others only into the "openICPSR" (anything related to code)
   - Order them by importance: `[REQUIRED]` items first, and within these, the most important at the top (correcting bugs, providing missing files).
   - `[SUGGESTED]`  items can be at the end of each section.
      - [`aeareq`](https://github.com/AEADataEditor/editor-scripts) extracts the `[SUGGESTED]`  tags only if provided with the additional argument `sug`
1. Fill out the **Summary section** of the report.
   - Start with a thank you, and a positive note: Highlight the merits of the replication i.e. how many figures/tables were replicated, if data citations were properly completed, etc. 
   - Add a template line with the proposed resolution. These are at the top of the [sample-language-report.md](https://github.com/AEADataEditor/replication-template/blob/master/sample-language-report.md).
1. (Re)generate the PDF of the report.
   - Use MarkdownPDF package if you are using Visual Studio Code
   - Use a script: [`aeaready`](https://github.com/AEADataEditor/editor-scripts) creates the PDF from the REPLICATION.md, crafts the commit message and pushes it to the repository.  It requires additional pieces of software that are noted in the link.
1. Select a recommendation on the `Other links` tab of the JIRA ticket (see [Choosing a Recommendation](choosing-recommendation))
   - If this is a `RR`, choose a recommendation in the `MCRecommendation` field.
   - If this is a `CA`, choose a recommendation in the `MCRecommendationV2` field.
1. Commit and push all changes to the repository.  Advance the JIRA ticket to "Pre-approved."  The pre-approval is now complete!

:::{note}
The pre-approver should reach out to the original replicator for clarifications should there be any confusions during the course of pre-approving the report.  If bugs in the code seem trivial i.e. missing packages, missing `Results` directory, replicator cannot find output etc., the pre-approver should reach out to the original replicator for further clarification.
:::

::::{warning}
For the majority of the `[REQUIRED]` comment tags, it is best to use them verbatim to preserve uniformity across our reports.  However, there are times where a more accurate description can help the author pinpoint what exactly is required of them.

For example, say we have a scenario where the author did not include code for Table A.6 in the code deposit but everything else has been provided and replicates perfectly.

Instead of writing:


> [REQUIRED] Please provide complete code, including for construction of the analysis data from raw data, and for appendix tables and figures, and identify source for inline numbers.


It is clearer to the authors if we write:


> [REQUIRED] Please provide complete code for appendix tables and figures, in particular Table A.6.


::::

