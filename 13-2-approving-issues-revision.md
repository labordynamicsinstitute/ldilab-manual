#  Revision Report

The checklist of items to review are roughly the same as above.  In addition:

- The pre-approver should check that `[We REQUESTED]` tags are used in place of `[REQUIRED]` tags.  These tags should be preceded by a ">" to create a comment rather than "-," which creates a bullet point.
   - The script [`aeareview`](https://github.com/AEADataEditor/editor-scripts) changes all the `[REQUIRED]` to `[We REQUESTED]`.
- The report should reflect the **current** state of the replication.
- In the **Summary Section:**
   - Create a new section "`### Previously`" that covers all the action items from the previous round.
   - Create a list of persisting issues that require attention. These should be added as action items to the usual section, in addition to any new items. 
   - There is no need to distinguish new from persistent action items: the action item list should simply contain a complete and exhaustive (check)list of items that need to be done.

Example:

```
### Action Items (Manuscript)

- [REQUIRED] The data collection reported in this article had IRB approval. Please provide full IRB approval information, including protocol number and home institution of the IRB, in the titlepage footnote.

### Action Items (openICPSR)

...

### Previously

> [We REQUESTED] The data collection reported in this article had IRB approval. Please provide full IRB approval information, including protocol number and home institution of the IRB, in the titlepage footnote.

Not done. The manuscript still does not mention the IRB information in the titlepage footnote.
```
