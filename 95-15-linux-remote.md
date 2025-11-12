(linux-remote)=
# Connecting to remote Linux servers

We have access to various Linux clusters:

- BioHPC
- Occassionally NBER linux servers
- Others, as provided by authors



## First-time setup

Run this ONCE the first time you ever access any Linux servers:

```
echo "umask 007" >> $HOME/.bash_profile
```

Then do the usual [Bash setup](setup-bash). That should work on nearly any Linux server.



::::{tab-set}

:::{tab-item} BioHPC


**Request an account**

1. Go to the [BioHPC account request page](https://biohpc.cornell.edu/NewUserRequest.aspx), and create an account on the BioHPC cluster.
2. Then [contact BioHPC support](https://biohpc.cornell.edu/contact.aspx), requesting to join the ECCO group and lv39 (Lars') "lab" (`ecco_lv39`).

Consult the [ECCO general documentation](https://labordynamicsinstitute.github.io/ecco-notes/docs/biohpc/slurm-quick-start.html) for more details on the BioHPC cluster for economists!

**Access a node**

See [Getting Started Guide](https://biohpc.cornell.edu/lab/userguide.aspx?a=quickstart) and [Remote Access](https://biohpc.cornell.edu/lab/doc/Remote_access.pdf). SSH is the best path (if you don't need graphical applications). See [Access via VSCode](linux-vscode) for a more user-friendly way to use SSH to access the server.

```{tip}

For first-time access,  [set up](https://labordynamicsinstitute.github.io/ldilab-manual/95-50-setup-bash.html#configure-bitbucket-access) your bash environment.
```

:::

:::{tab-item} NBER servers

**Request an account**

You need an account with NBER to access their servers. Contact Lars  to get an account.


**Access a node**

Access for us is primarily via SSH. See [Access via VSCode](linux-vscode) for a more user-friendly way to use SSH to access the server.

:::

::::

(linux-vscode)=
## Accessing Linux nodes with VSCode

- Check that you have installed the [Remote-SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) on VSCode.
- Open VSCode and select the Remote-SSH extension from the Command Palette.
- Enter the host name when prompted. The host name should follow this naming convention: 
  - BioHPC: "netid@cbsuecco##.biohpc.cornell.edu".
  - NBER: "loginid@nber##.nber.org".
- You may be prompted to "Select the platform of the remote host". If so, select the "Linux" option in the drop down menu.

```{tip}
If you get the following message in the bottom right: "Setting up SSH Host BioHPC: (details) Initializing VS Code Server", then it may be waiting for you to enter your TFA code
```

- Enter your account password when prompted.
- Once connected, 
  - `Open Folder` and navigate to your working directory.
  - open a new terminal using the "Terminal" option in the top menu of VSCode (or `Ctrl-\``).
- You should now be able to work on the Linux server via command line. 

Some benefits of connecting to BioHPC with VSCode: You can view/edit programs, check log files, and run jobs simultaneously in a given instance of VSCode. Note that you should still use [`tmux`](https://github.com/labordynamicsinstitute/replicability-training/wiki/Getting-access-to-BioHPC-Linux-nodes#utilize-tmux) within the VSCode terminal, in case of a disconnect. 

In particular, you can navigate to your working directory and `git clone` the Bitbucket repository (using either the command line, or VSCode prompt to `Clone Repository`). VSCode recognizes Git, so you can visually navigate through tracked and untracked files via the lefthand side menu.

For more information, see [VSCode Remote Development using SSH](https://code.visualstudio.com/docs/remote/ssh).

```{tip}
A tutorial video (thanks to Lars' former RA Ilona Khimey) is available at [Cornell Video-on-demand](https://vod.video.cornell.edu/media/BioHPC+Walkthrough+%28Mac%29/1_x2tmxhk9).
```

## Where to run code


::::{tab-set}

:::{tab-item} BioHPC

You should use `/home2/ecco_lv39/Workspace` to clone your Bitbucket repository.

```bash
cd /home2/ecco_lv39/Workspace
```

:::

:::{tab-item} NBER servers

Consult the Jira issue to figure out where you should run the code.

:::

::::

```{tip}
For instructions on how to setup and run code see [ECCO Notes](https://labordynamicsinstitute.github.io/ecco-notes/docs/intro.html)
```

## Running Code

Running code on Biohpc is not as simple as opening the Stata GUI. Instead, you submit jobs through the SLURM scheduler. A detailed walkthrough can be seen [here](https://labordynamicsinstitute.github.io/ecco-notes/docs/biohpc/sbatch.html). 

### Modules

[details on running modules]

### SBATCH

To submit a job to the server, you create a script with a header. Below is an example from the replication template.

```bash
#!/bin/bash
# Job name:
#SBATCH --job-name=RunStata
#
# Memory
#SBATCH --mem=32G
#
# Request one node:
#SBATCH --nodes=1
#
# Specify number of tasks for use case (example):
#SBATCH --ntasks-per-node=1
#
# Processors per task: here, 8 bc we have Stata-MP/8
#SBATCH --cpus-per-task=8
#
# Wall clock limit: adjust accordingly. Format is HH:MM:SS or DD-HH:MM:SS where DD are days.
#SBATCH --time=00:00:30
#
# Email?
# Probably do not need "--mail-user=youremail@cornell.edu"
# Just add your email to the file "$HOME/.forward"
# 
#SBATCH --mail-type=ALL
#
## Command(s) to run (example):
#
# Stata example
#
/usr/local/stata16/stata-mp -b main.do
#
## Matlab - will run "main.m", output to "main.log"
## Assumes you have done the setup at https://labordynamicsinstitute.github.io/ecco-notes/docs/biohpc/slurm-quick-start.html#one-time-setup
# module load matlab/2023a
# matlab -nodisplay -r "addpath(genpath('.')); main" -logfile main.$(date +%F_%H-%M-%S).log
#
# R example - caution with version and parallel processing
module load R/4.4.2
R CMD BATCH main.R main.$(date +%F_%H-%M-%S).log
```

Each item in the header specifies some detail for the server. Jobs submitted must specifiy levels of compute (such as memory required), time to run, . A good starting point for these details is an authors `README`.

To view the status of your jobs, you can run

```bash
squeue
```

or 

```bash
squeue -u <netid>
```


### Interactivly

Sometimes, it can be helpful to run code interactively, rather than through SBATCH, on the BioHPC shell. Details [here](https://labordynamicsinstitute.github.io/ecco-notes/docs/biohpc/slurm-quick-start.html#interactive-shell). 

The most important idea is not to run code on the login node of BioHPC. You must transfer over to a computing node, using

```bash
srun --pty bash -l
```

Here, you can load modules, run programs, 

## Obtaining Data on Biohpc

### From A Deposit

The instructions from the manual [Deposit Download Instructions](https://labordynamicsinstitute.github.io/ldilab-manual/94-01-how-to-use-openICPSR-backend.html) will work. Note that you need to use the scripts instead of doing it manually. That page also has a link to non-icpsr deposit instructions

### From Another Source

The following page [Obtaining Data on Biohpc](https://labordynamicsinstitute.github.io/ecco-notes/docs/transfer.html) has extensive instructions on how to get data onto Biohpc from other sources. When obtaining data on your personal laptop is easy then using WinSCP will be straightforward. 


## Additional setup and tips-and-tricks

### Utilize `tmux`

If the Linux server has `tmux` installed, use it to make a persistent session that survives disconnects. 

```{tip}
Cheatsheet: https://gist.github.com/MohamedAlaa/2961058
```

1. Login via SSH
2. Launch tmux with a session name that makes sense, e.g. `tmux new -s AEAREP-xxxx`
3. Launch your Matlab, Stata, etc job
4. Disconnect from tmux: `ctrl-b d`. You don't need to press this both Keyboard shortcut at a time. First press "Ctrl+b" and then press "d".
5. Log out of SSH

Next time:

1. Login via SSH
2. Reconnect to your tmux session: `tmux a -t AEAREP-xxxx`
3. If you forgot what session, `tmux ls`

To save the output of a `tmux` session to a file, see [https://unix.stackexchange.com/questions/26548/write-all-tmux-scrollback-to-a-file](https://unix.stackexchange.com/questions/26548/write-all-tmux-scrollback-to-a-file).

### Unzipping large ZIP files fails

In some cases, unzipping large ZIP files (larger than 2GB) may fail:

```
error: invalid zip file with overlapped components (possible zip bomb)
```

If this is detected, you need to use a 64-bit version of a decompression program. This may vary by Linux host.


::::{tab-set}


:::{tab-item}  BioHPC

Instead of `zip`, use `7z` as follows:

```
ICPSRNUM=123456
/programs/bin/util/7z x -O${ICPSRNUM} ${ICPSRNUM}.zip
```

(which is the equivalent to the zip command `zip -n ${ICPSRNUM} -d ${ICPSRNUM}`). The first option (`-O`) is an upper-case letter `O`, not zero.

:::

:::{tab-item} Others

If `7z` is available, use it as well (path may differ). Other options include using `jar`. Contact system administrator of the system for guidance.

:::

::::

### Setting up SSH Agent for password-less login

The SSH protocol allows you to create a public-private key pair. You deposit the public key on the Linux server, and keep the (passphrase-protected) private key on your laptop. You can then configure a "ssh-agent" running on your laptop to store (temporarily) your passphrase in memory, and provide it every time you log in to the Linux server. This works very easily on Unix-like systems (macOS, Linux laptops), but is a bit trickier on Windows laptops.

:::::{tab-set}

::::{tab-item} macOS

To be completed.

::::

::::{tab-item} Linux (laptop)

To be completed.

::::

::::{tab-item} Windows (laptop only)

First, you need to ensure that the SSH subsystem is installed.

To be completed.


Finally, you will want to start the SSH-agent. The following [website](https://interworks.com/blog/2021/09/15/setting-up-ssh-agent-in-windows-for-passwordless-git-authentication/) explains how to do so. You will likely need admin privileges on your laptop.

First, as admin in a PowerShell:

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic -PassThru | Start-Service
```

Then either reboot, or start the service

```powershell
start-ssh-agent.cmd
```



::::

:::::

The next steps are common to all operating systems.

You will want to create a key, then transfer it to the Linux server. The following commands should do this (should work on both Powershell and Bash):

```bash
ssh-keygen -t ed25519 -C "For BioHPC"
```

`ed25519` is the encryption type, "For BioHPC" is an arbitrary comment for your own tracking of keys. When prompted, you should add a passphrase.

This should have created two files in your `.ssh` directory:

```bash
ls $HOME/.ssh
```

Add the new key to your SSH-agent (optional, but recommended):

```bash
ssh-add $HOME/.ssh/id_ed25519.pub
# you should be prompted for your passphrase.
```

You will want to transfer the `.pub` file to the Linux server. You can do this with the command `ssh-copy-id` (if it exists), or manually. We show you how to do this manually:

:::{note}

You should open two terminals: one locally on your laptop, one remotely on the Windows server!

:::


This creates a directory used by SSH:

```bash
# this is on the remote server
mkdir $HOME/.ssh
# stay logged in!
```

This transfer the public key to the remote Linux server

```bash
# this is on your laptop
netid=lv39  # adjust to be your own netid!
scp $HOME/.ssh/*.pub ${netid}@cbsulogin.biohpc.cornell.edu:.ssh/
```

You should now see the `.pub` key in your `.ssh` directory on the remote Linux server:

```bash
# this is on the remote server
# this should show the *.pub file
ls $HOME/.ssh
# this authorizes you to use the SSH key to log in:
cat $HOME/.ssh/*.pub >> $HOME/.ssh/authorized_keys
```

Now test it:

```bash
# This is run from your laptop
ssh ${netid}@cbsulogin.biohpc.cornell.edu
```

You should now be prompted for your SSH passphrase:

```
$ ssh netid@cbsulogin.biohpc.cornell.edu
Enter passphrase for key `C:\Users\netid\.ssh\id_ed15559.pub`:
```

### Utilizing Aliases

Workflows on Linux Systems can be simplified by using bash aliases. The example below can exist on your personal machine

```bash
alias biohpc='ssh <netid>@cbsulogin.biohpc.cornell.edu'
```

Adding this to your `~/.bashrc` enables you to type `bihopc` in your terminal, and an ssh connection is opened.

### Using `linux-system-info.sh`

Part of replicating packages is capturing as much information as we can. You will see in the replication report that we must specify the amount of compute our replication used, under `Computing Environment of the Replicator`. This can be captured by adding the following line to your SBATCH script.

```bash
echo "Linux System Info:"
<package>/tools/linux-system-info.sh
```

This will output the computing resources in the SLURM output file.


```{tip}
Additional tips-and-tricks can be found on the [LDIlab wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Getting-access-to-BioHPC-Linux-nodes). These are focused on the BioHPC cluster, but may work on other servers as well. 
```
