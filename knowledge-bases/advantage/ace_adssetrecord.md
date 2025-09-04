AdsSetRecord




Advantage Database Server 12  

AdsSetRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetRecord Advantage Client Engine ace\_Adssetrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetRecord  Advantage Client Engine |  |  |  |  |

Sets the current record to the given data buffer.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetRecord (ADSHANDLE hObj,  UNSIGNED8 \*pucRec,  UNSIGNED32 ulLen); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, or index order. |
| pucRec (I) | Return record contents in the buffer. |
| ulLen (I) | Length of record. This is a validation parameter to tell the Advantage Client Engine the calling application has the correct record length. |

Remarks

Using AdsSetRecord is not recommended, especially if there are memo fields or extended data types used in the table. It is very easy to corrupt data with errant calls.

Note The first byte of the record image contains status information on encryption, deletion, and transaction processing that should only be manipulated by Advantage. Therefore, the first byte passed to this function is ignored.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to AdsInitRawKey and AdsBuildRawKey.

Example

[Click Here](ace_examples.htm#adssetrecordexample)

See Also

[AdsGetRecord](ace_adsgetrecord.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsGetRecordLength](ace_adsgetrecordlength.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)