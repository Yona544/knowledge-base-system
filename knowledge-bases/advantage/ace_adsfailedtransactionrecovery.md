AdsFailedTransactionRecovery




Advantage Database Server 12  

AdsFailedTransactionRecovery

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFailedTransactionRecovery  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFailedTransactionRecovery Advantage Client Engine ace\_Adsfailedtransactionrecovery Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFailedTransactionRecovery  Advantage Client Engine |  |  |  |  |

Instructs Advantage Database Server to clean up any failed transactions

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsFailedTransactionRecovery (UNSIGNED8 \*pucServerPath); |

Parameters

|  |  |
| --- | --- |
| pucServerPath (I) | Drive letter or server name on which to recover failed transactions. If this is NULL, then a failed transaction recovery command will be sent to each connected server. If the application uses a server name as the parameter, it must include the share name as well. For example, use "\\server\share" or "\\server\vol1:". |

Remarks

It is unlikely that use of this function will be necessary.

Note This API has no effect when used with the Advantage Local Server.

Example

[Click Here](ace_examples.htm#adsfailedtransactionrecoveryexample)

See Also

[AdsBeginTransaction](ace_adsbegintransaction.htm)

[AdsCommitTransaction](ace_adscommittransaction.htm)

[AdsRollbackTransaction](ace_adsrollbacktransaction.htm)

[AdsInTransaction](ace_adsintransaction.htm)

[AdsConnect](ace_adsconnect.htm)