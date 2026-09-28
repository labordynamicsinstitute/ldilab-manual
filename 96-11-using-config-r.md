(using-config-r)=
# Using template-main.R in R

In "Verification" stage, we ask you to keep a log of what you do. Moreover, authors often use packages that are not default programs of R, and increasingly use `renv` to pin package versions. We provide `template-main.R` in the [template repository](https://github.com/AEADataEditor/replication-template) you clone which addresses these problems. In contrast to the Stata `config.do` file, this file both configures the environment **and** runs the author's code (a "main" file). In this section, we will walk you through how to set up `template-main.R`; in the [next section](running-code-in-r), how to run it in a way that generates log files automatically.

::::{warning}

If the authors use `groundhog` or another package management system that is not `renv`, you should NOT use `template-main.R`. Instead, follow the author's instructions for setting up the environment, and proceed to [running code in R](running-code-in-r).

If the authors use `renv`, you should still use `template-main.R`. It  detects and restores an author-provided `renv.lock` automatically (see [below](template-main-renv)).

::::

## Why do we have to install programs?

- R, or other statistical software, does not provide all the packages (or "libraries", or "modules") that enable or facilitate the analysis. Therefore, many user-written programs or extensions are publicly available for downloads. For R, this is most often comes from [CRAN](https://cran.r-project.org/), but the specific "mirror" of CRAN that is used may vary. You install packages with something like `install.packages("package name")` or multiple packages with `install.packages(c("package1","package2"))`. You might also see the use of `remotes::install_github("r-lib/conflicted")` (to install a package from Github) or `install_version("devtools", "1.11.0")` to install a specific version.
- We differ in installation process from many others in the sense that, we want to install programs in a specified directory that is NOT a system directory.
    - This is to ensure that the set of packages used by replication package is complete. A complete replication package should be stand-alone, regardless of packages installed elsewhere in the machine that program is run on.
    - `template-main.R` achieves this using `renv`, which creates and manages a project-local package library automatically — you do not need to configure this yourself.

## Explaining template-main.R

Start by copying `template-main.R` into the authors' code directory, renaming it to `main.R`. The top of the file has a few things to configure. Everything below a clearly identified line normally does not need to change.

### Step 1: Packages

Any libraries identified by the authors as needing manual installation (i.e. that the author's own code does not already install) should be listed here, in double-quotes, comma-separated.

```
readme.libraries <- c() # ex: c("paletteer", "viridis")
```

For instance, if the authors say you need `ggplot2` and `nonsenseR`, then add them to this line (and remember to keep case exactly as the authors provide it, so `nonsenser` is not the same as `nonsenseR`).

```
readme.libraries <- c("ggplot2","nonsenseR")
```

These packages will be installed into the project's `renv` library, so they are picked up correctly by `renv::snapshot()` at the end of the run.

### Confidential data location

In some cases, authors provide us privately with data that is not part of the public replication package (the part on openICPSR is generally public). We put this on the Z-drive, or what used to be called the S-drive. Put the location of that here, if any:

```
sdrive <- "Z:/Workspace/aearep-9999-implicit-nda"
```

:::{note}

If you are working on Windows (e.g. CCSS-Cloud) then you would need to use `/` or `\\` to write filepaths or use the file.path() function. So, for example, the above would become:

```
sdrive <- "Z:\\Workspace\\aearep-9999-implicit-nda"
```

:::

Wherever the author later references the confidential data, you can insert this placeholder, for instance:

```
# original author reference
# ols.data <- readRDS("data/confidential/analysis.Rds")
# you change it to
ols.data <- readRDS(file.path(sdrive,"data/confidential/analysis.Rds"))
```

### Step 3: Script order

Add all author R scripts to `author.programs`, in the order specified in the README. If the author provides a main or master file, likely only that file needs to be added:

```
author.programs <- c(
  "code/pull_race_from_name.R"
)
```

or, for multiple scripts:

```
author.programs <- c(
  "code/01_data.R",
  "code/02_analysis.R",
  "code/03_figures.R"
)
```



### Step 4: Make sure this script carries over

Check any author scripts you're adding to `author.programs` for lines like `rm(list = ls(all = TRUE))`. Because `source()` runs in the calling (global) environment, such a line would clear everything `template-main.R` just set up — including `rootdir` — partway through the run.

:::{admonition} Caution:

Comment these lines out in the author's scripts:

```R
# rm(list = ls(all = TRUE))
... (rest of code)
```
:::

(base-root-directory-r)=
### Base (root) directory

The base directory (or here, `rootdir`) is the directory that contains the replication package, as intended by the author. How do you figure that out?

**Example 1:**

```
aearep-9999/
    123456/
        Replication-package/
            code/
            data/
            README.pdf
```

In this case, the base directory is `aearep-9999/123456/Replication-package/`.

**Example 2:**

```
aearep-9999/
    123456/
        code/
        data/
        README.pdf
```

In this case, the base directory is `aearep-9999/123456/`.

You do not actually need to hard-code this in `template-main.R`. We will use a package called `here`, which can detect this automatically, **if** some files are present:

- The author has a `rproj` file - it will take that as the base directory.
- The (hidden) file `.here` is present - it will take the directory that contains that as the base directory.

The `here` package will get confused by the presence of **our** git setup, so if the two above files are not present, we need to manually create the latter:

```bash
cd 123456/Replication-package
```

or

```bash
cd 123456
```

and then

```bash
touch .here
git add .here
```

depending on the case. Now R will set the root directory correctly.

:::{note}

If for some reason that does not work, simply override the automatic detection, by setting the `rootdir` manually, using `/` or `\\` as appropriate for your OS:

```
rootdir <- "C:/user/Workspace/aearep-9999/123456/Replication-package"
```

:::

### Directories to create

`template-main.R` creates a `logs` subdirectory by default, but does not automatically create any other output directories the author's code may expect. Add any additional directories that your debugging identifies as being necessary. Do write any path names with `/`, not `\`.

```
create.paths <- c("logs")
```

For instance, if the authors state that output should be written to "outputs", you can add

```
create.paths <- c("logs","outputs")
```

`template-main.R` will create these directories if they do not exist.

## What template-main.R does for you automatically

Everything below the ASCII-art divider in `template-main.R` runs without edits. It is useful to understand what it does, in case something goes wrong.

(template-main-renv)=
### Package management with renv

`template-main.R` now manages packages with [`renv`](https://rstudio.github.io/renv/) automatically:

- It searches up to one directory level up and one level down from `rootdir` for an author-provided `renv.lock` file.
- If one is found, it runs `renv::restore()` against that lockfile, so the exact package versions the author used are installed into a project-local library.
- If none is found, it initializes a blank, project-local `renv` project instead, so packages you add via `readme.libraries` are still isolated from the rest of the machine.

This means you no longer need to special-case authors who use `renv` — the same `template-main.R` handles both cases. (Authors using `groundhog` or another non-`renv` system are still out of scope; see the warning at the top of this page.)

### Package installation source (Posit Package Manager)

For packages that are not already pinned by an author's `renv.lock`, we use the Posit Package Manager (PPM), which provides date-based snapshots. `template-main.R` picks a date about a month in the past, adjusts it off weekends (PPM does not snapshot then). The first time it runs, it writes that date to `logs/posit_date.txt`. Every subsequent run of the same replication package reuses that stored date, so re-running after adding packages stays consistent with the first run.

:::{note}

If the stored date is causing problems, delete `logs/posit_date.txt` to regenerate it, or set `posit.date` manually in the script.

:::

### System information and the final snapshot

`template-main.R` records `Sys.info()`, `R.version`, and `sessionInfo()` as part of the log. After the author's programs have been sourced, it  writes a `renv.lock.replicator_snapshot` file, capturing the exact packages used during the run — without overwriting the author's original `renv.lock`, if any.

## How to use template-main.R

### Rename the file

The template is called `template-main.R`. Rename it to `main.R` and put it into the folder that the author says to run the code from (or next to an existing author main file, if one exists — see [Step 3](#step-3-script-order) above for how to fold that into `author.programs`).

> **[ACTION]** Check the README or the repository and determine what the authors' code entry point(s) are, and list them in `author.programs` in the correct order.

Once `readme.libraries`, `sdrive`, `author.programs`, and (if needed) `rootdir` and `create.paths` are set, `main.R` is ready to run — proceed to [running code in R](running-code-in-r).
