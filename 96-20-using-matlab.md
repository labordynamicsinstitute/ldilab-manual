(matlab-related-procedures)=
# MATLAB-related procedures

In this section, we will show you a few things related specifically to running code reproducibly with MATLAB. For more general debugging tips for MATLAB and other computer languages, see [our wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Matlab-Tips).

## Adding `config.m` to MATLAB and path names

When you replace hard-coded filepaths in Matlab, please do the following:

Say the author has code like

```
xlsread('C:\Users\me\submission\AEJMacro\yesterday\data.xlsx')
```

You should do the following:

- Copy [`template-config.m`](https://raw.githubusercontent.com/AEADataEditor/replication-template/master/template-config.m) to the directory of the Matlab script you are running, and call it `config.m`.
- Adjust the options. 
- Add the line `config` to the main Matlab script.

Then

```
% Add this ONCE at the top of the program. Do NOT repeat it.
config
% wherever the hard-coded path appears, replace with
xlsread(fullfile(rootdir,'data.xlsx')
```

This works on any platform.


## Running MATLAB without the desktop GUI and with log file

::::{tab-set}

:::{tab-item} Windows


See [these instructions](https://www.mathworks.com/matlabcentral/answers/102082-how-do-i-call-matlab-from-the-dos-prompt) for finding the Matlab binary on the system. However, this should work "out of the box" on CCSS-managed systems from the Bash prompt. 

```
start matlab -nosplash  -minimize -r  "addpath(genpath('.'));main"  -logfile matlab.log
```

where `main.m` is the Matlab program you want to run (you omit the `.m` when calling it). 

```{note}
This will still open a Matlab window in the background (check your taskbar). 
```

:::

:::{tab-item} Linux

Assuming MATLAB is in your path (check with `matlab`), the following will generate a logfile. 

```
time matlab -nodisplay -r "addpath(genpath('.')); main" -logfile matlab-$(date +%F_%H-%M-%S).log
```

where `main.m` is the Matlab program you want to run (you omit the `.m` when calling it). 

If you do not have `matlab` in your path, check with system admins. For BioHPC, as long as you are on the ECCO nodes, you should have access. See [BioHPC ECCO page](https://biohpc.cornell.edu/lab/ecco.htm) for some details.

:::

::::



## The .m program is using a software extension to MATLAB called "Dynare"

:::{admonition} Do not attempt to **install** Dynare on CCSS or BioHPC computers. 

However, it is not necessary to *install* Dynare, it is sufficient to unpack the ZIP files. Try the information below first:  

:::

:::{warning} 

Use the precise version of Dynare specified by the authors. If that version is not located on `L:\common`, then talk to your supervisor.

:::

- Be sure to include the `config.m` file as outlined above!
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

- You will want the path for the system you are working on. If CCSS Cloud, use the `L:` path. If on BioHPC, you will need to add a path like `/home/ecco_lv39/common/dynare`.
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

If a specific version is mentioned and is not there, download it from the [Dynare website](https://www.dynare.org/download/) - choose the **ZIP** version. Then unzip it to the `L: drive` (move it around if necessary so you get the same structure as in the example above, i.e. `L:\common\dynare\(SOME VERSION)\matlab`). Then include the `addpath` command as before.

If you don't have access to the L drive yet, contact us.
 
## Mention of MEX programs, what do I do?

(or: MEX files provided for Linux/MacOS, but you need to run on Windows)

- There should be `.cpp` files provided - if not, they should be requested from the author
- From within Matlab, run `mex name_of_file.cpp` (though this should also be provided by the author).

## MATLAB complains about a missing Toolbox

Check that the Path includes said Toolbox, see <https://it.mathworks.com/help/matlab/ref/pathtool.html>. It may also be that we are not licensed to use that Toolbox. Make a note of the error in the replication report.
