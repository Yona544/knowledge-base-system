AdsWriteAllRecords




Advantage Database Server 12  

AdsWriteAllRecords

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsWriteAllRecords  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsWriteAllRecords Advantage Client Engine ace\_Adswriteallrecords Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsWriteAllRecords  Advantage Client Engine |  |  |  |  |

Writes changes for all open tables in the current application.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsWriteAllRecords(); |

Parameters

None.

Remarks

AdsWriteAllRecords will flush all pending updates on all open tables to disk. It will also release all implicit locks held in all tables.

Example

[Click Here](ace_examples.htm#adswriteallrecordsexample)

See Also

[AdsWriteRecord](ace_adswriterecord.htm)