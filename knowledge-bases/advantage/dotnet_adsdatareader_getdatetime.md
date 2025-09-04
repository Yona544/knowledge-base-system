AdsDataReader.GetDateTime




Advantage Database Server 12  

AdsDataReader.GetDateTime

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetDateTime  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetDateTime Advantage .NET Data Provider dotnet\_Adsdatareader\_getdatetime Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetDateTime / Dear Support Staff, |  |
| AdsDataReader.GetDateTime  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a DateTime object.

public DateTime GetDateTime( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a DateTime object. No conversions are performed, therefore, the data retrieved must already be a DateTime-compatible value, or an exception is generated. This method can be used to retrieve timestamp, ModTime, and date field values, but cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)