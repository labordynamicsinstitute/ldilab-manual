# External reproducibility checks

In some cases, reproducibility checks must be conducted externally—particularly when restricted-access data is involved. This section outlines how to integrate such reports and ensure they are properly archived in our systems. The next section describes how an external replicator should prepare such a report.

## When External Reproducibility Reports Are Used

Instances that require the use of restricted-access data for a full reproducibility check can occasionally be sent out for an external report. These cases often arise when data cannot be shared with our team.

For more information, see the [AEA Policy and Protocol on Third-Party Verifications](https://aeadataeditor.github.io/third-party-verification-policy/), which describes who can conduct these external reports and the expected process.

> 🔒 In all cases where an external reproducibility check is used (e.g., CASCAD or World Bank), the **"external validation" checkbox in JIRA must be checked**.

::::{admonition} If you are the external replicator...
:class: tip

... you should read the [next section](writing-an-external-report).

::::

## Integrating the External Report

The external replicator will send us a filled out copy of [this template](https://github.com/AEADataEditor/replication-template/blob/master/EXTERNAL-REPORT.md) ([Word version](https://github.com/AEADataEditor/replication-template/blob/master/EXTERNAL-REPORT.docx)). 

:::{warning}

The external report must be added to the **repository**. It is **not sufficient** to leave it attached to a JIRA ticket or email.

:::

1. Start with the internal `REPLICATION.md` report.
2. **Do not delete** any section titles from the internal report.
3. In relevant sections, add a note such as:

   > “Please refer to the external report below.”

4. Review the external report and ensure all **bugs** and **discrepancies** are recorded in the **Summary and Findings** section of the internal report.
