(debugging-stata)=
# Debugging Stata

Also check the [LDI Replication Lab Wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Stata-Tips)!

## Basic debugging

### Ado files not found

**Issue:** When an error message such as `xml_tab command not recognized` or `outreg2 command not recognized` appears...

**Solution** it usually means that you need to first install the command before running the .do file. Try

```
ssc install outreg2
```
or possibly 
```
search this_great_command
```
followed by
```
net install  this_great_command, from(https://this_great_command.com/stata)
```
In some cases, this will be a reference to the Stata Journal packages, which do NOT have the same name as the command they provide:

```
search frmttable
```

yields:
```
Search of official help files, FAQs, Examples, and Stata Journals
-----------------------------------------------------------------

SJ-12-4 sg97_5  . A programmer's command to build formatted statistical tables
        (help frmttable if installed) . . . . . . . . . . . . . . J. L. Gallup
        Q4/12   SJ 12(4):655--673
        create formatted tables from statistics and write them to
        Word or LaTeX files
```

Further below, you see this in a different way:

```
5 packages found (Stata Journal listed first)
---------------------------------------------

sg97_5 from http://www.stata-journal.com/software/sj12-4
    SJ12-4 sg97_5. Update: A programmer's command... / Update: A programmer's
    command to build / formatted statistical tables / by John Luke Gallup,
    Portland State University / Support:  jlgallup@pdx.edu / After
    installation, type help frmttable
```

Now you see how to construct this with a one-line net install command:

```
net install <pkgname>, from(<pkgurl>)
```

where you replace `<pkgname>` with the name of the Stata Journal package (here: `sg97_5`) and the `from()` command gets the URL that is listed in the help.

For `frmttable`, this yields:

```
net install sg97_5, from(http://www.stata-journal.com/software/sj12-4)
```


:::{warning}

_Please be sure to make a note of this installation in the REPLICATION.md!!_

You must include all these commands in the `config.do`. For all `ssc install` commands, add them to the appropriate line at the top of the `config.do`.

:::


:::{admonition} **Great tip:**
When searching for a package, the Stata help browser will show in the address bar "`net describe  this_great_command, from(https://this_great_command.com/stata)`. Simply copy and paste into your `config.do` and change `describe` to `install`.
:::



#### unknown egen function wtmean()

Add package `_gwtmean` to the `config.do`, or `ssc inst _gwtmean`

#### unknown egen function .... 

Add package `egenmore` to the `config.do`

#### struct_ ms_vcvorthog undefined (`ivreghdfe`)

You may find this with `ivreg2` or `ivreghdfe`:

```
struct ms_vcvorthog undefined
(817 lines skipped)
(error occurred while loading ivreghdfe.ado)
r(3000);
```

Solution: Ensure that you are using the `config.do` correctly, your `config.do` installs the relevant package (`ivreg2`, `ivreghdfe`, etc.), and that `ranktest` is also included. The code in the `config.do` that calls 
```
mata: mata mlib index
```
should fix any additional issues.

#### Last estimates not found (`ivreghdfe`,`reghdfe`)

If you then get 

```
last estimates not found
```

