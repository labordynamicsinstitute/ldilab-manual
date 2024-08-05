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


## Graphical overview of flow

```{code-cell} 
:tags: [hide-input]
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges with labels
edges = [('RR', 'CA'), ('RR', 'RR'), ('CA', 'CA'), ('CA', 'Accept'), ('Accept', 'Published')]
edge_labels = {('RR', 'RR'): 'Revise-and-resubmit',
               ('RR', 'CA'): '(Conditional) Accept', 
               ('CA', 'CA'): 'Conditional Accept', 
               ('CA', 'Accept'): 'Accept [with changes]', 
               ('Accept', 'Published'): 'Assessment complete'}

G.add_edges_from(edges)

# Set up the plot
#plt.figure(figsize=(12, 6))
fig, ax = plt.subplots(figsize=(12, 6))

# Define custom positions
pos = {'RR': (-1, 0), 'CA': (0, 0), 'Accept': (1, 0), 'Published': (2, 0)}


# Draw nodes
nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', 
                       node_size=3000)


# Add a box around B and C
box_nodes = ['CA', 'Accept']
box_pos = {node: pos[node] for node in box_nodes}
box = plt.Rectangle((-0.5, -0.5), 2, 1, fill=True, 
                    facecolor='lightgray', edgecolor='gray', 
                    linestyle='--', alpha=0.5)
plt.gca().add_patch(box)
plt.text(-0.4, -0.7, 'Our regular process', fontsize=16)


# Draw edges
nx.draw_networkx_edges(G, pos, ax=ax, arrowsize=20, node_size=3200)

# Draw node labels
nx.draw_networkx_labels(G, pos, ax=ax)

# Custom function to position edge labels
def edge_label_pos(pos, label_pos=0.5, offset=-0.1):
    return {(u, v): ((pos[u][0] + pos[v][0])/2, (pos[u][1] + pos[v][1])/2 + offset)
            for (u, v) in G.edges()}

# Add edge labels with custom positioning
edge_label_pos = edge_label_pos(pos)
for edge, label in edge_labels.items():
    if edge != ('CA', 'CA'):  # Handle all edges except the self-loop
        x, y = edge_label_pos[edge]
        plt.text(x, y, label, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.7), fontsize=8)



# Handle the self-loop for B separately
rad = 1.3
ax.text(pos['CA'][0], pos['CA'][1] + rad , edge_labels[('CA','CA')], ha='center', va='center', 
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.7), 
        fontsize=8)

# Handle the self-loop for A separately
ax.text(pos['RR'][0], pos['RR'][1] + rad , edge_labels[('RR','RR')], ha='center', va='center', 
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.7), 
        fontsize=8)

# Adjust the plot limits to ensure all elements are visible
ax.set_xlim(-1.5, 2.5)
ax.set_ylim(-1, 2)

# Show the plot
ax.axis('off')

plt.tight_layout()
plt.show()
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

