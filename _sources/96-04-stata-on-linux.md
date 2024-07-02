(stata-on-biohpc)=
# Stata on Linux


:::{admonition} BioHPC specific
:class: note

On BioHPC, Stata is only available on ECCO nodes, and is not described in the general software notes. See [Stata notes for BioHPC using ECCO](https://labordynamicsinstitute.github.io/ecco-notes/docs/biohpc/stata.html). Follow the notes on how to set up `modules` at [https://labordynamicsinstitute.github.io/ecco-notes/docs/biohpc/software.html#using-module](https://labordynamicsinstitute.github.io/ecco-notes/docs/biohpc/software.html#using-module).

:::

## Finding Stata

- There are multiple versions of Stata on BioHPC: 14, 16, and 18
- You should always use `stata-mp`
- Stata is not "in the path", so you should do one of the following:
  - Reference the version of Stata explicitly: `/usr/local/stata16/stata-mp` or `/usr/local/stata18/stata-mp`
  - Add Stata to the path: 

```
export PATH=/usr/local/stata16:$PATH
```

and then simply use `stata-mp` in the same session (the `PATH` gets reset once you log out from a session or close the terminal.

## TMP directory

Ensure that the `tmp` directory being used is running on the BioHPC `/workdir` space, by running the following commands before executing your program(s):

```
export STATATMP=/workdir/netid/tmp
mkdir $STATATMP
```

before launching Stata.
