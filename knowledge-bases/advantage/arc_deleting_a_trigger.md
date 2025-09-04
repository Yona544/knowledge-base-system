Deleting a Trigger




Advantage Database Server 12  

Deleting a Trigger

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Deleting a Trigger  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Deleting a Trigger Advantage Data Architect arc\_Deleting\_a\_trigger Advantage Data Architect > Databases > Triggers > Deleting a Trigger / Dear Support Staff, |  |
| Deleting a Trigger  Advantage Data Architect |  |  |  |  |

To delete a trigger, from the tree view within the Connection Repository, right-click the table that owns the trigger you want to delete and select Triggers. Select the trigger in question from the Name combo box. Click Delete. For [database triggers](master_database_triggers.htm), right-click the database object in the Connection Repository and choose Database Triggers from the context menu to visit the trigger dialog.

Note If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.