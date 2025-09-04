AdsDataReader.GetFloat




Advantage Database Server 12  

AdsDataReader.GetFloat

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetFloat  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetFloat Advantage .NET Data Provider dotnet\_Adsdatareader\_getfloat Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetFloat / Dear Support Staff, |  |
| AdsDataReader.GetFloat  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a single-precision floating-point number.

public float GetFloat( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a single-precision floating-point number. No conversions are performed, therefore the data retrieved must already be a float or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[GetDouble](dotnet_adsdatareader_getdouble.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)