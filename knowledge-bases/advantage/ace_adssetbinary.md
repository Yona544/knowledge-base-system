AdsSetBinary




Advantage Database Server 12  

AdsSetBinary

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetBinary  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetBinary Advantage Client Engine ace\_Adssetbinary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetBinary  Advantage Client Engine |  |  |  |  |

Stores given data as a BLOB in the given field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetBinary (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 usBinaryType,  UNSIGNED32 ulTotalLength,  UNSIGNED32 ulOffset,  UNSIGNED8 \*pucBuf,  UNSIGNED32 ulLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table, cursor, or statement. |
| pucFldName (I) | Name of field to set. |
| usBinaryType (I) | Indicates type of binary data. Values are ADS\_IMAGE and ADS\_BINARY. |
| ulTotalLength (I) | Total length of data being stored. If the data is being stored with a single call, this parameter should be the same as ulLen. If the data is being stored with multiple calls, then this parameter should be the same for each call and must represent the total length of the binary date. |
| ulOffset (I) | Offset to which to start writing. See the remarks below about using AES encryption. |
| pucBuf (I) | Store this data in the field. |
| ulLen (I) | Length of data in the buffer for this call. |

Remarks

AdsSetBinary sets binary objects that are held in memory. For larger binary objects, [AdsFileToBinary](ace_adsfiletobinary.htm) is provided. Be sure to specify ADS\_IMAGE if storing an image in the field. This API can be used to store binary data in memo fields. If used this way, [AdsGetMemoDataType](ace_adsgetmemodatatype.htm) can be called to determine the type of data stored in the memo field.

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

When using [AES encryption](master_encryption.htm) and when writing a BLOB in chunks (non-zero offsets), some care must be taken. When a BLOB write occurs at offset zero, Advantage generates a new AES message to produce a unique encryption stream. This means that any existing BLOB data beyond the written portion (if less than the total is written) will not be recoverable in its unencrypted state. For example, suppose a BLOB is 10 bytes. If you write all 10 bytes and then write one byte to offset zero, Advantage will generate a new AES message number, and the remaining 9 bytes will be unusable because they were encrypted using the old AES message number that  was generated when the 10 bytes were written.

When writing to a compressed BLOB field, writing data in chunks is not allowed. The [5227](error_5227_compression_failed.htm) error will be returned if ulOffset is not 0 or ulTotalLength does not equal to ulLen.

Another aspect of the AES message number generation is that if you write to a non-zero offset in the BLOB multiple times with different data, the data will be encrypted each time with the same encryption stream. This would introduce a weakness that could possibly be exploited and allow an attacker to find out information about the BLOB data. Thus, if different data is being written multiple times to the same offset, the entire BLOB should be re-written.

Example 1

AdsPrepareSQL( hStatement,

"INSERT INTO test ( bin\_field ) VALUES ( :bin\_data )" );

AdsSetBinary( hStatement, "bin\_data", ADS\_BINARY, ulBufferSize, 0, aiData, ulBufferSize );

AdsExecuteSQL( hStatement, &hCursor);

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"INSERT INTO test ( bin\_field ) VALUES ( :bin\_data )" );

AdsSetBinary( hStatement, ADSFIELD(1), ADS\_BINARY, ulBufferSize, 0, aiData, ulBufferSize );

AdsExecuteSQL( hStatement, &hCursor);

Note Use of this function is illegal in a transaction if the entire binary value is not being stored to the Binary/Image field in a single call. In other words, if the value in the ulTotalLength parameter is not the same as the value in the ulLen parameter, use of this function is illegal in a transaction. If the entire binary value is sent in a single call to AdsSetBinary, use of this function is supported in a transaction.

Example 3

[Additional Example](ace_examples.htm#adssetbinaryexample)

See Also

[AdsGetBinary](ace_adsgetbinary.htm)

[AdsGetBinaryLength](ace_adsgetbinarylength.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsGetFieldType](ace_adsgetfieldtype.htm)

[AdsGetMemoDataType](ace_adsgetmemodatatype.htm)

[AdsFileToBinary](ace_adsfiletobinary.htm)

[AdsPrepareSQL](ace_adspreparesql.htm)