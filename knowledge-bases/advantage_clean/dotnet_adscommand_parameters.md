---
title: Dotnet Adscommand Parameters
slug: dotnet_adscommand_parameters
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_parameters.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 754cde6a44a5955e61020dc643df2ea3b4515887
---

# Dotnet Adscommand Parameters

AdsCommand.Parameters

AdsCommand.Parameters

Advantage .NET Data Provider

| AdsCommand.Parameters  Advantage .NET Data Provider |  |  |  |  |

Provides access to the [AdsParameter](dotnet_adsparameter.md) collection associated with the AdsCommand object.

public AdsParameterCollection Parameters {get;}

Remarks

The parameter collection is empty by default. The Advantage .NET Data Provider supports both named and unnamed parameters. Named parameters consist of a colon followed by a valid identifier (e.g., :value). Unnamed parameters consist of a question mark.

Example

This example executes a statement with a single parameter.

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

AdsParameter prm;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand( "", conn );

// specify a statement

cmd.CommandText = "select [last name] from employee " +

"where [employee number] = :empid";

 

// create a parameter and put it in the collection

prm = cmd.CreateParameter();

prm.Value = 94;

cmd.Parameters.Add( prm );

 

// dump the first row/column of the table

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();

See Also

[AdsCommand.CreateParameter](dotnet_adscommand_createparameter.md)
