---
title: Dotnet Adscommand Commandtext
slug: dotnet_adscommand_commandtext
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_commandtext.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 8b8d45a302074a856c00e18703bfeb240d74a0e5
---

# Dotnet Adscommand Commandtext

AdsCommand.CommandText

AdsCommand.CommandText

Advantage .NET Data Provider

| AdsCommand.CommandText  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the SQL statement, stored procedure, or table name to execute or open at the data source.

public string CommandText {get; set;}

Remarks

The SQL command, stored procedure name, or table name to be executed is stored in the CommandText property. If it is an SQL statement, the [AdsCommand.CommandType](dotnet_adscommand_commandtype.md) property should be set to Text. If the CommandText property has a stored procedure name, the CommandType property should be set to StoredProcedure. And, finally, if a table name is stored in the CommandText property, the CommandType should be set to TableDirect. The default CommandType is Text.

Example

This example executes a SELECT statement and retrieves the single row/column value as a scalar. The default type of CommandType is Text, so it does not need to be specified.

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

This example executes a stored procedure and uses the [DeriveParameters](dotnet_adscommandbuilder_deriveparameters.md) to automatically build up the parameter collection for the stored procedure.

conn = new AdsConnection( "data source=c:\\data\\test.add;" +

"user id=test;" );

 

conn.Open();

 

AdsCommand cmd = conn.CreateCommand();

 

// assign the procedure name

cmd.CommandText = "testproc";

// set command type to stored procedure

cmd.CommandType = CommandType.StoredProcedure;

// load the parameter collection from the data dictionary info

cmd.DeriveParameters();

// assign in put parameters

cmd.Parameters["inparam1"].Value = 234;

cmd.Parameters["inparam2"].Value = "xyz";

 

// execute the stored procedure

cmd.ExecuteNonQuery();

// print an output parameter

Console.WriteLine( cmd.Parameters["outparam"].Value );

See Also

[AdsCommand.CommandType](dotnet_adscommand_commandtype.md)

[AdsCommand.Parameters](dotnet_adscommand_parameters.md)
