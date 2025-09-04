AdsParameter Constructor ( string, DbType, string, DataRowVersion )




Advantage Database Server 12  

AdsParameter Constructor ( string, DbType, string, DataRowVersion )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter Constructor ( string, DbType, string, DataRowVersion )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter Constructor ( string, DbType, string, DataRowVersion ) Advantage .NET Data Provider dotnet\_Adsparameter\_constructor\_string\_dbtype\_string\_datarowversion\_ Advantage .NET Data Provider > AdsParameter Class > AdsParameter Constructors > AdsParameter Constructor ( string, DbType, string, DataRowVersion ) / Dear Support Staff, |  |
| AdsParameter Constructor ( string, DbType, string, DataRowVersion )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name, type, source column, and source version.

public AdsParameter

(

string parameterName, // (I) param name

DbType dbType, // (I) param type

string srcColumn, // (I) dataset source column mapping

DataRowVersion srcVersion // (I) current or original

);

Example

AdsParameter param = new AdsParameter( "pk", DbType.String,

"pk", DataRowVersion.Original );