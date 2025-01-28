(matlab-config)=
# Adding `config.m` to MATLAB and path names

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

