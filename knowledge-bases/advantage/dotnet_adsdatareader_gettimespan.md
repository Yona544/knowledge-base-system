AdsDataReader.GetTimeSpan




Advantage Database Server 12  

AdsDataReader.GetTimeSpan

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetTimeSpan  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetTimeSpan Advantage .NET Data Provider dotnet\_Adsdatareader\_gettimespan Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetTimeSpan / Dear Support Staff, |  |
| AdsDataReader.GetTimeSpan  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a TimeSpan object.

public TimeSpan GetTimeSpan( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a TimeSpan object. No conversions are performed, therefore the data retrieved must already be a time field or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

Note This method can be used to retrieve Advantage Time field values. The System.TimeSpan type is the closest match to the Advantage Time column type.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)