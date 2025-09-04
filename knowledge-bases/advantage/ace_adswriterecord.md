AdsWriteRecord




Advantage Database Server 12  

AdsWriteRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsWriteRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsWriteRecord Advantage Client Engine ace\_Adswriterecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsWriteRecord  Advantage Client Engine |  |  |  |  |

Writes any changes in the current record.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsWriteRecord (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |

Remarks

AdsWriteRecord flushes any data changes to the Advantage server. If an implicit lock is held on the record, calling this function will release it.

Example

[Click Here](ace_examples.htm#adswriterecordexample)

See Also

[AdsWriteAllRecords](ace_adswriteallrecords.htm)