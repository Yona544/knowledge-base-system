---
title: Dotnet Adscommand Constructor String Adsconnection Adstransaction
slug: dotnet_adscommand_constructor_string_adsconnection_adstransaction_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_constructor_string_adsconnection_adstransaction_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: bd1c7180c233c9b5e82acf1889d1b9edc640552a
---

# Dotnet Adscommand Constructor String Adsconnection Adstransaction

AdsCommand Constructor( string, AdsConnection, AdsTransaction )

AdsCommand Constructor( string, AdsConnection, AdsTransaction )

Advantage .NET Data Provider

| AdsCommand Constructor( string, AdsConnection, AdsTransaction )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsCommand object with a command, an AdsConnection object, and an AdsTransaction object.

public AdsCommand( string cmdText, AdsConnection connection,

AdsTransaction transaction );

Remarks

This constructor accepts an SQL command, stored procedure name, or table name and initializes the command text with the given informaiton. It also accepts an AdsConnection object with which to associate the command object and an AdsTransaction object.

Example

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

[AdsConnection](dotnet_adsconnection.md)

[AdsTransaction](dotnet_adstransaction.md)
