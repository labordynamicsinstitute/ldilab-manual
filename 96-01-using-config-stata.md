(using-config-do)=
# Using config.do in STATA

When [running code](running-code-partb), we ask you to keep a log of what you do. Moreover, authors often use packages that are not part of STATA. How can you keep track of what is needed, and what was used by the code? We provide `template-config.do` in the [template repository](https://github.com/AEADataEditor/replication-template) you clone which addresses these problems. 

## Why do we need log files?

- Log files record each step of the analysis and its results as a text. It also records error messages if you encounter any error upon running the code.
- There are other purposes to have log files, but for us, it is to communicate with other team members. 
    - When a replicator submits the report, a preapprover (and an approver) needs to verify how the code ran. It is to ensure that any discrepancies we find are not due to mistakes on our end.
    - A log file is crucial for this verification. Otherwise, preapprovers and approvers have to run the code again to verify which is not an ideal use of time, nor an efficient way to process the case.

## Why do we have to install programs?

- STATA, or many other statistical software, does not provide all the packages (or "libraries", or "modules") that enable or facilitate the analysis. Therefore, many user-written programs or extensions are publicly available for downloads. For STATA, this is often at the [SSC](https://ideas.repec.org/s/boc/bocode.html) (`ssc install package`), but sometimes at the [STATA Journal archives](https://www.stata-journal.com/) (`net install sjt0444, using(http://www.stata-journal.com/software/sj16-3)`), and sometimes in authors' webpages (`net install package, using(https://author.com/packages)`)
- We differ in installation process from many others in the sense that, we want to install programs in a specified directory that is NOT a system directory.
    - This is to ensure that the set of packages used by replication package is complete. A complete replication package should be stand-alone, regardless of packages installed elsewhere in the machine that program is run on.

## Explaining config.do


```{note}
In the following text, the line numbers mentioned are approximate. We regularly update the `template-config.do` to improve it, which may shift specific lines.
```

### Setting directory structure information

The directory structure of the replication package and of the `main.do` within determines the location of  `config.do`. It also determins a few other parameters within the `config.do`.

:::{admonition} **[ACTION]** Adjust the `config.do`

- If the main .do file is directly placed in the root directory, set the parameter `scenario` to be `B` and save. 
- If the main .do file is inside a folder, open `config.do` and set the parameter `scenario` to `A` and save. (This is the default, so really no action is necessary.)
- If the replication package includes a folder with STATA packages, add the line  `adopath ++` followed by the path of the location of that folder and save. See "[Using Config.do](using-config-do)" for details.
- Add packages that need to be installed to `config.do`. See "[Using Config.do](using-config-do)" for details.

:::

We will refer to the `directory` that contains the package as `$rootdir`. The scenarios helps us to define that programmatically. 


- line 80, `global rootdir : pwd` sets the current working directory as a root directory, a.k.a. `rootdir`. It does not explicitly write the directory path, but see [later](right-click-stata) on how to run STATA so that it picks that up **automatically**.

```{warning}
Many authors of replication package tell you to "write the path where the package is". DO NOT DO THIS. Use `$rootdir` instead.
```

```{note}
Any other paths defined or used within the replication package should be relative to `$rootdir`. This is to ensure that the replication package is self-contained, and can be moved to another machine without breaking.
```

#### Scenario A

A simplified directory structure that correspond to scenario "A" look like this:

```
 directory/
              code/
                 main.do
                 01_dosomething.do
              data/
                 data.dta
                 otherdata.dta

```

:::{admonition} Example

- A main .do file is  inside a folder and you have placed `config.do` in that same folder. 

```
* Template config.do */

local scenario "A" 
* *** Add required packages from SSC to this list ***
local ssc_packages "estout ivreg2"
    // Example:
    // local ssc_packages "estout boottest"
    // If you need to "net install" packages, go to the very end of this program, and add them there.
```

:::

#### Scenario B

A simplified directory structure that correspond to scenario "B" looks like this:

```
 directory/
        main.do
        scripts/
             01_dosomething.do
        data/
             data.dta
             otherdata.dta
```


#### Scenario C

Sometimes, we encounter Scenario C, which adds an additional level. A simplified directory structure that correspond to scenario "C" looks like this:

```
directory/
	    step1/
            scripts/
                main.do
                01_dosomething.do
        step2/
	        scripts/
	            othermain.do
		        01_analysis.do
        data/
            data.dta
            otherdata.dta
```

Note: you would place the `config.do` in **all** directories that have some sort of `main.do`. 

:::{admonition} Example


- A main .do file is in the main directory, and you have placed `config.do` in the main directory. The package `estout` and `ivreg2` need to be installed:


```
/* Template config.do */

local scenario "B"  // around line 48
*** Add required packages from SSC to this list ***
local ssc_packages "estout ivreg2"
    // Example:
    // local ssc_packages "estout boottest"
```

:::


### Directory paths for log files.

`config.do` creates a subdirectory and saves log files in the subdirectory. Let's say the current working directory path is the following, since Jira issue number is `AEAREP-9999` and openICPSR case number is `111111`

```
L:/Workspace/aearep-9999/111111
```


- line 97, `global logdir "${rootdir}/logs"` sets the following directory as a directory for log files: `U:/Workspace/aearep-9999/111111/logs`. Note that it will automatically use the `$rootdir` created earlier based on your choice of scenario.

```
global logdir "${rootdir}/logs"
cap mkdir "$logdir"
```

- The first time you run the code,  no such directory exists. Therefore, the do file creates a new directory in line 98.
    - `mkdir` is a command to create a directory 

### Opening a log file with current date and time

Since we usually run the program several times until the code is completely [debugged](debugging-stata) (!), we would like to record all the runs. Therefore, we record the initial time we start running the code and use it in the name of the log file. 

- Lines 102-110 create a log file with the current date and time, and an identifier of who is running the code:

```
/* check if the author creates a log file. If not, adjust the following code fragment */

local c_date = c(current_date)
local cdate = subinstr("`c_date'", " ", "_", .)
local c_time = c(current_time)
local ctime = subinstr("`c_time'", ":", "_", .)
local ldilog = "$logdir/logfile_`cdate'-`ctime'-`c(username)'.log"
local systeminfo = "$logdir/system_`cdate'-`ctime'-`c(username)'.log"

/* global logfile */
log using "`ldilog'", name(ldi) replace text
``` 

- the last line starts the log file, with an internal name `ldi` which prevents collision with any log files opened by authors.

### System information

We require system information as part of the replication package. This is because some commands are sensitive to the OS, STATA version, machine type, etc. Lines 113 calls a separate logfile so as not to clutter up the main logfile:

```
/* used only for system info */
log using "`systeminfo'", name(system) replace text
```

### Package installation

As explained above, we often need to install packages. Even when the packages were installed in previous cases, it should be irrelevant to your current case, since we install those packages within our deposit directory so that we can verify the completeness of the replication packages. 

```
* *** Add required packages from SSC to this list ***
local ssc_packages ""
    // Example:
    // local ssc_packages "estout boottest"
    // 
    // If you have packages that need to be unconditionally installed (the name of the package differs from the included commands), then list them here.
    // examples are moremata, egennmore, blindschemes, etc.
local ssc_unconditional ""

    // If you need to "net install" packages, go to the very end of this program, and add them there.
```

- Add list of packages in the quotation marks in **line 50**
    - line 52 provides an example.

```
local ssc_packages "estout"
```

- If there are packages that do not contain a command of the same name (examples are `egenmore` and `moremata`), add these packages to **line 56**.

```
local ssc_unconditional "egenmore"
```

- normally, no additional changes are needed!

```
/* install any packages locally */
di "=== Redirecting where Stata searches for ado files ==="
capture mkdir "$rootdir/ado"
adopath - PERSONAL
adopath - OLDPLACE
adopath - SITE
sysdir set PLUS     "$rootdir/ado/plus"
sysdir set PERSONAL "$rootdir/ado"       // may be needed for some packages
sysdir
```

- The `adopath` and `sysdir` commands (lines 120-124) redirect STATA to search for, and install ado files in the directories referenced. 

```

/* add packages to the macro */
    
    display in red "============ Installing packages/commands from SSC ============="
    display in red "== Packages: `ssc_packages'"
    if !missing("`ssc_packages'") {
        foreach pkg in `ssc_packages' {
            capture which `pkg'
            if _rc == 111 {                 
               dis "Installing `pkg'"
                ssc install `pkg', replace
            }
            which `pkg'
        }
    }

```

- Lines 159-170  installs each package if there are packages listed and these packages do not already exist.   

```
/* add unconditionally installed packages */
    display in red "=============== Unconditionally installed packages from SSC ==============="
    display in red "== Packages: `ssc_unconditional'"
    if !missing("`ssc_unconditional'") {
        foreach pkg in `ssc_unconditional' {
            dis "Installing `pkg'"
            ssc install `pkg', replace
        }
    }

```

- Lines 172-180 do the same for packages that do not have a command with the same name.

```

/*==============================================================================================*/
/* If you need to "net install" packages, add lines to this section                             */
    * Install packages using net
    * net install grc1leg, from("http://www.stata.com/users/vwiggins/")
```

- Some packages are not hosted on SSC. In that case, you have to use "`net install..`" instead of "`ssc install`". Write such `net install`  commands after line 185, an example is given in line 185. **This is one of the RARE instances where you have to edit something in the latter part of `config.do`!!**

- In case where the authors provided ado files, we may need to specify this extra path, if the authors have not done so themselves (this varies across packages). Line 68

```
local author_adopath ""
```

will allow you to set that path at the top of the file. Lines 132-134 will implement this:

```
if "`author_adopath'" != "" {             // The author adopath variable is filled out
    adopath ++ "$rootdir/`author_adopath'"
}
```



## How to deploy config.do

### Copy the config file to the right location


:::{admonition} **[ACTION]** Copy the  [`template-config.do`](https://github.com/AEADataEditor/replication-template/blob/master/template-config.do) to the right location.

You should copy it (using Windows actions, or command line) and paste it into the folder where the main file is located. Change the name from `template-config.do` to `config.do`

::: 

The template is called `template-config.do`. In order to use it, copy it into the openICPSR folder (e.g. , `111111`) next to the author's main file, and rename it to `config.do`. If there is no `main.do` or similar, create one. See the [next section](running-code-in-stata) for more details.

### Include config.do

- If there is a main dofile, you should put the following line at the beginning of the `main.do`:

```
include config.do
```

- You should also add to the end of the `main.do`:


```
log close _all
```

:::{note}

Do NOT include it in the individual code files that are being called from the `main.do`. This will lead to errors.

:::

#### Notes

- If there is no main dofile, you should try to create one (see [how in the next section](create-master)), starting with the lines above, and ending with the `log close` command.
- If creating a main dofile is not possible, **and only then**, add the  lines at the beginning and the end, respectively, of **each** code file.
- There will be cases where authors **create their own log files**. Do NOT comment out the log file creation here, as the named logfile will not conflict with any author-generated files.

