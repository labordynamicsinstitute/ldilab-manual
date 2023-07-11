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

- Go to [BioHPC Reservations page](https://biohpc.cornell.edu/lab/labres.aspx), choose "Restricted", and reserve a node:
  - cbsuecco02: up to 7 days
  - all others: up to 3 days
  - in both cases, renewable
- Then go to 'My Reservations' and share the reservation with Lars (`lv39`) and others, if necessary.

**Access a node**

See [Getting Started Guide](https://biohpc.cornell.edu/lab/userguide.aspx?a=quickstart) and [Remote Access](https://biohpc.cornell.edu/lab/doc/Remote_access.pdf). SSH is the best path (if you don't need graphical applications).

Note that, for off-campus access, you will need to use Cornell VPN. Instructions can be found [here](https://it.cornell.edu/cuvpn).


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

