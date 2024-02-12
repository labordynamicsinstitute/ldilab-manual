(linux-remote)=
# Connecting to remote Linux servers

We have access to various Linux clusters:

- BioHPC
- Occassionally NBER linux servers
- Others, as provided by authors



::::{tab-set}

:::{tab-item} BioHPC


**Request an account**

Go to the [BioHPC account request page](https://biohpc.cornell.edu/NewUserRequest.aspx), and create an account on the BioHPC cluster.

Then [contact BioHPC support](https://biohpc.cornell.edu/contact.aspx), requesting to join the ECCO group and lv39 (Lars') "lab" (`ecco_lv39`).

**Reserve a node**

- Go to "User", then  [Reservations page](https://biohpc.cornell.edu/lab/labres.aspx), choose "Restricted", and reserve a node:
  - cbsuecco02: up to 7 days
  - all others: up to 3 days
  - in both cases, renewable
- Then go to 'My Reservations' and share the reservation with Lars (`lv39`) and others, if necessary.

```{note}
Skip this step if somebody else added you to their reservation!
```

```{note}
If you do not see an open server, ask on the mailing list (ldi-lab-l@cornell.edu) if somebody has an active reservation that they can add you to!
```

**Access a node**

See [Getting Started Guide](https://biohpc.cornell.edu/lab/userguide.aspx?a=quickstart) and [Remote Access](https://biohpc.cornell.edu/lab/doc/Remote_access.pdf). SSH is the best path (if you don't need graphical applications). See [Access via VSCode](linux-vscode) for a more user-friendly way to use SSH to access the server.

Note that, for off-campus access, you will need to use Cornell VPN. Instructions can be found [here](https://it.cornell.edu/cuvpn).

For **VNC**: 

- Once your have a reserved node, click ["My Reservation"](https://biohpc.cornell.edu/lab/labresman.aspx) to manage all your active reservations. 
- Choose your reservation. 
- Click "Connect VNC" under "Action" and you will have your machine name and port number. To disconnect, click "Cancel VNC" under "Action".
- Open VNC Viewer and type in session number in the form of "machine name:port number" given by BioHPC.

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
For this to work on BioHPC, verify that you have a valid reservation and an active VPN! 
```

- Enter your account password when prompted.
- Once connected, 
  - `Open Folder` and navigate to your working directory.
  - open a new terminal using the "Terminal" option in the top menu of VSCode (or `Ctrl-\``).
- You should now be able to work on the Linux server via command line. 

Some benefits of connecting to BioHPC with VSCode: You can view/edit programs, check log files, and run jobs simultaneously in a given instance of VSCode. Note that you should still use [`tmux`](https://github.com/labordynamicsinstitute/replicability-training/wiki/Getting-access-to-BioHPC-Linux-nodes#utilize-tmux) within the VSCode terminal, in case of a disconnect. 

In particular, you can navigate to your working directory and `git clone` the Bitbucket repository (using either the command line, or VSCode prompt to `Clone Repository`). VSCode recognizes Git, so you can visually navigate through tracked and untracked files via the lefthand side menu.



## Additional setup and tips-and-tricks

### First-time setup

Run this ONCE the first time you ever access Linux servers:

```
echo "umask 007" >> $HOME/.bash_profile
```

Then do the usual [Bash setup](setup-bash). That should work on nearly any Linux server.


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


### Configuring automatic reservation cancellation (BioHPC only)

If you use the BioHPC reservation system, it helps others if at the end of a long-running job, your reservation is cancelled as soon as possible. One way to do this is to add the following to the scripts you are running:




::::{tab-set}


:::{tab-item}  Stata

```stata
// Use the code below at the bottom of the Stata "main" or 
// "master" script to automatically sign out 

shell /programs/bin/labutils/endres.pl 
```


:::

:::{tab-item} R

```r
# Add to end of main or last script.
system("/programs/bin/labutils/endres.pl")
```


:::

:::{tab-item} Matlab

```
%Use code below at end of MATLAB main script, or last script, to automatically sign out

system("/programs/bin/labutils/endres.pl")
```


:::

:::{tab-item}  Python

```python
# Use code below at bottom of Python/Anaconda script 
# to automatically sign out

import os

os.system("/programs/bin/labutils/endres.pl")
```

:::


:::{tab-item}  Bash

```bash
#Use the code below at the bottom of the bash "main" or 
# "master" script to automatically sign out 
/programs/bin/labutils/endres.pl 
```

:::

::::



```{tip}
Additional tips-and-tricks can be found on the [LDIlab wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Getting-access-to-BioHPC-Linux-nodes). These are focused on the BioHPC cluster, but may work on other servers as well.
```
