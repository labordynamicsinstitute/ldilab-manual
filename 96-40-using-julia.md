(julia-related-procedures)=
# Julia-related procedures

In this section, we will show you a few things related specifically to running code reproducibly with Julia. For more general debugging tips for Julia and other computer languages, see [our wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Julia-Tips).

:::{admonition} The following instructions are primarily for Linux. 
:class: warning dropdown

You may need to use Conda on our Windows systems.

:::


## Managing multiple Julia versions

Julia has a native version manager. Follow instructions at [https://github.com/JuliaLang/juliaup](https://github.com/JuliaLang/juliaup) to install it - it will be installed in your personal directory (so is not shared). Then, to add a particular Julia version,

```
juliaup add 1.9.2
juliaup default 1.9.2
```

and your next call to Julia will launch 1.9.2. 

## Julia is picky about how environments are passed to workers

```
julia --project=julia16 -p 4
```
should start with the project installed in `julia16` and 4 worker processes. In fact, the worker processes ignore the project packages, and the whole thing fails (see [this link](https://github.com/JuliaLang/julia/issues/28781)).

Workaround:

```
export JULIA_PROJECT=julia16
julia -p 4
```
seems to work.
