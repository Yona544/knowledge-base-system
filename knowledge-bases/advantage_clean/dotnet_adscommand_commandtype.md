---
title: Dotnet Adscommand Commandtype
slug: dotnet_adscommand_commandtype
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_commandtype.htm
source: Advantage CHM
tags:
  - dotnet
checksum: d32de946da06eaa5dabc980a65452885f9287162
---

# Dotnet Adscommand Commandtype

AdsCommand.CommandType

AdsCommand.CommandType

Advantage .NET Data Provider

| AdsCommand.CommandType  Advantage .NET Data Provider |  |  |  |  |

Gets or sets a value indicating how the [AdsCommand.CommandText](dotnet_adscommand_commandtext.md) property is to be interpreted.

public CommandType CommandType {get; set;}

Remarks

The CommandType property can have one of the following values. The [AdsCommand.CommandText](dotnet_adscommand_commandtext.md) property must be set consistently.

| CommandType | CommandText |
| Text (default) | Set CommandText to a valid SQL statement such as SELECT, UPDATE, INSERT, CREATE, etc. |
| StoredProcedure | Set CommandText to an existing stored procedure name. Note that you can use CommandType.Text for executing stored procedures providing an EXECUTE PROCEDURE statement. |
| TableDirect | Set CommandText to a table name. The table will be opened directly by the Advantage .NET Data Provider. The Advantage .NET Data Provider does not support a list of tables. Only one table name can be specified. |

Example

This example opens a table directly.

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object with a table name

cmd = new AdsCommand( "employee", conn );

// set command type to open the table

cmd.CommandType = CommandType.TableDirect;

 

// dump the first row/column of the table

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();

See Also

[AdsCommand.CommandText](dotnet_adscommand_commandtext.md)
