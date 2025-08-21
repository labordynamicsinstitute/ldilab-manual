(setup-bash)=
# Setting up your Bash environment

The following setup applies to any computer you may be using to run Bash commands (except for CodeOcean).

```{note}
On Windows, this will be "Git bash". On Linux, you are usually using `bash`, but check with your sysadmin if you are unsure. On MacOS, newer versions have changed the default shell to `zsh`, which should work mostly the same. It is possible to use the `bash` shell there as well. 
```

## Preparing the BASHRC

### Open up VS Code

Open up a VS Code window as follows:

```bash
code $HOME/.bashrc
```

- copy the above exactly as shown. There is a "dot" before the word "`bashrc`".

:::{warning}

- If this code shows an error, stop here, and debug! 
- If no VS Code windown shows, stop here, and debug.

:::

You should now have a (new) VS Code window, either empty or with some pre-written script. If there is content, place your cursor at the very end of the edit window (you may need to scroll down). 

Now, copy-paste the following code into the VS Code window. We will edit the values with the appropriate replacements. Keep all the line breaks, quotes, and spaces (or absence thereof) as shown!

```bash
# env for ICPSR
export ICPSR_EMAIL=mylogin@cornell.edu
export ICPSR_PASS='supersecretpwd'
# env for Bitbucket
export P_BITBUCKET_PAT='supersecretPAT' 
export P_BITBUCKET_USERNAME=bitbucketusername
```

:::{note}

The use of single-quotes for the password ensures that special characters are correctly preserved.

:::

### Get the Bitbucket PAT

First, create a [Bitbucket PAT](bitbucket-authentication). Once you have created it,

- paste the PAT into the line with `P_BITBUCKET_PAT` (remember to keep the single-quotes!)
- also put your  `bitbutcketusername` (if you can't find it, see in the Bitbucket Profile (top-right corner, gear icon, etc.)).



### Get the openICPSR info

Next, find your openICPSR login (should be your NetID + `@cornell.edu`) and your **openICPSR** password (not your Cornell or Google password)

:::{admonition} The ICPSR password is *not* your NetID or your CMail/Google password! 
:class: dropdown

It must be set separately, by invoking the "Forgot Password" functionality. See [openICPSR authentication](openicpsr-authentication) for more details.

:::

- paste the openICPSR login (probably `netid@cornell.edu`) into the line with `ICPSR_EMAIL`
- paste the openICPSR password into the line with `ICPSR_PASS`

### Why?

This will 

- allow you to use the `aeagit` shortcut to download a Bitbucket repository to your workspace directly from the Bash command line
- allow you to use the `tools/download_openicpsr_private.py` script to download replication packages from openICPSR from the Bash command line (see [Helpful scripts](helpful-scripts) for details on this and other scripts).


### Verifying it works

:::{warning}
On Windows, close the Git Bash window and open a new one to make the changes take effect. On Linux and MacOS, you can just run the following command in the terminal.


```bash
source $HOME/.bashrc
```
:::

You should now be able to verify that the configuration setup worked, by typing the following at the terminal prompt:"

```bash
export | grep BIT
```

should show your Bitbucket username and PAT.

```bash
export | grep ICPSR
```

should show your openICPSR login and password. 


:::{admonition} Now clear the confidential information from your screen!

Just to be sure, now type

```bash
clear
```

:::

## Configure some convenience scripts

We have a bunch of scripts, some of which can make your life easier. See [https://github.com/AEADataEditor/editor-scripts](https://github.com/AEADataEditor/editor-scripts). You can make these available to your Bash shell by running the following command:

### If you do not yet have a `$HOME/bin` directory

Check first if you already have a `$HOME/bin` directory:

```bash
ls -l $HOME/bin
```

If that yields an error, then you don't have one. So run the next part:

```bash
git clone https://github.com/AEADataEditor/editor-scripts $HOME/bin
```

You should now have access to the various scripts, such as `aeagit`.

### If you already have a `$HOME/bin` directory

If you *do* have a `$HOME/bin` directory, you will need to manually adjust a few more things. Contact your supervisor.





## Other software dependencies


::::{tab-set}

:::{tab-item} Windows

You may need

- Python
- Rsync

On CCSS Cloud, Python should be installed. You may need to add `rsync` only if you are a LDI Lab Admin working with CodeOcean. Installation has only been tested on a laptop and may not work on CCSS Cloud.

Installing Python is best done using `winget`. From a **Powershell**, run these install commands:

```powershell
winget install Python.Python.3.12
```

If you need `rsync`, run the following in a Bash shell

```bash
setup-rsync.sh
```


:::

:::{tab-item} MacOS

Both Python and rsync should be installed. If you need a newer version of Python 3.x, check the internet...

:::

:::{tab-item} Linux

Both Python and rsync should be installed. If not, check your version of package manager. You mean need to reference `python3` because the default Python might be `python2`, which won't work.

:::
::::

## Configuring Python defaults

The last step you do once you have cloned your first repository (this can be run from within **any** recently cloned repository).

If you are on a machine that has Python installed, run the following command (if it fails with `python3`, replace with `python`). You should do this once, from any recently cloned Bitbucket repository (which will contain a `requirements.txt` file). You do NOT have to do it every time!



::::{tab-set}

:::{tab-item} Windows

When running in Bash, this should work:

- Change the working directory to one of your recent cases, say `xxxx`:

```bash
cd /l/workspace/aearep-xxxx
```

then

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

## Updating

Sometimes, updates are made. 

### Scripts

If you installed them in `$HOME/bin`, then simply run

```bash
cd $HOME/bin
git pull
```

Adjust if you installed them somewhere else.

### Python dependencies

It is safe to re-run

```bash
python -m pip install -r requirements.txt
```

at any time.

## Optional customizations

### Windows: Add Git Bash to the Windows Terminal

It can be convenient to add the Git Bash to the Windows Terminal application that is present in Windows 10 and higher (better fonts, etc.).

Follow instructions at [https://www.commandlinewizardry.com/post/how-to-add-git-bash-to-windows-terminal](https://www.commandlinewizardry.com/post/how-to-add-git-bash-to-windows-terminal) to do so.

