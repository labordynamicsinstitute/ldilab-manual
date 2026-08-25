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

````{margin}
```{note}
If this does not work (you get an error), you may need to install the `code` command in your Path. See  [instructions for MacOS](https://code.visualstudio.com/docs/setup/mac#_launch-vs-code-from-the-command-line). For Windows, there is an option during installation to "Add to PATH". After installation, on both operating systems, open **VS Code**, then press `Ctrl+Shift+P` (or `Cmd+Shift+P` on MacOS) and type "Shell Command: Install 'code' command in PATH" and select it. (You may need to restart your terminal or your computer for this to take effect.) On most Linux distributions, this is not necessary.   
```
````


- copy the above exactly as shown. There is a "dot" before the word "`bashrc`". You should be able to mouse-over and choose the copy-icon to the right!

:::{warning}

- If this code shows an error, stop here, and debug! 
- If no VS Code windown shows, stop here, and debug.

:::

You should now have a (new) VS Code window, either empty or with some pre-written script. If there is content, place your cursor at the very end of the edit window (you may need to scroll down). 

Now, copy-paste the following code into the VS Code window. We will edit the values with the appropriate replacements. Keep all the line breaks, quotes, and spaces (or absence thereof) as shown!

```bash
# Add $HOME/bin to path
export PATH="$HOME/bin:$PATH"

# add Python exec to path. May need to be adjusted for future Python upgrades
PYTHONVERSION=314
export PATH="$PATH:$HOME/AppData/Roaming/Python/Python$PYTHONVERSION/Scripts"

# env for ICPSR
ICPSR_EMAIL=mylogin@cornell.edu
ICPSR_PASS='supersecretpwd'
# env for Bitbucket
P_BITBUCKET_PAT='supersecretPAT' 
P_BITBUCKET_USERNAME=bitbucketusername
# export them all
export ICPSR_EMAIL ICPSR_PASS P_BITBUCKET_PAT P_BITBUCKET_USERNAME
```

:::{note}

The use of single-quotes for the password ensures that special characters are correctly preserved.

:::

:::{admonition} Advanced setup
:class: dropdown note

If you are using more than just these few passwords, a more advanced setup  is suggested. 

- You should probably be using a Password Manager to store your passwords. However, there are few password managers that are cross-platform and available on all of our used platforms. 
- Splitting the setup above into a separate file (e.g., `$HOME/.envvars`) and sourcing it from the main `.bashrc` file is a good idea, and several of our [Python scripts](helpful-scripts) search for that. To leverage that, instead of the above lines added to the `$HOME/.bashrc`, do the following:

```bash
# Check for env vars
# Add $HOME/bin to path
export PATH="$HOME/bin:$PATH"

# add Python exec to path. May need to be adjusted for future Python upgrades
PYTHONVERSION=314
export PATH="$PATH:$HOME/AppData/Roaming/Python/Python$PYTHONVERSION/Scripts"

# Check for env vars
if [ -f $HOME/.envvars ]
then
        . "$HOME/.envvars"
fi
```

and then create a new file `$HOME/.envvars` with the following content:

```bash
# other secret
SERVICE_API='supersecretAPI'
# env for ICPSR
ICPSR_EMAIL=mylogin@cornell.edu
ICPSR_PASS='supersecretpwd'
# env for Bitbucket
P_BITBUCKET_PAT='supersecretPAT' 
P_BITBUCKET_USERNAME=bitbucketusername
# export them all. Add new ones to this list. Edit to remove unused ones.
export ICPSR_EMAIL ICPSR_PASS P_BITBUCKET_PAT P_BITBUCKET_USERNAME SERVICE_API
```

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

## One-time setup on  some systems

::::{tab-set}

:::{tab-item} CCSS Cloud

::::{admonition} As of August 2026:
:class: warning

Two one-time action items:

1. In Git Bash, type

```bash
git config --global --add safe.directory '%(prefix)///ccssilr.file.core.windows.net/lv39/*'
```

to avoid pesky warnings about ownership in the common workarea on the network drive.

2. To set a global variable, common to everybody, and necessary for the ICPSR download script, type

```bash
cmd //c lv39_ICPSR_Token.bat
```

You may need to start a new Git bash shell afterwards for it to take effect.


:::
:::{tab-item} Linux

See [Linux remote system setup]((linux-remote) for any special notes.

:::
::::

## Configure some convenience scripts

We have a bunch of scripts, some of which can make your life easier. See the [Useful scripts](helpful-scripts) page.

## Other software dependencies


::::{tab-set}

:::{tab-item} CCSS Cloud

You should have all software that is needed. If you need additional software, remember that you **cannot** install software yourself. Reach out to your supervisor before contacting the CCSS Cloud support team.

:::

:::{tab-item} Other Windows

You may need to install Python.

Installing Python is best done using `winget`. From a **Powershell**, run these install commands:

```powershell
winget install Python.Python.3.12
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
cd /z/workspace/aearep-xxxx
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

### Problems


::::{tab-set}

:::{tab-item} Windows

**Permission errors on CCSS Cloud**

If you get an error about permissions on CCSS Cloud, such as the following or similar:

```
WARNING: Failed to write executable - trying to use .deleteme logic
ERROR: Could not install packages due to an OSError: [WinError 2] The system cannot find the file specified: 'C:\\Users\\lv39\\AppData\\Roaming\\Python\\Python313\\Scripts\\dotenv.exe' -> 'C:\\Users\\lv39\\AppData\\Roaming\\Python\\Python313\\Scripts\\dotenv.exe.deleteme'
```

then you will need to use Anaconda Python instead of the default Python installation. To do so, run the following commands in your Bash shell:

```bash
/c/ProgramData/Anaconda3/Scripts/conda init bash
```

You will be prompted for an admin password, which you should say "No" to. The command will report that it failed, but should have modified your `.bashrc` file to use Anaconda Python. Close that Bash window, and open a new one. It should display the word `(base)` at the beginning of the prompt, indicating that Anaconda Python is now active.

```
(base)
lv39@RS-CCSSlv39-16 MINGW64 ~
```

Now, go back to the repository directory (e.g., `cd /z/Workspace/aearep-xxxx`) and re-run the `python -m pip install -r requirements.txt` command from above.

:::

:::{tab-item} Linux

Newer versions of Ubuntu disallow the "global" installation of packages, even with the `--user` flag. You may need to create a virtual environment in your home directory first, and activate it every time you log on.

**Creating the virtual environment:**

```bash
python3 -m venv $HOME/aeapyenv
source $HOME/aeapyenv/bin/activate
```

Then run the `pip install` command again, from the `aearep-xxxx` directory.

**Activating the virtual environment every time you log on:**

Add the following line to your `$HOME/.bashrc` file, using the same methods described earlier.

```bash
source $HOME/aeapyenv/bin/activate
```
:::
::::

## Updating

Sometimes, updates are made. 

### Scripts

See [Updating scripts](editor-scripts#updating-the-scripts) for instructions on how to update the scripts.

### Python dependencies

It is safe to re-run

```bash
python -m pip install -r requirements.txt
```

at any time.

## Optional customizations

### Windows: Add Git Bash to the Windows Terminal

It can be convenient to add the Git Bash to the Windows Terminal application that is present in Windows 10 and higher (better fonts, etc.). This should be automatic, but if not:

Follow instructions at [https://www.commandlinewizardry.com/post/how-to-add-git-bash-to-windows-terminal](https://www.commandlinewizardry.com/post/how-to-add-git-bash-to-windows-terminal) to do so.

