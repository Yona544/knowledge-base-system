---
title: Dotnet Adstransaction Rollback
slug: dotnet_adstransaction_rollback
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adstransaction_rollback.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 4cc07ff5ad8af3f0e8d20a9d09628f3e534deb01
---

# Dotnet Adstransaction Rollback

AdsTransaction.Rollback

AdsTransaction.Rollback

Advantage .NET Data Provider

| AdsTransaction.Rollback  Advantage .NET Data Provider |  |  |  |  |

Rolls back the database transaction.

public void Rollback();

public void Rollback( string strSavepoint);

Remarks

If the transaction is still active, this will roll back the transaction running on the associated [AdsConnection](dotnet_adsconnection.md). If the transaction has already been committed or rolled back, this will throw an InvalidOperationException. If a savepoint is specified the transaction will be rolled back to the savepoint.

When using [nested transactions](master_nesting_transactions.md), calling Rollback without a savepoint name rolls back all work to the outermost begin transaction operation and ends the transaction.

See Also

[AdsTransaction.Commit](dotnet_adstransaction_commit.md)

[AdsTransaction.CreateSavepoint](dotnet_adstransaction_createsavepoint.md)
