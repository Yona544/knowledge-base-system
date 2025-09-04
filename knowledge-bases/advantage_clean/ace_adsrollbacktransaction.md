---
title: Ace Adsrollbacktransaction
slug: ace_adsrollbacktransaction
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsrollbacktransaction.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8c8fff91254d8f95d2aca2dd7d00441a14e2019b
---

# Ace Adsrollbacktransaction

AdsRollbackTransaction

AdsRollbackTransaction

Advantage Client Engine

| AdsRollbackTransaction  Advantage Client Engine |  |  |  |  |

Rolls back the active transaction on the given connection

Syntax

| UNSIGNED32 | AdsRollbackTransaction (ADSHANDLE hConnect); |

Parameters

| hConnect (I) | Connection handle on which to roll back the transaction. If this is 0, then open transactions on all connected servers will be rolled back. |

Remarks

If zero is passed as the connection handle, then the Advantage Client Engine rolls back the transaction on all connections that have active transactions. The error code, AE\_TRANS\_OUT\_OF\_SEQUENCE, will be returned if a specific connection handle is given to [AdsCommitTransaction](ace_adscommittransaction.md) and that connection is not in a transaction or if zero is given and no connections have active transactions. If zero is given and at least one connection is in a transaction, then the transaction(s) will be rolled back and no error will be returned. When using [nested transactions](master_nesting_transactions.md), AdsRollbackTransaction rolls back all work to the outermost begin transaction operation and ends the transaction.

Note This API has no effect when used with the Advantage Local Server.

See Also

[AdsBeginTransaction](ace_adsbegintransaction.md)

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsInTransaction](ace_adsintransaction.md)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.md)

[AdsConnect](ace_adsconnect.md)

[AdsGetTransactionCount](ace_adsgettransactioncount.md)

[AdsRollbackTransaction80](ace_adsrollbacktransaction80.md)
