---
title: Dotnet Adscommand Executereader Commandbehavior
slug: dotnet_adscommand_executereader_commandbehavior_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_executereader_commandbehavior_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 8f2cee8e1f389c8dd2bb5fd4e0b26521a06419dc
---

# Dotnet Adscommand Executereader Commandbehavior

AdsCommand.ExecuteReader( CommandBehavior )

AdsCommand.ExecuteReader( CommandBehavior )

Advantage .NET Data Provider

| AdsCommand.ExecuteReader( CommandBehavior )  Advantage .NET Data Provider |  |  |  |  |

Executes the [AdsCommand.CommandText](dotnet_adscommand_commandtext.md) and returns an [AdsDataReader](dotnet_adsdatareader.md) with the result set based on the CommandBehavior value.

public AdsDataReader ExecuteReader( CommandBehavior behavior );

Remarks

Depending on the CommandBehavior value, this executes the SQL statement or stored procedure or opens the table that is specified in the AdsCommand.CommandText property.

The CommandBehavior values that affect the AdsDataReader are shown in the following table. Bitwise combinations of these values can be used.

| Member name | Description |
| CloseConnection | When the command is executed, the associated Connection object is closed when the associated DataReader object is closed. |
| Default | Default sets no CommandBehavior flags, so calling ExecuteReader(CommandBehavior.Default) is functionally equivalent to calling ExecuteReader(). |
| KeyInfo | The query returns column and primary key information. |
| SchemaOnly | The query returns column information only. No result set is returned. |
| SingleRow | The query is expected to return a single row. The Advantage .NET Data Provider will return multiple rows if requested by Read operations, but it will not be as efficient because the provider will use a smaller read cache size when this option is specified. |

Example

This example executes the reader with the SchemaOnly bit set.

// create a connection object

AdsConnection conn = new AdsConnection( "data source=c:\\data;" );

AdsCommand cmd;

AdsDataReader reader;

 

try

{

 

// make the connection to the server

conn.Open();

 

// create a command object

cmd = conn.CreateCommand();

 

// specify a table name

cmd.CommandText = "departments";

cmd.CommandType = CommandType.TableDirect;

 

// get the schema for the table

reader = cmd.ExecuteReader( CommandBehavior.SchemaOnly );

 

// get the schema table itself

DataTable datatable = reader.GetSchemaTable();

 

// print some schema information

foreach ( DataRow row in datatable.Rows )

{

Console.Write( row["ColumnName"] );

Console.Write( "\t" + row["DataType"].ToString() );

Console.WriteLine( "\t" + row["IsKey"].ToString() );

}

 

conn.Close();

See Also

[ExecuteReader](dotnet_adscommand_executereader.md)

[ExecuteScalar](dotnet_adscommand_executescalar.md)

[ExecuteNonQuery](dotnet_adscommand_executenonquery.md)

[CommandText](dotnet_adscommand_commandtext.md)

[AdsDataReader.GetSchemaTable](dotnet_adsdatareader_getschematable.md)

[AdsExtendedReader](dotnet_adsextendedreader.md)
