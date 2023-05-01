(Access_to_computers)=
# Access to Computers

You will be working on a variety of computers

- your laptop (Windows, OS X, Linux) to access the various resources
- a computer to run the code
  - your laptop (but not necessarily)
  - a Windows remote desktop at 
    - [CCSS-RS](https://socialsciences.cornell.edu/research-support/compute-infrastructure) ([Login instructions](https://socialsciences.cornell.edu/research-support/login-instructions))
    - (beta) [Cloud CCSS](https://client.wvd.microsoft.com/arm/webclient/) ([Instructions](https://cornellprod-my.sharepoint.com/:f:/g/personal/cd642_cornell_edu/EvxDKmDjZyZBsrQvimUR8xABE4x6TYDenmLOY8ZFMLRjUw))
  - possibly a [Linux cluster](https://biohpc.cornell.edu/lab/lab.aspx)
  - [WholeTale](https://docs.google.com/document/d/1hyXMnEKh52V7uFG7C4sLZUdUzF4gGNIvy6990YHGUwg/edit?usp=sharing) (experimental)
  - [CodeOcean](https://codeocean.com/dashboard)
  - [Github Codespaces](https://github.com/codespaces) ([experimental instructions](https://github.com/labordynamicsinstitute/replicability-training/blob/master/draft-codespaces.md))
- [Bitbucket](https://bitbucket.org/account/signup/) 

## General considerations

You only need to use **one** of them, but which one may depend on the particular circumstances of the project you are working on.

### What can you do where

In principle, assuming you have the necessary software, you can work on any computer. Just remember to `git push` all changes back to Bitbucket.

### Where is the data

We are currently exploring how to make the data *mobile*. At present, we do not want the data in Bitbucket, so you will need to re-download the data on each computer you intend to **run programs**. So you should decide on one particular computer. You can edit documents and code anywhere else, but again, remember to `git push` any changes from your *other* computer, and to `git pull` on your *compute* computer.

### What software

By default, you should expect to run the code on , which has a [broad selection of software](https://socialsciences.cornell.edu/research-support/software).

If you actually have the software on your laptop, you should feel free to run code there, but see the caveat below. We will not purchase software for your personal laptop, and we do not provide you with a computationally capable laptop.

Some software is not available or installable on all systemS. If you encounter the following, you should check with your supervisor:

| Software | Computing environment |
|----------|--------------------|
| Dynare   | Red Cloud Windows node, CCSS, CodeOcean|
| Fortran compiler | BioHPC linux cluster, Docker |
| C compiler  | BioHPC linux cluster, CodeOcean (depends on compiler) |
| Eviews | Not currently available |
| RATS   | Not currently available (trial license for laptop)

Much statistical software loads data into memory. Your laptop has a limited amount of memory (in 2018, between 2GB and 8GB, rarely more). CCSS-RS nodes and BioHPC nodes can have between 256GB and 1024 GB of memory!

### What if the code runs for a long time / I need to run to class / I need my life = Twitter back on my laptop

One of the advantages of running on the CCSS-RS or BioHPC nodes is that you can *disconnect* from the server, while leaving your programs running. That is one of the reasons to use them instead of your laptop. 

### Requesting Access

See [setup checklist](checklist).


## Details

The following sections will walk you through the various options. 