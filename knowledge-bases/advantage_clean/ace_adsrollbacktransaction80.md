---
title: Ace Adsrollbacktransaction80
slug: ace_adsrollbacktransaction80
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsrollbacktransaction80.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 22aa8220170d4c502c737405f217e3d7506f7823
---

# Ace Adsrollbacktransaction80

AdsRollbackTransaction80

AdsRollbackTransaction80

Advantage Client Engine

| AdsRollbackTransaction80  Advantage Client Engine |  |  |  |  |

Rolls back the active transaction on the given connection entirely or to an existing savepoint.

Syntax

UNSIGNED32 AdsRollbackTransaction80 (ADSHANDLE hConnect,

                                    UNSIGNED8 \*pucSavepoint,

                                    UNSIGNED32 ulOptions );

Parameters

| hConnect (I) | Connection handle on which to roll back the transaction. |
| pucSavepoint(I) | The name of the savepoint to roll back to. This value should be NULL to rollback an entire transaction. |
| ulOptions(I) | Options for the command. At this time there are no options. |

Remarks

This command rolls back an active transaction to an existing savepoint or rolls back the transaction entirely. When rolling back a transaction to a savepoint, all savepoints created after the savepoint are removed while the savepoint itself remains. The error code, AE\_TRANS\_OUT\_OF\_SEQUENCE, will be returned if the connection handle given is not in a transaction. When using [nested transactions](master_nesting_transactions.md), calling AdsRollbackTransaction81 without a savepoint name rolls back all work to the outermost begin transaction operation and ends the transaction.

Note This API has no effect when used with the Advantage Local Server.

See Also

[AdsBeginTransaction](ace_adsbegintransaction.md)

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[AdsCreateSavepoint](ace_adscreatesavepoint.md)

[AdsInTransaction](ace_adsintransaction.md)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.md)

[AdsConnect](ace_adsconnect.md)

[AdsConnect60](ace_adsconnect60.md)

[AdsGetTransactionCount](ace_adsgettransactioncount.md)
