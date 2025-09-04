---
title: Dotnet Adsconnection Begintransaction
slug: dotnet_adsconnection_begintransaction_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_begintransaction_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ff4ef893843a04cca055012f0d65d1845f62e32f
---

# Dotnet Adsconnection Begintransaction

AdsConnection.BeginTransaction()

AdsConnection.BeginTransaction()

Advantage .NET Data Provider

| AdsConnection.BeginTransaction()  Advantage .NET Data Provider |  |  |  |  |

Begins a database transaction.

public AdsTransaction BeginTransaction();

Remarks

This returns an [AdsTransaction](dotnet_adstransaction.md) object that represents the new transaction. Distributed transactions are not supported. If any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is started. Note that Advantage Local Server does not support transactions. If the ServerType property ([AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md)) is LOCAL, no transaction will actually be started, although an AdsTransaction object will still be returned. Transactions can be nested by calling BeginTransaction inside of an existing transaction.

Example

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

[BeginTransaction( IsolationLevel )](dotnet_adsconnection_begintransaction_isolationlevel_.md)

[AdsTransaction](dotnet_adstransaction.md)
