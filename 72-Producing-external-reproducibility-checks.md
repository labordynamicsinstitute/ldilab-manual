(writing-an-external-report)=
# Writing an External Report

If you have agreed to provide us with an external reproducibility check, we kindly ask that you follow these instructions.

## The manuscript, code, and data are confidential at this stage

Do not post them to any public place. Use the resources we provide you with, or those that your institution provides you with. While we may provide you with Github or Bitbucket repositories, those are to remain private, i.e., require a login for access. 

Once you have completed the task and sent us the report, delete all data and code when told to do so (don't do this immediately, as we may have clarifying questions).

## Use a separate environment to run the code where possible

While you *can* use your laptop, you should follow certain procedures to both not affect the reproducibility check nor affect your usual working environment. Notes below.


## Access to code and data

You may have been provided access to code in two different ways

::::{tab-set}

:::{tab-item} openICPSR link

You may have been provided with a link to openICPSR. If so, you should download the code and data from there. 

:::  

:::{tab-item} Bitbucket link


In rare cases, we may provide you with the code in a Git repository (the data will be separate). If you have questions on how to use Git, please let us know, and we will help and guide you.

> You should NOT use the file upload or download capability of the web-based interface (i.e., Github.com, Bitbucket.com).

:::

::::


## Follow the procedures in the authors' README

You should follow instructions as closely as possible. However,

- you are not required to do extremely tedious or time-intensive manual steps.
- you are not required to "bog down" your personal laptop (see resources)
- you should lightly improve on the procedures, by following our replication procedures (below)
- you are not required to install software or packages that might mess up your own research

## Reproduction procedures

In addition to any setup instructions from authors, a few things to take into account

- Use the resources we provide you with, where possible
- Use the procedures to use "config.do" or similar files. 
  - This is always possible for Stata. See [instructions](stata-related-procedures). 
  - Similar procedures are available, to some extent, for R (use separate libraries, if possible, or the `renv` or similar packages). See [instructions](r-related-procedures).
  - Similar procedures are possible for Python and Julia (use `environments`)
  - Matlab and SAS will always use whatever is installed system-wide - this is a known caveat.

## Log everything

Create a log file, if possible, for every run.

- For Stata, our [template config.do file](https://github.com/AEADataEditor/replication-template/blob/master/template-config.do) will handle this, if used correctly. See [instructions](using-config-do).
- For R, use "R CMD BATCH" to run code, even when using Rstudio (use the Terminal tab). See [instructions](running-code-in-r).
- For Matlab, where possible, use the command line method of launching it. See [instructions](matlab-related-procedures). Alternatively, use "`sink`", but note that it might interfere with some programs.
- For Julia and Python, we have no good solutions other than to use the command line where possible, and capture the output.

Keep every log file: you will send them to us with the report (or commit them, if you are working in a Git repository we provided).

## Document everything

Keep a journal of what you are doing. You should be able to point to the journal, together with a log file or screenshots, to document problems, and how you solve them. 

An example:

>
> - Downloaded code and data from openICPSR
> - Added line to use `config.do`
> - Ran `main.do`  as instructed by the author
>   - I used the "right-click" method on Windows
> - Code stopped at the third step, looking for package `xyz`
> - Added the package to the relevant section in `config.do` so it would get installed, and ran the entire `main.do` again
> - Programs finished but no figures were output. Inspection of the code showed that they only display on-screen. Added `graph export` as PNG files at all relevant parts, then ran entire `main.do` again.

If the authors' instructions say to "view" something interactively, investigate native methods (`graph export`) to capture the information. Otherwise, use screenshot to capture the information. Make a note of that, too.

## Keep all logs, outputs, etc.

Keep all logs and outputs, but not data. You will send them to us together with the report. If you are working in a Git repository we provided, commit them to Git instead.

## Compile a report

Our standard report template is [EXTERNAL-REPORT.md](https://github.com/AEADataEditor/replication-template/blob/master/EXTERNAL-REPORT.md) ([Word version](https://github.com/AEADataEditor/replication-template/blob/master/EXTERNAL-REPORT.docx)).

- Don't forget to report your computer and software configuration
- You may fill out either the Markdown or the Word version. There is no need to convert it to PDF.

## Send a report

Send the completed report by email, together with the log files and outputs (zipped, if there are many). 

::::{warning}

If any logs or outputs contain confidential information, or are too large to send by email, ask us how to transmit them, and check with the data custodians..

::::

:::{note}

 Please "reply-all" to the email you received.
:::

:::{admonition} If we provided a Git repository...
:class: note dropdown

If, in rare cases, we provided you with a Git repository, commit the report, logs, and outputs to that repository instead, and send an email notification that all is complete.

:::

## Final confirmation

We will confirm to you when we have exhausted all our questions, at which point we will ask you to delete all code and data.

## Wrap-up: Delete all code and data

Once you have completed the task, sent us the report (or committed it to the Git repository we provided), AND have answered all of our clarifying questions, please delete all data and code that you received from us.


