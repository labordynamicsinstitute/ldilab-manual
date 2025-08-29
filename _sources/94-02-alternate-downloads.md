(notes-on-downloading-other-repos)=
# Alternate sources of data

We sometimes encounter replication packages that reference Dataverse or Zenodo. Download those as they are found on those sites. Extract them as you would the openICPSR downloads, but please pay attention to the directory naming structure:

| Source | DOI or project | Directory name (`DIRNAME`) | Pipeline Variable |
|--------|----------------|------------------|----|
| openICPSR | https://doi.org/10.3886/E**123456**V1 | `123456` | `123456` |
| openICPSR | openicpsr-**123456**  | `123456` |  `123456` |
|Dataverse  | https://doi.org/10.7910/DVN/RE5ZVI |  `dv-10.7910-DVN-RE5ZVI`| |
|Dataverse  | https://doi.org/10.3456/ABCDE |  `dv-10.3456-ABCDE`|  |
|Zenodo     | https://doi.org/10.5281/zenodo.7041706|  `zenodo-7041706`| `7041706` |
| World Bank| https://doi.org/10.60572/101y-vn15 | `wb-101y-vn15` | `101y-vn15` or entire DOI |

If a `Pipeline Variable` is given, use that in the [Bitbucket Pipeline](create-repo) when [creating](create-repo) or [updating](updating-repository-pipeline) the repository.

## Usage

Whether [manually downloading the files](using-pre-pub-openicpsr) or using the scripts, once the ZIP file is downloaded, you would still use

```bash
    unzip -n NAME_OF_ZIP.zip -d DIRNAME
```

where `DIRNAME` is defined as in the table above, and `NAME_OF_ZIP.zip` is whatever you downloaded from the repository. In the case of the [openICPSR download script]((get-the-data), the file downloaded from openICPSR is typically called `DIRNAME.zip`, e.g, `123456.zip`. It will be called something else in most other cases.

## Utility scripts

We have a few scripts, some of which have not yet been integrated into the pipeline. All can be run from the command line instead of manually downloading the repository. All are in the `tools` directory of your issue-specific repository. If not, refresh the tools.

- [**download_openicpsr-private.py**](help-download_openicpsr-private): For downloading from private openICPSR deposits (also integrated into the pipeline)
- [**download_dv.py**](help-download_dv): For downloading from Dataverse repositories.
- [**download_osf.sh**](help-download_osf): For downloading from OSF repositories.
- [**download_worldbank.py**](help-download_worldbank): For downloading from World Bank Reproducibility Repository, including the public reproducibility report!
- [**download_zenodo_public.sh**](help-download_zenodo_public): For downloading from public Zenodo repositories
- [**download_zenodo_draft.py**](help-download_zenodo_draft): For downloading from private/draft Zenodo deposits (also integrated into the pipeline)