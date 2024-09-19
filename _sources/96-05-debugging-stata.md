(debugging-stata)=
# Debugging Stata

Also check the [LDI Replication Lab Wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Stata-Tips)!

## Specific to certain systems

### RedCloud

#### Problems with temp files

Some (user-written) Stata packages do improper handling of Windows network paths. This affects the use of temp files.

**Symptom**

```stata
> graph ..., saving(`tempfile')
(file \\rschfs2x\share\statatemp\ST_7390_000002.tmp not found)

file \\rschfs2x\share\statatemp\ST_7390_000002.tmp saved as .gph format

...
> graph combine `tempfile` other_file.gph, ...

file \rschfs2x\share\statatemp\ST_7390_000002.tmp not found
```

(the error is not specific to the `graph` command). Note the missing double-backslash in the path.

**Solution**

You need to redirect the STATATMP directory to a non-networked drive:

```bash
export STATATMP="/c/Users/$USERNAME/statatmp"
mkdir "$STATATMP"
cd "/l/workspace/aearep-5697/203501/Data and do-files"
"/c/Program Files/Stata18/StataMP-64.exe" -b master.do
```

This normally succeeds.
