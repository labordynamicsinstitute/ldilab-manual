(Manual1)=
# Prepare the working area 

Before we can verify code, data, and documentation, we need to get the code and data onto your "working area". 

```{note}
You now need to decide where you are going to do the data analysis - that should be the place you do the next few steps. 
This is because the git setup we use does not allow you to include the data files in the Bitbucket repository, so when you download the replication package from openICPSR or elsewhere, they do not get added to the Bitbucket repository.
```

::::{tab-set}

:::{tab-item} CCSS 


- [ ] Clone the Bitbucket repository onto the computer you are working on
  ```
  git clone https://yourname@bitbucket.org/aeaverification/aearep-xxx.git
  ```
- [ ] Verify that the code is present, i.e., that the automated scripts run during the [Code Ingest](ingesting-author-materials) worked. **If they did not, you need to switch to the "Manual steps"!**
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
- [ ] Verify that the code is present, i.e., that the automated scripts run during the [Code Ingest](ingesting-author-materials) worked. **If they did not, you need to switch to the "Manual steps"!**
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

If the automated population of the author's code directory did not work, you will need to manually download the replication package. Try to do this first using scripts.

**Downloading using scripts**

See [the details in the appendix](using-pre-pub-openicpsr). You can do this on CCSS or on Github CS. 

**Downloading using a browser**

If you are still unsuccesful at this point, try this manual method (typically, on CCSS)

- [ ] Download the code (and data) from openICPSR (typicaly for most cases). See [details in the appendix](using-pre-pub-openicpsr) for instructions on downloading these materials. Typically called `111234.zip`.
  ![icpsr screen](images/icpsr-download.png)
  - Copy/paste the downloaded openICPSR ZIP file into the local copy of the `aearep-123` repository
    - The ZIP file should be called something like `111234.zip`. Note: it might *look* like a folder, but it is not! (on Windows) 
    - The ZIP file will be wherever your browser downloads materials - probably your `Download` folder.

**Next manual steps**

The local repository should now have the relevant LDI replication template materials and the openICPSR ZIP file containing the replication materials provided by the authors.

- [ ] If uploading to CS, copy the downloaded ZIP file into the CS. There are two ways to do this:
  - Drag-and-drop the downloaded openICPSR ZIP file into the file pane of VSC. 
  - Use the `gh` command line tool from a non-VSC terminal (on your local computer): 
    ```bash
    gh cs cp 111234.zip remote:/workspaces/aearep-123
    ``` 
    (adjust accordingly)
- [ ] Unzip the openICPSR folder under a folder **named for the openICPSR repostory number**. 
  - From bash: 
    ```bash
    unzip -n 111234.zip -d 111234
    ```
  - On Windows, right-click and select "Extract all". When asked, do not overwrite files.
  - On OSX, double-click. When asked, do not overwrite files.
  - The individual files that are part of the replication package should now be in a subdirectory (e.g, `111234`, the openICPSR repository number). 
  - Perform a `git add`: `git add 111234` should do the right thing.
- [ ] Add the manuscript, and any response by the authors (if a revision)
  - Add them to the Git repo 
- [ ] Be sure to `git push` it all to Bitbucket, with a meaningful commit message. 
  ```bash
  git add PDF_Proof.pdf DataCodeAvailability.pdf
  git push
  ```


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
:::

::::

- [ ] Be sure to `git push` it all to Bitbucket, with a meaningful commit message. 

:::{note}

  ```bash
  git commit -m "My message here"
  git push
  ```

:::


- [ ] Check with `git status` that there are no uncommited files.
