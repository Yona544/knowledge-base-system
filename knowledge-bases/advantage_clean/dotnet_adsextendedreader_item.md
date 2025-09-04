---
title: Dotnet Adsextendedreader Item
slug: dotnet_adsextendedreader_item
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_item.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 3bfca2f7dd2d2183311b19c0a0cf66e156c1a810
---

# Dotnet Adsextendedreader Item

AdsExtendedReader.Item

AdsExtendedReader.Item

Advantage .NET Data Provider

| AdsExtendedReader.Item  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the value of the specified column in its native format given the column name or number.

public object this[ string name ] {get; set;}

public object this[ int i ] {get; set;}

Remarks

In C#, this property is the indexer for the AdsExtendedReader class. The column name or the zero-based column ordinal can be used to retrieve or set the value.

Example

AdsConnection conn = new AdsConnection( "data source=c:\\data;" );

 

conn.Open();

AdsCommand cmd = new AdsCommand( "select \* from departments", conn );

AdsExtendedReader r = cmd.ExecuteExtendedReader( CommandBehavior.CloseConnection );

 

r.Read();

Console.WriteLine( "Current value is {0}", r["department code"] );

r["department code"] = 88;

r.Close();

See Also

[AdsDataReader.GetValue](dotnet_adsdatareader_getvalue.md)

[AdsExtendedReader.SetValue](dotnet_adsextendedreader_setvalue.md)
