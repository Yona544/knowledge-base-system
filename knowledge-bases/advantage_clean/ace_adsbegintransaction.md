---
title: Ace Adsbegintransaction
slug: ace_adsbegintransaction
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsbegintransaction.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d2af70417d87b9e15ef379acbaea1b3e03f99720
---

# Ace Adsbegintransaction

AdsBeginTransaction

AdsBeginTransaction

Advantage Client Engine

| AdsBeginTransaction  Advantage Client Engine |  |  |  |  |

Begins a transaction for all connected servers or for the given server

Syntax

| UNSIGNED32 | AdsBeginTransaction (ADSHANDLE hConnect); |

Parameters

| hConnect (I) | Connection handle on which to start transaction. If this is 0, then a transaction will be started on all connected servers. |

Remarks

If a transaction is not active on a connection then a transaction will be started.  If a transaction is active a [nested transaction](master_nesting_transactions.md) will be started. If zero is passed as the connection handle, then the Advantage Client Engine begins a transaction on all connections that do not already have an active transaction. . Any connection with an active transaction will start a nested transaction.

Note AdsBeginTransaction has no effect when used with the Advantage Local Server.

See Also

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.md)

[AdsConnect](ace_adsconnect.md)

[AdsInTransaction](ace_adsintransaction.md)

[AdsGetTransactionCount](ace_adsgettransactioncount.md)
