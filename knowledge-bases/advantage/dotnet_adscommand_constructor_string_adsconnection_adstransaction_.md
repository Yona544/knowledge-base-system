AdsCommand Constructor( string, AdsConnection, AdsTransaction )




Advantage Database Server 12  

AdsCommand Constructor( string, AdsConnection, AdsTransaction )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand Constructor( string, AdsConnection, AdsTransaction )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand Constructor( string, AdsConnection, AdsTransaction ) Advantage .NET Data Provider dotnet\_Adscommand\_constructor\_string\_adsconnection\_adstransaction\_ Advantage .NET Data Provider > AdsCommand Class > AdsCommand Constructors > AdsCommand Constructor( string, AdsConnection, AdsTransaction ) / Dear Support Staff, |  |
| AdsCommand Constructor( string, AdsConnection, AdsTransaction )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsCommand object with a command, an AdsConnection object, and an AdsTransaction object.

public AdsCommand( string cmdText, AdsConnection connection,

AdsTransaction transaction );

Remarks

This constructor accepts an SQL command, stored procedure name, or table name and initializes the command text with the given informaiton. It also accepts an AdsConnection object with which to associate the command object and an AdsTransaction object.

Example

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object and start a new transaction

cmd = new AdsCommand( "update departments set budget = budget \* 1.05",

conn, conn.BeginTransaction() );

// execute the query

cmd.ExecuteNonQuery();

// commit the transaction

cmd.Transaction.Commit();

// close the connection.

conn.Close();

See Also

[AdsConnection](dotnet_adsconnection.htm)

[AdsTransaction](dotnet_adstransaction.htm)