---
title: Ace Adsintransaction
slug: ace_adsintransaction
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsintransaction.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 82baa0b5ac3236b0058caed9783840985c27e68b
---

# Ace Adsintransaction

AdsInTransaction

AdsInTransaction

Advantage Client Engine

| AdsInTransaction  Advantage Client Engine |  |  |  |  |

Returns a flag to the caller to indicate if the given connection has an active transaction

Syntax

| UNSIGNED32 | AdsInTransaction (ADSHANDLE hConnect,  UNSIGNED16 \*pbInTrans); |

Parameters

| hConnect (I) | Connection handle to check. If this is 0, then all connected servers will be checked for open transactions. |
| pbInTrans (O) | Returns True if in a transaction, False if not. |

Remarks

AdsInTransaction will return a True if the connection specified by hConnect is currently in a transaction. If zero is given as the connection handle, then pbInTrans will be set to True if any connection has an active transaction.

Example

[Click Here](ace_examples.md#adsintransactionexample)

See Also

[AdsBeginTransaction](ace_adsbegintransaction.md)

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.md)

[AdsConnect](ace_adsconnect.md)
