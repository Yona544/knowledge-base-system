AdsGetTransactionCount




Advantage Database Server 12  

AdsGetTransactionCount

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTransactionCount  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTransactionCount Advantage Client Engine ace\_AdsGetTransactionCount Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTransactionCount  Advantage Client Engine |  |  |  |  |

Returns a count of the current transaction nesting level.

Syntax

UNSIGNED32 AdsGetTransactionCount( ADSHANDLE hConnect,

                                  UNSIGNED32 \*pulTransactionCount);

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle to check. |
| pulTransactionCount (O) | Returns the current transaction nesting depth if in a transaction, 0 if not. |

Remarks

AdsGetTransactionCount will return 0 if the connection specified by hConnect is currently not in a transaction. If the specified connection is in a transaction, the current transaction nesting depth will be returned.  The transaction nesting depth is incremented each time a call to AdsBeginTransaction is executed and decremented each time a call to AdsCommitTransaction is made.  The nesting depth is set to 0 when either AdsRollbackTransaction or AdsRollbackTransaction90 is called.

A value of  0 will always be returned with Advantage Local Server.

See Also

[Nesting Transactions](master_nesting_transactions.htm)

[AdsBeginTransaction](ace_adsbegintransaction.htm)

[AdsCommitTransaction](ace_adscommittransaction.htm)

[AdsRollbackTransaction](ace_adsrollbacktransaction.htm)

[AdsRollbackTransaction80](ace_adsrollbacktransaction80.htm)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.htm)

[AdsConnect](ace_adsconnect60.htm)

[AdsInTransaction](ace_adsintransaction.htm)