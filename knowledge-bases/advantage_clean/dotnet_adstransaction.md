---
title: Dotnet Adstransaction
slug: dotnet_adstransaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adstransaction.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 4f5db5267668826f25e1c67760e8b24cec5f56f6
---

# Dotnet Adstransaction

AdsTransaction

AdsTransaction

Advantage .NET Data Provider

| AdsTransaction  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsTransaction

Implements: System.Data.IDbTransaction

[Properties](dotnet_adstransaction_properties.md)

[Methods](dotnet_adstransaction_methods.md)

The AdsTransaction class represents a transaction running on Advantage Database Server. When the [AdsConnection.BeginTransaction](dotnet_adsconnection_begintransaction_.md) method is called, Advantage Database Server starts a transaction, and the BeginTransaction method returns an AdsTransaction object. To end the transaction, call either [AdsTransaction.Commit](dotnet_adstransaction_commit.md) or [AdsTransaction.Rollback](dotnet_adstransaction_rollback.md).

Advantage Local Server does not support transactions. You can use the BeginTransaction method and AdsTransaction objects when connected to Advantage Local Server, but the calls to AdsConnection.BeginTransaction, AdsTransaction.Commit, and AdsTransaction.Rollback are no-ops in that environment.

Unlike other .NET data providers, it is not necessary to assign the AdsTransaction object to the AdsCommand.Transaction property prior to using a command object in a transaction. With Advantage Database Server, all commands executed on an AdsConnection while that connection has a transaction active are automatically run in that transaction.

Example

The following C# code connects to Advantage Database Server, makes an update in a transaction and then commits it if there are no errors.

public static void TestTransaction()

{

AdsConnection conn = new AdsConnection( "data source = c:\\data; " +

"ServerType=remote" );

AdsCommand cmd;

AdsTransaction txn;

 

// open the connection

conn.Open();

// create a command object

cmd = conn.CreateCommand();

// specify an update

cmd.CommandText = "update departments set budget = budget \* 1.05";

// start the transaction

txn = conn.BeginTransaction();

 

try

{

// execute the query

int iUpdates = cmd.ExecuteNonQuery();

// commit the transaction

txn.Commit();

}

catch( Exception e )

{

// some error occurred (e.g., a lock failure)

Console.WriteLine( e.Message );

 

// roll back the transaction

txn.Rollback();

}

finally

{

// close the connection.

conn.Close();

}

 

}

See Also

[AdsConnection.BeginTransaction](dotnet_adsconnection_begintransaction_.md)

[AdsCommand.Transaction](dotnet_adscommand_transaction.md)
