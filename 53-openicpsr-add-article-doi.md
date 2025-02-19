
(adding-article-doi-icpsr)=
# Adding the article DOI to the openICPSR deposit metadata

- Choose the space "related publications"

[screenshot here]

- (optional) remove the existing manually added temporary link (usually with date "n.d.")
- obtain the article's DOI
- use the "Import from DOI" functionality
- Verify that all information seems correct.
- Save.

It is not necessary to publish the deposit again, this metadata takes effect immediately.

```{note}
Authors can also do this themselves. In the case of PSID or related repositories, this action **must** be performed by authors themselves.
```

(adding-article-doi-dataverse)=
# Adding the article DOI to the Dataverse deposit metadata

When the replication package is hosted at a Dataverse repository, the article DOI must be added to the metadata by the authors or the Dataverse curators. The following steps describe how to convey this to the authors or curators

## Go to the deposit

The deposit DOI should be available in the field `RepositoryDOI`. Click on it.

## Choose `Contact Owner`

There usually is a button called `Contact Owner` top right:

![Contact Owner](images/dataverse-contact-form-1.png)

## Fill out the `Email Dataset Contact` form

You should use the following information:

- **From**: `dataeditor@aeapubs.org`
- **Subject**: `Please add article DOI to deposit metadata`
- **Message**: 

```
Dear [AUTHOR], others,

please add the article DOI ([DOI HERE]) to the "Related Publication" field. We would appreciate it.

Sincerely,

Lars Vilhuber and the Data Editor team
```

where you should replace `[AUTHOR]` with the author's name, and `[DOI HERE]` with the article DOI.

Then fill out the math problem, and hit `Send Message`.

![Send message](images/dataverse-contact-form-2.png)

## Make a note in Jira

Add a comment in the Jira ticket:

```
Left note on Dataverse contact form, requesting that authors  add article DOI to deposit metadata.
```
