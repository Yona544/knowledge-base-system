---
title: Arc Field Mapping Utility
slug: arc_field_mapping_utility
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_field_mapping_utility.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: e4a0c2c06bff5ee65179688270f06eeed295d40e
---

# Arc Field Mapping Utility

Field Mapping Utility

Field Mapping Utility

Advantage Data Architect

| Field Mapping Utility  Advantage Data Architect |  |  |  |  |

Why youre here?

| 1. | You attempted to paste data into a grid with different header rows than the source grid. |

| 2. | You attempted to paste data into a grid without a header row. |

What to do?

Select the item from Data Fields you wish to match, and select the destination cell in Matched Fields, then select [Replace >>]. Alternatively if you already know all the fields are in the correct order and you have a header row then you can select [Replace All >>>].

If the matching is not how you would like it then feel free to select rows and press [<< Remove], if you wish to destroy the entire match then press [<<< Remove All ]. Then you can make a custom match to your preference.

If you have no header row on your data then de-select Header Row and match accordingly.

Feel free to drag and drop rows in the Matched Fields grid in order to get the proper order for your matching. Alternatively you can select the row you want to move and either press [Up] or [Down]. The side by side grids on the right hand side will display the matching order.

When you feel as though the match is how you would like then you can press [Ok] to commit the changes and proceed with the paste operation. If at any time you wish to abort the past operation then press [Cancel].

If your matching configuration violates any constraints you may have placed on the destination table, then the records that caused the violation will be presented in a failure dialog where you can either save the data, or destroy it and retry your paste with a different matching configuration.
