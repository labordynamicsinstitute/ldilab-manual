# External reproducibility checks

In some cases, reproducibility checks must be conducted externally—particularly when restricted-access data is involved. This section outlines how to integrate such reports and ensure they are properly archived in our systems.

## When External Reproducibility Reports Are Used

Instances that require the use of restricted-access data for a full reproducibility check can occasionally be sent out for an external report. These cases often arise when data cannot be shared with our team.

For more information, see the [AEA Policy and Protocol on Third-Party Verifications](https://aeadataeditor.github.io/third-party-verification-policy/), which describes who can conduct these external reports and the expected process.

> 🔒 In all cases where an external reproducibility check is used (e.g., CASCAD or World Bank), the **"external validation" checkbox in JIRA must be checked**.

## Integrating the External Report

The external report must be included in the repository. It is **not sufficient** to leave it attached to a JIRA ticket or email.

1. Start with the internal `REPLICATION.md` report.
2. **Do not delete** any section titles from the internal report.
3. In relevant sections, add a note such as:

   > “Please refer to the external report below.”

4. Review the external report and ensure all **bugs** and **discrepancies** are recorded in the **Summary and Findings** section of the internal report.

## Writing an External Report 

If you have agreed to provide us with an external reproducibility check, we kindly ask that you follow these instructions.

## The manuscript, code, and data are confidential at this stage

Do not post them to any public place. Use the resources we provide you with, or those that your institution provides you with. While we may provide you with Github or Bitbucket repositories, those are to remain private, i.e., require a login for access. 

Once you have completed the task, and sent back all changes you had to make, or sent us the report from a secure system, delete all data and code when told to do so (don't do this immediately, as we may have clarifying questions).

## Use a separate environment to run the code where possible

While you *can* use your laptop, you should follow certain procedures to both not affect the reproducibility check nor affect your usual working environment. Notes below.


## Access to code and data

You may have been provided access to code in two different ways

::::{tab-set}

:::{tab-item} openICPSR link

You may have been provided with a link to openICPSR. If so, you should download the code and data from there. 

:::  

:::{tab-item} Bitbucket link


We  provide you with the code in a Git repository (the data will be separate). If you have questions on how to use Git, please let us know, and we will help and guide you.

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

Once you have a log file, commit it.

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

## Commit all logs, outputs, etc. to Git

All logs and outputs, but not data, should be committed to Git. 

## Compile a report

Our standard report template is included: [external-REPORT.md](https://github.com/AEADataEditor/replication-template/blob/master/external-REPORT.md).

- Don't forget to report your computer and software configuration
- The report should be committed to git as well. There is no need to convert it to PDF.

## Send a report

Reports should be committed to git (**not** sent by email). An email notification that all is complete is sufficient. 

> Please "reply-all" to the email you received.

## Final confirmation

We will confirm to you when we have exhausted all our questions, at which point we will ask you to delete all code and data.

## Wrap-up: Delete all code and data

Once you have completed the task, and committed all changes to the Git repo we provide you with, or sent us the report from a secure system, AND have answered all of our clarifying quesitons, please delete all data and code. 


## Resources

You can have access to all the resources we regularly use:

::::{tab-set}


:::{tab-item} General

- [BioHPC compute cluster](https://biohpc.cornell.edu/lab/lab.aspx). If you do not have an account, request one. Even if you have an account, request to be added to the "lv39" lab.
- [CodeOcean](https://www.codeocean.com) - Don't forget to share with "dataeditor@aeapubs.org". Instructions are [here](https://labordynamicsinstitute.github.io/replicability-training-curriculum/access-to-computers.html#reproducibility-checks-in-codeocean)
- [WholeTale](https://labordynamicsinstitute.github.io/replicability-training-curriculum/access-to-computers.html#conducting-reproducibility-checks-on-wholetale)
- [Github Codespaces](https://github.com/codespaces) - with some caveats, talk to us
- Your laptop 

:::


:::{tab-item} Cornell-affiliated

- [CCSS ("CISER") compute nodes](https://ciser.cornell.edu/computing/computing-help/how-to-login/). If you do not have an account, request a Research account with "lv39" as sponsor. Do not use the restricted data access!

:::

::::

