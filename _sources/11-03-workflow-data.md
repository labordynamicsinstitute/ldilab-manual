
# Data 

::::{tab-set}

:::{tab-item} CCSS-RS (CISER)

- [ ] Ensure that you have set up your CCSS-RS environment (see [appendix](setup-bash))
- [ ] On CISER, the data will be stored locally.
  - In some cases, you may be asked to use (restricted) data on the S: drive. Follow instructions as you receive them.
- [ ] Download the openICPSR data (if not already done in the previous step, and if available). 
  - Manually, see [Manual steps](#Manual) above.
    ```bash
    python tools/download_openicpsr-private.py 111234 . netid@cornell.edu
    unzip -n 111234 -d 111234
    ```
    or the short version (first do [this additional setup](setup-bash))
    ```
    python tools/download_openicpsr-private.py 111234
    ```
    which should unpack the data files only, not overwriting anything else.
- [ ] attempt to download data from various sources indicated by the authors, but ONLY if no sign-up/ application process is involved. 
- [ ] If there is data: Run the PII-checking code, review the output, and record the result in the `REPLICATION.md`.
  - This may already have been generated, check `generated/pii_stata_output.csv` and `generated/PII_stata_scan_summary.txt`.

:::

:::{tab-item} Github Codespaces (CS)  


- [ ] Be sure you still have the Bitbucket repository clone, if not, follow instructions under [Code](#code)
- [ ] Download the openICPSR deposit using the LDI short-cut command
  - `python3 tools/download_openicpsr-private.py 111234`
  - The ZIP file should now be in the same folder as `REPLICATION.md`.
- [ ] Unzip the openICPSR ZIP file againto a folder **named for the openICPSR repostory number**. 
    - In the terminal 
      ```bash
      unzip -n 111234 -d 111234
      ```
- [ ] Upload data that you obtained from other sources to CS. There are two ways to do this:
    - Drag-and-drop the downloaded data file into the file pane of VSC, into the appropriate location.
    - Use the `gh` command line tool from a non-VSC terminal (on your local computer): 
      ```bash
      gh cs cp datafile.dat remote:/workspaces/aearep-123/111234/data/location
      ``` 
      (adjust accordingly as per the author's instructions)
- [ ] If there is data: Run the PII-checking code, review the output, and record the result in the `REPLICATION.md`.
    - This may already have been generated, check `generated/pii_stata_output.csv` and `generated/PII_stata_scan_summary.txt`.

:::
::::

- [ ] You should check the output - it is not automatic.
  - You should use words, and examples, from the output if it looks like there is Personally Identifying Information (PII) like names, addresses, etc. in the output.
  - The author will NOT see the output from the program unless you copy **relevant** parts of it into the report.
- [ ] Describe the data 
  - [ ] do relevant variables have labels? 
  - [ ] Is the data readable?
  - [ ] Is the data in archive-ready formats (`csv` or `txt` are the preferred formats by librarians, but `dta` or `spss` are also OK; `mat` files are discouraged)

Fill out the following Jira fields:

  - [ ] `DATA PROVENANCE` Where, specifically, are you accessing the data? Typically this is the openICPSR repo URL (same as `CODE PROVENANCE`), but may be a user-provided URL or DOI. 
    - if the data is in multiple places, enter "Multiple" here, and record the details in the REPLICATION.md
  - [ ] `WORKING LOCATION OF THE DATA` Where did you put the data? Examples: CISER, laptop, or Git LFS, or somewhere else

You can now proceed to change the status to `Write Preliminary Report`. You will be asked to provide additional information:

  - [ ] `DATASETSINCLUDED` Are all datasets included as part of the replication package (on openICPSR or, if not using openICPSR, on the other repository)?
  - [ ] `DATAAVAILABILITYACESS` Do the data require users to apply for access, purchase, or otherwise sign or enter into agreements to access the data? This could be a license agreement, or even a click-through acknowledgement. (This should be mentioned in the Readme PDF or in the article) 
  - [ ] `DATAAVAILABILITYEXCLUSIVE` Are there data that are **only** accessible to the author (nobody else)?
  - [ ] `REASON FOR NON-ACCESSIBILITY OF DATA` Fill this out for **any** data that is not accessible/ not included as part of this archive; check **all** that apply. This should be clear from the authors' descriptions (in the README)
    - `Too big`: The data can be accessed elsewhere, but they are too big for this replication package
    - `Application process`: In order to access the data, an application needs to be made to an institution (not a purchase). 
    - `Cost`: It costs money to obtain the data. This may be because it has to be purchased, or because there is a fee for the application process.
    - `Confidential data`: The data are sensitive / confidential and are therefore not made available in this replication package. They can be available elsewhere, subject to conditions.
    - `Proprietary data`: The data "belong" to somebody - a company, or in rare cases, a specific author, and cannot be redistributed. 
    - `Licensed data`: A license must be obtained. This can be different than an application process (generally, less complicated).
    - `Redistribution not authorized`: Often, even if data are not confidential, not proprietary, etc., there may be redistribution restrictions. An example are some IPUMS data, as well as many others.
    - `Other download site provided`: When data can be downloaded elsewhere, possibly due to `licenses` or `application process`. In other cases, even if they could be provided, they may already be archived elsewhere, and are not included here. 
    - `Not found`: This should be checked when data cannot be found as per the instructions by the author. This is rarely a final finding for pre-publication verification.
  - [ ] `NUMBEROFDATASETS` How many datasets are used in the article (whether or not they are included in the replication package you downloaded)? This is meant to include datasets that you are asked to download, or that you were given access to via the "S:" drive, or "CRADC", or some other secure mechanism.

