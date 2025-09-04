AdsBeginTransaction




Advantage Database Server 12  

AdsBeginTransaction

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsBeginTransaction  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsBeginTransaction Advantage Client Engine ace\_Adsbegintransaction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsBeginTransaction  Advantage Client Engine |  |  |  |  |

Begins a transaction for all connected servers or for the given server

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsBeginTransaction (ADSHANDLE hConnect); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle on which to start transaction. If this is 0, then a transaction will be started on all connected servers. |

Remarks

If a transaction is not active on a connection then a transaction will be started.  If a transaction is active a [nested transaction](master_nesting_transactions.htm) will be started. If zero is passed as the connection handle, then the Advantage Client Engine begins a transaction on all connections that do not already have an active transaction. . Any connection with an active transaction will start a nested transaction.

Note AdsBeginTransaction has no effect when used with the Advantage Local Server.

See Also

[AdsCommitTransaction](ace_adscommittransaction.htm)

[AdsRollbackTransaction](ace_adsrollbacktransaction.htm)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.htm)

[AdsConnect](ace_adsconnect.htm)

[AdsInTransaction](ace_adsintransaction.htm)

[AdsGetTransactionCount](ace_adsgettransactioncount.htm)