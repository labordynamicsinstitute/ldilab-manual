(running-code-in-r)=
# Running Code in R

Although, there are plenty of ways to run code in R, our goal with these instructions is to show the easiest way to do it, by minimizing both the manual steps replicators have to go through and the chance of making a mistake that prevents a successful run.

## Why do we need log files?

- Log files record each step of the analysis and its results as a text. It also records error messages if you encounter any error upon running the code.
- There are other purposes to have log files, but for us, it is to communicate with other team members. 
    - When a replicator submits the report, a preapprover (and an approver) needs to verify how the code ran. It is to ensure that any discrepancies we find are not due to mistakes on our end.
    - A log file is crucial for this verification. Otherwise, preapprovers and approvers have to run the code again to verify which is not an ideal use of time, nor an efficient way to process the case.


## Step 1: check for a "main" .R file

A `main.R` file is a R script that will call, in the correct sequence, all the programs necessary to construct analysis datasets, do all computations, and produce figures and tables. If a `main.R` file exists, it should be mentioned in the README. In most cases, running a single `main.R` file is sufficient to complete the reproduction. In general, a main script does not need to be a .R file. However, we will focus on cases where all work done in R is reduced to executing a single .R file.

```{note}
If there is no `main.R` file, you should create one. See [previous section](using-config-r).
```


## Step 2: Run the Code

We will run R from the command line to create log files. We will use the `main.R` file to run the code.

```{note}
If the R code fails, you will see this in the `Rout` file, which you can open in VS Code. It is OK to debug using Rstudio, but the final (clean) run after all debugging, or any run that needs outside help, needs to be logged, and run from the command line.
```

### Setting up the environment to run the code

::::{tab-set}

:::{tab-item}  Windows 

```{tip}
The most convenient way to run from the command line is to use Rstudio. Open Rstudio, and configure the **Terminal** as follows:
```

- Click on the Terminal tab in the bottom left corner of Rstudio
- Click on the downward-arrow to open up the menu for Terminal. Select `Terminal Options...`


![Rstudio Terminal Options](images/rstudio-terminal-options.png)


- Select "Git Bash" from the options.

![Rstudio Terminal Bash Selection](images/rstudio-terminal-options-bash.png)

- Click "OK"





:::

:::{tab-item} Mac/Linux 

On Unix-style systems, the preferred way is to use the Terminal to run R code.

Open up a Terminal in the folder where the `main.R` file is located - this may differ depending on your system, and may involve using "`cd /path/to/code`" commands. Confirm with "`ls`" that you see the same files you might see in Finder / File Explorer. Refer to the command line training in the initial training.

On **BioHPC**, you may need to choose your R version, every time you launch a terminal (see [BioHPC documentation for more details](https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=37#c):

```
module load R/4.3.2
```

Type 

```
module avail
```

to see which R versions are available. 

::: 

::::

### Run the code

Once the above is done, running R is simple:

```bash
R CMD BATCH main.R
```

This will create a `main.Rout` file, which you can open up in VS Code. 



> Consider how much time a complete run would take before you run everything one last time. If it would take too long, you may want to skip a complete run, but ensure that you have log files for all partial runs. Make a note of this in the report.


## Possible failures

### Use of Rstudio API

We sometimes see authors use the Rstudio API. In most cases, this will prevent the code from running in the `R CMD BATCH` method. Also in most cases, this can be remedied easily.

For instance, the following code leverages the Rstudio API to figure out the location of the code: 

```R
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
```

If using the  [`config.R`](using-config-r) setup, this can be easily replaced with 

```R
setwd(rootdir)
```

or 

```R
setwd(file.path(rootdir,"code")
```

(if the file in question is in a subdirectory of the rootdir)
