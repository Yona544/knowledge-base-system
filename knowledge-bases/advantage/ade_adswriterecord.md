AdsWriteRecord




Advantage Database Server 12  

TAdsTable.AdsWriteRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsWriteRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsWriteRecord Advantage TDataSet Descendant ade\_Adswriterecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsWriteRecord  Advantage TDataSet Descendant |  |  |  |  |

Writes any changes in the current record.

Syntax

procedure AdsWriteRecord;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: Post. See your Delphi documentation for more information about this native Delphi method.

Description

AdsWriteRecord flushes any data changes to the servers disk. If an implicit lock is held on the record, calling this function will release it.

Example

AdsTable1.Append;

AdsTable1.FieldByName( LastName ).AsString := Smith;

AdsTable1.Post;

See Also

None.