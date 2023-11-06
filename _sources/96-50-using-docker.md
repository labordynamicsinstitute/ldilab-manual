(docker-related-procedures)=
# Docker-related procedures

In this section, we will show you a few things related specifically to running code reproducibly with Docker. For more general debugging tips for Docker and other computer languages, see [our wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Docker-Tips).

(coming soon)

## Checklist

- [ ] If running licensed software (e.g. MATLAB, Stata), know where the license is stored. If you do not, you cannot run the relevant Docker image.
- [ ] Docker (or equivalent) is installed
- [ ] The replication package's main directory will be mounted into the Docker container. The precise location will depend on the Docker image. Know where it is.



::::{tab-set}

:::{tab-item}  Windows 

```{note}
Docker does not run on CCSS Cloud! These instructions may work on a personal laptop.
```


:::

:::{tab-item} Mac/generic Linux

```{note}

Mac-specific: In addition to the default Docker client, [OrbStack](https://orbstack.dev/) can be used for personal use. We have found it to have less of a computational burden.

```


::: 


:::{tab-item} BioHPC

```{note}
BioHPC procedures differ somewhat. Wherever it says `docker`, `docker1` must be replaced. Read the [Quickstart](https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=340#c) for other things. Where relevant, we will point out differences below.
```
- Ensure you are either connected to the campus network directly or through a VPN. You cannot connect to the compute node without being on campus or connected via VPN. See [instruction](https://it.cornell.edu/cuvpn) for CU VPN setup. 
- Login to BioHPC through this [link](https://biohpc.cornell.edu/login_bio.aspx?ReturnURL=/lab/labresman.aspx). If do not have an account yet, click "Request a BioHPC account" below the login palette.
- Go to "Reservation" under "User" to reserve a node. Select `restricted` for machine class and reserve a server. You need a credit account to reserve a server, you can set one up using the [My Credit Accounts](https://biohpc.cornell.edu/lab/projects.aspx) submenu. Click on "New Credit Account", name it and create. 
  - Skip this step if you are already added to a node.
- Once your have a reserved node, click ["My Reservation"](https://biohpc.cornell.edu/lab/labresman.aspx) to mange all your active reservations. Click "Connect VNC" under "Action" and you will have your machine name and port number. To disconnect, click "Cancel VNC" under "Action".
- Open VNC Viewer and type in session number in the form of "machine name:port number" given by BioHPC.
- [Set up](https://labordynamicsinstitute.github.io/ldilab-manual/95-50-setup-bash.html#configure-bitbucket-access) your bash environment.
- Launch a terminal and change your directory to /home2/ecco_lv39/Workspace. Do not work on the home directory which has your NetID. Type `pwd` to check your current directory. Clone your repository into this directory `aeagit-###`.
- Change the directory to your Docker folder and build the image `./build.sh`. Check completion by `docker1 images`.
- Once the image is built, go to the directory where you want to run your container. Type `docker1 run -it --rm -v "$(pwd)":/project -w /project biohpc_lv39/aearep-###:TAG` (modify repository number and TAG as needed).
  - In the bash shell inside the Docker container, run any command lines as identified by the authors.

- For Oxl:
  - Run `oxl filename | tee filename.log` to save the log files.
  - If need to modify files as instructed by the authors, exit the Docker container and type `gedit filename`.


::: 

::::

## Run the code
