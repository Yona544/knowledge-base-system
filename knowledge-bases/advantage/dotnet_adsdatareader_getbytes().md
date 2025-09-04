AdsDataReader.GetBytes()




Advantage Database Server 12  

AdsDataReader.GetBytes()

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetBytes()  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetBytes() Advantage .NET Data Provider dotnet\_Adsdatareader\_getbytes() Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetBytes() / Dear Support Staff, |  |
| AdsDataReader.GetBytes()  Advantage .NET Data Provider |  |  |  |  |

Retrieves a binary or raw field as an array of bytes.

public byte[] GetBytes( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as an array of bytes. No conversions are performed; therefore the data retrieved must already be a byte array (raw field or BLOB field). This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)

[GetBytes(int, long, byte[], int, int)](dotnet_adsdatareader_getbytes(int_long_byte_int_int).htm)