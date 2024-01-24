(partc)=
# Writing Report

At this stage, you will write the final version of the report.

## Signalling where you are

Move the Jira issue to "`Writing report`". 

![Move to Writing report](images/AEA-Data-Editor-Workflow-V3-20240114-short-345-3.png)


## Standard steps

- Compare images and tables
  - Some of this may involve "squinting" at images...
  - For tables that are output to Excel, you may be able to use some Excel tools (copy the old numbers, create a difference function between all cells). This is hard to provide examples for, as every table differs.
  - For tables that are output as LaTeX (files ending with `tex`) or as  CSV files, *and* if the authors provided previous versions, you may be able to use Bitbucket to compare them globally, without looking at individual numbers (see [details further down](bitbucket-diff)).

```{warning}
We want to learn about ALL differences that you see, even if minor. 
```

- When there are differences: Include images of figures and screenshots of tables (both paper and as-reproduced) in the report
  - For paper images, use a screenshot tool to grab them from the `PDF_Proof.PDF` and save them as PNG.
  - For reproduced images, reference the location within the replication directory.
  - Using an annotation tool on your computer, circle or highlight where you see differences.

Example:

```

Figure 5 in the paper:

![Figure 5 in paper](figure5-paper.PNG)

Figure 5 as reproduced:

![Figure 5 reproduced](12345/results/figure5.png)

```

- Highlight differences:
    - if only a small number of table entries: mention them by table in the report
    - if a larger number: Highlight on the reproduced images (of figures, screenshots of tables) the differences you have observed
- If there are **too** many differences, let us know immediately, we may then simply send back to the authors with the raw output, and let them address it. 

- There is sample language for commonly encountered problems at the [sample-language-report.md](https://github.com/AEADataEditor/replication-template/blob/master/sample-language-report.md) link in the tall grey bar



:::{admonition} Advanced: Comparing TeX files on Bitbucket
:class: dropdown

If the authors provided LaTeX files as part of the replication package, you may be able to leverage Bitbucket or Git to compare them. 

- Note first that the typical table when output, if identical, will not register as "modified" with Git. 
  - Check the date stamps - if the date is the date you ran the code, then the files were, in fact, replaced, but are not any different.
  - Alternatively, before you run the code, but after you have written the preliminary report, delete all the TeX files (do not git commit!), then run the code. 
  - If the files are reproduced, but git shows no difference, they are identical.
- If for some reason there is a change in platform, git might see a difference, but it is solely the "whitespace" encoding, which differs between Mac, Linux, and Windows. In that case, proceed as follows.
- `git add *tex` then `git commit` and `push` as usual.
- Navigate to the Bitbucket repository, and select the tab "`Commits`". Click on the commit you just made.
- You should see a list of files. Click on the first of the `tex` files you want to inspect.
- You might see the following information:

![Diff too big](/images/Bitbucket-diff-too-big.png)

- Click on the "`give it another chance`". You will now see (or were already seeing) a "git diff", identifying first the old lines (in red), then the new lines (in green). This list can be long.

![Lots of lines](/images/Bitbucket-diff-long.png)

- Navigate to the right of the screen. Choose from the dotted menu the item "Ignore whitespace" (you only need to select the "whitespace" option for the first file).

![Ignore whitespace](/images/Bitbucket-diff-ignore-whitespace.png)

- The page will recalculate the "diffs". If you see the "`give it another chance`", click it again. YOu should now, if the files are truly the same, see the following:

![Files unchanged](/images/Bitbucket-diff-ignore-whitespace-unchanged.png)

- Do this for all `tex` files (you only need to select the "whitespace" option for the first file). If you scroll up to the summary again, you should see a count next to the file. This shows the number of lines changed, taking into account the "whitespace" option.

![0 lines changes](/images/Bitbucket-diff-ignore-whitespace-summary.png)

:::

## Cleaning up

- Clean up the REPLICATION.md - it should be factual, objective, and not written in the first person.
- Copy-and-paste from the `code-check.xlsx`, including the column "Reproduced?" and any notes column, into the "Findings" part. Use the [Excel-to-Markdown plugin](https://marketplace.visualstudio.com/items?itemName=csholmq.excel-to-markdown-table) for VSCode. 
- Delete all of the instructional lines in REPLICATION.md  before finishing the report.

## On Jira

- Check that the `DataCitationSummary` field is filled out indicating how many data citations are in order: all, some, or none. 
- Check that the `Report Location` is filled out. 
  - If it is, do not change it.
  - If for some reason, it is missing, enter the full URL from the repository, e.g., `https://bitbucket.org/aeaverification/aearep-123/src/master/REPLICATION.md`

You can now submit your report for review by changing the status to `Under Review`


![Move to Under Review](images/AEA-Data-Editor-Workflow-V3-20240114-short-345-4.png)