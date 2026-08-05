(editor-scripts)=
# Installing AEA editor scripts

We have a bunch of scripts, some of which can make your life easier. See [https://github.com/AEADataEditor/editor-scripts](https://github.com/AEADataEditor/editor-scripts). You can make these available to your Bash shell by running the following command:

## First-time installation

### If you do not yet have a `$HOME/bin` directory

Check first if you already have a `$HOME/bin` directory:

```bash
ls -l $HOME/bin
```

If that yields an error, then you don't have one. So run the next part:

```bash
git clone https://github.com/AEADataEditor/editor-scripts $HOME/bin
cd $HOME/bin
./install.sh # installs some Python scripts
```

You should now have access to the various scripts, such as `aeagit` (a bash script) and `aea-parse-tags` (a Python script).


### If you already have a `$HOME/bin` directory

If you *do* have a `$HOME/bin` directory, you will need to manually adjust a few more things. Contact your supervisor.

## Updating the scripts


:::{note}

The scripts are actively updated frequently. To update the scripts, run

```bash
cd $HOME/bin
git pull
./install.sh # will re-install and update Python scripts
```

:::

## Debugging

If you see a notice like the following

::::{tab-set}

:::{tab-item} Windows

```
  WARNING: The scripts aea-box-clean-folders.exe, aea-box-recover-files.exe, aea-parse-tags.exe, aeagit-create.exe, aeagit-py.exe, jira-approval-manager.exe, jira-purge-query.exe, jira-status-manager.exe and zenodo-metadata-editor.exe are installed in 'C:\Users\lv39\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

:::
:::{tab-item} Linux/macOS 

:::
::::

then you must do what it says: Add the path where Python puts command line scripts so that your terminal can recognize them. (This applies to Bash shells).

To do so, from the command line, open VSCode and edit your `.bash_profile`, which is located  in your home directory. 

```bash
code $HOME/.bash_profile
```

Add the following line to the end of the file:


::::{tab-set}

:::{tab-item} Windows

Inspect the error message, and translate. If the error is

```
C:\Users\lv39\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts
```

then add the following line to the end of your `.bash_profile`:

```bash
export PATH="$HOME/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/Scripts:$PATH"
```

where you converted all the `\` to `/` and removed the `C:` drive letter, replacing your profile directory with `$HOME`.

:::
:::{tab-item} Linux/macOS

```bash
export PATH="$HOME/.local/bin:$PATH"
```
:::
::::

To activate the new path, you can "source" the `.bash_profile` file:

```bash
source $HOME/.bash_profile
```

or open a new terminal.