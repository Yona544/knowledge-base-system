AdsCommand Constructor()




Advantage Database Server 12  

AdsCommand Constructor()

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand Constructor()  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand Constructor() Advantage .NET Data Provider dotnet\_Adscommand\_constructor\_ Advantage .NET Data Provider > AdsCommand Class > AdsCommand Constructors > AdsCommand Constructor() / Dear Support Staff, |  |
| AdsCommand Constructor()  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsCommand object.

public AdsCommand();

Remarks

This is the default constructor. All property values are initialized to their default values. When using this constructor, it is necessary to assign an AdsConnection object to the [AdsCommand.Connection](dotnet_adscommand_connection.htm) property prior to using the command.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand();

// assign the connection

cmd.Connection = conn;

// specify a query

cmd.CommandText = "select now() from system.iota";

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

// close the connection.

conn.Close();

See Also

[AdsCommand.Connection](dotnet_adscommand_connection.htm)

[AdsConnection](dotnet_adsconnection.htm)