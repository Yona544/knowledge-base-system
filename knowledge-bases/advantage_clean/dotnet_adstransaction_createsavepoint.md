---
title: Dotnet Adstransaction Createsavepoint
slug: dotnet_adstransaction_createsavepoint
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adstransaction_createsavepoint.htm
source: Advantage CHM
tags:
  - dotnet
checksum: f07f351fadc41f2ce251e08672c1fa6242ab313a
---

# Dotnet Adstransaction Createsavepoint

AdsTransaction.CreateSavepoint

AdsTransaction.CreateSavepoint

Advantage .NET Data Provider

| AdsTransaction.CreateSavepoint  Advantage .NET Data Provider |  |  |  |  |

Creates a savepoint in the current transaction.

public void CreateSavepoint( string strSavepoint);

Remarks

This function creates a savepoint in the transaction associated with the AdsConnection. If the transaction has already been committed or rolled back, this will throw an InvalidOperationException.

See Also

[AdsTransaction.Commit](dotnet_adstransaction_commit.md)

[AdsTransaction.Rollback](dotnet_adstransaction_rollback.md)
