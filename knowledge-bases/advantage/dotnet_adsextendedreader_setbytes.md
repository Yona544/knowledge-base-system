AdsExtendedReader.SetBytes




Advantage Database Server 12  

AdsExtendedReader.SetBytes

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.SetBytes  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.SetBytes Advantage .NET Data Provider dotnet\_Adsextendedreader\_setbytes Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.SetBytes / Dear Support Staff, |  |
| AdsExtendedReader.SetBytes  Advantage .NET Data Provider |  |  |  |  |

Stores the given array of bytes to a binary or raw field in the specified column.

 

public void SetBytes( int iCol, byte[]abBuffer);

 

public void SetBytes( int iCol,

int iFieldOffset,

int iTotalLength,

byte[] abBuffer,

int iBufferOffset,

int iLength );

Parameters

|  |  |
| --- | --- |
| iCol | The zero based column for the field to be set. |
| iFieldOffset | The offset to which to start writing. This value is supported only for binary or image type. A non-zero value for iFieldOffset for a Raw type field will cause an exception. |
| iTotalLength | Total length of data being stored. If the data is being stored with a single call, this parameter should be the same as iLength. If the data is being stored with multiple calls, then this parameter should be the same for each call and must represent the total length of the binary date. |
| abBuffer | Data to be stored. |
| iBufferOffset | The offset into abBuffer from which to begin copying data. Note that the offset plus the length cannot exceed the size of the buffer. |
| iLength | The number of bytes to be stored. |

Remarks

This method sets the specified zero-based column value iCol to the given array of bytes. No conversions are performed, so the field must be a byte array type (raw or BLOB). To set a byte array field to NULL, use SetValue with a null or empty value.

The first overload assumes a field offset and buffer offset of zero and a total length equal to the size of the byte array.

The second overload will store iLength bytes of data from the iBufferOffset offset into abBuffer to the iFieldOffset offset of the field.

Note Raw type fields do not support field offsets. A non-zero iFieldOffset will cause an exception if iCol is a raw field.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.htm)

[AdsDataReader.GetBytes](dotnet_adsdatareader_getbytes().htm)