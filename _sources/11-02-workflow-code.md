
# Code 


In this stage, you will download the code, inspect the authors' README, and should anything have failed in the automated steps above, correct for that manually.

## Downloading code

```{note}
You now need to decide where you are going to do the data analysis - that should be the place you do the next few steps. 
This is because the git setup we use does not allow you to include the data files in the Bitbucket repository, so when you download the replication package from openICPSR or elsewhere, they do not get added to the Bitbucket repository.
```

::::{tab-set}

:::{tab-item} CISER 


- [ ] Clone the Bitbucket repository onto the computer you are working on (`git clone https://yourname@bitbucket.org/aeaverification/aearep-xxx.git` )
- [ ] From the JIRA issue, download and add Manuscript, Data and Code Availability Form (DCAF). 
    - Download from Jira issue attachments. The manuscript is often called `PDF_Proof.pdf`. 
- [ ] Add the manuscript, and any response by the authors (if a revision)
  - Add them to the Git repo 
- [ ] Be sure to `git push` it all to Bitbucket, with a meaningful commit message. 
  ```bash
  git add PDF_Proof.pdf DataCodeAvailability.pdf
  git push
  ```
:::

:::{tab-item} Github Codespaces (CS) 

All actions in Github Codespaces (CS for short) will be performed in Visual Studio Code (VSC): the left pane for file and Git actions, in the Terminal, or in the text editor. To connect to CS, see [instructions to come]. It is assumed that you will run this from your laptop, but it can be run from any internet-connected computer.

- [ ] Use the Terminal built into VSC (`Menu` -> `Terminal` -> `New Terminal` )
- [ ] Populate CS with the Bitbucket repo (yes, this is a bit weird)
  - Use the LDI short-cut command 
    ```bash
    aeagit 123
    ```
    to clone the Bitbucket repository for `aearep-123` onto CS (this executed `git clone (URL)/aearep-123` behind the scenes).
    - If this is the first repository you run on this CS instance, you may need to configure authentication. Follow the instructions from the `aeagit` command.
    - Once the  `aeagit 123 ` has completed, it will open a new VSC windows. **All subsequent actions should be done in that window.**
- [ ] Add the manuscript, and any response by the authors (if a revision)
  - Copy the manuscript to the CS.    There are two ways to do this:
    - Drag-and-drop the downloaded manuscript into the file pane of VSC. 
    - Use the `gh` command line tool from a non-VSC terminal (on your local computer): 
      ```bash
      gh cs cp PDF_Proof.pdf remote:/workspaces/aearep-123
      ```
  - Add the manuscript to the Git repo
    - In the terminal: 
      ```bash
      git add PDF_Proof.pdf; git commit 'Manuscript'; git push
      ```
    - Or use the VSC Git tools
:::

:::{tab-item} Manual steps 

If neither of the other two methods work, try this method (typically, on CISER)

- [ ] Download the code (and data) from openICPSR (typicaly for most cases). See [openICPSR repositories](`r config$url$reploldmd`openICPSR_training.md) for instructions on downloading these materials. Typically called `111234.zip`.
  ![icpsr screen](images/icpsr-download.png)
  - Copy/paste the downloaded openICPSR ZIP file into the local copy of the `aearep-123` repository
    - The ZIP file should be called something like `111234.zip`. Note: it might *look* like a folder, but it is not! (on Windows) 
    - The ZIP file will be wherever your browser downloads materials - probably your `Download` folder.
  - The local repository should now have the relevant LDI replication template materials and the openICPSR ZIP file containing the replication materials provided by the authors.
- [ ] If uploading to CS, copy the downloaded ZIP file into the CS. There are two ways to do this:
    - Drag-and-drop the downloaded openICPSR ZIP file into the file pane of VSC. 
    - Use the `gh` command line tool from a non-VSC terminal (on your local computer): 
      ```bash
      gh cs cp 111234.zip remote:/workspaces/aearep-123
      ``` 
      (adjust accordingly)
- [ ] Unzip the openICPSR folder under a folder **named for the openICPSR repostory number**. 
    - On Windows, right-click and select "Extract all". When asked, do not overwrite files.
    - On OSX, double-click. When asked, do not overwrite files.
    - From bash: 
      ```bash
      unzip -n 111234.zip -d 111234
      ```
  - The individual files that are part of the replication package should now be in a subdirectory (e.g, `111234`, the openICPSR repository number). 
  - Perform a `git add`: `git add 111234` should do the right thing.
  - Perform `git commit`, `git push` sequence to populate the Bitbucket repo with the authors' replication materials (see above how to handle data).

:::

::::

- [ ] Clean-up: Delete (`git rm`) unused files from the template! 
  - Example: `git rm README.md template-config.R` if the replication archive does not contain any R files (you can do this at any time before writing the **Preliminary Report**)

- The root of the repository should contain only our files (i.e., REPLICATION.md, etc.), the manuscript files (main manuscript, any online appendices and README files provided through the JIRA ticket), and the code.
  - Example:
    ```
    111234/
    code-check.xlsx
    config.do
    PDF_Proof.PDF
    PII_stata_scan.do
    DataCodeAvailability.pdf
    REPLICATION.md
    ```

- [ ] Be sure to `git push` it all to Bitbucket, with a meaningful commit message. 

```{note}

  ```bash
  git commit -m "My message here"
  git push
  ```

```

- [ ] Check with `git status` that there are no uncommited files.



## Verifying completeness of the README

The first section of the Replication report is titled "[General](https://github.com/AEADataEditor/replication-template/blob/master/REPLICATION.md#general)". Here you want to verify how complete the README is. 

