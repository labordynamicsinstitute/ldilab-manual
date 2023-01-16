## Using scan_packages.do

In "Writing Preliminary Report" stage, we ask you to check the completeness of the information on system requirements. Often, authors do not list out packages they installed that are not default packages in STATA. The authors should list them in the README (even when they provide ado files!), but it does not always happen. To help you identify these packages, we provide an useful tool for this exercise.

- Locate a directory named "tools/Stata_scan_code/".
- Change the following command in line 11 with your system information:
    ```
    global codedir "XXXCODEDIRXXX"
    ``` 
    You should locate the directory where the codes are (typically `112233`, the openICPSR space number):
    ```
    global codedir "../../112233"
    ```
    This will be the directory where the output excel file will be saved.
- Execute the dofile.
- Locate the file "`candidatepackages.xlsx`", use the information there, and remember to push the file to the repository.