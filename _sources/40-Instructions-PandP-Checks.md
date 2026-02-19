(aea-pandp-instructions)=
# AEA: Instructions for Papers and Proceedings checks

You will be assigned a Jira issue. It should look something like this:

![](images/jira-pnp_screenshot.png)

Take note of the 4 highlighted fields:

- \(1) the "AEAREP" number (identifier for the issue on Jira)

- \(2) the "Manuscript Central Number" (identifier on the AEA's editorial system)

- \(3) the "openICPSR Project Number" (identifier on the ICPSR system)

- \(4) the link for "Replication package URL", which should direct you directly to openICPSR

Additionally, certain steps below (i.e. transitioning to "Pending Publication") require that you have "Publisher" permission in Jira. If it is unclear whether or not you have that permission, please reach out to a supervisor.  

:::{note}

Here's the [guidance document](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html).

:::

## Step 1

You should now do the following:

- Open the link in (4) on openICPSR, (more rarely) Zenodo, or Dataverse 

  - If you need to find the openICPSR repository, use [this link](https://www.openicpsr.org/openicpsr/tenant/openicpsr/module/aea/reports)
    
<!-- -->

- Open the 2026 form: [link here](https://forms.gle/jZRzdrqHC5WLsjhG8)

- Assess the openICPSR repository, filling out the form as you go along

| Requirements                     | open ICPSR | Dataverse                                        | Zenodo                                       |
|----------------------------------|------------|--------------------------------------------------|----------------------------------------------|
| open ICPSR number                | Applicable | N/A: Use doi number to distinguish                | N/A: Use doi number to distinguish            |
| Manuscript Number                | Applicable | Applicable                                       | Applicable                                   |
| Jira Ticket (Internal Reference) | Applicable | Applicable                                       | Applicable                                   |
| Title                            | Applicable | Applicable                                       | Applicable                                   |
| Principal Investigators          | Applicable | Applicable: Go to metadata, look for author      | Applicable: Name is right below title        |
| Summary/Description              | Applicable | Applicable: Go to metadata, look for description | Applicable: Look at description below Author |
| JEL Classification               | Applicable | N/A                                              | N/A                                          |
| Manuscript ID                    | Applicable | Applicable                                       | Applicable                                   |
| No ZIP Files                     | Applicable | Applicable                                       | Applicable                                   |
| README Format                    | Applicable | Applicable                                       | Applicable                                   |
| Subject Terms                    | Applicable | N/A                                              | N/A                                          |
| Geographic Coverage              | Applicable | N/A                                              | N/A                                          |
| Time Period(s)                   | Applicable | N/A                                              | N/A                                          |
| Funding Sources                  | Applicable | N/A                                              | N/A                                          |
| Collection Dates                 | Applicable | N/A                                              | N/A                                          |
| Data Types                       | Applicable | N/A                                              | N/A                                          |
| Data Sources                     | Applicable | N/A                                              | N/A                                          |
| Unit of Observation              | Applicable | N/A                                              | N/A                                          |

  - It is important that you enter the AEAREP and Manuscript numbers accurately. We suggest copying-and-pasting.

- Submit the form.

- Close the form after each issue, and open it again for the next one.

- Navigate to the "PandP Docs" Google Drive folder [here](https://drive.google.com/drive/u/0/folders/1RiFDf6QgOLMyx5FUQXR1ACRdvITdCySz), locate the PDF with the Jira ticket of the case you are working on (PDF format: `Report-PandP-AEAREP-xxxx.pdf`), and download the file. This is the PDF version of the checklist form using the information you entered.

In **Jira**:

- Move the issue forward by choosing "**Process PandP**" to status
     "*Submitted PandP Form*"
  - This indicates that you have completed the form.
- Attach the downloaded PDF to the Jira ticket.

## Step 2

Once the form PDF has been added to the issue, you should first return to the openICPSR repository, and then come back to Jira. Depending on what's on the form, proceed to do one of the following:

### If the form has all "required" elements checked, you should "sign off"


::::{tab-set}

:::{tab-item}  On openICPSR

- Write a "Project communication log" entry. After clicking on "+ add entry", copy the following to the relevant cell. Update AEAREP number accordingly.
  - *Subject line:* 
    ```
    AEAREP-xxx Data and Code Deposit for P&P submission accepted
    ```
  - *Content*: 
    ```
    Thank you for uploading your code and data. This
    deposit is accepted. No computational verification was
    conducted, only compliance with required metadata was checked.
    ```

::: 

:::{tab-item} On Dataverse
- Select "Contact Owner"
![](images/dataverse-contact-form-1.png)

From: dataeditor@aeapubs.org
Subject line:

```
AEAREP-xxx Data and Code Deposit for P&P submission accepted
```
Message:

```
Thank you for uploading your code and data. This
deposit is accepted. No computational verification was
conducted, only compliance with required metadata was checked.

```

![](images/dataverse-contact-form-2.png)

:::

:::{tab-item} On Zenodo

TBD

:::

::::

#### In Jira

- Move it through the workflow
  - Choose "**Prepare for publication**"
  - Resolution: *Evaluation only*
  - MCRecommendationV2: *Accept*

### If the form does not have all "required" elements checked, make the following entry

::::{tab-set}

:::{tab-item} On openICPSR

1) If `Deposit Status` = `Deposit in Progress`

- Write a "Project communication log" entry
  - *Subject line:* 
    ```
    AEAREP-XXX Modifications to make to your P&P deposit
    ```
  - *Content:* 
    ```
    Thank you for uploading your code and data. We have checked the deposit for compliance with the required metadata
    elements. Please see the attached form for modifications to make. Once all changes have been made, please change the status of your deposit to "Submit to AEA".
    ```
  - Attach the PDF from the issue to the communication log.

2) If `Deposit Status` = `Submitted`, 

- Change the status of the deposit to "Request Revisions" with the note:
  - Please see the attached form for modifications to make.
- Write a "Project communication log" entry
  - *Subject line:* 
    ```
    AEAREP-XXX Modifications to make to your P&P deposit
    ```
  - *Content:* 
    ```
    Thank you for uploading your code and data. We have checked the deposit for compliance with the required metadata
    elements. Please see the attached form for modifications to make. Once all changes have been made, please change the status of your deposit to "Submit to AEA".
    ```
  - Attach the PDF from the issue to the communication log.


::: 

:::{tab-item} On Dataverse

- Tag Assistant to the Data Editor (Sofia) in the Jira ticket that there are noncompliant fields.

:::

:::{tab-item} On Zenodo

- Tag Assistant to the Data Editor (Sofia) in the Jira ticket that there are noncompliant fields.

:::

::::

#### Back in Jira,

- Choose "**Wait for openICPSR response (PandP)**"
  - Resolution: "*Evaluation only*"
  - MCRecommendationV2 = "Accept with changes"
- Later, once the issues have been resolved (typically days or
        weeks later) follow the process under "required elements
        checked"
