(setup-bash)=
# Setting up your Bash environment

The following setup applies to any computer you may be using to run Bash commands (except for CodeOcean).

```{note}
On Windows, this will be "Git bash". On Linux, you are usually using `bash`, but check with your sysadmin if you are unsure. On MacOS, newer versions have changed the default shell to `zsh`, which should work mostly the same. It is possible to use the `bash` shell there as well. 
```

## Configure the openICPSR download script and Bitbucket access

First, create a [Bitbucket PAT](bitbucket-authentication). Keep it handy, you will need it below.

Next, find your openICPSR login (should be your NetID + `@cornell.edu`) and your password.

:::{admonition} The ICPSR password is *not* your NetID or your CMail/Google password! 
:class: dropdown

It must be set separately, by invoking the "Forgot Password" functionality. See [Setting ICPSR password](setting-icpsr-password) for more details.

:::

Then, copy-paste the following code into an empty VS Code window, edit the email and password, then copy-paste it into the Git bash shell. Keep all the line breaks as shown!

```bash
echo '
# env for ICPSR
export ICPSR_EMAIL=mylogin@cornell.edu
export ICPSR_PASS="supersecretpwd"
export P_BITBUCKET_PAT="supersecretPAT" 
export P_BITBUCKET_USERNAME=netid-replace-me
' >> $HOME/.bashrc
```

```{note}
You can also use VS Code to open up the file `.bashrc` directly, if you prefer.
```

This will 

- allow you to use the `aeagit` shortcut to download a Bitbucket repository to your workspace directly from the Bash command line
- allow you to use the `tools/download_openicpsr_private.py` script to download replication packages from openICPSR from the Bash command line

```{warning}
Now might be a good time to log out and back in to make this work.
```

## Configure some convenience scripts

We have a bunch of scripts, some of which can make your life easier. See [https://github.com/AEADataEditor/editor-scripts](https://github.com/AEADataEditor/editor-scripts). You can make these available to your Bash shell by running the following command:

### If you do not yet have a `$HOME/bin` directory

Check first if you already have a `$HOME/bin` directory:

```bash
ls -l $HOME/bin
```

If that yields an error, then you don't have one. So run the next part:

```bash
cd $HOME
git clone https://github.com/AEADataEditor/editor-scripts bin
```

You should now have access to the various scripts, such as `aeagit`.

### If you already have a `$HOME/bin` directory

If you *do* have a `$HOME/bin` directory, you will need to manually adjust a few more things. Contact your supervisor.


## Configuring Python defaults

The last step you do once you have cloned your first repository.

If you are on a machine that has Python installed, run the following command (if it fails with `python3`, replace with `python`). You should do this once, from any recently cloned Bitbucket repository (which will contain a `requirements.txt` file). You do NOT have to do it every time!

::::{tab-set}

:::{tab-item} Windows

When running in Bash, this should work:

```bash
python -m pip install -r requirements.txt
```

:::

:::{tab-item} Linux/macOS

While the use of `python` might work, using `python3` is more robust:

```bash
python3 -m pip install -r requirements.txt
```

:::

::::

## Optional customizations

### Windows: Add Git Bash to the Windows Terminal

It can be convenient to add the Git Bash to the Windows Terminal application that is present in Windows 10 and higher (better fonts, etc.).

Follow instructions at [https://www.commandlinewizardry.com/post/how-to-add-git-bash-to-windows-terminal](https://www.commandlinewizardry.com/post/how-to-add-git-bash-to-windows-terminal) to do so.

