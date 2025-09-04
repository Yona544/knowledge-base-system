---
title: Ade Rollback
slug: ade_rollback
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_rollback.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 443c4b4ae7dfb3388dd9a904ab83108a90e03319
---

# Ade Rollback

Rollback

TAdsConnection.Rollback

Advantage TDataSet Descendant

| TAdsConnection.Rollback  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Aborts all of the database updates, inserts, and deletes sent to the server since the transaction began.

Syntax

procedure Rollback;

procedure Rollback( strSavepoint: string );

 

Description

Call this function to abort the database updates, inserts, and deletes made during the transaction. If a savepoint is specified, the transaction is rolled back to that savepiont. When using [nested transactions](master_nesting_transactions.md), calling Rollback without a savepoint name rolls back all work to the outermost begin transaction operation and ends the transaction.

This method is ignored if the connection is using Advantage Local Server. See [Advantage Transaction Processing](master_transaction_processing_system.md) for more information.

See Also

[BeginTransaction](ade_begintransaction.md)

[Commit](ade_commit.md)

[CreateSavepoint](ade_createsavepoint.md)
