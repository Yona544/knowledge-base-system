AdsDataReader.GetBytes(int, long, byte[], int, int)




Advantage Database Server 12  

AdsDataReader.GetBytes(int, long, byte[ ], int, int)

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetBytes(int, long, byte[ ], int, int)  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetBytes(int, long, byte[ ], int, int) Advantage .NET Data Provider dotnet\_Adsdatareader\_getbytes(int\_long\_byte\_int\_int) Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetBytes(int, long, byte[], int, int) / Dear Support Staff, |  |
| AdsDataReader.GetBytes(int, long, byte[ ], int, int)  Advantage .NET Data Provider |  |  |  |  |

Reads a stream of bytes from the specified column offset into the buffer an array starting at the given buffer offset.

public long GetBytes

(

int iCol, // (I) 0-based column index

long lFieldOffset, // (I) offset to start reading from

byte[] buffer, // (O) output buffer

int iBufferOffset,// (I) starting offset in output buffer

int iLength // (I) number of bytes to read

);

Return Value

The actual number of bytes read.

Remarks

If you pass a buffer that is a null reference (Nothing in Visual Basic), GetBytes returns the length of the field in bytes.

No conversions are performed; therefore the data retrieved must already be a byte array. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)

[GetBytes()](dotnet_adsdatareader_getbytes().htm)