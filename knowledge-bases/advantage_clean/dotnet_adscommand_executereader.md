---
title: Dotnet Adscommand Executereader
slug: dotnet_adscommand_executereader
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_executereader.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 9616e5c89b51a58b953bf0e83c79c36d28162ba9
---

# Dotnet Adscommand Executereader

AdsCommand.ExecuteReader

AdsCommand.ExecuteReader

Advantage .NET Data Provider

| AdsCommand.ExecuteReader  Advantage .NET Data Provider |  |  |  |  |

Executes the [AdsCommand.CommandText](dotnet_adscommand_commandtext.md) and returns an [AdsDataReader](dotnet_adsdatareader.md) with the result set.

public AdsDataReader ExecuteReader();

Remarks

ExecuteReader executes the SQL statement or stored procedure or opens the table that is specified in the AdsCommand.CommandText property.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source=c:\\data;" );

AdsCommand cmd;

AdsDataReader reader;

int iField;

 

try

{

 

// make the connection to the server

conn.Open();

 

// create a command object

cmd = conn.CreateCommand();

 

// specify a simple SELECT statement

cmd.CommandText = "select \* from departments";

 

// execute the statement and create a reader

reader = cmd.ExecuteReader();

 

// dump the results of the query to the console

while ( reader.Read() )

{

for ( iField = 0; iField < reader.FieldCount; iField++ )

Console.Write( reader.GetValue(iField) + " ");

Console.WriteLine();

}

 

// close the reader (cant execute other statements

// on this command or connection) until it is closed

reader.Close();

 

conn.Close();

}

catch ( AdsException e )

{

// print the exception message

Console.WriteLine( e.Message );

}

See Also

[ExecuteReader( CommandBehavior )](dotnet_adscommand_executereader_commandbehavior_.md)

[CommandText](dotnet_adscommand_commandtext.md)

[AdsDataReader](dotnet_adsdatareader.md)

[AdsExtendedReader](dotnet_adsextendedreader.md)
