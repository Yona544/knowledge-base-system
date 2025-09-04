---
title: Ace Adscommittransaction
slug: ace_adscommittransaction
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscommittransaction.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 16b958fbd9abac7e91f0ba0360ab808c5b073ebe
---

# Ace Adscommittransaction

AdsCommitTransaction

AdsCommitTransaction

Advantage Client Engine

| AdsCommitTransaction  Advantage Client Engine |  |  |  |  |

Commits an active transaction on the given connection

Syntax

| UNSIGNED32 | AdsCommitTransaction (ADSHANDLE hConnect); |

Parameters

| hConnect (I) | Connection handle on which to commit the transaction. If this is 0, then open transactions on all connected servers will be committed. |

Remarks

If zero is passed as the connection handle, then the Advantage Client Engine commits the transaction on all connections that have active transactions. If a connections has [nested transactions](master_nesting_transactions.md), the nesting level will be decremented, but the work will not be committed The error code AE\_TRANS\_OUT\_OF\_SEQUENCE will be returned if a specific connection handle is given to AdsCommitTransaction and that connection is not in a transaction, or if zero is given and no connections have active transactions. If zero is given and at least one connection is in a transaction, then the transaction(s) will be committed and no error will be returned.

When used in [nested transactions](master_nesting_transactions.md), commits of the inner transactions do not commit the data or release locks. Only committing the outer most transaction will commit the work and end the transaction.

Note This API has no effect when used with the Advantage Local Server.

See Also

[AdsBeginTransaction](ace_adsbegintransaction.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.md)

[AdsConnect](ace_adsconnect.md)

[AdsInTransaction](ace_adsintransaction.md)

[AdsGetTransactionCount](ace_adsgettransactioncount.md)
