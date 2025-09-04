AdsExtendedReader.PackTable




Advantage Database Server 12  

AdsExtendedReader.PackTable

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.PackTable  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.PackTable Advantage .NET Data Provider dotnet\_Adsextendedreader\_packtable Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.PackTable / Dear Support Staff, |  |
| AdsExtendedReader.PackTable  Advantage .NET Data Provider |  |  |  |  |

Removes deleted records and re-indexes the table.

public void PackTable();

Remarks

PackTable will remove all deleted records from the specified table. Internal fragmentation in memo files will also be eliminated. The table is then re-indexed. If a progress callback function is available, it will be called during the reindexing. The indexes must be opened during the pack or they will become logically invalid. [AdsConnection.CloseCachedTables](dotnet_adsconnection_closecachedtables.htm) This operation requires exclusive access to the table, specified in theConnectionString (Shared=FALSE).

Note If encryption was ever enabled on the table, the table cannot be packed unless the encryption is enabled by setting the correct password.

 

Note PackTable only supports tables (CommandType.TableDirect). The use of cursors with this method is illegal and will result in an exception.

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

 

// remove deleted records from the table.

rdr.PackTable();

 

rdr.Close();

conn.Close();

}

catch ( Exception ex )

{

Console.WriteLine( ex.ToString() );

}

 

See Also

[EncryptionPassword](dotnet_adsextendedreader_encryptionpassword.htm)

[ZapTable](dotnet_adsextendedreader_zaptable.htm)

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)