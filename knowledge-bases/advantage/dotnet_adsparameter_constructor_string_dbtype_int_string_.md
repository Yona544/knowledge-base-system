AdsParameter Constructor ( string, DbType, int, string )




Advantage Database Server 12  

AdsParameter Constructor ( string, DbType, int, string )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter Constructor ( string, DbType, int, string )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter Constructor ( string, DbType, int, string ) Advantage .NET Data Provider dotnet\_Adsparameter\_constructor\_string\_dbtype\_int\_string\_ Advantage .NET Data Provider > AdsParameter Class > AdsParameter Constructors > AdsParameter Constructor ( string, DbType, int, string ) / Dear Support Staff, |  |
| AdsParameter Constructor ( string, DbType, int, string )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name, type, parameter width, and source column mapping.

public AdsParameter

(

string parameterName, // (I) param name

DbType dbType, // (I) param type

int iSize, // (I) parameter width

string sourceColumn // (I) mapping to dataset column

);

Remarks

The Size will be inferred from the value of the DbType parameter and the value if it is not explicity set in the size parameter. This constructor can be used when creating parameters for commands in an [AdsDataAdapter](dotnet_adsdataadapter.htm) where it is necessary to map parameters to columns in the DataSet.

Example

AdsParameter param = new AdsParameter( "Description", DbType.String,

100, "Description" );

param.Direction = ParameterDirection.Output;