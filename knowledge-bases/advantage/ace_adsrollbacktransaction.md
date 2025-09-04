AdsRollbackTransaction




Advantage Database Server 12  

AdsRollbackTransaction

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRollbackTransaction  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRollbackTransaction Advantage Client Engine ace\_Adsrollbacktransaction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRollbackTransaction  Advantage Client Engine |  |  |  |  |

Rolls back the active transaction on the given connection

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRollbackTransaction (ADSHANDLE hConnect); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle on which to roll back the transaction. If this is 0, then open transactions on all connected servers will be rolled back. |

Remarks

If zero is passed as the connection handle, then the Advantage Client Engine rolls back the transaction on all connections that have active transactions. The error code, AE\_TRANS\_OUT\_OF\_SEQUENCE, will be returned if a specific connection handle is given to [AdsCommitTransaction](ace_adscommittransaction.htm) and that connection is not in a transaction or if zero is given and no connections have active transactions. If zero is given and at least one connection is in a transaction, then the transaction(s) will be rolled back and no error will be returned. When using [nested transactions](master_nesting_transactions.htm), AdsRollbackTransaction rolls back all work to the outermost begin transaction operation and ends the transaction.

Note This API has no effect when used with the Advantage Local Server.

See Also

[AdsBeginTransaction](ace_adsbegintransaction.htm)

[AdsCommitTransaction](ace_adscommittransaction.htm)

[AdsInTransaction](ace_adsintransaction.htm)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.htm)

[AdsConnect](ace_adsconnect.htm)

[AdsGetTransactionCount](ace_adsgettransactioncount.htm)

[AdsRollbackTransaction80](ace_adsrollbacktransaction80.htm)