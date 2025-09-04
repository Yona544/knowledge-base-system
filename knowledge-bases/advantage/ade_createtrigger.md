CreateTrigger




Advantage Database Server 12  

TAdsDictionary.CreateTrigger

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.CreateTrigger  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.CreateTrigger Advantage TDataSet Descendant ade\_Createtrigger Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.CreateTrigger  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

TAdsTrigType = ( ttBefore, ttInsteadOf, ttAfter );

TAdsTrigEventType = ( etInsert, etUpdate, etDelete );

TAdsTrigContainerType = ( ctStdLib, ctCOM, ctScript );

TAdsTrigOption = ( toNoMemosOrBlobs, toNoValues );

TAdsTrigOptions = set of TAdsTrigOption;

 

procedure CreateTrigger( strTriggerName : string;

strTableName : string;

EventType : TAdsTrigEventType;

TriggerType : TAdsTrigType;

ContainerType : TAdsTrigContainerType;

strContainerName : string;

strFunctionName : string;

ulPriority : UNSIGNED32;

strComments : string;

Options : TAdsTrigOptions );

Parameters

|  |  |
| --- | --- |
| strTriggerName (I) | Name of the trigger to create. |
| strTableName (I) | Name of the table the trigger will fire on. |
| EventType (I) | Event that will cause the trigger to fire. |
| TriggerType (I) | Type of trigger to create. |
| ContainerType (I) | Container the trigger code lives in. |
| strContainerName (I) | Name of the container. |
| strFunctionName (I) | The name of the function to call inside the container. This value is ignored if the container type is ctScript. |
| ulPriority (I) | Firing order priority if multiple triggers of the same type exist on a table (for example, multiple AFTER triggers). |
| strComments (I) | Optional description of the trigger. |
| Options (I) | Set of trigger options. Valid options are:  toNoValues: Dont pass values tables (\_\_new and \_\_old) to the trigger function.  toNoMemosOrBlobs: Dont populate values tables when firing a trigger. This can increase performance when large memo or blob fields exist but are not utilized by the trigger.  toNoTransaction: Implicit transaction will not be started for this trigger. |

Remarks

Trigger creation does not verify library or .NET assembly existence. If a trigger is defined on a library or assembly that does not exist, a run-time error will occur when the trigger is executed.

Statements inside script triggers are validated for syntactical correctness only. If any semantic errors exist, a run-time error will occur when the trigger is executed.

If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.

See [Triggers](master_triggers.htm) for more detailed information.

ALTER permissions on the associated table are required to create a trigger. See Advantage Data Dictionary User Permissions for more information

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

See Also

[RemoveTrigger](ade_removetrigger.htm)