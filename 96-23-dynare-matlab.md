(dynare-matlab)=
# Running Dynare from MATLAB

Dynare is often used as an extension from within MATLAB. Files are usually identified as `.mod`, though many other countries also use that extension.

## Obtaining Dynare

Dynare is available for download from <https://www.dynare.org/download/>.

:::{admonition} Do not attempt to **install** Dynare on CCSS or BioHPC computers. 

However, it is not necessary to *install* Dynare, it is sufficient to unpack the ZIP files. Try the information below first:  

:::

:::{warning} 

Use the precise version of Dynare specified by the authors. If that version is not located on `L:\common` (CCSS Cloud) or `/home2/ecco_lv39/software`, then talk to your supervisor.

:::


If a specific version is mentioned and is not there, download it from the [Dynare website](https://www.dynare.org/download/) - choose the **ZIP** version. Then unzip it to the `L: drive` (move it around if necessary so you get the same structure as in the example above, i.e. `L:\common\dynare\(SOME VERSION)\matlab`). Then include the `addpath` command as before.


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


## Running Dynare+MATLAB in Docker


:::{admonition} This is experimental!

Your mileage will vary 

:::

- Consult the [BioHPC Software page](https://biohpc.cornell.edu/lab/userguide.aspx?a=software) to learn how to run Docker on BioHPC. See also [Docker-related procedures](docker-related-procedures).

:::{admonition} Simple command line
:class: note

Obtain the value of `SERVER` from your supervisor.

```bash
MATLAB_VERSION=2021a
MATLAB_LICENSE=27000@SERVER.cornell.edu
DYNARE=4.6.4-2024-04-21
docker1 run --rm -it \
   -v $(pwd):/project \
   -w /project \
   -e MLM_LICENSE_FILE=$MATLAB_LICENSE \
   --entrypoint /bin/bash \
   dynare/dynare:$DYNARE_VERSION
```

:::

### Additional info

- [Building Docker image with MATLAB Toolboxes](https://github.com/mathworks-ref-arch/matlab-dockerfile/tree/main/alternates/building-on-matlab-docker-image)
- [Dynare Docker images with MATLAB](https://hub.docker.com/r/dynare/dynare)