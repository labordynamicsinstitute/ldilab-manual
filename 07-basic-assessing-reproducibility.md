# Assessing computational reproducibility

The basic workflow is simple:

- obtain the (pre-publication) manuscript and any materials
- analyze the README, and possibly appendixes and data sections, to identify all data sources, and all processing instructions
- obtain all code
- obtain all data
- execute all code
- compare the output with the manuscript tables, figures, and in-text 

In practice, this quickly becomes more complicated, and requires a multitude of if-then instructions. At the LDI Lab, we have implemented the generic workflow within a system called Jira, which replicators use to go through the steps above. 

![A complete workflow for reproducibility checks](https://github.com/labordynamicsinstitute/replicability-training/raw/master/images/AEADataEditorWorkflow-20191217.png)

At each step, additional information is requested, mostly through in-app fields and questionnaires, but also via some external tools if the Jira app did not provide the functionality. At the end, a report is created by the replicator, identifying all steps taken, which steps succeeded, and the final outcome.

We will first describe the [prototypical report](#proto-report) and its elements, and then walk through the [detailed steps](#detailed-steps) of the replicator's journey through the system. In our live training, replicators will also work on examples to "get the hang of it."
