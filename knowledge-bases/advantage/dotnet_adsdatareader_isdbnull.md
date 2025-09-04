AdsDataReader.IsDBNull




Advantage Database Server 12  

AdsDataReader.IsDBNull

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.IsDBNull  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.IsDBNull Advantage .NET Data Provider dotnet\_Adsdatareader\_isdbnull Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.IsDBNull / Dear Support Staff, |  |
| AdsDataReader.IsDBNull  Advantage .NET Data Provider |  |  |  |  |

Indicates whether or not the column contains a null.

public bool IsDBNull( int columnNumber );

Remarks

This returns True if the specified zero-based column has a null value. Call this method to check for null column values before calling the typed get methods (for example, [GetBoolean](dotnet_adsdatareader_getboolean.htm), [GetString](dotnet_adsdatareader_getstring.htm), etc.) to avoid raising an error.

DBF tables (TableType of CDX or NTX) do not have null values except for date fields, so this will always return False for non-date fields unless the connection string property DbfsUseNulls is set to True. See [AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm).

See Also

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)