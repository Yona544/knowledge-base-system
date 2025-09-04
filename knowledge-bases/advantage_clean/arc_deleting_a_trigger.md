---
title: Arc Deleting A Trigger
slug: arc_deleting_a_trigger
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_deleting_a_trigger.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 24f27571ebcb57369fd009769ee5ad4288cb7ece
---

# Arc Deleting A Trigger

Deleting a Trigger

Deleting a Trigger

Advantage Data Architect

| Deleting a Trigger  Advantage Data Architect |  |  |  |  |

To delete a trigger, from the tree view within the Connection Repository, right-click the table that owns the trigger you want to delete and select Triggers. Select the trigger in question from the Name combo box. Click Delete. For [database triggers](master_database_triggers.md), right-click the database object in the Connection Repository and choose Database Triggers from the context menu to visit the trigger dialog.

Note If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.
