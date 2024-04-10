(include-screenshots)=
# Include Screenshots in the Report

Once you have collected all screenshots, and annotated any discrepancies, you will include them in the report. 

## Describe the differences in words

Describe what you see. In the "Findings"  section, there are separate Table and Figures sections. List out, as a bulleted lists, the differences that you see:

```
- Table 1: The reproduced standard errors are all larger in the 6th column.
- Figure A1: There is a bar missing at the value "6"  in the histogram.
```

## Copy from the `code-check.xlsx`

After the list of all the changes, you should also copy from the `code-check.xlsx` (use the VSCode [Excel to Markdown table](https://marketplace.visualstudio.com/items?itemName=csholmq.excel-to-markdown-table) extension).


## Include the screenshots

Use the Markdown syntax to include the screenshots. 

- for reproduced figures, use the path to the figure as produced
- the figure must be in PNG or JPEG format. Markdown cannot include PDF or Word files. If you need to convert, contact your supervisor, or check to see if there are pipelines available to convert files.

You can use the following syntax:

```markdown

Figure A1 as reproduced:

![Figure A1 as reproduced](123456/figures/figureA1.png)

Figure A1 from the original manuscript:

![Figure A1 from the original manuscript](paper/figureA1.png)

```