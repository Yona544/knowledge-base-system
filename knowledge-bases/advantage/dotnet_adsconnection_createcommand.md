AdsConnection.CreateCommand




Advantage Database Server 12  

AdsConnection.CreateCommand

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.CreateCommand  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.CreateCommand Advantage .NET Data Provider dotnet\_Adsconnection\_createcommand Advantage .NET Data Provider > AdsConnection Class > AdsConnection Methods > AdsConnection.CreateCommand / Dear Support Staff, |  |
| AdsConnection.CreateCommand  Advantage .NET Data Provider |  |  |  |  |

Creates and returns an AdsCommand object associated with the AdsConnection.

public AdsCommand CreateCommand();

Remarks

This method creates a new AdsCommand object that can be used for executing queries against the open connection. The [AdsCommand.Connection](dotnet_adscommand_connection.htm) property is automatically set when this method is used.

Example

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object

cmd = conn.CreateCommand();

// specify a query

cmd.CommandText = "select now() from system.iota";

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();