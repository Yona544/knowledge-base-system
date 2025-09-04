AdsDataReader.GetDouble




Advantage Database Server 12  

AdsDataReader.GetDouble

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetDouble  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetDouble Advantage .NET Data Provider dotnet\_Adsdatareader\_getdouble Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetDouble / Dear Support Staff, |  |
| AdsDataReader.GetDouble  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a double-precision floating-point number.

public double GetDouble( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a double-precision floating-point number. No conversions are performed, therefore the data retrieved must already be a double or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)