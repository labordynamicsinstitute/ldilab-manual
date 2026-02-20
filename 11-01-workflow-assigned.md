
(workflow-assigned)=
# Assigned  

When you are first assigned an issue, it will in the `Assigned` status. 

```{note}
The link to JIRA is [https://aeadataeditors.atlassian.net/jira](https://aeadataeditors.atlassian.net/jira) (requires login).
```

## Identifying whether the issue is a revision or not

```{warning}
Is the current Jira issue an **original report** (first time we see the manuscript) or **is it a revision** (we've seen the manuscript before)?
```

![Is it a revision or not?](images/AEA-Data-Editor-Workflow-V3-20240114-short-123.png)

### Signs that this case is a revision

![Signs that it's a revision](images/revisions.png)

- [ ] Check the `MCStatus` field: 
  - If it says "`RR`" or "`CA`", then it is an "original report" - proceed to the next step ([`Creating repository`](create-repo)).
  - If it says "`CA` `Revision`", then it is ... a revision! 
    - Follow the instructions at "[Revision reports after author resubmission](aea-revision-reports-after-author-resubmission)".
    - In particular, **do NOT create a new repository** - you will re-use the previous repository. Enter the previous repository "stub" into the `Bitbucket short name` field.
    - In particular, **do NOT create "update" or "new" directories** The current state of the repository should always correspond to the author's structure. Overwrite files, delete files. The previous state is preserved in Git. This will also tell you what files have changed.
    - When running a second replication on the same archive, please be sure to have the committed "REPLICATION.md" be accurate when you commit it - do not let it contain holdover data from a previous replication attempt, as this can lead to confusion.
    - Once you have entered the previous repository "stub" into the `Bitbucket short name` field, you can proceed to [`In Progress`](in-progress).

```{warning}
If a field on Jira is already filled out, **do not edit it**. The only exception is if software is missing from the `Software used` field.
```

## If this is not a revision

The next thing you must do, if this is **not a revision** is to either create a new repository ([`Create repository`](create-repo)) in order to move to `In Progress`.

- This lets us know that you have started working on replication.

## If this is a "split" case

It will happen that the usual order (first Part A, then Part B) is not followed. This may happen if the reproducibility check was done automatically, by a third party, or for various other reasons.

- One person will be assigned the overall responsibility for the case. This is the person the case is **Assigned** to, and they take responsibility for tracking Parts A, B, and C, all the way through to submission for review.
- Usually (but not always), that same person will be assigned Part A.
- If Part B is assigned to a different person, then often the FIRST person to touch the case will have ([`created a repository`](create-repo)). 

:::{warning}

Whoever creates the repository first should leave a note in the comments, and be sure to fill out the `Bitbucket short name` field on Jira, so that the second person can find the repository and use it for their work.

:::

- The person who is assigned Part B, if not the primary assignee, **should ALWAYS work in a branch** of the repository (typically called `part-b`) and should not touch any of the documents usually used by Part A. See [notes in **Preparing to Run Code**](prepare-to-run-code).