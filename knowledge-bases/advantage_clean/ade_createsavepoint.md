---
title: Ade Createsavepoint
slug: ade_createsavepoint
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_createsavepoint.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3f36040b9454ff77b574b23565dadef6f279c21d
---

# Ade Createsavepoint

CreateSavepoint

TAdsConnection.CreateSavepoint

Advantage TDataSet Descendant

| TAdsConnection.CreateSavepoint  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Creates a savepoint in the current transactions.

Syntax

procedure CreateSavepoint( strSavepoint: string );

Description

Call this function to create a savepoint inside the current transaction. This method is ignored if the connection is using Advantage Local Server. See [Advantage Transaction Processing](master_advantage_transaction_processing_system_overview.md) for more information.

See Also

[BeginTransaction](ade_begintransaction.md)

[Commit](ade_commit.md)

[Rollback](ade_rollback.md)
