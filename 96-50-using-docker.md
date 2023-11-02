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

::: 

::::

## Run the code