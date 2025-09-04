ace\_AdsIsTableTransactionFree




Advantage Database Server 12  

AdsIsTableTransactionFree

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsTableTransactionFree  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsTableTransactionFree Advantage Client Engine Ace\_AdsIsTableTransactionFree Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsTableTransactionFree  Advantage Client Engine |  |  |  |  |

Determines if the given table is currently a transaction-free table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsTableTransactionFree( ADSHANDLE hTable,                            UNSIGNED16\* pusTransFree ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table |
| pusTransFree (O) | Current transaction-free state of the table.  Will be True on return if the table is currently a transaction-free table. |

Remarks

AdsIsTableTransactionFree returns true if the table is currently configured as a transaction-free table, and false otherwise.

See Also

[AdsBeginTransaction](ace_adsbegintransaction.htm)

[AdsCommitTransaction](ace_adscommittransaction.htm)

[AdsRollbackTransaction](ace_adsrollbacktransaction.htm)

[AdsSetTableTransactionFree](ace_adssettabletransactionfree.htm)

[Transaction-Free Tables](master_transaction_free_tables.htm)