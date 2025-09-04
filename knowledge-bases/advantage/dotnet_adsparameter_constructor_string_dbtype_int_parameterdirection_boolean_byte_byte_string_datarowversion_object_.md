AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, string, DataRowVersion, object )




Advantage Database Server 12  

AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, string, DataRowVersion, object )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, string, DataRowVersion, object )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, string, DataRowVersion, object ) Advantage .NET Data Provider dotnet\_Adsparameter\_constructor\_string\_dbtype\_int\_parameterdirection\_boolean\_byte\_byte\_string\_datarowversion\_object\_ Advantage .NET Data Provider > AdsParameter Class > AdsParameter Constructors > AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, st / Dear Support Staff, |  |
| AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, string, DataRowVersion, object )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new AdsParameter instance with name, type, size, direction, null flag, precision, scale, source column, source version, and a value.

public AdsParameter

(

string parameterName, // (I) parameter name

DbType dbType, // (I) parameter type

int iSize, // (I) parameter width

ParameterDirection direction, // (I) input or output

Boolean isNullable, // (I) can parameter be null?

Byte precision, // (I) precision for numeric

Byte scale, // (I) scale for numeric

string srcColumn, // (I) dataset source column mapping

DataRowVersion srcVersion, // (I) current or original

object value // (I) the parameter value

);

Example

AdsParameter param = new AdsParameter( "name", DbType.String, 15,

ParameterDirection.Input,

false, 0, 0, "Department Name", DataRowVersion.Current,

"Administration" );