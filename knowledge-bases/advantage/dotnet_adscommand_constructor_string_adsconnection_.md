AdsCommand Constructor( string, AdsConnection )




Advantage Database Server 12  

AdsCommand Constructor( string, AdsConnection )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand Constructor( string, AdsConnection )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand Constructor( string, AdsConnection ) Advantage .NET Data Provider dotnet\_Adscommand\_constructor\_string\_adsconnection\_ Advantage .NET Data Provider > AdsCommand Class > AdsCommand Constructors > AdsCommand Constructor( string, AdsConnection ) / Dear Support Staff, |  |
| AdsCommand Constructor( string, AdsConnection )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsCommand object with an SQL statement, stored procedure name or table name and the AdsConnection object.

public AdsCommand( string cmdText, AdsConnection connection );

Remarks

This constructor accepts an SQL command, stored procedure name, or table name and initializes the command text with the given informaiton. It also accepts an AdsConnection object with which to associate the command object.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object and give the command and connection

cmd = new AdsCommand( "select now() from system.iota", conn );

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();

See Also

[AdsConnection](dotnet_adsconnection.htm)