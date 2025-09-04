AdsDataReader.GetBoolean




Advantage Database Server 12  

AdsDataReader.GetBoolean

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetBoolean  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetBoolean Advantage .NET Data Provider dotnet\_Adsdatareader\_getboolean Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetBoolean / Dear Support Staff, |  |
| AdsDataReader.GetBoolean  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a Boolean.

public bool GetBoolean( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a Boolean. No conversions are performed, therefore the data retrieved must already be a Boolean or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)