AdsDataReader.GetChars




Advantage Database Server 12  

AdsDataReader.GetChars

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetChars  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetChars Advantage .NET Data Provider dotnet\_Adsdatareader\_getchars Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetChars / Dear Support Staff, |  |
| AdsDataReader.GetChars  Advantage .NET Data Provider |  |  |  |  |

Reads a stream of characters from the specified column offset into the buffer as an array starting at the given buffer offset.

public long GetChars

(

int iCol, // (I) 0-based column index

long lFieldOffset, // (I) offset to start reading from

char[] buffer, // (O) output buffer

int iBufferOffset,// (I) starting offset in output buffer

int iLength // (I) number of bytes to read

);

Return Value

The actual number of characters read.

Remarks

If you pass a buffer that is a null reference (Nothing in Visual Basic), GetChars returns the length of the field in characters.

No conversions are performed; therefore the data retrieved must already be a character array (memo or string field). This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.htm) to check for null values before calling this method.

Note This method is not affected by the TrimTrailingSpaces option (see [AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)).

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)

[IsDBNull](dotnet_adsdatareader_isdbnull.htm)