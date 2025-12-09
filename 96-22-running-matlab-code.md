(matlab-running)=
#  Running MATLAB without the desktop GUI and with log file

::::{tab-set}

:::{tab-item} Windows


See [these instructions](https://www.mathworks.com/matlabcentral/answers/102082-how-do-i-call-matlab-from-the-dos-prompt) for finding the Matlab binary on the system. However, this should work "out of the box" on CCSS-managed systems from the **Bash** prompt. 

```
start matlab -nosplash  -batch  "addpath(genpath('.'));main;exit"  -logfile matlab-$(date +%F_%H-%M-%S).log
```

where `main.m` is the Matlab program you want to run (you omit the `.m` when calling it). 

```{note}
This will exit, and first appear to do nothing for a few seconds. It will in fact open a Matlab window in the background (check your taskbar after a few seconds). At the end of the MATLAB code, you may need to manually exit MATLAB, but do so only when it is clear that MATLAB has ended! 
```

:::

:::{tab-item} Linux

Assuming MATLAB is in your path (check with `matlab`), the following will generate a logfile. 

```
time matlab -nodisplay -r "addpath(genpath('.')); main; exit" -logfile matlab-$(date +%F_%H-%M-%S).log
```

where `main.m` is the Matlab program you want to run (you omit the `.m` when calling it). 

If you do not have `matlab` in your path, check with system admins. For BioHPC, as long as you are on the ECCO nodes, you should have access. See [BioHPC ECCO page](https://biohpc.cornell.edu/lab/ecco.htm) for some details.

:::

::::

