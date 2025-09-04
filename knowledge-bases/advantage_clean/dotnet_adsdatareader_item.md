---
title: Dotnet Adsdatareader Item
slug: dotnet_adsdatareader_item
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_item.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 1f0517f73dcf339c9e239c95db425eda13ced3e9
---

# Dotnet Adsdatareader Item

AdsDataReader.Item

AdsDataReader.Item

Advantage .NET Data Provider

| AdsDataReader.Item  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column in its native format given the column name or number.

public object this[ string name ] {get;}

 

public object this[ int i ] {get;}

Remarks

In C#, this property is the indexer for the AdsDataReader class. The column name or the zero-based column ordinal can be used to retrieve the value.

Example

AdsConnection conn = new AdsConnection( "data source=c:\\data;" );

AdsCommand cmd;

AdsDataReader reader;

 

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

 

reader.Read();

 

// print column with both versions of indexer

Console.WriteLine( reader[0].ToString() );

Console.WriteLine( reader["department code"].ToString() );

 

conn.Close();

}

catch ( AdsException e )

{

// print the exception message

Console.WriteLine( e.Message );

}

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)