try installing from the Github website for `ivreghdfe` (see [this link](https://github.com/sergiocorreia/ivreghdfe/issues/54#issuecomment-1988774628)):

:::{warning}
These commands should be included in the `config.do`!
:::

```
* Install ftools (remove program if it existed previously)
cap ado uninstall ftools
net install ftools, from("https://raw.githubusercontent.com/sergiocorreia/ftools/master/src/")

* Install reghdfe
cap ado uninstall reghdfe
net install reghdfe, from("https://raw.githubusercontent.com/sergiocorreia/reghdfe/master/src/")

* Install ivreg2, the core package
cap ado uninstall ivreg2
ssc install ivreg2

* Finally, install this package
cap ado uninstall ivreghdfe
net install ivreghdfe, from(https://raw.githubusercontent.com/sergiocorreia/ivreghdfe/master/src/)

* Rebuild mata library index
mata: mata mlib index
```

This problem is *always* fixable, contact your Team lead if you run into persistent problems.

#### `assert_msg() not found` (`reghdfe`)

This seems to happen when an older version of `reghdfe` is run (i.e., with `version(3)` flag). One solution appears to be to 

- install the latest version of `reghdfe` etc. from Github (see above)
- Add the command `ftools, compile` before the `mata: mata mlib index` line in the `config.do`



#### `reg2hdfespatial` and `ols_spatial_HAC`

These programs are usually included. If they are not, they can be installed using the following commands:

```
cap mkdir reg2hdfespatial
copy http://www.trfetzer.com/wp-content/uploads/reg2hdfespatial-id1id2.ado reg2hdfespatial/reg2hdfespatial.ado
copy https://www.dropbox.com/s/pf2vtvgqhjk7rc8/spatial_HAC.zip?dl=1 spatial_HAC.zip
unzipfile spatial_HAC.zip // should create a directory "spatial_HAC"
local pwd : pwd
adopath ++ "`pwd'/spatial_HAC"
adopath ++ "`pwd'/reg2hdfespatial"
```


#### Installing grc1leg

If you encounter the `grc1leg` package, it cannot be installed by `ssc install grc1leg`. Use the following:
```
net install grc1leg, from("http://www.stata.com/users/vwiggins/")
```


## Exporting Graphs

If a manuscript contains figures but the authors do not include code to automatically export those figures, there exists very straightforward code to fix this.

Stata package information: [Stata Manual](https://www.stata.com/manuals13/g-2graphexport.pdf).

Syntax:
> graph export newfilename.suffix [, options]

Example:

> graph export Figure.pdf

> graph export Figure.png


### I want to run my program in an older version of Stata?
  
Use the [version](https://www.stata.com/manuals/pversion.pdf) command to emulate running the program on an older version. For example, to emulate Stata 12.1, use the following line:  

```  
version 12.1 
```  

This fix may be relevant when running into problems with the tobit regression. This does not always work. We have some other, somewhat more involved solutions, involving running [Stata in Docker](https://github.com/AEADataEditor/docker-stata) and have access to Stata versions 12, 13, 14, 16, and 17.

## MAIN DO FILE

### Running other do files

Some code has a main "`replication.do`" or "`main.do`" etc., which will have lines such as

```
do tables.do
```

This is a problem, because any parameters from main.do, such as changing where you install Stata packages (`sysdir PERSONAL "/path/to/somewhere"`) are lost...

Replace the above with

```
include "tables.do"
```
and you will be fine.

The difference is that the first one executes the `tables.do` in a somewhat fresh environment. The second one simply includes the code (as if copying-and-pasting) in the `main.do`, by reference, and thus inherits everything that is transient (such as tempfiles, etc.)

This may not always work - sometimes authors rely on that reset that happens when you use the `do tables.do` version. 

Always use `include config.do` for `config.do` files however. 


## Running Stata from the command line

It sometimes is more convenient to run Stata from the command line. How to do this varies by operating system. In almost all cases, you need to know where Stata is installed. 

- Windows: See [this Stata page](https://www.stata.com/support/faqs/windows/batch-mode/). In essence, on CISER nodes, navigate to the directory where the Stata program you want to run is located (here: `master.do`). Then, in the address bar of the file browser, type `powershell`. In the command line window, type

```
& 'C:\Program Files\Stata16\StataMP-64.exe' /b do .\master.do
```

will run the program, and create a logfile `master.log` (and any configured log files). Note that you can also right-click and request "Run (silently)".

- Linux/MacOS: Similar to the Windows instructions, in a terminal, navigate (`cd /path/to/directory`) to the directory with the program you want to run. Most Linux systems will have the Stata command in the "path", meaning it will be automatically found. 

```
stata-mp -b do master.do
```

will run the program.


## Stata Errors

### `Varlist required` error:

* May occur if the author calls upon a varlist that s/he forgets to define. Check the other .do files to see if it has been defined elsewhere. If the definition is obvious (based on the article & data) insert a line of code defining it yourself.

### `Too many values` error:
(SOLUTION?)

### `Varlist not allowed` error:
(SOLUTION?)

### `Maxvar too small` error:

* Run .do file using Stata-MP and add `set maxvar 32767` (maximum number of variables) to the `config.do`.

### `File ___ could not be opened` error:

* May appear after the `esttab` command, or when Unix and Windows paths are mixed, or when running with Network paths (of style `\\network\path\to\folder`)

```
esttab using "$res/Cage_Rueda_Table_4.tex"
```

*Solution 1* (most likely)

The directory `$res` has one or more elements that are missing (ie a subdirectory does not exist). For instance, if `$res` resolves to `D:/project/tables` but the subdirectory `tables/` does not exist, Stata will fail.

You need to create the directory, as part of the code (and make a note of this in the report). Add the following line above the problematic line, or in the `config.do`:

```
cap mkdir "$res"
```

(NOTE: this will *still* fail if there are additional parts of the path that do not exist.)

*Solution 2* (preferred if Solution 1 does not solve the problem)

Verify that `$res` does not contain a Windows "network path" (`\\rschfs\users\A-K\fellow\project`). Rather, it should contain a "letter drive" (`D:/project`). On Unix systems, it may help to remove relative paths (`../project`) and use a fully-qualified path (`/home/user/fellow/project`)

> For reference: Filed with the package author on [Github](https://github.com/benjann/estout/issues/58)

If `$res` does actually contain a Windows network path, install the newest Github version of `estout`:

```
net install estout, replace from(https://raw.githubusercontent.com/benjann/estout/master/)
```

(this is also an optional install in the LDILab's `config.do`).


### `Options IK, CCT, and CV have been deprecated` error:

May occur when using the `bwselect()` option after the `rdrobust` command. To fix this an older version of the `rdrobust` command must be installed. Install this by typing 
```
net install st0366.pkg, from("http://www.stata-journal.com/software/sj14-4/") 
```
into the `config.do`. _Don't forget to make a note of this in the Replication.txt!!_



### Problems with "xi" command:

The outdated command xi may sometimes cause errors that cannot be remedied by using an older version of Stata. To update the syntax follow this example:

```
xi: gen i.year i.adjustedmsc
```
This line of code currently produces the error message "invalid name". Correct this by dividing up the command into:
```
xi i.year
xi i.adjustedmsc
```
### Problems with the "kdens" command:

May require the installation of `kdens` and possibly `moremata`.

### .tex files cannot be opened 

(this is a variant of the "`File ___ could not be opened` error")

**Basic idea**: Try setting your global directory (however that is specified in the code) to reference the name of the local drive on CISER. 

Instead of setting the directory as something like: 
`\\rschfs1x\userRS\K-Q\msw274_RS\aea_workspace\stata-training-redo\aer_replication`

Replace the beginning part with (where anything after the U: is going to be specific to your project and set up): 
`U:/aea_workspace/stata-training-redo/aer_replication`

**Suggested solution**

- Make the following modifications to the "config.do"
- modify, if necessary the last line (where "global rootdir" is set) to reference the local drive on CISER 
global rootdir "U:/Documents/Workspace/aearep-950/112343/replication_package"
Note the use of "/" instead of "\" - please always do so.
- if the use of esttab using "$rootdir/output/table.tex" does not work, then try the next solution. Otherwise, you are done.
Note the use of the quotes! they are important in this case, because the path contains spaces!

**Expanded solution:**
- add a line global texdir "${rootdir}/output" (preferred) or the full path, to the BOTTOM of the config.do 
- then replace  esttab using "$texdir/table.tex"

If you do it like that, your modified programs will never have your personal path in the program code, only $rootdir and $texdir. Those are defined in the "config.do", and are easy to change by the next replicator.

## Specific to certain systems

### RedCloud

#### Problems with temp files

Some (user-written) Stata packages do improper handling of Windows network paths. This affects the use of temp files.

**Symptom**

```stata
> graph ..., saving(`tempfile')
(file \\rschfs2x\share\statatemp\ST_7390_000002.tmp not found)

file \\rschfs2x\share\statatemp\ST_7390_000002.tmp saved as .gph format

...
> graph combine `tempfile` other_file.gph, ...

file \rschfs2x\share\statatemp\ST_7390_000002.tmp not found
```


(the error is not specific to the `graph` command). Note the missing double-backslash in the path.

**Solution**

You need to redirect the STATATMP directory to a non-networked drive. 
Use a terminal, and set the `STATATMP` variable before launching Stata. In all examples, we assume that the new directory is `U:\Documents\tmpdir`. If it doesn't exist, create it. The path to Stata may be different on different systems, use command line expansion to find the right path.

:::::{tab-set}

::::{tab-item} Bash

```bash
export STATATMP="/c/Users/$USERNAME/statatmp"
mkdir "$STATATMP"
cd "/l/workspace/aearep-5697/203501/Data and do-files"
"/c/Program Files/Stata18/StataMP-64.exe" -b master.do
```

::::


::::{tab-item} Powershell

```
$env:STATATMP="U:\Documents\tmpdir"
& 'C:\Program Files\Stata18\StataMP-64.exe'
```

::::

::::{tab-item}  Command Prompt

```
set STATATMP="U:\Documents\tmpdir"
'C:\Program Files\Stata18\StataMP-64.exe'
```
::::


::::{tab-item} Alternate

Use the "Permanent fix" described here:  https://www.stata.com/support/faqs/data-management/statatmp-environment-variable/

::::

:::::

This normally succeeds.



### CCSS Classic


#### When trying to install some extension Stata shows an error message such as: `_file c:\ado\plus\next.trk already exists_`

This issue usually occurs when running on a university system where you do not have rights to install to C:

**Solution:** Be sure you are including `config.do`, which has lines like


```
global basepath "/path/to/your/project/directory"
sysdir set PERSONAL "$basepath/ado/personal"
sysdir set PLUS "$basepath/ado/plus"
```

where you would create a "ado" directory in the "project" folder you are currently using for the replication (i.e., `..../10.1257/mac.12345/replication_netid/ado`). See  the [template-config.do](https://github.com/AEADataEditor/replication-template/blob/master/template-config.do).

Stata will then install the new extension into that directory instead of c:\ado\plus ([source](https://www.stata.com/support/faqs/programming/personal-ado-directory/) )
