---
title: Ade Begintransaction
slug: ade_begintransaction
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_begintransaction.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 03c7cba6f26af5f054a7f10089033b7ae6047788
---

# Ade Begintransaction

BeginTransaction

TAdsConnection.BeginTransaction

Advantage TDataSet Descendant

| TAdsConnection.BeginTransaction  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Begins a transaction for the current connection.

Syntax

procedure BeginTransaction;

Description

Call this function to begin a transaction for the current connection. This function provides the ability to rollback or commit database updates, inserts, and deletes made during the transaction. Transactions can be nested by calling BeginTransaction inside of an existing transaction.

This method is ignored if the connection is using [Advantage Local Server](master_advantage_local_server.md). See [Advantage Transaction Processing](master_transaction_processing_system.md) for more information.

See Also

[Nesting Transactions](master_nesting_transactions.md)

[Commit](ade_commit.md)

[Rollback](ade_rollback.md)
