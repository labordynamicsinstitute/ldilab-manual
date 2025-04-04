
# Background

On July 16, 2019, the AEA announced an updated "[Data and Code Availability Policy](https://www.aeaweb.org/journals/policies/data-code)" {cite:p}`AEA-announcement-July-2019,10.1257/pandp.110.dcap`. Henceforth, 
replication materials were to be made available to the AEA *prior* to acceptance - previously, it was prior to publication, but *after* acceptance. 
Computer code should be provided for all stages of the data cleaning and data analysis (code for the data cleaning portion was previously optional). 
Raw data must be uniformly made available, when permissions allow (also for author-collected survey data,   data from experiments). For restricted-access or proprietary data, to the extent permissible, the data must be made available to the AEA Data Editor for verification, even if the data cannot be published by the author.^[We regularly and successfully do so.]
Enforcement of an existing but unenforced **data citation requirement** as per [AEA Citation Guidelines](https://www.aeaweb.org/journals/policies/sample-references).

We also test licenses, access restrictions, and sometimes question the ability of authors to publish the data. We have had cases both ways: data provided after initial refusal, and data rejected by us because the license did not allow distribution.

For now, we also check for obvious personally identifiable information (PII). However,  the ultimate responsibility lies with authors.

All data and code must be available in a "trusted repository," which in most cases means the AEA's Data and Code Repository at openICPSR, for better transparency and findability. 		 ZIP files are no longer  accepted as supplementary packages, and we check that. 		Supplements are  tagged with JEL codes, other keywords (e.g., "`Current Population Survey`" or "`behavioral study`"), and optionally with methodological information (time period,  geographic region, survey method used). 		Each deposit gets its own DOI - a permanent unique identifier. Deposits can be found  through various search engines, such as the native search engine on openICPSR, through [Google Data Search](https://toolbox.google.com/datasetsearch) or through DOI registries such as [DataCite](https://search.datacite.org/).
		
To implement all this, we built a system using Jira, and connect to it from ScholarOne (system used for manuscript submission) and  openICPSR. 

## Activities of the LDI Replication Lab

The LDI Replication Lab conducts reproducibility checks in two way.


### Pre-Publication Evaluation of Reproducibility and Quality of Supplemental Materials

The Lab performs pre-publication evaluation for the American Economic Association, i.e., prior to publication. Think of it as a "reviewer" of the data supplement.

- Analyze the provided materials - see [Verification guidance](https://social-science-data-editors.github.io/guidance/Verification_guidance.html)
- Verify data citations
- Verify ability to post data (do the authors have the right to post the data?)
- If possible, attempt replication

### Post-Publication Evaluation of Reproducibility 

We download articles and supplements, assess to what extent an undergraduate student can run the code that produces the analysis reported in the paper.
We have also in the past done an evaluation of the response of authors when the code is only available "upon request". Not currently an active project.

This is a secondary goal, as time permits or as research goals suggest. It is quite similar to the first goal, but there is no interaction with authors, and no method to improve authors' files.

> Interested parties might visit [ACRE](https://bitss.github.io/ACRE/) for how to incorporate this kind of activity into a class curriculum.

## Learning goals

In this training, you will learn how to verify compliance with the policy. This means going through a variety of checklists, obtaining data, and running code, as per instructions provided by authors. You will not be required to actively program, but you will learn a lot about how to program (and sometimes, how not to program). You will gain an appreciation for a well-structured empirical analysis, which you will benefit from for your own studies (now) and in your work (after graduation).
