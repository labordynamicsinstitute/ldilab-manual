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

**Access a node**

See [Getting Started Guide](https://biohpc.cornell.edu/lab/userguide.aspx?a=quickstart) and [Remote Access](https://biohpc.cornell.edu/lab/doc/Remote_access.pdf). SSH is the best path (if you don't need graphical applications).

Note that, for off-campus access, you will need to use Cornell VPN. Instructions can be found [here](https://it.cornell.edu/cuvpn).

For VNC: 

- Once your have a reserved node, click ["My Reservation"](https://biohpc.cornell.edu/lab/labresman.aspx) to manage all your active reservations. 
- Choose your reservation. 
- Click "Connect VNC" under "Action" and you will have your machine name and port number. To disconnect, click "Cancel VNC" under "Action".
- Open VNC Viewer and type in session number in the form of "machine name:port number" given by BioHPC.

```{tip}

For first-time access,  [set up](https://labordynamicsinstitute.github.io/ldilab-manual/95-50-setup-bash.html#configure-bitbucket-access) your bash environment.
```

:::

:::{tab-item} NBER servers

TBD


**Access a node**

:::

::::

## Additional setup and tips-and-tricks

Run this ONCE the first time you ever access Linux servers:

```
echo "umask 007" >> $HOME/.bash_profile
```

Then do the usual [Bash setup](setup-bash). That should work on nearly any Linux server.

Additional tips-and-tricks can be found on the [LDIlab wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Getting-access-to-BioHPC-Linux-nodes). These are focused on the BioHPC cluster, but may work on other servers as well.

## Configuring automatic reservation cancellation

If you use the BioHPC reservation system, it helps others if at the end of a long-running job, your reservation is cancelled as soon as possible. One way to do this is to add the following to the scripts you are running:




::::{tab-set}


:::{tab-item}  Stata

```stata
*Use the code below at the bottom of the Stata "main" or "master" script to automatically sign out 

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
%Use code below at bottom of Python/Anaconda script to automatically sign out

import os

os.system("/programs/bin/labutils/endres.pl")
```

:::


:::{tab-item}  Bash

```bash
#Use the code below at the bottom of the bash "main" or "master" script to automatically sign out 
/programs/bin/labutils/endres.pl 
```

:::

::::

