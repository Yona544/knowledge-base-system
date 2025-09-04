AdsDataReader.GetInt64




Advantage Database Server 12  

AdsDataReader.GetInt64

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetInt64  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetInt64 Advantage .NET Data Provider dotnet\_Adsdatareader\_getint64 Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetInt64 / Dear Support Staff, |  |
| AdsDataReader.GetInt64  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a 64-bit signed integer.

public long GetInt64( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a 64-bit signed integer. No conversions are performed, therefore the data retrieved must already be a 64-bit signed integer or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)