AdsDataReader.GetDecimal




Advantage Database Server 12  

AdsDataReader.GetDecimal

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetDecimal  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetDecimal Advantage .NET Data Provider dotnet\_Adsdatareader\_getdecimal Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetDecimal / Dear Support Staff, |  |
| AdsDataReader.GetDecimal  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a Decimal object.

public Decimal GetDecimal( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a Decimal object. No conversions are performed, therefore the data retrieved must already be a Decimal or an exception is generated. It can be used to retrieve numeric, money, and integer field values. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)