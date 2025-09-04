AdsDataReader.GetByte




Advantage Database Server 12  

AdsDataReader.GetByte

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetByte  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetByte Advantage .NET Data Provider dotnet\_Adsdatareader\_getbyte Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetByte / Dear Support Staff, |  |
| AdsDataReader.GetByte  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a byte.

public byte GetByte( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a byte. No conversions are performed, therefore the data retrieved must already be a byte or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)