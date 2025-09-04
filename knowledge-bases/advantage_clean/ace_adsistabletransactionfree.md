---
title: Ace Adsistabletransactionfree
slug: ace_adsistabletransactionfree
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsistabletransactionfree.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fb21aa43bcb5d475934be5568ec5e7a7e9d8bb81
---

# Ace Adsistabletransactionfree

ace\_AdsIsTableTransactionFree

AdsIsTableTransactionFree

Advantage Client Engine

| AdsIsTableTransactionFree  Advantage Client Engine |  |  |  |  |

Determines if the given table is currently a transaction-free table.

Syntax

| UNSIGNED32 | AdsIsTableTransactionFree( ADSHANDLE hTable,                            UNSIGNED16\* pusTransFree ); |

Parameters

| hTable (I) | Handle of table |
| pusTransFree (O) | Current transaction-free state of the table.  Will be True on return if the table is currently a transaction-free table. |

Remarks

AdsIsTableTransactionFree returns true if the table is currently configured as a transaction-free table, and false otherwise.

See Also

[AdsBeginTransaction](ace_adsbegintransaction.md)

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[AdsSetTableTransactionFree](ace_adssettabletransactionfree.md)

[Transaction-Free Tables](master_transaction_free_tables.md)
