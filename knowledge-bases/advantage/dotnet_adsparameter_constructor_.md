AdsParameter Constructor ()




Advantage Database Server 12  

AdsParameter Constructor ()

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter Constructor ()  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter Constructor () Advantage .NET Data Provider dotnet\_Adsparameter\_constructor\_ Advantage .NET Data Provider > AdsParameter Class > AdsParameter Constructors > AdsParameter Constructor () / Dear Support Staff, |  |
| AdsParameter Constructor ()  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with all default values for the properties.

public AdsParameter();

Remarks

Using this constructor is equivalent to calling [AdsCommand.CreateParameter](dotnet_adscommand_createparameter.htm).

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

param = new AdsParameter();

param.Value = 400000;

param.ParameterName = "budget";

cmd.Parameters.Add( param );

param = new AdsParameter();

param.Value = 110;

param.ParameterName = "code";

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );

See Also

[AdsCommand.CreateParameter](dotnet_adscommand_createparameter.htm)