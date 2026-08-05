(helpful-scripts)=
# Various helpful scripts

The Lab has two sets of auxiliary scripts. They are made available in different ways.

## Replication template tools

The [replication template](https://github.com/AEADataEditor/replication-template) provides a variety of scripts to assist with common tasks. These scripts are available in the `tools/` folder in each repository. 

> Detailed documentation can be found at <https://aeadataeditor.github.io/replication-template/tools/>



:::{note}

If you do not see a script referenced there, or the script does not behave as intended, you may need to **update** the scripts.

1. `git commit` all changes, and `git push` them
2. Run the `Refresh repository` script in Bitbucket.
3. `git pull` in your local copy to get the latest scripts.

:::

## Editor scripts

We have a bunch of scripts, some of which can make your life easier, see the [dedicated page](editor-scripts).

:::{note}

Here too, frequent updates are made. To update the scripts, 

1. `cd $HOME/bin`
2. `git pull`
3. `./install.sh` (will re-install and update Python scripts)

:::