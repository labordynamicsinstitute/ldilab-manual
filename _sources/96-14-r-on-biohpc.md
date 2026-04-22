(r-on-biohpc)=
# Running R on Linux systems

Linux allows us to run specific versions of R, but may also pose particular challenges when it comes to installing packages. 

:::{admonition} BioHPC specific
:class: note

See [R notes for BioHPC](https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=37#c).

:::

## Specific versions of R

You may either need to use `module` or `docker` to run specific versions of R. Both can work on BioHPC.


:::{admonition} BioHPC specific
:class: note

Use `module avail` to see which versions of R are available. Use `module load R/4.2.1-r9` to load a specific version.

:::

## Installing packages

### R Packages Through CRAN

R on Linux will usually install packages from CRAN, and compile from source. This may be feasible to circumvent by using [Package Archives](https://packagemanager.posit.co/client/#/), and defining the specific operating system you are using.


:::{admonition} BioHPC specific
:class: note

BioHPC uses `Rocky Linux 9`.

:::

This is the default for `rocker/` provided Docker images.

### R Packages through Conda

On BioHPC, installing packages through R can fail, with errors such as 

```

----------------------------- ANTICONF -------------------------------
Configuration failed to find libgit2 library. Try installing:
 * brew: libgit2 (MacOS)
 * deb: libgit2-dev (Debian, Ubuntu, etc)
 * rpm: libgit2-devel (Fedora, CentOS, RHEL)
If libgit2 is already installed, check that 'pkg-config' is in your
PATH and PKG_CONFIG_PATH contains a libgit2.pc file. If pkg-config
is unavailable you can set INCLUDE_DIR and LIB_DIR manually via:
R CMD INSTALL --configure-vars='INCLUDE_DIR=... LIB_DIR=...'
-------------------------- [ERROR MESSAGE] ---------------------------
<stdin>:1:10: fatal error: git2.h: No such file or directory
compilation terminated.
----------------------------------------------------------------------
```

This occurs since libraries on BioHPC are often installed in directories which R does not expect. To solve this, we use conda. Conda handles dependencies of both R packages and other libraries. See installation details [here][https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=574#c]. To create a conda environment, run the command

```
conda env create --name <name> r-base=<version>
```

- This creates a conda environment with the proper R version installed. After activating the environment, install R packages with the command

```
conda install conda-forge::r-tidyverse
```

R packages on conda often follow the format `r-<package>`. You can search for packages [here][https://anaconda.org/]. 

On Anaconda, R packages are often hosted by the R repository, and conda-forge. Packages from the R repository tend to be pickier about version compatibility than those from conda-forge.


## Errors

### Package not available

If you get 

```
3: package ‘NameOfPackage’ is not available for this version of R
```

check

- the package may have been obsoleted, and removed from CRAN. You may need to use [Package Archives](https://packagemanager.posit.co/client/#/), or [versioned installers](https://rdrr.io/cran/remotes/man/install_version.html):

```R
install_version("mypackage", "1.15") 
```

- your version of R is too young (see above for specific versions)
- your version of R is too old (see above for specific versions)

### MRAN no longer available

Some older packages may attempt to use MRAN - the "Microsoft R Application Network". This was shut down on July 1, 2023 (see [this notice](https://techcommunity.microsoft.com/t5/azure-sql-blog/microsoft-r-application-network-retirement/ba-p/3707161)).

Solution: Switch to [Posit Package Manager (PPM)](https://packagemanager.posit.co/client/#/).
