AdsCommand.Unprepare




Advantage Database Server 12  

AdsCommand.Unprepare

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.Unprepare |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.Unprepare dotnet\_AdsCommand\_Unprepare Advantage .NET Data Provider > AdsCommand Class > AdsCommand Methods > AdsCommand\_Unprepare / Dear Support Staff, |  |
| AdsCommand.Unprepare |  |  |  |  |

Unprepares the query that has been executed previously, and releases the resources allocated on the client and the server for the query.

public void Unprepare();

Remarks

Unprepare() frees the statement handle allocated for the command object. Freeing the statement handle allows Advantage Database Server to close the tables that have been opened to execute the queries on the statement handle, and to reclaim the memory allocated to parse and execute the last query.

Note: An exception will be thrown if the AdsDataReader obtained from ExecuteReader() is still active for this AdsCommand object. To avoid the exception, use the AdsDataReader.Close() method to close the data reader before unpreparing the query.

Example

AdsConnection conn = new AdsConnection( "data source=c:\\data;");

conn.Open();

AdsCommand cmd = conn.CreateCommand();

cmd.CommandText = "Select \* from Table1";

AdsDataReader reader = cmd.ExecuteReader();

// Table opened on both client and server.

// Close the client side instance

reader.Close();

// Close the server side instance

cmd.Unprepare();

// Force the server and client to reclaim resources

// allocated for the closed tables for this connection.

conn.CloseCachedTables();

See Also

[ExecuteReader](dotnet_adscommand_executereader.htm)