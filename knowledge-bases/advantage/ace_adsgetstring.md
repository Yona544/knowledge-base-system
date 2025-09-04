AdsGetString




Advantage Database Server 12  

AdsGetString / AdsGetStringW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetString / AdsGetStringW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetString / AdsGetStringW Advantage Client Engine ace\_Adsgetstring Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetString / AdsGetStringW  Advantage Client Engine |  |  |  |  |

Retrieves the text string version of the given field from the given table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetString (ADSHANDLE hTable,               UNSIGNED8 \*pucFldName,               UNSIGNED8 \*pucBuf,               UNSIGNED32 \*pulLen,               UNSIGNED16 usOption); |
| UNSIGNED32 | AdsGetStringW ( ADSHANDLE hTable,                 UNSIGNED8  \*pucFldName,                 WCHAR      \*pwcBuf,                 UNSIGNED32 \*pulLen,                 UNSIGNED16 usOption ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| pucBuf (O) | Return ANSI/OEM encoded text string in this buffer. |
| pwcBuf (O) | Return UTF16 encoded Unicode text string in this buffer. |
| pulLen (I/O) | Length of given buffer on input, length of returned data on output. For AdsGetString, the length is number of bytes. For AdsGetStringW, the length is number of UTF16 characters. |
| usOption (I) | Option to trim spaces from the returned data. ADS\_NONE, ADS\_TRIM, ADS\_LTRIM, and ADS\_RTRIM. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INSUFFICIENT\_BUFFER | The buffer passed to the function was insufficient to return all data. |
| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF. |
| AE\_UNICODE\_CONVERSION | Unicode data cannot be converted into ANSI/OEM encoded string without loss. |

Remarks

AdsGetString and AdsGetStringW may be used to retrieve strings, numerics, dates, logicals, ModTime, and memos. AdsGetString returns data in ANSI/OEM encoding string. AdsGetStringW returns data in UTF16 encoded Unicode string.  Dates are returned in their raw format (CCYYMMDD). Binary data will be retrieved as base64 encoded strings. In addition, this function does not support short date, double, CurDouble, integer, short integer, time, or timestamp data.

If AdsGetString returns AE\_INSUFFICIENT\_BUFFER, the number of bytes needed for the call to succeed is returned in the pulLen parameter.

If AdsGetStringW returns AE\_INSUFFICIENT\_BUFFER, the number of UTF16 characters needed for the call to succeed is returned in the pulLen parameter.

The AE\_UNICODE\_CONVERSION error is returned if AdsGetString called to get ANSI/OEM encoded string from a Unicode column, and the data cannot be encoded using the ANSI/OEM code page without loss.

When called on a logical field, the value returned will be a T, an F, or a space representing a NULL value.

For memo fields use [AdsGetMemoLength](ace_adsgetmemolength.htm) to get the size in bytes that will be returned if needed.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.htm#adsgetstringexample)

See Also

[AdsSetString](ace_adssetstring.htm)

[AdsSetStringW](ace_adssetstring.htm)

[AdsGetField](ace_adsgetfield.htm)

[AdsGetFieldW](ace_adsgetfield.htm)

[AdsGetMemoLength](ace_adsgetmemolength.htm)

[AdsGetBinaryLength](ace_adsgetbinarylength.htm)