AdsExtendedReader.ZapTable




Advantage Database Server 12  

AdsExtendedReader.ZapTable

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.ZapTable  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.ZapTable Advantage .NET Data Provider dotnet\_Adsextendedreader\_zaptable Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.ZapTable / Dear Support Staff, |  |
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

[PackTable](dotnet_adsextendedreader_packtable.htm)

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)