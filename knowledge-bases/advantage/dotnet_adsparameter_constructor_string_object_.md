AdsParameter Constructor ( string, object )




Advantage Database Server 12  

AdsParameter Constructor ( string, object )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter Constructor ( string, object )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter Constructor ( string, object ) Advantage .NET Data Provider dotnet\_Adsparameter\_constructor\_string\_object\_ Advantage .NET Data Provider > AdsParameter Class > AdsParameter Constructors > AdsParameter Constructor ( string, object ) / Dear Support Staff, |  |
| AdsParameter Constructor ( string, object )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name and value.

public AdsParameter

(

string parameterName, // (I) parameter name

object value // (I) parameter value

);

Remarks

The DbType will be inferred from the value of the given object. It can be changed if desired after creating the AdsParameter object via the [AdsParameter.DbType](dotnet_adsparameter_dbtype.htm) property.

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

param = new AdsParameter( "name", "Research & Development" );

cmd.Parameters.Add( param );

param = new AdsParameter( "code", 104 );

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );