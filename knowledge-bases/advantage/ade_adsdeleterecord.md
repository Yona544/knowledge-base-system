AdsDeleteRecord




Advantage Database Server 12  

TAdsTable.AdsDeleteRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsDeleteRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsDeleteRecord Advantage TDataSet Descendant ade\_Adsdeleterecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsDeleteRecord  Advantage TDataSet Descendant |  |  |  |  |

Marks the current record in the given table as deleted.

Syntax

procedure AdsDeleteRecord;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: Delete. See your Delphi documentation for more information about this native Delphi method.

Description

In DBF tables, AdsDeleteRecord works with the current record. AdsDeleteRecord does not actually remove the current record from the DBF table. The record is marked as deleted in the first byte of the record image. The record can be recalled using AdsRecallRecord. Query the deleted status of a record by using AdsIsRecordDeleted. Deleted records can be removed from tables completely by using [AdsPackTable](ade_adspacktable.htm).

In Advantage proprietary ADT tables, AdsDeleteRecord will permanently delete the current record. The record cannot be recalled using AdsRecallRecord after the record has been written.

Note Deleted ADT records are automatically placed in a record re-use list. Because of this, they are unlocked by the server even if the user has an explicit lock on the record.

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.Delete;

See Also

[AdsIsRecordDeleted](ade_adsisrecorddeleted.htm)

[AdsPackTable](ade_adspacktable.htm)

[AdsRecallRecord](ade_adsrecallrecord.htm)