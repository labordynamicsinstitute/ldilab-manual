(dynare-matlab)=
# Running Dynare from MATLAB

Dynare is often used as an extension from within MATLAB. Files are usually identified as `.mod`, though many other countries also use that extension.

:::{warning} 

Use the precise version of Dynare specified by the authors. If that version is not located on `L:\common` (CCSS Cloud) or `/home2/ecco_lv39/software` or as a Docker file, then talk to your supervisor.

:::


## Obtaining Dynare

Dynare is available for download from <https://www.dynare.org/download/>. But pay attention to the details for the platform where you will run this!

:::::{tab-set}

::::{tab-item} CCSS Cloud

:::{admonition} Do not attempt to **install** Dynare on CCSS or BioHPC computers. 

However, it is not necessary to *install* Dynare, it is sufficient to unpack the ZIP files. Try the information below first:  

:::


If a specific version is mentioned and is not there, download it from the [Dynare website](https://www.dynare.org/download/) - choose the **ZIP** version. Then unzip it to the `L: drive` (move it around if necessary so you get the same structure as in the example above, i.e. `L:\common\dynare\(SOME VERSION)\matlab`). Then include the `addpath` command as before.

::::

::::{tab-item} BioHPC


The preferred way to run Dynare on BioHPC is through the use of Docker. 

:::{admonition} This is very technical!

Your mileage will vary, ask for help if you need to do this and don't know how.

:::

- Consult the [BioHPC Software page](https://biohpc.cornell.edu/lab/userguide.aspx?a=software) to learn how to run Docker on BioHPC. See also [Docker-related procedures](docker-related-procedures).

:::{admonition} Simple command line
:class: note

- Obtain the value of `SERVER` from your supervisor.
- Look up the full Docker tag from the [Dynare Docker Hub page](https://hub.docker.com/r/dynare/dynare/tags) and set the `DYNARE` variable accordingly. Each Dynare version is paired with a specific version of MATLAB. 
  - You should use the precise version of Dynare that the authors used, or a very close one.
  - Ideally, you should use the same or higher version of MATLAB, but that is much less sensitive.
- If running elsewhere, you should replace `docker1` with `docker` in the command below.

```bash
SERVER=something
dockerbin=docker1
MLM_LICENSE_FILE=${MLM_LICENSE_FILE:-27000@${SERVER}.cornell.edu}
DYNARE=6.5-R2025b
$dockerbin run --rm -it \
   -v $(pwd):/project \
   -w /project \
   -e MLM_LICENSE_FILE=$MLM_LICENSE_FILE \
   --entrypoint /bin/bash \
   dynare/dynare:$DYNARE
```

:::

- You may need to put these lines into an `sbatch` file. See the `tools/sbatch-shell.sh` file for an example of how to do this (included in every repo).

::::

:::::


## Configuring MATLAB to recognize Dynare


- Be sure to include the `config.m` file as outlined in [Configuring MATLAB](matlab-config)!
- Inspect the last part of the `config.m`, it should have code much like the following:

```
%%% Dynare settings
%
% The following are possible Dynare settings. Uncomment the one you need.

% dynarepath = "/Applications/Dynare/4.6.1/matlab"
% dynarepath = "L:\LDILab\dynare\dynare-4.5.7\matlab"
%dynarepath = "L:\common\dynare-4.5.7\matlab"

% 
% Then uncomment the following line:
%
%addpath(genpath(dynarepath))
```

- You will want the path for the system you are working on. If CCSS Cloud, use the `L:` path. If on BioHPC, you will need to add a path like `/home2/ecco_lv39/software/dynare-x.y.z`.
- Then uncomment the `addpath()` statement at the end.

Your modified `config.m` should look somewhat like this:

```
%%% Dynare settings
%
% The following are possible Dynare settings. Uncomment the one you need.

% dynarepath = "/Applications/Dynare/4.6.1/matlab"
% dynarepath = "L:\LDILab\dynare\dynare-4.5.7\matlab"

dynarepath = "L:\common\dynare-4.5.7\matlab"

% 
% Then uncomment the following line:
%

addpath(genpath(dynarepath))
```

The Matlab program should now run, and call out to the Dynare software as needed.


### Additional info

- [Building Docker image with MATLAB Toolboxes](https://github.com/mathworks-ref-arch/matlab-dockerfile/tree/main/alternates/building-on-matlab-docker-image)
- [Dynare Docker images with MATLAB](https://hub.docker.com/r/dynare/dynare)