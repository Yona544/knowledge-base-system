AdsAppendRecord




Advantage Database Server 12  

AdsAppendRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsAppendRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsAppendRecord Advantage Client Engine ace\_Adsappendrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsAppendRecord  Advantage Client Engine |  |  |  |  |

Appends an empty record to the end of the given table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsAppendRecord (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |

Remarks

AdsAppendRecord appends a blank record to the end of the table, locks the record, and positions the table to the new record. Changes are written when the user moves off of the appended record or calls [AdsWriteRecord](ace_adswriterecord.htm). Transactions have some affect on appending records; see [Advantage Transaction Processing](master_transaction_processing_system.htm) for more information on appends during transactions.

Note With ADT tables, Advantage implements a record re-use algorithm that recycles records that have been deleted ([AdsDeleteRecord](ace_adsdeleterecord.htm)). This means that the newly appended record may not actually be at the end of the table. An application should not make any assumptions about the new record number.

Example

[Click Here](ace_examples.htm#adsappendrecordexample)

See Also

[AdsDeleteRecord](ace_adsdeleterecord.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)