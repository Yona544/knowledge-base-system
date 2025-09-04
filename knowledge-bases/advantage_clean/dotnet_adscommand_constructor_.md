---
title: Dotnet Adscommand Constructor
slug: dotnet_adscommand_constructor_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_constructor_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 1a31e8cabf41eb6f4c2d999be243cb8c16872d58
---

# Dotnet Adscommand Constructor

AdsCommand Constructor()

AdsCommand Constructor()

Advantage .NET Data Provider

| AdsCommand Constructor()  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsCommand object.

public AdsCommand();

Remarks

This is the default constructor. All property values are initialized to their default values. When using this constructor, it is necessary to assign an AdsConnection object to the [AdsCommand.Connection](dotnet_adscommand_connection.md) property prior to using the command.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand();

// assign the connection

cmd.Connection = conn;

// specify a query

cmd.CommandText = "select now() from system.iota";

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();

See Also

[AdsCommand.Connection](dotnet_adscommand_connection.md)

[AdsConnection](dotnet_adsconnection.md)
