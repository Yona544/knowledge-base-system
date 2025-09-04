Advantage Client Engine Transaction Processing APIs




Advantage Database Server 12  

Advantage Client Engine Transaction Processing APIs

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Client Engine Transaction Processing APIs  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Advantage Client Engine Transaction Processing APIs Advantage Client Engine ace\_Advantage\_client\_engine\_transaction\_processing\_apis Advantage Client Engine > API Reference > Advantage Client Engine Transaction Processing APIs / Dear Support Staff, |  |
| Advantage Client Engine Transaction Processing APIs  Advantage Client Engine |  |  |  |  |

The Advantage Client Engine provides API functions to support transaction processing.

[AdsBeginTransaction](ace_adsbegintransaction.htm)

AdsBeginTransaction begins a transaction for all connected servers or for the indicated connection.

[AdsCommitTransaction](ace_adscommittransaction.htm)

AdsCommitTransaction commits active transactions for all connected servers or for a given connection.

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.htm)

AdsFailedTransactionRecovery instructs the Advantage Database Server to clean up any failed transactions.

[AdsInTransaction](ace_adsintransaction.htm)

AdsInTransaction returns a flag to the caller to indicate if the given connection has an active transaction.

[AdsIsTableTransactionFree](ace_adsistabletransactionfree.htm)

AdsIsTableTransactionFree returns a flag to the caller to indicate if the given table is defined as a [transaction-free table](master_transaction_free_tables.htm).

[AdsRollbackTransaction](ace_adsrollbacktransaction.htm)

AdsRollbackTransaction rolls back active transactions on all connected servers or the given connection.

[AdsGetTransactionCount](ace_adsgettransactioncount.htm)

AdsGetTransactionCount get the current transaction nesting level on the given connection.

[AdsSetTableTransactionFree](ace_adssettabletransactionfree.htm)

AdsSetTableTransactionFree allows application developers to define a table as a [transaction-free table](master_transaction_free_tables.htm).