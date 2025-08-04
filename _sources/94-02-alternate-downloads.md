(notes-on-downloading-other-repos)=
# Alternate sources of data

We sometimes encounter replication packages that reference Dataverse or Zenodo. Download those as they are found on those sites. Extract them as you would the openICPSR downloads, but please pay attention to the directory naming structure:

| Source | DOI or project | Directory name (`DIRNAME`) |
|--------|----------------|------------------|
| openICPSR | https://doi.org/10.3886/E**123456**V1 | `123456` |
| openICPSR | openicpsr-**123456**  | `123456` |
|Dataverse  | https://doi.org/10.7910/DVN/RE5ZVI |  `dv-10.7910-DVN-RE5ZVI`| 
|Dataverse  | https://doi.org/10.3456/ABCDE |  `dv-10.3456-ABCDE`| 
|Zenodo     | https://doi.org/10.5281/zenodo.7041706|  `zenodo-7041706`|

## Usage

Whether [manually downloading the files](using-pre-pub-openicpsr) or using the scripts, once the ZIP file is downloaded, you would still use

```bash
    unzip -n NAME_OF_ZIP.zip -d DIRNAME
```

where `DIRNAME` is defined as in the table above, and `NAME_OF_ZIP.zip` is whatever you downloaded from the repository. In the case of the [openICPSR download script]((get-the-data), the file downloaded from openICPSR is typically called `DIRNAME.zip`, e.g, `123456.zip`. It will be called something else in most other cases.
