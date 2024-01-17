(setup-bash)=
# Setting up your Bash environment

The following setup applies to any computer you may be using to run Bash commands (except for CodeOcean).

```{note}
On Windows, this will be "Git bash". On Linux, you are usually using `bash`, but check with your sysadmin if you are unsure. On MacOS, newer versions have changed the default shell to `zsh`, which should work mostly the same. It is possible to use the `bash` shell there as well. 
```

## Configure the openICPSR download script

Run this once in a Bash shell:

```bash
echo "
# env for ICPSR
export ICPSR_EMAIL=mylogin@cornell.edu
export ICPSR_PASS='supersecretpwd' 
" >> $HOME/.bashrc
```
(you should copy-paste this into an empty VS Code window, edit the editable pieces, then copy-paste it into the Git bash shell. Keep all the line breaks as shown!).

```{note}
You can also use VS Code to open up the file `.bashrc` directly, if you prefer.
```

This will "prime" the script to use that email and password for downloading the information. 

```{warning}
You may need to log out and back in to make this work; but wait until you have made all the adjustments here!
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

## Configure Bitbucket access

For Bitbucket, you often copy your [Bitbucket PAT](bitbucket-authentication) into the Bash window. The following can streamline that, if using the `aeagit` command above.

```bash
echo '# adding Bitbucket credentials
export P_BITBUCKET_PAT="supersecretPAT" 
export P_BITBUCKET_USERNAME=netid-replace-me
' >> $HOME/.bashrc
```

(you should copy-paste this into an empty VS Code window, edit the editable pieces, then copy-paste it into the Git bash shell. Be sure to keep all line breaks and spaces!).


```{warning}
Now might be a good time to log out and back in to make this work.
```

## Configuring Python defaults

If you are on a machine that has Python installed, run the following command (if it fails with `python3`, replace with `python`). You should do this once, from any recently cloned Bitbucket repository (which will contain a `requirements.txt` file)

```bash
python3 -m pip install -r requirements.txt
```
