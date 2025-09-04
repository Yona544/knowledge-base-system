AdsCommand Constructor( string )




Advantage Database Server 12  

AdsCommand Constructor( string )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand Constructor( string )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand Constructor( string ) Advantage .NET Data Provider dotnet\_Adscommand\_constructor\_string\_ Advantage .NET Data Provider > AdsCommand Class > AdsCommand Constructors > AdsCommand Constructor( string ) / Dear Support Staff, |  |
| AdsCommand Constructor( string )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsCommand object with an SQL statement, stored procedure name, or table name.

public AdsCommand( string cmdText );

Remarks

This constructor accepts an SQL command, stored procedure name, or table name and initializes the command text with the given information. When using this constructor, it is necessary to assign an AdsConnection object to the [AdsCommand.Connection](dotnet_adscommand_connection.htm) property prior to using the command.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand("select now() from system.iota");

// assign the connection

cmd.Connection = conn;

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();

See Also

[AdsCommand.Connection](dotnet_adscommand_connection.htm)

[AdsConnection](dotnet_adsconnection.htm)