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
- Login to BioHPC through this [link](https://biohpc.cornell.edu/login_bio.aspx?ReturnURL=/lab/labresman.aspx). If do not have an account yet, follow instructions at [Linux Remote](linux-remote)
- [Reserve a node](linux-remote)
- [Access the node](linux-remote)
- Launch a terminal and change your directory to `/home2/ecco_lv39/Workspace`. Do not work on the home directory which has your NetID. Type `pwd` to check your current directory. 
- Clone your repository into this directory `aeagit-###`.

**If there is no Docker folder**

- Create a folder `Docker` in the same directory as your repository.
- Create a `Dockerfile`. A simple example might be (here, to install Ox)

```bash
# syntax=docker/dockerfile:1.2
# First stage
FROM ubuntu:22.04 
ENV VERSION 9
ENV SUBVERSION 10
ENV MINORVERSION 0

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
         locales \
         libncurses5 \
         libfontconfig1 \
         git \
         nano \
         unzip \
         wget \
    && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

# Set a few more things
ENV LANG en_US.utf8

# Adding Ox
RUN wget -O oxconsole.deb https://www.doornik.com/download/oxmetrics${VERSION}/Ox_Console/oxconsole_${VERSION}.${SUBVERSION}-${MINORVERSION}_amd64.deb \
    && apt-get install ./oxconsole.deb
```

- You might also find a `build.sh` script useful:

```
#!/bin/bash

[[ -z $1 ]] && TAG=$(date +%F) || TAG=$1
MYHUBID=aeadataeditor
MYIMG=aearep-XXXX

DOCKER_BUILDKIT=1 docker1 build   -t ${MYIMG}:$TAG $(pwd)/

```
- Make this file executable: `chmod +x build.sh`
- Go back to your repository directory (`cd ..`)
- `git add Docker` and push.

**If there is a Docker folder**

- Change the directory to your Docker folder and build the image `./build.sh`. Check completion by `docker1 images`.
- Once the image is built, go to the directory where you want to run your container. Type

```bash
docker1 run -it --rm -v "$(pwd)":/project -w /project biohpc_lv39/aearep-###:TAG
```
(modify repository number and TAG as needed).

- In the bash shell inside the Docker container, run any command lines as identified by the authors.


::: 

::::

## Run the code
