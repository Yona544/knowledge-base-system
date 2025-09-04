AdsParameter Constructor ( string, DbType )




Advantage Database Server 12  

AdsParameter Constructor ( string, DbType )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter Constructor ( string, DbType )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter Constructor ( string, DbType ) Advantage .NET Data Provider dotnet\_Adsparameter\_constructor\_string\_dbtype\_ Advantage .NET Data Provider > AdsParameter Class > AdsParameter Constructors > AdsParameter Constructor ( string, DbType ) / Dear Support Staff, |  |
| AdsParameter Constructor ( string, DbType )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name and type.

public AdsParameter

(

string parameterName, // (I) parameter name

DbType type // (I) parameter type

);

Example

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

AdsParameter param;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand( "update departments set budget = :budget " +

"where [department code] = :code",

conn );

 

// create the two parameters.

param = new AdsParameter( "budget", DbType.Currency );

param.Value = (Decimal)8400000;

cmd.Parameters.Add( param );

param = new AdsParameter( "code", DbType.Int32 );

param.Value = 104;

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );