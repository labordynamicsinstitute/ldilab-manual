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

R on Linux will usually install packages from CRAN, and compile from source. This may be feasible to circumvent by using [Package Archives](https://packagemanager.posit.co/client/#/), and defining the specific operating system you are using.


:::{admonition} BioHPC specific
:class: note

BioHPC uses `Rocky Linux 9`.

:::

This is the default for `rocker/` provided Docker images.



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