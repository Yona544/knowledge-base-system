AdsParameterCollection.Add( string, DbType, int, string )




Advantage Database Server 12  

AdsParameterCollection.Add( string, DbType, int, string )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameterCollection.Add( string, DbType, int, string )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameterCollection.Add( string, DbType, int, string ) Advantage .NET Data Provider dotnet\_Adsparametercollection\_add\_string\_dbtype\_int\_string\_ Advantage .NET Data Provider > AdsParameterCollection Class > AdsParameterCollection Methods > AdsParameterCollection.Add( string, DbType, int, string ) / Dear Support Staff, |  |
| AdsParameterCollection.Add( string, DbType, int, string )  Advantage .NET Data Provider |  |  |  |  |

Adds a new AdsParameter with the given name, type, size, and source column to the collection.

public AdsParameter Add

(

string parameterName, // (I) parameter name

DbType dbType, // (I) param type

int iSize, // (I) width of parameter

string sourceColumn // (I) name to map to source table

);

Remarks

This returns a reference to the newly created parameter.