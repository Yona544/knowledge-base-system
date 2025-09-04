AdsGetRecordLength




Advantage Database Server 12  

AdsGetRecordLength

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetRecordLength  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetRecordLength Advantage Client Engine ace\_Adsgetrecordlength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetRecordLength  Advantage Client Engine |  |  |  |  |

Retrieves the record size for the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetRecordLength (ADSHANDLE hTable,  UNSIGNED32 \*pulSize); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pulSize (O) | Return size of record. This includes the deleted byte as well. |

Remarks

The record size returned includes space for the deleted byte for DBF table records. For ADT records, this record size will include 5 extra bytes used internally by Advantage. This length may not reflect the actual amount of data accessible for this record if the table includes variable-length fields.

Example

[Click Here](ace_examples.htm#adsgetrecordlengthexample)

See Also

[AdsGetRecord](ace_adsgetrecord.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)