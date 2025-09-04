---
title: Dotnet Adsextendedreader Zaptable
slug: dotnet_adsextendedreader_zaptable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_zaptable.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 1a3c51596e7ec1a82c8cf5323bc4190c20d77a06
---

# Dotnet Adsextendedreader Zaptable

AdsExtendedReader.ZapTable

AdsExtendedReader.ZapTable

Advantage .NET Data Provider

| AdsExtendedReader.ZapTable  Advantage .NET Data Provider |  |  |  |  |

Removes all records from the table and reindexes it.

public void ZapTable()

Remarks

ZapTable will remove all records from the table and all data from the memo file, then the Advantage Client Engine will reindex the table. The indexes must be opened during the zap or they will become invalid. This operation requires exclusive access to the table, specified in the ConnectionString (Shared=FALSE). ZapTable is illegal in a transaction.

Note ZapTable is supported for tables only (CommandType.TableDirect). Calling ZapTable on a cursor will cause an exception.

Example

try

{

AdsConnection conn;

AdsCommand cmd;

AdsExtendedReader rdr;

 

// Set shared=false so the table will be opened exclusively

conn = new AdsConnection( @"data source=c:\data; shared=false" );

conn.Open();

 

// Create a command that specifies just the table name (not an

// SQL statement).

cmd = new AdsCommand( "testdata", conn );

 

// open it as a table (not a cursor)

cmd.CommandType = CommandType.TableDirect;

rdr = cmd.ExecuteExtendedReader();

 

// empty the table.

rdr.ZapTable();

 

rdr.Close();

conn.Close();

}

catch ( Exception ex )

{

Console.WriteLine( ex.ToString() );

}

 

See Also

[PackTable](dotnet_adsextendedreader_packtable.md)

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md)
