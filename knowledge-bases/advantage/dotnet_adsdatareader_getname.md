AdsDataReader.GetName




Advantage Database Server 12  

AdsDataReader.GetName

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetName  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetName Advantage .NET Data Provider dotnet\_Adsdatareader\_getname Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetName / Dear Support Staff, |  |
| AdsDataReader.GetName  Advantage .NET Data Provider |  |  |  |  |

Gets the name of the specified column.

public String GetName( int columnNumber );

Remarks

Retrieve the name of the column as it is given in the SQL statement or table. If you need the base column name (e.g., for aliased names in SQL statements), you must call [AdsDataReader.GetSchemaTable](dotnet_adsdatareader_getschematable.htm), which provides access to that information.

See Also

[GetSchemaTable](dotnet_adsdatareader_getschematable.htm)

[GetOrdinal](dotnet_adsdatareader_getordinal.htm)