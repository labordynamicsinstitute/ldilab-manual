(Access_to_computers)=
# Access to Computers

You will be working on a variety of computers

- your laptop (Windows, OS X, Linux) to access the various resources
- a computer to run the code
  - your laptop (but not necessarily)
  - a Windows remote desktop at [CCSS-RS](https://socialsciences.cornell.edu/research-support/compute-infrastructure) 
    - [Login instructions](https://socialsciences.cornell.edu/research-support/login-instructions)
  - possibly a [Linux cluster](https://biohpc.cornell.edu/lab/lab.aspx)
  - [WholeTale](https://docs.google.com/document/d/1hyXMnEKh52V7uFG7C4sLZUdUzF4gGNIvy6990YHGUwg/edit?usp=sharing) (experimental)
  - [CodeOcean](https://codeocean.com/dashboard)
  - [Github Codespaces](https://github.com/codespaces) ([experimental instructions](https://github.com/labordynamicsinstitute/replicability-training/blob/master/draft-codespaces.md))
- [Bitbucket](https://bitbucket.org/account/signup/) 

## General guidelines

### Additional setup instructions

::::{tab-set}

:::{tab-item} CCSS-RS

- You should synchronize your VSCode settings with your *normal* computer. This will bring over any settings and extensions! Very useful.
- You should do additional setup for your Git bash shell: this includes making downloads from openICPSR simpler. See [appendix](setup-bash).

### What can you do where

In principle, assuming you have the necessary software, you can work on any computer. Just remember to `git push` all changes back to Bitbucket.

### Where is the data

We are currently exploring how to make the data *mobile*. At present, we do not want the data in Bitbucket, so you will need to re-download the data on each computer you intend to **run programs**. So you should decide on one particular computer. You can edit documents and code anywhere else, but again, remember to `git push` any changes from your *other* computer, and to `git pull` on your *compute* computer.

### What software

By default, you should expect to run the code on , which has a [broad selection of software](https://socialsciences.cornell.edu/research-support/software).

If you actually have the software on your laptop, you should feel free to run code there, but see the caveat below. We will not purchase software for your personal laptop, and we do not provide you with a computationally capable laptop.

Some software is not available on CCSS-RS. If you encounter the following, you should check with your supervisor:

| Software | CCSS-RS |
|----------|--------------------|
| Dynare   | Red Cloud Windows node |
| Fortran compiler | BioHPC linux cluster |
| C compiler  | BioHPC linux cluster |
| Eviews | Not currently available |

Much statistical software loads data into memory. Your laptop has a limited amount of memory (in 2018, between 2GB and 8GB, rarely more). CCSS-RS nodes and BioHPC nodes can have between 256GB and 1024 GB of memory!

### What if the code runs for a long time / I need to run to class / I need my life = Twitter back on my laptop

One of the advantages of running on the CCSS-RS or BioHPC nodes is that you can *disconnect* from the server, while leaving your programs running. That is one of the reasons to use them instead of your laptop. 

### Requesting Access

See [setup checklist](checklist).


### Where can I learn more

- For CCSS-RS nodes, see [CCSS-RS](https://socialsciences.cornell.edu/research-support/compute-infrastructure).
- For special *Red Cloud* nodes, see [here](https://github.com/labordynamicsinstitute/replicability-training/wiki/Connect-to-a-CCSS-RS-Custom-Red-Cloud-Machine)
