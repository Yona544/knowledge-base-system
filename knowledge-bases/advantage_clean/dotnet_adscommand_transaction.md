---
title: Dotnet Adscommand Transaction
slug: dotnet_adscommand_transaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_transaction.htm
source: Advantage CHM
tags:
  - dotnet
checksum: cfb51170dfa830714a169233b317fca280992795
---

# Dotnet Adscommand Transaction

AdsCommand.Transaction

AdsCommand.Transaction

Advantage .NET Data Provider

| AdsCommand.Transaction  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the transaction in which the AdsCommand executes.

public AdsTransaction Transaction {get; set;}

Remarks

This property can be used to store a transaction object. With the Advantage .NET Data Provider, it is not necessary to assign this property in order to use the AdsCommand object within a transaction. With Advantage Database Server, all commands executed on an AdsConnection while that connection has a transaction active are automatically run in that transaction.

Advantage Local Server does not support transactions. To use transactions, it is necessary to use Advantage Database Server.

Example

This example performs an update statement within a transaction. It uses the Transaction property of the command object to store the transaction object and retrieves it after the UPDATE statement to perform the commit.

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object and start a new transaction

cmd = new AdsCommand( "update departments set budget = budget \* 1.05",

conn, conn.BeginTransaction() );

// execute the query

cmd.ExecuteNonQuery();

// commit the transaction

cmd.Transaction.Commit();

// close the connection.

conn.Close();

See Also

[AdsConnection.BeginTransaction](dotnet_adsconnection_begintransaction_.md)

[AdsTransaction](dotnet_adstransaction.md)
