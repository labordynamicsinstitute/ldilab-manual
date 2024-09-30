(ox-related-procedures)=
# Ox-related procedures

In this section, we will show you a few things related specifically to running code reproducibly with Ox. For more general debugging tips for this and other computer languages, see [our wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/).

## Files

Ox uses the file extension `.ox`. 


## Instructions

Ox is not installed on any of our machines. The best way to run it is to use [Docker on BioHPC](docker-related-procedures).

- Run the Docker image you will have built.
- Inside the running container:
  - Run `oxl filename | tee filename.log` to save the log files (modify `filename` as needed.)
  - If need to modify files as instructed by the authors, exit the Docker container and type `gedit filename`, or do so from your VSCode window.
