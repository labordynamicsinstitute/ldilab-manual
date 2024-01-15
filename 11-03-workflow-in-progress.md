(in-progress)=
# In Progress

At this point, the repository exists. 

(collecting-information)=
## Collecting information 

At this stage, you are collecting information. 

- [ ] Fill out the following fields in the Jira ticket (some may be pre-populated):
    - [x] `Replication package URL` In almost all cases, this is the openICPSR repo for which you will have received a notification email.
      - If code and/or data are provided by email, `Replication package URL` should be filled out with  "https://email", otherwise with a DOI or URL.
    - [x] `Journal` 
    - [x] `Manuscript Central identifier`
    - [ ] `Bitbucket short name` (e.g., `aearep-123`) 
      - this should then auto-fill  `Git working location`.
- The following fields, located in the **REPL. INFO** tab area 2 of the screen, must also be filled out:
  ![Replication Info](images/jira-screen.png)
    - [ ] `Empirical Article`: "Does the article contain empirical work, simulations, or experimental work?" 
      - typically the answer should be "Yes". You should answer "No" only if you read the article and find that it is entirely theoretical, no simulations or empirical work at all.
    - [ ] `RCT`: Is the paper about a randomized control trial? This should be immediately obvious from the abstract.
      - `RCT NUMBER`: If it is an RCT, fill in the associated RCT registration number (typically in the title page footnote)

## Choosing the next steps

From here, there should be two sub-tasks. There are two possibilities now:

### You complete the subtasks sequentially

- [ ] First, complete the [`Prepare preliminary report (Part A)`](parta) subtask.
- [ ] Then, [`run the code` and complete the Part B report](running-code-partb).

### You and somebody else complete the subtasks in parallel

In some cases, you will be working with somebody else. 

- One person does [`Part A`](parta): _____________
- Another person does [`Part B`](running-code-partb): ________________

In general, the person doing `Part A` should then also, once `Part B` is completed, merge in the information from `Part B` and write the final `Findings` section (`Part C`).

We will describe Parts A and B in sequence, but as needed, you should skip ahead.
