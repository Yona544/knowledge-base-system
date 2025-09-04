---
title: Dotnet Adsconnection Createcommand
slug: dotnet_adsconnection_createcommand
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_createcommand.htm
source: Advantage CHM
tags:
  - dotnet
checksum: fff82f834a27d09dcb70a53517557369f7bc337d
---

# Dotnet Adsconnection Createcommand

AdsConnection.CreateCommand

AdsConnection.CreateCommand

Advantage .NET Data Provider

| AdsConnection.CreateCommand  Advantage .NET Data Provider |  |  |  |  |

Creates and returns an AdsCommand object associated with the AdsConnection.

public AdsCommand CreateCommand();

Remarks

This method creates a new AdsCommand object that can be used for executing queries against the open connection. The [AdsCommand.Connection](dotnet_adscommand_connection.md) property is automatically set when this method is used.

Example

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object

cmd = conn.CreateCommand();

// specify a query

cmd.CommandText = "select now() from system.iota";

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();
