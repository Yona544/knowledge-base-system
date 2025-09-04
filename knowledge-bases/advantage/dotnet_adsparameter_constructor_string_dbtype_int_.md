AdsParameter Constructor ( string, DbType, int )




Advantage Database Server 12  

AdsParameter Constructor ( string, DbType, int )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter Constructor ( string, DbType, int )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter Constructor ( string, DbType, int ) Advantage .NET Data Provider dotnet\_Adsparameter\_constructor\_string\_dbtype\_int\_ Advantage .NET Data Provider > AdsParameter Class > AdsParameter Constructors > AdsParameter Constructor ( string, DbType, int ) / Dear Support Staff, |  |
| AdsParameter Constructor ( string, DbType, int )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name, type, and parameter width.

public AdsParameter

(

string parameterName, // (I) parameter name

DbType type, // (I) parameter type

int iSize // (I) parameter width

);

Remarks

The Size is inferred from the value of the DbType parameter and the value if it is not explicity set in the size parameter.

Example

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

AdsParameter param;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand( "update departments set [Department Name] = :name " +

"where [department code] = :code",

conn );

 

// create the two parameters.

param = new AdsParameter( "name", DbType.String, 15 );

param.Value = "R & D";

cmd.Parameters.Add( param );

param = new AdsParameter( "code", DbType.Int32, 4 );

param.Value = 104;

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );