GetTriggerNames




Advantage Database Server 12  

TAdsDictionary.GetTriggerNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetTriggerNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetTriggerNames Advantage TDataSet Descendant ade\_Gettriggernames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetTriggerNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

TAdsDictionary.GetTriggerNames( poTriggerNames : TStringList );

 

TAdsDictionary.GetTriggerNames( strTableName : string;

poTriggerNames : TStringList );

Parameters

|  |  |
| --- | --- |
| strTableName (I) | The name of the table to retrieve triggers for. |
| poTriggerNames (O) | The list of trigger names names. |

Remarks

This method will retrieve the name of all triggers in a database. If strTableName is specified then only the name of triggers associated with that table will be returned.

See Also

[GetQualifiedTriggerNames](ade_getqualifiedtriggernames.htm)

[GetDatabaseTriggerNames](ade_getdatabasetriggernames.htm)