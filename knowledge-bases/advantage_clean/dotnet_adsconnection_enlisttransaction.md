---
title: Dotnet Adsconnection Enlisttransaction
slug: dotnet_adsconnection_enlisttransaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_enlisttransaction.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5114514543d9e2b37a5625ab1be6bbfc16a50adb
---

# Dotnet Adsconnection Enlisttransaction

AdsConnection.EnlistTransaction

AdsConnection.EnlistTransaction

Advantage .NET Data Provider

| AdsConnection.EnlistTransaction  Advantage .NET Data Provider |  |  |  |  |

Note This method is new in the .NET Framework version 2.0.

Enlist the AdsConnection instance in the given transaction.

AdsConnection.EnlistTransaction( System.Transactions.Transaction transaction );

Remarks

This method provides the capability to explicitly enlist an AdsConnection instance in a transaction as defined by the .NET Framework System.Transactions namespace. The recommended practice is to use implicit transactions via the TransactionScope class (see [Transaction Support in the Advantage .NET Data Provider](dotnet_transaction_support_in_the_advantage_net_data_provider.md) for an example). The following code shows a simple example of explicitly enlisting in a transaction.

CommittableTransaction txn = new CommittableTransaction();

AdsConnection conn = new AdsConnection( @"data source=c:\data" );

conn.Open();

conn.EnlistTransaction( txn );

 // perform updates

txn.Commit();

 

See Also

[AdsTransaction](dotnet_adstransaction.md)

[AdsConnection.BeginTransaction](dotnet_adsconnection_begintransaction_.md)
