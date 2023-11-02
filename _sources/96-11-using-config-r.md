(using-config-r)=
# Using config.R in R

In "Verification" stage, we ask you to keep a log of what you do. Moreover, authors often use packages that are not default programs of R. We provide `template-config.R` in the [template repository](https://github.com/AEADataEditor/replication-template) you clone which addresses these problems. In this section, we will walk you through how to update the `config.R`, in the [next section](running-code-in-r) how to run R in a way that generates log files automatically.

## Why do we have to install programs?

- R, or other statistical software, does not provide all the packages (or "libraries", or "modules") that enable or facilitate the analysis. Therefore, many user-written programs or extensions are publicly available for downloads. For R, this is most often comes from [CRAN](https://cran.r-project.org/), but the specific "mirror" of CRAN that is used may vary. You install packages with something like `install.packages("package name")` or multiple packages with `install.packages(c("package1","package2"))`. You might also see the use of `remotes::install_github("r-lib/conflicted")` (to install a package from Github) or `install_version("devtools", "1.11.0")` to install a specific version.
- We differ in installation process from many others in the sense that, we want to install programs in a specified directory that is NOT a system directory.
    - This is to ensure that the set of packages used by replication package is complete. A complete replication package should be stand-alone, regardless of packages installed elsewhere in the machine that program is run on.

## Explaining template-config.R

Start by copying the `template-config.R` into the authors' code directory. 

### Installing packages

Any libraries identified by the authors should be listed here, unless the authors already provide a setup program, or lines that install these packages. 

```
global.libraries <- c("foreign","devtools","rprojroot")
```

For instance, if the authors say you need `ggplot2` and `nonsenseR`, then add them to this line (and remember to keep case exactly as the authors provide it, so `nonsenser` is not the same as `nonsenseR`).

```
global.libraries <- c("foreign","devtools","rprojroot","ggplot2","nonsenseR")
```

### S-drive, L-drive

In some cases, authors provide us privately with data that is not part of the public replication package (the part on openICPSR is generally public). We put this on the L-drive, or what used to be called the S-drive. Put the location of that here, if any:

```
s-drive <- "L:/Workspace/aearep-9999-implicit-nda"
```

Wherever the author later references the confidential data, you can insert this placeholder, for instance:

```
# original author reference
# ols.data <- readRDS("data/confidential/analysis.Rds")
# you change it to
ols.data <- readRDS(file.path(s-drive,"data/confidential/analysis.Rds"))
```


### Directory paths for log files, libraries, and other things

`config.R` creates a subdirectory for log files, but does not automatically create the log file (in contrast to Stata). Here, you should add any additional directories that your debugging identifies as being necessary. Do write any path names with `/`, not `\`, and leave the directory names already listed untouched.

```
create.paths <- c("logs","libraries")
```

For instance, if the authors state that output should be written to "outputs", you can add

```
create.paths <- c("logs","libraries","outputs")
```

The `config.R` wird 

### Opening a log file with current date and time

Since we usually run the program several times until the code is completely debugged (!), we would like to record all the runs. Therefore, we record the initial time we start running the code and use it in the name of the log file. Area 2 calls current date and time as local macro and opens the log file.

- line 64-67: calls the current date and time as local macro
- line 69: starts the log file, with an internal name `ldi` which prevents collision with any log files opened by authors.

### System information

We require system information as part of the replication package. This is because some commands are sensitive to the OS, STATA version, machine type, etc. Area 3 calls in that information from the system and displays in the log file.

### Package installation

As explained above, we often need to install packages. Even when the packages were installed in previous cases, it should be irrelevant to your current case, since we install those packages within our deposit directory so that we can verify the completeness of the replication packages. Area 4 does this job.

- The `sysdir` commands (in line 89-91) redirects Stata to search for, and install ado files in the directories referenced. It won't automatically install them.
    - In case where the authors provided the ado files, adding a new command to the end of the config.R would suffice. For instance, if the authors have provided ado files in the directory `packages`, then

```
adopath ++ "${rootdir}/packages"
```

- Add list of packages in the quotation marks in **line 37**
    - line 39 provides an example.
    - line 97-106 installs each package if there are packages listed and these packages do not already exist.

- In some cases, the installation would fail since you have to use "`net install..`" instead of "`ssc install`". In this case, write such `net install`  commands after line 112, an example is given in line 111. 


## How to use config.R

### Rename the config file.

The template is called `template-config.R`. In order to use it, rename it to `config.R` and move it into the openICPSR folder (e.g. , `111111`).

### Include config.R

- If there is a master dofile, you should put the following line at the beginning of the `master.do`:


```
include config.R
```

and the end of the `master.do`:


```
log close _all
```

Do NOT include it in the individual code files.

- If there is no master dofile, you should try to create one (see [how in the next section](create-master)), starting with the lines above, and ending with the `log close` command.
- If creating a master dofile is not possible, add the  lines at the beginning and the end, respectively, of **each** code file.
- There will be cases where authors create their own log files. Do NOT comment out the log file creation here, as the named logfile will not conflict with any author-generated files. 
