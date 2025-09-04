DELETED()




Advantage Database Server 12  

DELETED()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DELETED()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DELETED() Advantage Concepts master\_Deleted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DELETED()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the deleted status of the current record.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DELETED( [<tablealias>] ) à lDeleted

Return Values

DELETED() returns true (.T.) if the current record is marked for deletion; otherwise, it returns false (.F.).

Remarks

DELETED() is a database function that determines if the current record in the table is marked for deletion. Since each table has a current record, each table has its own DELETED() value.

In SQL usage, the DELETED() scalar function accepts an optional table alias that can be used when the table reference is ambiguous (e.g., in the case of a join where multiple tables are involved).

See Also

[sp\_PackTable](master_sp_packtable.htm)

[sp\_PackTableOnline](master_sp_packtableonline.htm)

Advantage TDataSet Descendant

[AdsDeleteRecord](ade_adsdeleterecord.htm)

[AdsPackTable](ade_adspacktable.htm)

[AdsRecallRecord](ade_adsrecallrecord.htm)

[AdsIsRecordDeleted](ade_adsisrecorddeleted.htm)

[TAdsSettings.ShowDeleted](ade_showdeleted.htm)

Advantage Client Engine API

[AdsDeleteRecord](ace_adsdeleterecord.htm)

[AdsShowDeleted](ace_adsshowdeleted.htm)

[AdsPackTable](ace_adspacktable.htm)

[AdsRecallRecord](ace_adsrecallallrecords.htm)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.htm)