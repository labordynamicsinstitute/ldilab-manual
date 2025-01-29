(debugging-r)=
# Debugging R

See below, or [our wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/R-Tips).

## Library installation problems

> You are not allowed to install packages in C: because you do not have administrator rights.

This will happen on computers where you are a guest (not the owner), for instance CCSS Cloud or RedCloud.

### Solution:

Run the following in an R console (or the console in Rstudio):

```r
dir.create(Sys.getenv("R_LIBS_USER"), recursive = TRUE)  # create personal library
```

Then restart R, and try the install again.

## Using different versions of R

For Linux, see [R on Linux](r-on-biohpc).

For Windows and MacOS, when using Rstudio, see [Rstudio help pages](https://support.posit.co/hc/en-us/articles/200486138-Changing-R-versions-for-the-RStudio-Desktop-IDE). 

:::{admonition} Note that this only works if there is, in fact, another R version installed. 
:class: note dropdown

You can find older versions of R at [CRAN](https://cran.r-project.org/bin/windows/base/old/). To install, simply run the program, select an installation location under `C:\Users\[YOUR USER NAME]\AppData`, and uncheck any additional checkboxes during the installation process. You can then **browse** from the `R Selection Dialog` mentioned at the [Rstudio help pages](https://support.posit.co/hc/en-us/articles/200486138-Changing-R-versions-for-the-RStudio-Desktop-IDE) to find that version of R. 

:::

## Pathnames

Use **single** forward slashes everywhere ([source](http://www.dummies.com/programming/r/how-to-work-with-files-and-folders-in-r/)):

For a Windows path that would read `F:\\rschfs1x\userRS\F-J\XXXX_RS\Documents\Workspace\app.20160004`, use 

```r
lest<-read.dta("F:/rschfs1x/userRS/F-J/XXXX_RS/Documents/Workspace/app.20160004/ddd_long.dta")
``` 

Even better, use the `file.path()` function:

```r
rootdir <- "F:/rschfs1x/userRS/F-J/XXXX_RS/Documents/Workspace/app.20160004"
lest    <- read.dta(file.path(rootdir,"ddd_long.dta")
```

Even better better, use the `here()` function used in the `config.R` (see notes in the file on how to create the `.here` file).

```r
rootdir <- here()
lest    <- read.dta(file.path(rootdir,"ddd_long.dta")
```

## Package Dependency - if you want to use an earlier version of a package

The trick is to use the COPY of the CRAN repository at <strike>Microsoft, called the MRAN.</strike> Posit/Rstudio, called the "[Posit Package Manager](https://packagemanager.posit.co/)". 

At the top of any R code  add the following lines:

```
ppm.date <- "2019-09-01"
ppm.url  <- "https://packagemanager.posit.co/cran/"
options(repos=paste0(ppm.url,mran.date,"/"))
```

:::{note}
Even better, the `config.R` already has lines like this, use them!
:::

You should use a judicious "`ppm.date`", probably based on the date JUST prior to the release of the next version of R. You can look up those dates [here](https://cran.r-project.org/bin/windows/base/old/).

So for instance, if you want the last MRAN date prior to the release of R 4.0, you might choose "2020-03-15" (mid-March, prior to the release of R 4.0). At that time, the latest R version was R 3.6.3.

You should then be able to install packages in a version that is compatible with R 3.6.3 from the MRAN.

All package install functions in R should work "as-is", unless they explicitly download github versions or similar ("`remotes::install_github()`" or similar).

### Special note for BioHPC 

On BioHPC, which runs a Linux version called "Rocky 9.0", you should use the following instead:

```
ppm.date <- "2019-09-01"
ppm.url  <- "https://packagemanager.posit.co/cran/__linux__/rhel9/"
options(repos=paste0(ppm.url,ppm.date,"/"))
```

This will (hopefully) install pre-compiled packages, rather than trying to compile every package from source, which is a LOT faster.


## `trying to use CRAN without setting a mirror`

For example,

```
install.packages("reshape2")
Installing package into 'C:/Users/Mbrown_RS/AppData/Local/R/win-library/4.2'
(as 'lib' is unspecified)
Error in contrib.url(repos, "source") :
  trying to use CRAN without setting a mirror
```

If you get this error, you need to set a CRAN repository within R. The best way is to set it globally, once and for all (as per [this note](https://www.r-bloggers.com/2011/11/permanently-setting-the-cran-repository/). You can do this by manually editing the `.Rprofile` file, or simply running the following command:

:::{note}
Even better, this is already configured  in the `config.R` - use it!
:::

```bash
echo '# set the default repository
local({
  r <- getOption("repos")
  r["CRAN"] <- "https://cran.rstudio.com/"
  options(repos = r)
})
# create the local library if it does not exist
if ( !file.exists(Sys.getenv("R_LIBS_USER") ) ) {
   dir.create(Sys.getenv("R_LIBS_USER"),recursive=TRUE)
} ' > $HOME/.Rprofile
```

but see about the correct setting for `r["CRAN"]` [here](#package-dependency---if-you-want-to-use-an-earlier-version-of-a-package)


