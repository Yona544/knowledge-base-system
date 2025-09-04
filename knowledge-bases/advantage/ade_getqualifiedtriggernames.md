GetQualifiedTriggerNames




Advantage Database Server 12  

TAdsDictionary.GetQualifiedTriggerNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetQualifiedTriggerNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetQualifiedTriggerNames Advantage TDataSet Descendant ade\_Getqualifiedtriggernames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetQualifiedTriggerNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

TAdsDictionary.GetQualifiedTriggerNames( poTriggerNames : TStringList );

TAdsDictionary.GetQualifiedTriggerNames( strTableName : string;

poTriggerNames : TStringList );

Parameters

|  |  |
| --- | --- |
| strTableName (I) | The name of the table to retrieve triggers for. |
| poTriggerNames (O) | The list of trigger names. |

Remarks

This method will retrieve the name of all triggers in a database, or if strTableName is specified, then only the name of triggers associated with that table will be returned.

This method retrieves the qualified name of a trigger object. The qualified name includes the table name prefix, followed by two colon characters ( :: ), followed by the trigger name.

See Also

[GetTriggerNames](ade_gettriggernames.htm)

[GetDatabaseTriggerNames](ade_getdatabasetriggernames.htm)