AdsZapTable




Advantage Database Server 12  

AdsZapTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsZapTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsZapTable Advantage Client Engine ace\_Adszaptable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsZapTable  Advantage Client Engine |  |  |  |  |

Removes all records from the table and reindexes it

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsZapTable (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table. |

Remarks

AdsZapTable will remove all records from the table and all data from the memo file, and then the Advantage Client Engine will reindex the table. The indexes must be opened during the zap or they will become invalid. This operation requires exclusive access to the table, which is specified during the open. AdsZapTable is illegal in a transaction.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.htm) for more details.

Example

[Click Here](ace_examples.htm#adszaptableexample)

See Also

[AdsPackTable](ace_adspacktable.htm)

[AdsOpenTable](ace_adsopentable.htm)