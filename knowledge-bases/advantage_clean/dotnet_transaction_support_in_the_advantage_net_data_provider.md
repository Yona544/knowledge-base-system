---
title: Dotnet Transaction Support In The Advantage Net Data Provider
slug: dotnet_transaction_support_in_the_advantage_net_data_provider
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_transaction_support_in_the_advantage_net_data_provider.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 00d9b70e19896ec8c48cc04c94f77ba7fd188fbd
---

# Dotnet Transaction Support In The Advantage Net Data Provider

Transaction Support in the Advantage .NET Data Provider

Transaction Support in the Advantage .NET Data Provider

Advantage .NET Data Provider

| Transaction Support in the Advantage .NET Data Provider  Advantage .NET Data Provider |  |  |  |  |

When connected to Advantage Database Server, it is easy to use transactions to ensure data integrity. You can use [AdsConnection.BeginTransaction](dotnet_adsconnection_begintransaction_.md) and the [AdsTransaction](dotnet_adstransaction.md) class to specify transaction processing behavior. Another method for using transactions is to use the BEGIN TRANSACTION and COMMIT WORK statements directly in your SQL.

If you are using the .NET Framework version 2.0, another possibility is to take advantage of the System.Transactions namespace. This namespace contains classes that provide an elegant method for specifying the scope of a transaction. In order to use this functionality, you must use Advantage .NET Data Provider version 8.1 or greater.

The following code snippet is a simple example demonstrating TransactionScope class usage. In this example, the AdsConnection class will enlist in the active transaction as defined by the TransactionScope class. If no exceptions occur and the TransactionScope.Complete() method runs, the transaction will be committed. If any exception occurs that prevents the TransactionScope.Complete() method from running, the transaction will be rolled back.

using ( TransactionScope ts = new TransactionScope() )

{

using ( AdsConnection conn = new AdsConnection( @"Data Source=\\server1\share\data" ) )

{

conn.Open();

AdsCommand cmd = new AdsCommand( "update ...", conn );

cmd.ExecuteNonQuery();

}

ts.Complete();

}

It is possible to use multiple connections inside the scope of a TransactionScope instance. If any exception occurs during the processing, the transaction will be rolled back as expected on all connections even if they are to different servers. However, it is important to note that this is not a true distributed transaction. Advantage Database Server does not currently support a two-phase commit protocol. This means that it is not guaranteed that the commit will succeed on all connections within a given transaction scope. In the following example, if an exception occurs at any point prior to the ts.Complete() call, the transactions on both servers will be rolled back. If all updates succeed and no exceptions occur prior to the ts.Complete() call, then the transaction manager will issue the phase one commit request on both servers. Without the two-phase commit protocol, however, this means that the transaction is fully committed at both servers in the first phase. If, for example, there is a disk failure during the commit of the transaction on the second server, the transaction at the first server will not be rolled back.

using ( TransactionScope ts = new TransactionScope() )

{

using ( AdsConnection conn = new AdsConnection( @"Data Source=\\server1\share\data" ) )

{

conn.Open();

// run SQL statements

 

using ( AdsConnection conn2 = new AdsConnection( @"Data Source=\\server2\share\data" ) )

{

conn2.Open();

// run SQL statements on connection 2

}

}

 

ts.Complete();

}
