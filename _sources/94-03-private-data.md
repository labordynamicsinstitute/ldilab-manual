## Accessing privately provided data

### When there is privately provided data

In some cases, authors will provide us privately with data we cannot publish.

```{block, type='rmdcomment'}
VERY IMPORTANT: You must treat these data as confidential, never remove them from CISER!
```

You will know where the data are by looking at the JIRA issue. You will often (but not always) see a **subtask** which we use to request the confidential data:

![subtask for confidential data](/images/jira-subtask-restricted.png)

You should then look into the "`Data`" tab for the field `Working location of restricted data`:

![JIRA field for location: S:\LDILab\aearep-3756-nda_Implicit](/images/jira-field-restricted-data.png)


### How to prepare privately provided data

- Log into CISER as usual. You should never need to run code elsewhere when data are restricted/privately provided.
- Open the File Explorer
- Under "`This PC`", click "`Share (\\rschfs2x.ciserrsch.cornell.edu)`" under `Network Locations`. This location is also available as "`S:`".
- Find the `LDILab` folder. (You should probably bookmark/ add to favorites) 
- Within that folder is the corresponding restricted access data (e.g. `aearep-3756-nda_Implicit`)
   - If you cannot open the `LDILab` folder, contact the assistant to the Data Editor 
- If there is a ZIP file (looks like a folder, but is not), right-click and choose `Extract All` before working in the folder
- Remember the full location. This should correspond to what is entered in to the JIRA field, e.g., `S:\LDILab\aearep-3756-nda_Implicit`.

### How to use the data in this folder

There are two situations. 

1. The folder contains ONLY the confidential data. This *should* normally be the situation...
2. The folder contains a copy of the openICPSR deposit, but with the confidential data included.

There are two ways to run code using the data in this folder:

1. Run all programs within this folder, do not take the data out of this folder. However, you will need to transfer log files and output back to your regular "cloned" folder (i.e. `aearep-3756`).
2. More robust, but a bit more work, is to modify the code to reference the confidential data every time it is called.
  - In the `config.do`, is a line `global sdrive ""`. Modify that line to read `global sdrive "S:/LDILab/aearep-3756-nda_Implicit"`
  - Run the code in its usual location. When the code encounters (absent) confidential data in the usual location, it will break/stop.
  - Everywhere you encounter references to confidential data in the code, e.g., `use "${datadir}/mysuper.dta"`, modify the code to reference the S-drive: `use "${sdrive}/mysuper.dta`. 
  - commit all code modifications and log files as you normally would.
