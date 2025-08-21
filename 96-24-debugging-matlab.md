(matlab-debugging)=
# Debugging MATLAB-related problems


## The .m program is using a software extension to MATLAB called "Dynare"

See [Using Dynare in MATLAB](dynare-matlab).

 
## Mention of MEX programs, what do I do?

(or: MEX files provided for Linux/MacOS, but you need to run on Windows)

- There should be `.cpp` files provided - if not, they should be requested from the author
- From within Matlab, run `mex name_of_file.cpp` (though this should also be provided by the author).

## MATLAB complains about a missing Toolbox

Check that the Path includes said Toolbox, see <https://it.mathworks.com/help/matlab/ref/pathtool.html>. It may also be that we are not licensed to use that Toolbox. Make a note of the error in the replication report.
