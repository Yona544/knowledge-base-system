---
title: Ace Advantage Client Engine Transaction Processing Apis
slug: ace_advantage_client_engine_transaction_processing_apis
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_advantage_client_engine_transaction_processing_apis.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: eaf5f745a22ce67c672d9a47ca5645b71a7f90ec
---

# Ace Advantage Client Engine Transaction Processing Apis

Advantage Client Engine Transaction Processing APIs

Advantage Client Engine Transaction Processing APIs

Advantage Client Engine

| Advantage Client Engine Transaction Processing APIs  Advantage Client Engine |  |  |  |  |

The Advantage Client Engine provides API functions to support transaction processing.

[AdsBeginTransaction](ace_adsbegintransaction.md)

AdsBeginTransaction begins a transaction for all connected servers or for the indicated connection.

[AdsCommitTransaction](ace_adscommittransaction.md)

AdsCommitTransaction commits active transactions for all connected servers or for a given connection.

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.md)

AdsFailedTransactionRecovery instructs the Advantage Database Server to clean up any failed transactions.

[AdsInTransaction](ace_adsintransaction.md)

AdsInTransaction returns a flag to the caller to indicate if the given connection has an active transaction.

[AdsIsTableTransactionFree](ace_adsistabletransactionfree.md)

AdsIsTableTransactionFree returns a flag to the caller to indicate if the given table is defined as a [transaction-free table](master_transaction_free_tables.md).

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

AdsRollbackTransaction rolls back active transactions on all connected servers or the given connection.

[AdsGetTransactionCount](ace_adsgettransactioncount.md)

AdsGetTransactionCount get the current transaction nesting level on the given connection.

[AdsSetTableTransactionFree](ace_adssettabletransactionfree.md)

AdsSetTableTransactionFree allows application developers to define a table as a [transaction-free table](master_transaction_free_tables.md).
