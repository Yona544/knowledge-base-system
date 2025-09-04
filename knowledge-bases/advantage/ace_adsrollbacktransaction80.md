AdsRollbackTransaction80




Advantage Database Server 12  

AdsRollbackTransaction80

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRollbackTransaction80  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRollbackTransaction80 Advantage Client Engine ace\_Adsrollbacktransaction80 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRollbackTransaction80  Advantage Client Engine |  |  |  |  |

Rolls back the active transaction on the given connection entirely or to an existing savepoint.

Syntax

UNSIGNED32 AdsRollbackTransaction80 (ADSHANDLE hConnect,

                                    UNSIGNED8 \*pucSavepoint,

                                    UNSIGNED32 ulOptions );

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle on which to roll back the transaction. |
| pucSavepoint(I) | The name of the savepoint to roll back to. This value should be NULL to rollback an entire transaction. |
| ulOptions(I) | Options for the command. At this time there are no options. |

Remarks

This command rolls back an active transaction to an existing savepoint or rolls back the transaction entirely. When rolling back a transaction to a savepoint, all savepoints created after the savepoint are removed while the savepoint itself remains. The error code, AE\_TRANS\_OUT\_OF\_SEQUENCE, will be returned if the connection handle given is not in a transaction. When using [nested transactions](master_nesting_transactions.htm), calling AdsRollbackTransaction81 without a savepoint name rolls back all work to the outermost begin transaction operation and ends the transaction.

Note This API has no effect when used with the Advantage Local Server.

See Also

[AdsBeginTransaction](ace_adsbegintransaction.htm)

[AdsCommitTransaction](ace_adscommittransaction.htm)

[AdsRollbackTransaction](ace_adsrollbacktransaction.htm)

[AdsCreateSavepoint](ace_adscreatesavepoint.htm)

[AdsInTransaction](ace_adsintransaction.htm)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.htm)

[AdsConnect](ace_adsconnect.htm)

[AdsConnect60](ace_adsconnect60.htm)

[AdsGetTransactionCount](ace_adsgettransactioncount.htm)