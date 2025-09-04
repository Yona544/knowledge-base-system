---
title: Ade Transaction Processing With The Advantage Tdataset Descendant
slug: ade_transaction_processing_with_the_advantage_tdataset_descendant
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_transaction_processing_with_the_advantage_tdataset_descendant.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a26caef881d0a595faf4f185d7eeb36f039fefa9
---

# Ade Transaction Processing With The Advantage Tdataset Descendant

Transaction Processing with the Advantage TDataSet Descendant

Transaction Processing with the Advantage TDataSet Descendant

Advantage TDataSet Descendant

| Transaction Processing with the Advantage TDataSet Descendant  Advantage TDataSet Descendant |  |  |  |  |

Advantage Transaction Processing is aligned with the existing Delphi scheme as much as possible.

The Advantage TAdsConnection component has encapsulated Advantage Transaction Processing in the Advantage TDataSet Descendant solution. Use the TAdsConnection component to perform transaction processing with the Advantage TDataSet Descendant solution. The TAdsConnection methods and property applicable to transaction processing are:

[TAdsConnection.BeginTransaction](ade_begintransaction.md)

Begins a transaction for all tables associated with the instance of TAdsConnection.

[TAdsConnection.Rollback](ade_rollback.md)

Aborts a transaction. Any updates, deletes, and inserts issued since the transaction began will be aborted.

[TAdsConnection.Commit](ade_commit.md)

Commits the changes since the transaction began.

[TAdsConnection.TransactionActive](ade_transactionactive.md)

Boolean property to indicate if a transaction is active.

TAdsConnection.TransactionCount

Returns the current transaction nesting level.
