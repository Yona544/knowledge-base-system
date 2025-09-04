---
title: Arc Creating Ri Objects With The Er Diagramming Tool
slug: arc_creating_ri_objects_with_the_er_diagramming_tool
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_ri_objects_with_the_er_diagramming_tool.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: c5e4a44db62ccd04bef80383b6c08e3fed60c374
---

# Arc Creating Ri Objects With The Er Diagramming Tool

Creating Referential Integrity Objects with the ER Diagramming Tool

Creating Referential Integrity Objects with the ER Diagramming Tool

Advantage Data Architect

| Creating Referential Integrity Objects with the ER Diagramming Tool  Advantage Data Architect |  |  |  |  |

To create an RI object with the ER Diagramming Tool:

| 1. | Verify that the child and parent tables are on the ER View sheet. |

| 2. | Drag a field from the child table to the parent table. It does not matter which child field you drag to the parent table. |

| 3. | [Create a new RI object](arc_creating_or_modifying_an_ri_object.md). |

| 4. | To put all records that do not meet the new constraint into a table, you will need to enter a path for a fail table. If you enter a path to an existing table, make sure it is the same format as the child table. If a path is entered to a table that does not exist, it will be created. |

| 5. | Click OK to create the RI object and a line will be drawn between the two tables, representing the relationship. |
