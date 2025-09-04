---
title: Dotnet Adstransaction Commit
slug: dotnet_adstransaction_commit
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adstransaction_commit.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 1d087efde6227201354e3a1322a663a324667e9a
---

# Dotnet Adstransaction Commit

AdsTransaction.Commit

AdsTransaction.Commit

Advantage .NET Data Provider

| AdsTransaction.Commit  Advantage .NET Data Provider |  |  |  |  |

Commits the database transaction.

public void Commit();

Remarks

If the transaction is still active, this will commit the transaction running on the associated [AdsConnection](dotnet_adsconnection.md). If the transaction has already been committed or rolled back, this will throw an InvalidOperationException.

If a connections has [nested transactions](master_nesting_transactions.md), the nesting level will be decremented, but the work will not be committed. When used in nested transactions, commits of the inner transactions do not commit the data or release locks. Only committing the outer most transaction will commit the work and end the transaction.

See Also

[AdsTransaction.Rollback](dotnet_adstransaction_rollback.md)
