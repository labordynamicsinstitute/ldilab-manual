(r-from-other)=
# Running R from other software

Sometimes, authors will provide code that runs R from within, say, Stata or MATLAB. This is equivalent to calling R from the command line, though the specific command line will differ by system. 

:::{warning}

If R is calling other software, then consult the other sections in this guide.

:::

The example here works through a specific example where R is called from Stata. Adapt as necessary for other code.

## An example

Stata code calls out to R. This may be done in the following way (partial code)

```stata
global r_path "/something/here" //Set path to R program (Adjust this to your local R installation path)
cd "$do_path"
shell "${r_path}/R" --vanilla <"$do_path/Figure1.R" 
```

You need to figure out the path to R on your system. 


:::::{tab-set}

::::{tab-item} Windows

:::{admonition} Shell is not `bash`!
:class: warning

On Windows, the `shell` command is not `bash`. It will call `cmd.exe` command instead.

:::

The easiest way may be to navigate to where R is usually installed. This would be

- `C:\Program Files\R\`

with version-specific subdirectories, e.g.,

- `R-4.4.1`

The full path to the R software is then

- `C:\Program Files\R\R-4.4.1\bin\x64\R.exe` 

So the above would then be (note the forward slashes, not backslashes)

```stata
global r_path "C:/Program Files/R/R-4.4.1/bin/x64" //Set path to R program (Adjust this to your local R installation path)
cd "$do_path"
shell "${r_path}/R" --vanilla <"$do_path/Figure1.R" 
```

::::

::::{tab-item} macOS

On macOS, the path to R is usually

- `/Library/Frameworks/R.framework/Resources/bin/R`

So the above would then be

```stata
global r_path "/Library/Frameworks/R.framework/Resources/bin" //Set path to R program (Adjust this to your local R installation path)
cd "$do_path"
shell "${r_path}/R" --vanilla <"$do_path/Figure1.R" 
```

::::

::::{tab-item} Linux

On Linux, the path to R will depend heavily on the way it was installed. On BioHPC, consult the page. One location might be 

- `/programs/R-4.4.2/bin/R`

So the above would then be

```stata
global r_path "/programs/R-4.4.2/bin" //Set path to R program (Adjust this to your local R installation path)
cd "$do_path"
shell "${r_path}/R" --vanilla <"$do_path/Figure1.R" 
```

::::

:::::

## Caution

Always verify that the code actually ran as intended! 

