AdsDataReader.GetString




Advantage Database Server 12  

AdsDataReader.GetString

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetString  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetString Advantage .NET Data Provider dotnet\_Adsdatareader\_getstring Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetString / Dear Support Staff, |  |
| AdsDataReader.GetString  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a string.

public string GetString( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a string. No conversions are performed, therefore the data retrieved must already be a string or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

AdsDataReader.GetValue

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)