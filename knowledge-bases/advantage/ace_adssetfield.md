AdsSetField




Advantage Database Server 12  

AdsSetField / AdsSetFieldW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetField / AdsSetFieldW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetField / AdsSetFieldW Advantage Client Engine ace\_Adssetfield Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetField / AdsSetFieldW  Advantage Client Engine |  |  |  |  |

Stores the given data into the specified field

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetField ( ADSHANDLE hObj,               UNSIGNED8 \*pucFldName,               UNSIGNED8 \*pucValue,               UNSIGNED32 ulLen); |
| UNSIGNED32 | AdsSetFieldW ( ADSHANDLE hObj,               UNSIGNED8  \*pucFldName,               WCHAR      \*pwcValue,               UNSIGNED32 ulLen ); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, or index order. |
| pucFldName (I) | Name of field to set. |
| pucValue (I) | ANSI/OEM code page encoded data to store in field. |
| pwcValue (I) | UTF16 encoded Unicode data to store in field. |
| ulLen (I) | Length of data in the buffer. For AdsSetField, the length is the number of bytes. For AdsSetFieldW, the length is the number of UTF16 characters. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_DATA\_TOO\_LONG | The data given was too long to fit in the field. |
| AE\_DATA\_TRUNCATED | The data given was too long to fit in the field. The data was truncated to fit into the field. |
| AE\_INVALID\_MONTH | The month given is not valid. Valid months are 1-12. |
| AE\_INVALID\_DAY | The day given is not valid for the given month. |

|  |  |
| --- | --- |
| AE\_UNICODE\_CONVERSION | Unicode data cannot be converted into ANSI/OEM code page encoded string without loss. |

Remarks

AdsSetField and AdsSetFieldW can be used to store logical, string, memo, numeric, date, short date, double, CurDouble, Money, long integer, integer, short integer, time, timestamp, image, binary, RowVersion, ModTime, raw and GUID data.

Dates, times, timestamps, and numerics (including integers, doubles and numeric), and Money values are expected to be given as text strings. Dates are expected to be formatted the same as the current [AdsSetDateFormat](ace_adssetdateformat.htm) setting. For example, to set a timestamp field, the value could be "7/28/1996 14:30:25". To set empty or null values in fields, use [AdsSetEmpty](ace_adssetempty.htm). Setting the value of a field requires a data lock on the table, either a record lock or a file lock. If no lock is held on the current record or table, the Advantage Client Engine will attempt to get an implicit lock on the record. Implicit locks are released when the record is updated on the server.

For GUID data, the value is expected to be text strings of the GUID in "registry format", for example, "{A4AB-43C4-84E5-010204081020}". The curly braces are optional. The values will be converted into 16 byte raw data and stored in the table.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to AdsInitRawKey and AdsBuildRawKey.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.htm#adssetfieldexample)

See Also

[AdsGetField](ace_adsgetfield.htm)

[AdsGetFieldW](ace_adsgetfield.htm)

[AdsGetFieldName](ace_adsgetfieldname.htm)

[AdsSetLogical](ace_adssetlogical.htm)

[AdsSetDate](ace_adssetdate.htm)

[AdsSetDouble](ace_adssetdouble.htm)

[AdsSetEmpty](ace_adssetempty.htm)

[AdsSetJulian](ace_adssetjulian.htm)

[AdsSetLong](ace_adssetlong.htm)

[AdsSetString](ace_adssetstring.htm)

[AdsSetStringW](ace_adssetstring.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsSetLongLong](ace_adssetlonglong.htm)

[AdsSetMoney](ace_adssetmoney.htm)