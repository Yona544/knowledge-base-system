RemoveTrigger




Advantage Database Server 12  

RemoveTrigger

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| RemoveTrigger  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - RemoveTrigger Advantage TDataSet Descendant ade\_Removetrigger Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| RemoveTrigger  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Removes a trigger from the database.

Syntax

procedure TAdsDictionary.RemoveTrigger( strTriggerName : string );

Parameters

|  |  |
| --- | --- |
| strTriggerName (I) | Name of the trigger to remove. |

Remarks

Removes the specified trigger from the database.

The strTriggerName parameter should be qualified with the table name the trigger belongs to followed by two colon characters ( :: ). For example, "Customers::AfterInsertTrig" would specify you want the property for the trigger called "AfterInsertTrig" that belongs to the "Customers" table.

If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.

ALTER permissions on the associated table are required to remove a trigger from a data dicitonary. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

See Also

[CreateTrigger](ade_createtrigger.htm)