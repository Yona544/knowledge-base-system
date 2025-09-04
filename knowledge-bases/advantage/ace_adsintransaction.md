AdsInTransaction




Advantage Database Server 12  

AdsInTransaction

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsInTransaction  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsInTransaction Advantage Client Engine ace\_Adsintransaction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsInTransaction  Advantage Client Engine |  |  |  |  |

Returns a flag to the caller to indicate if the given connection has an active transaction

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsInTransaction (ADSHANDLE hConnect,  UNSIGNED16 \*pbInTrans); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle to check. If this is 0, then all connected servers will be checked for open transactions. |
| pbInTrans (O) | Returns True if in a transaction, False if not. |

Remarks

AdsInTransaction will return a True if the connection specified by hConnect is currently in a transaction. If zero is given as the connection handle, then pbInTrans will be set to True if any connection has an active transaction.

Example

[Click Here](ace_examples.htm#adsintransactionexample)

See Also

[AdsBeginTransaction](ace_adsbegintransaction.htm)

[AdsCommitTransaction](ace_adscommittransaction.htm)

[AdsRollbackTransaction](ace_adsrollbacktransaction.htm)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.htm)

[AdsConnect](ace_adsconnect.htm)