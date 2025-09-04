---
title: Ace Adsfailedtransactionrecovery
slug: ace_adsfailedtransactionrecovery
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsfailedtransactionrecovery.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 679182a3ea06e717922a8967ae3a91c86602a086
---

# Ace Adsfailedtransactionrecovery

AdsFailedTransactionRecovery

AdsFailedTransactionRecovery

Advantage Client Engine

| AdsFailedTransactionRecovery  Advantage Client Engine |  |  |  |  |

Instructs Advantage Database Server to clean up any failed transactions

Syntax

| UNSIGNED32 | AdsFailedTransactionRecovery (UNSIGNED8 \*pucServerPath); |

Parameters

| pucServerPath (I) | Drive letter or server name on which to recover failed transactions. If this is NULL, then a failed transaction recovery command will be sent to each connected server. If the application uses a server name as the parameter, it must include the share name as well. For example, use "\\server\share" or "\\server\vol1:". |

Remarks

It is unlikely that use of this function will be necessary.

Note This API has no effect when used with the Advantage Local Server.

Example

[Click Here](ace_examples.md#adsfailedtransactionrecoveryexample)

See Also

[AdsBeginTransaction](ace_adsbegintransaction.md)

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[AdsInTransaction](ace_adsintransaction.md)

[AdsConnect](ace_adsconnect.md)
