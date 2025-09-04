---
title: Ace Adsgettransactioncount
slug: ace_adsgettransactioncount
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettransactioncount.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7482d23f9063804d8ce25b02d1e06c1e43505c55
---

# Ace Adsgettransactioncount

AdsGetTransactionCount

AdsGetTransactionCount

Advantage Client Engine

| AdsGetTransactionCount  Advantage Client Engine |  |  |  |  |

Returns a count of the current transaction nesting level.

Syntax

UNSIGNED32 AdsGetTransactionCount( ADSHANDLE hConnect,

                                  UNSIGNED32 \*pulTransactionCount);

Parameters

| hConnect (I) | Connection handle to check. |
| pulTransactionCount (O) | Returns the current transaction nesting depth if in a transaction, 0 if not. |

Remarks

AdsGetTransactionCount will return 0 if the connection specified by hConnect is currently not in a transaction. If the specified connection is in a transaction, the current transaction nesting depth will be returned.  The transaction nesting depth is incremented each time a call to AdsBeginTransaction is executed and decremented each time a call to AdsCommitTransaction is made.  The nesting depth is set to 0 when either AdsRollbackTransaction or AdsRollbackTransaction90 is called.

A value of  0 will always be returned with Advantage Local Server.

See Also

[Nesting Transactions](master_nesting_transactions.md)

[AdsBeginTransaction](ace_adsbegintransaction.md)

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[AdsRollbackTransaction80](ace_adsrollbacktransaction80.md)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.md)

[AdsConnect](ace_adsconnect60.md)

[AdsInTransaction](ace_adsintransaction.md)
