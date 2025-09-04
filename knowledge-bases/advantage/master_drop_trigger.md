DROP TRIGGER




Advantage Database Server 12  

DROP TRIGGER

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DROP TRIGGER  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - DROP TRIGGER Advantage SQL Engine master\_Drop\_trigger Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DROP TRIGGER  Advantage SQL Engine |  |  |  |  |

Deletes a trigger from the database.

Syntax

DROP TRIGGER <table-name>.<trigger-name>

Remarks

Triggers are supported through the use of the Advantage Data Dictionary. DROP TRIGGER statements must be executed on a valid dictionary connection, and from the dictionary administrator account.

If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.

Example

DROP TRIGGER customers.trigger1