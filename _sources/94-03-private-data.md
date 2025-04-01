# Accessing privately provided data

## When there is privately provided data

In some cases, authors will provide us privately with data we cannot publish.

```{warning}
VERY IMPORTANT: You must treat these data as confidential, never remove them from CCSS!
```

You will know where the data are by looking at the JIRA issue. You will often (but not always) see a **subtask** which we use to request the confidential data:

![subtask for confidential data](/images/jira-subtask-restricted.png)

You should then look into the "`Data`" tab for the field `Working location of restricted data`:

![JIRA field for location: S:\LDILab\aearep-3756-nda_Implicit](/images/jira-field-restricted-data.png)


## How to prepare privately provided data

::::{tab-set}

:::{tab-item} CCSS Cloud

- Log into remote desktop as usual.
- The restricted access data will be stored in the L drive. If you haven't mapped the L drive, do that first ([instructions here](https://labordynamicsinstitute.github.io/ldilab-manual/95-10-windows-remote.html)).
- Navigate to the folder `Restricted-Access-Data` and find the corresponding folder that is in the Jira field, e.g., `L:\Restricted-Access-Data\aearep-4400`.
- If there is a ZIP file (looks like a folder, but is not), right-click and choose `Extract All` before working in the folder

:::

:::{tab-item} CCSS Classic

- Log into CISER as usual. You should never need to run code elsewhere when data are restricted/privately provided.
- Open the File Explorer
- Under "`This PC`", click "`Share (\\rschfs2x.ciserrsch.cornell.edu)`" under `Network Locations`. This location is also available as "`S:`".
- Find the `LDILab` folder. (You should probably bookmark/ add to favorites) 
- Within that folder is the corresponding restricted access data (e.g. `aearep-3756`)
   - If you cannot open the `LDILab` folder, contact the assistant to the Data Editor 
- If there is a ZIP file (looks like a folder, but is not), right-click and choose `Extract All` before working in the folder
- Remember the full location. This should correspond to what is entered in to the JIRA field, e.g., `S:\LDILab\aearep-3756`.

:::


::::

## How to use the data in this folder

There are two situations. 

1. The folder contains ONLY the confidential data. This *should* normally be the situation...
2. The folder contains a copy of the openICPSR deposit, but with the confidential data included.

There are two ways to run code using the data in this folder:

1. Run all programs within this folder, do not take the data out of this folder. However, you will need to transfer log files and output back to your regular "cloned" folder (i.e. `aearep-3756`).
2. More robust, but a bit more work, is to modify the code to reference the confidential data every time it is called.
  - In the `config.do`, is a line `global sdrive ""`. Modify that line to read `global sdrive "L:\Restricted-Access-Data\aearep-3756-nda_Implicit"`
  - Run the code in its usual location. When the code encounters (absent) confidential data in the usual location, it will break/stop.
  - Everywhere you encounter references to confidential data in the code, e.g., `use "${datadir}/mysuper.dta"`, modify the code to reference the L-drive: `use "${sdrive}/mysuper.dta`. 
  - commit all code modifications and log files as you normally would.

## Examples

These are *simple* examples. Most situations will be more complex.

### Stata Example 1

Some replication packages make this very straightforward, usually by the inclusion of a global specifically set for a "`confidential`" data folder. It may contain an **original** master file that looks something like this...

#### Original master file

```
*					Master File							*
*														*
*********************************************************
*********************************************************

******************************************
*** Set-up the directories and install packages
******************************************

***set the working directory here:
global path "C:/Users/author/path"

*** The raw data folder contains two subdirectories, one for the public data and one for the confidential
global rawdata "$path/data"
global public "$rawdata/public"
global confidential "$rawdata/confidential"

global code "$path/code"
global results "$path/output"
```

#### Adjusting for LDI specific situation

1. Include the `config.do` in the master file as usual.
2. In the `config.do`, adjust the (existing) global for the L: drive: `global sdrive "L:\Restricted-Access-Data\aearep-4991-nda_Implicit"`. The global is defined at the very end of the `config.do`.
3. In the master file, incorporate the `rootdir` from the `config.do` as the main global `path`. This should reflect your workspace on the U: drive.
4. Incorporate the new global `sdrive` to set the authors' global `confidential`. 

#### Updated master file

```
*					Master File							*
*														*
*********************************************************
*********************************************************

include "config.do"

******************************************
*** Set-up the directories and install packages
******************************************

***set the working directory here:
global path "$rootdir"

*** The raw data folder contains two subdirectories, one for the public data and one for the confidential
global rawdata "$path/data"
global public "$rawdata/public"
global confidential "$sdrive/confidential"

global code "$path/code"
global results "$path/output"
```



