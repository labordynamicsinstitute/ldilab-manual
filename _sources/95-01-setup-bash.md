(setup-bash)=
# Setting up your Bash environment

The following setup applies to any computer you may be using to run Bash commands.

```{note}
On Windows, this will be "Git bash". On Linux, you are usually using `bash`, but check with your sysadmin if you are unsure. On MacOS, newer versions have changed the default shell to `zsh`, which should work mostly the same. It is possible to use the `bash` shell there as well. 
```

## Configure the openICPSR download script

Run this once in a Bash shell:

```bash
echo "
# env for ICPSR
export ICPSR_EMAIL=mylogin@cornell.edu
export ICPSR_PASS=supersecretpwd
" >> $HOME/.bashrc
```

This will "prime" the script to use that email and password for downloading the information. 



## Configuring Python defaults

If you are on a machine that has Python installed, run the following command (if it fails with `python3`, replace with `python`). You should do this once, from any recently cloned Bitbucket repository (which will contain a `requirements.txt` file)

```bash
python3 -m pip install -r requirements.txt
```