- Go through the entire README, and compare both to the [template README](https://social-science-data-editors.github.io/template_README/template-README.html) and the sections in the **General** section. 
  - Check off the sections for which you appear to have information. 
  - Leave blank the sections that are either not provided, or that are empty
- In JIRA, identify the question called "`DCAF_README_compliant`". 
  - If all or most of the sections are in the same order, and are filled with meaningful information, then check `Fully`
  - If information is provided, but in different order, or only mostly, mark "`Content only`".
  - If very little of the information is provided, mark it as "`No`"


## List of Data Sources

Now you will establish a **list of data sources used**.

- Please check the **Data and Code Availability Form**.
  - The form should be attached in the JIRA ticket. 
  - In area 2 of the screen, choose `DCAF`.
    - Open the **Data and Code Availability Form**, and check if all blanks are filled out.
    - Once you checked the form, and in particular, if the checkbox next to "README" is checked, choose "`Yes`" from the dropdown menu of `DCAF_README_checked` cell.
    - If the answer to the following question at the bottom of the form is "Yes", then, choose "`Yes`" from the dropdown menu of `DCAF_Access_Restrictions`. Otherwise, choose "`No`".
      "Is any of the data used in this manuscript subject to access restrictions?"
  ![jira screen](images/jira-screen.png)


```{note}
What is the difference between a "**data source**" and a "**dataset**" or "data file"? 

- A **data source** is more general. A data source may provide multiple data files. One example is the "Current Population Survey".
- A **dataset** or **data file** is a single file that appears in the replication package. An example is "`data_cps.dta`", which is presumably the data file containing the Current Population Survey. 

For this section, you should list **data sources**.
```

- From the **README** provided by the authors, the **data section of the article itself**, or an **appendix**, establish a list of data sources used in the article. For each data source
  - [ ] write the corresponding `Data description` section of REPLICATION.md. This should provide detail about the datasets 
    - If data are cited, copy and past the citation to the replication report, clarify which one you are referring to. Be sure to check  [AEA Sample References](https://www.aeaweb.org/journals/policies/sample-references) and the [additional guidance](https://social-science-data-editors.github.io/guidance/addtl-data-citation-guidance.html) to be sure it is a **data citation**, and not a citation to an article or a document describing the data!
  - [ ] check any provided URL, and verify if there is a **"Data Use Agreement", "Citation requirement", "License"** on the web page. Check any such data use agreement for conditions. These may require that the authors cite a particular paper, or cite the data in a particular way (check this), or that the authors may not actually redistribute (provide) the data (check this!). If you have doubts, check with your supervisor. 
  - [ ] Check that there is enough information to obtain the data in the README. Based on the README, you should be able to find, on the linked website, the data that you would need. (Ignore at this point that the data might be provided)
- [ ] Add the list of data sources to the repository by committing the preliminary version of the REPLICATION.md (`git add`, `git commit`, `git push`)
- [ ] Fill out the `DataCitationSummary` field indicating how many data citations are in order: `all`, `some`, or `none`. 
- [ ] Fill out the `Data Provenance` section 
  - Are the data in the openICPSR repository, or are they someplace else? "Various" is a legitimate answer if data are in various locations.
- [ ] Please refer to [Chapter 9 A guided walk through the Replication Report](a-guided-walk-through-the-replication-report.html) for more details about which data sources to include and how to assess the provided information.

## Other information

Have a look at the **README** again. 

- [ ] Is there information about **Requirements**? 
  - Is there information about the **software**? 
  - How long does the author say the code will run?
  - How much memory, or processors, does the code need? 
  - This may tell you if you, or somebody else, will need to run the code, and whether CISER, or someplace else, is a good place to run the code.

## Review of Code

Now do a first pass through the code files provided:


```{note}
Do NOT run any code!
```
 

- [ ] review the code in detail. 
- [ ] In the template, you will find *[code-check.xlsx](https://github.com/AEADataEditor/replication-template/blob/master/code-check.xlsx)*. 
  - Use this to create a list of all Tables and Figures in the paper, and use this to guide you in [REPLICATION.md](https://github.com/AEADataEditor/replication-template/blob/master/REPLICATION.md).
- [ ] Fill out the "Code Description" section of the REPLICATION.md
  - Provide some information about the program files (are there 3 Stata files? Are there 5 Matlab programs?). You will use this information to fill out the `Software Used` later as well, but provide details here.
    - You can use the file "`generated/programs-list.txt` to help you here.
  - Did you have difficulty aligning the README with the files? Does the sequence suggested by the programs differ from what's written in the README? 
  - Are there files in the archive not explained in the README?
  - Copy-and-paste the *code-check.xlsx* into the code description part, listing the programs. Omit the "Reproduced?" Column in doing so. Use the [Excel-to-Markdown plugin](https://marketplace.visualstudio.com/items?itemName=csholmq.excel-to-markdown-table) for VSCode. 
    - This table will be pasted in under "Findings" again, with "Reproduced?" column, once code has been run.

Next fill out the following fields in the Jira ticket:

  - [ ] `BITBUCKET SHORT NAME` - if not already done earlier

> Commit! 

You can now proceed to change the status to `Data`. As you select that transition, you will be asked various questions:

  - [ ] `Software Used` Start typing the name of the software program you will use for the replication. Software that have been used in the past will show up as  options (e.g. start typing "Stata" and you will see it pop up).
  - [ ] `PROGRAMSEQUENCE` Does the README tell you the correct sequence for running the code?
  - [ ] `PROGRAMSDOCUMENTATION` Are the provided programs well commented? Are they documented in the README?
  - [ ] `PROGRAMSSTRUCTUREMANUAL` Does the README note any manual changes that you need to make to the code in order for it to run?
