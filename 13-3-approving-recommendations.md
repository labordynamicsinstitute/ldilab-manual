---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(choosing-recommendation)=
# Choosing a Recommendation


```{code-cell} 
:tags: [margin hide-input]
from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Flow Diagram')

# Add nodes
dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.node('D', 'D')

# Add edges with labels
dot.edge('A', 'B', 'Label 1')
dot.edge('B', 'B', 'Label 2')
dot.edge('B', 'C', 'Label 3')
dot.edge('C', 'D', 'Label 4')

# Create a subgraph for the box around B and C
with dot.subgraph(name='cluster_0') as c:
    c.attr(style='filled', color='lightgrey')
    c.node_attr.update(style='filled', color='white')
    c.nodes('B', 'C')
    c.attr(label='Box')

# Display the graph
dot
```

## Recommendations for `CA` reports

Approvers must select/confirm one of the recommendations (field `MCRecommendationV2`):

- **Accepted** - the manuscript moves forward in the publishing workflow on Manuscript Central, the Data Editor does not see the manuscript again.
- **Accepted with changes** - same, but some conditions may be imposed. However, the Data Editor does not need to see the manuscript again.
- **Revisions requested - manuscript ready** - Some revisions need to be made, and the Data Editor needs to see the authors' response. However, the manuscript can move forward in the publishing workflow. This is rarely used, but opens up the possibility that the managing editors can pull out a manuscript from this category to move forward, depending on the backlog for publication.
- **Conditional Acceptance** - the Data Editor expects to see a response from the authors to the report.
- **Revise and resubmit** - the Data Editor has detected a serious problem which needs to go back to the "Revise and resubmit" phase of the publishing workflow. This is only invoked if there are significant concerns as to the validity of the manuscript's conclusions based on the reproduction attempt. **Rarely used, and only for the most serious cases.**


## Recommendations for `RR` reports

Approvers must select/confirm one of the recommendations (field `MCRecommendation`):

- **Accept** - the manuscript moves forward in the publishing workflow on Manuscript Central, the Data Editor does not need to see the manuscript again **during the `RR` phase** of the publishing workflow (we will see it again as a `CA`).
- **Revise and resubmit** - the Data Editor expects to see a response from the authors to the report, and wants to see it again before the Editor can issue a `CA` decision.
- **No recommendation** may be chosen in specific cases. Rare.
- **Reject** - the Data Editor has detected a serious problem. This is only invoked if there are significant concerns as to the validity of the manuscript's conclusions based on the reproduction attempt. **Rarely used, and only for the most serious cases.**
- **By email** kept for technical reasons, should not be chosen.


## Publication

Once all review rounds have been completed, the last revision will lead to a recommendation of "Accepted". The Data Editor's staff prepares the openICPSR deposit for final publication. See [Preparing for publication](aea-interfacing-with-the-journal-management-system) for details.

