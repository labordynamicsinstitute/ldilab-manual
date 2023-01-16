## Using config.do in STATA

In "Verification" stage, we ask you to keep a log of what you do. Moreover, authors often use packages that are not default programs of STATA. We provide `template-config.do` in the [template repository](https://github.com/AEADataEditor/replication-template) you clone which addresses these problems. 

### Why do we need log files?

- Log files record each step of the analysis and its results as a text. It also records error messages if you encounter any error upon running the code.
- There are other purposes to have log files, but for us, it is to communicate with other team members. 
    - When a replicator submits the report, a preapprover (and an approver) needs to verify how the code ran. It is to ensure that any discrepancies we find is not due to mistakes on our end.
    - Log file is crucial for this verification. Otherwise, preapprovers and approvers have to run the code again to verify which is not an ideal use of time, nor an efficient way to process the case.

### Why do we have to install programs?

- STATA, or any statistical software, does not provide all the package that enables or facilitates the analysis. Therefore, many user-written programs or extensions are publicly available for downloads. 
- We differ in installation process from many others in the sense that, we want to install programs in a specified directory that is NOT a system directory.
    - This is to ensure that the package is complete. A complete replication package should be stand-alone, regardless of packages installed in the machine that program is run.

### Explaining template-config.do

![template-config.do](images/stata_config.png)

#### Directory paths for log files.

`config.do` creates a subdirectory and saves log files in the subdirectory. Area 1 sets these directory paths. Let's say the current working directory path is the following, since Jira issue number is `AEAREP-9999` and openICPSR case number is `111111`
    ```
    U:/Workspace/aearep-9999/111111
    ```

- line 50, `global rootdir : pwd` sets the current working directory as a root directory, a.k.a. `rootdir`.
- line 59, `global logdir "${rootdir}/logs"` sets the following direcotry as a directory for log files: U:/Workspace/aearep-9999/111111/logs 
- Notice that there is no such directory exists. Therefore, the do file creates one new directory in line 60.
    - `mkdir` is a command to create a directory 


#### Opening a log file with current date and time

Since we usually run the program several times until we complete the replication, we would like to record all the instances. Therefore, we record the initial time we start running the code and use it in the name of the log file. Area 2 calls current date and time as local macro and open the log file.

- line 64-67: calls the current date and time as local macro
- line 69: start the log file, with an internal name `ldi` which prevents collision with any log files opened by authors.

#### System information

We require system information as part of the replication package. This is because some commands are sensitive to the OS, STATA version, machine type, etc. Area 3 calls in that information from the system and displays in the log file.

#### Package installation

As explained above, we often need to install packages. Even when the packages were installed in other cases before, it should be irrelevant to your current case, since we install those packages within our deposit directory so that we can verify the completeness of the replication packages. Area 4 does this job.

- The sysdir commands (in line 89-91) redirects Stata to search for, and install ado files in the directories referenced. It won't automatically install them.
    - In case where the authors provided the ado files, adding a new command to the end of the config.do would suffice. For instance, if the authors have provided ado files in the directory `packages`, then
    ```
    adopath ++ "${rootdir}/packages"
    ```

- Add list of packages in the quotation marks in **line 37**
    - line 39 provides an example.
    - line 97-106 installs each package if there are packages listed and these packages do not already exist.

- In some cases, the installation would fail since you have to use "`net install..`" instead of "`ssc install`". In this case, write such `net install`  commands after line 112, an example is given in line 111. 


### How to use config.do

#### Rename the config file.

The given name should be `template-config.do`. In order to use it, rename it to `config.do` and move it into the openICPSR folder (e.g. , `111111`).

#### Include config.do

- Add the following line at the beginning of each code file:
    ```
    include config.do
    ```
    and add the following at the end of each code file:
    ```
    log close _all
    ```
- If there is a master do file, you should put the above lines at the beginning and the end of the `master.do` once, and NOT include it in the individual code files.

- There will be cases where authors create their own log files. Do NOT comment out the log file creation here, as the named logfile will not conflict with any author-generated files. 
