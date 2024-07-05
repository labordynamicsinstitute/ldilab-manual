(using-pre-pub-openicpsr)=
# Using pre-publication openICPSR Projects 

Typically the AEA Data Editor team will access code and data provided by authors that is stored on [openICPSR](https://www.openicpsr.org/openicpsr/aea). 

> Cornell replicators: You will need to set up an openICPSR account using your Cornell email.

:::{note}

Not all deposits are provided to us on openICPSR. For instructions on how to handle other institutions (Zenodo, Dataverse, etc.), see [these notes](notes-on-downloading-other-repos).

:::

## Basics of openICPSR

- Authors will create a draft deposit that contains the replication archive for their paper.
- Each deposit is identified with a six digit number (`123456`)
- You will download the project and commit the code (but not the data) files to the corresponding Bitbucket repo.

(downloading-with-script)=
## Downloading from openICPSR

::::{tab-set}

:::{tab-item} Downloading using a script

The most convenient way to download the information is to use the LDI-specific script `tools/download_openicpsr-private.py` (be sure to have [set up your environment first](setup-bash)).

**Short version of call to script**

While in your repository directory, open a (Git) Bash shell, and type

```bash
python3 tools/download_openicpsr-private.py 123456
```

which will download a file `123456.zip`. If this has not been done before, it will unzip it into a directory `123456`.

You may need to adjust `python3`  to be `python`, depending on your environment.

**Full options for script**


```bash
python3 tools/download_openicpsr-private.py 123456 . mylogin@cornell.edu
```

where
 - `.` indicates the directory to download the ZIP file to (here, the current directory)
 - `mylogin@cornell.edu`  is the login you use on the openICPSR website (typically, `netid@cornell.edu`)

See [appendix](setup-bash) on how to set up the environment to make the script simpler (i.e., allow the short form to run).

**Expected output**

You should see the following output:

```
openICPSR downloader v2024-02-01
No debug:None
Getting session cookies...
Initiating OAuth flow...
Logging in...
Accessing files...
Getting file info...
Downloading file: 123456.zip
```

If you see anything other than `123456.zip` (replace with your openICPSR project number), then consult the debugging steps below.


:::

:::{tab-item} Downloading a project manually

- Log on to the openICPSR website by clicking on the `Replication package URL` link in Jira
- If you get an error, the project has probably not been shared with you. Contact your supervisor.
- If successfully logged on, you will be able to download the project from the "more" menu:

![](images/openICPSRexample.png)

:::

::::

## When it fails

(provide some guidance when it fails)

## Reminders

Normally, none of the actions below are technically possible, but you should nevertheless follow these guidelines:

- Do not publish the openICPSR projects.
- Do not upload files to the projects.
- Do not share projects with others unless instructed otherwise.
- Do not share screenshots with others

See [Privacy](privacy) section about expectations on privacy.

