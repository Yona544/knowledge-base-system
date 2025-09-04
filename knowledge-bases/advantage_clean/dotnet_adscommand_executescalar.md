---
title: Dotnet Adscommand Executescalar
slug: dotnet_adscommand_executescalar
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_executescalar.htm
source: Advantage CHM
tags:
  - dotnet
checksum: c20e2e51f7fe9d01c52eaf153c27dae87ba5a390
---

# Dotnet Adscommand Executescalar

AdsCommand.ExecuteScalar

AdsCommand.ExecuteScalar

Advantage .NET Data Provider

| AdsCommand.ExecuteScalar  Advantage .NET Data Provider |  |  |  |  |

Executes the query, and returns the first column of the first row in the result set returned by the query. Extra columns or rows are ignored.

public object ExecuteScalar();

Remarks

Use the ExecuteScalar method to retrieve a single value (for example, an aggregate value) from a database. This requires less code than using the [AdsCommand.ExecuteReader](dotnet_adscommand_executereader.md) method and the associated calls to the AdsDataReader.

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

 

// find number of rows in a table

cmd.CommandText = "select count(\*) from departments";

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

See Also

[ExecuteReader](dotnet_adscommand_executereader.md)

[ExecuteNonQuery](dotnet_adscommand_executenonquery.md)
