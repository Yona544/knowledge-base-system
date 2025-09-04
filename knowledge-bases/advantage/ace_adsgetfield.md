AdsGetField




Advantage Database Server 12  

AdsGetField / AdsGetFieldW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetField / AdsGetFieldW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetField / AdsGetFieldW Advantage Client Engine ace\_Adsgetfield Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetField / AdsGetFieldW  Advantage Client Engine |  |  |  |  |

Retrieves the text string version of the given field from the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetField (ADSHANDLE hTable,              UNSIGNED8 \*pucFldName,              UNSIGNED8 \*pucBuf,              UNSIGNED32 \*pulLen,              UNSIGNED16 usOption); |
| UNSIGNED32 | AdsGetFieldW ( ADSHANDLE hTable,                UNSIGNED8  \*pucFldName,                WCHAR      \*pwcBuf,                UNSIGNED32 \*pulLen,                UNSIGNED16 usOption); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| pucBuf (O) | For AdsGetField, this parameter returns field data as an ANSI/OEM encoded text string in this buffer. |
| pwcBuf (O) | For AdsGetFieldW, this parameter returns field data as a UTF16 encoded Unicode text string in this buffer. |
| pulLen (I/O) | Length of given buffer on input, length of returned data on output. For AdsGetField, the length is number of bytes. For AdsGetFieldW, the length is number of UTF16 characters. |
| usOption (I) | Option to trim spaces from the returned data.  ADS\_NONE,  ADS\_TRIM, (trims leading and trailing spaces)  ADS\_LTRIM, (trims leading spaces)  ADS\_RTRIM, (trims trailing spaces)  ADS\_GET\_GUID\_MINE, (returns GUID in mime encoded format)  ADS\_GET\_GUID\_FILE, (return GUID in file encoded format)  ADS\_GET\_GUID\_NUMBERS, (returns GUID in numbers only format)  ADS\_GET\_GUID\_REGISTRY, (returns GUID in registry format) |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INSUFFICIENT\_BUFFER | The buffer passed to the function was insufficient to return all data. |
| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF. |
| AE\_UNICODE\_CONVERSION | Unicode data cannot be converted into ANSI/OEM encoded string without loss. |

Remarks

AdsGetField and AdsGetFieldW can be used to retrieve string, numeric, date, logical, double, CurDouble, Money, long integer, integer, short date, time, timestamp, memo, image, RowVersion, ModTime, GUID and binary data. For numerics, Money, times, timestamps, and dates, it converts the result to a string (instead of storing the IEEE numeric data in the buffer). Dates are formatted according to the date mask set by [AdsSetDateFormat](ace_adssetdateformat.htm). For GUID field, the value is returned as text string encoded in one of the format specified by the usOptions. If no option is specified, the value is returned in "registry format" without the curly braces, see [NEWIDSTRING](master_newidstring_.htm) for example formats. AdsGetField returns data in an ANSI/OEM encoded string. AdsGetFieldW returns data in a UTF16 encoded Unicode string.

If AdsGetField returns AE\_INSUFFICIENT\_BUFFER, the number of bytes needed for the call to succeed is returned in the pulLen parameter.

If AdsGetFieldW returns AE\_INSUFFICIENT\_BUFFER, the number of UTF16 characters needed for the call to succeed is returned in the pulLen parameter.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.htm#adsgetfieldexample)

See Also

[AdsGetFieldType](ace_adsgetfieldtype.htm)

[AdsGetString](ace_adsgetstring.htm)

[AdsGetStringW](ace_adsgetstring.htm)

[AdsGetLogical](ace_adsgetlogical.htm)

[AdsGetLong](ace_adsgetlong.htm)

[AdsGetDouble](ace_adsgetdouble.htm)

[AdsGetDate](ace_adsgetdate.htm)

[AdsGetBinary](ace_adsgetbinary.htm)

[AdsGetLongLong](ace_adsgetlonglong.htm)