---
title: Dotnet Adscommand Constructor String
slug: dotnet_adscommand_constructor_string_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_constructor_string_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 7379f0c4acf5bc030d6f904d28de016770b47d53
---

# Dotnet Adscommand Constructor String

AdsCommand Constructor( string )

AdsCommand Constructor( string )

Advantage .NET Data Provider

| AdsCommand Constructor( string )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsCommand object with an SQL statement, stored procedure name, or table name.

public AdsCommand( string cmdText );

Remarks

This constructor accepts an SQL command, stored procedure name, or table name and initializes the command text with the given information. When using this constructor, it is necessary to assign an AdsConnection object to the [AdsCommand.Connection](dotnet_adscommand_connection.md) property prior to using the command.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand("select now() from system.iota");

// assign the connection

cmd.Connection = conn;

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();

See Also

[AdsCommand.Connection](dotnet_adscommand_connection.md)

[AdsConnection](dotnet_adsconnection.md)
