---
title: Dotnet Adscommand Executenonquery
slug: dotnet_adscommand_executenonquery
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_executenonquery.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 94edb659ce7acdebe33f28a5feaa32abaeee564f
---

# Dotnet Adscommand Executenonquery

AdsCommand.ExecuteNonQuery

AdsCommand.ExecuteNonQuery

Advantage .NET Data Provider

| AdsCommand.ExecuteNonQuery  Advantage .NET Data Provider |  |  |  |  |

Executes an SQL statement and returns the number of rows affected.

public int ExecuteNonQuery();

Remarks

You can use the ExecuteNonQuery to execute statements that do not return result sets (e.g., UPDATE, INSERT, DELETE, etc.).

Although the ExecuteNonQuery does not return any rows, any stored procedure output parameters mapped to [AdsParameter](dotnet_adsparameter.md) objects are still populated with data.

For UPDATE, INSERT, and DELETE statements, the return value is the number of rows affected by the command. For all other types of statements, the return value is -1.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand( "update departments set budget = budget \* 1.05",

conn );

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );

See Also

[ExecuteReader](dotnet_adscommand_executereader.md)

[ExecuteScalar](dotnet_adscommand_executescalar.md)
