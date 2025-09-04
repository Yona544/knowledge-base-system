---
title: Dotnet Adscommand Constructor String Adsconnection
slug: dotnet_adscommand_constructor_string_adsconnection_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_constructor_string_adsconnection_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 3e618ae5760ee0f28069470e2c6c1f9831f4d808
---

# Dotnet Adscommand Constructor String Adsconnection

AdsCommand Constructor( string, AdsConnection )

AdsCommand Constructor( string, AdsConnection )

Advantage .NET Data Provider

| AdsCommand Constructor( string, AdsConnection )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsCommand object with an SQL statement, stored procedure name or table name and the AdsConnection object.

public AdsCommand( string cmdText, AdsConnection connection );

Remarks

This constructor accepts an SQL command, stored procedure name, or table name and initializes the command text with the given informaiton. It also accepts an AdsConnection object with which to associate the command object.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object and give the command and connection

cmd = new AdsCommand( "select now() from system.iota", conn );

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();

See Also

[AdsConnection](dotnet_adsconnection.md)
