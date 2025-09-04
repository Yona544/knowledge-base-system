DBF Field Types and Specifications




Advantage Database Server 12  

DBF Field Types and Specifications

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DBF Field Types and Specifications  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DBF Field Types and Specifications Advantage Concepts master\_Dbf\_field\_types\_and\_specifications Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DBF Field Types and Specifications  Advantage Concepts |  |  |  |  |

Standard DBF Table Data Types

The following are standard field data types available in DBF tables. The length indicates the amount of data stored in the record image. For fields that include memo file storage, see the description for the amount of data that can be stored.

|  |  |  |  |
| --- | --- | --- | --- |
| Type | Length | Decimals | Description |
| Character | 1 to 65534 | N/A | Fixed-length character field that is stored entirely in the table. Note that if you want the table to be compatible with Visual FoxPro, you should limit the field length to 254 or less. |
| Numeric | 1 to 32 | 0 to Length-2 | Fixed-length (exact ASCII representation) numeric. |
| Date | 8 | N/A | 8-byte date field in the form of CCYYMMDD. |
| Logical | 1 | N/A | 1-byte logical (boolean) field. Recognized values for True are 1, T, t, Y, and y. |
| Memo | 10 or 4 | N/A | Variable-length memo field. The size of each field is limited to 4 GB.  Visual FoxPro memo fields require 4 bytes in the record image, while standard DBF memo fields require 10 bytes.  The memo data is actually stored in a separate file, called a memo file, to reduce table bloat. |

Extended DBF Table Data Types

The following are extended field data types available in DBF tables. The extended data types are non-standard DBF extensions. Non-Advantage applications that read DBF tables may not be able to open and read tables that have extended data types. Visual FoxPro will recognize double, integer, general, and picture fields. The NChar, NVarChar, and NMemo fields are an Advantage-specific extension.

|  |  |  |  |
| --- | --- | --- | --- |
| Type | Length | Decimals | Description |
| Double | 8 | 0-20 | 8-byte IEEE floating point value in the range 1.7E +/-308 (15 digits of precision). The decimal value affects NTX indexes and the use of the field in expressions. It does not affect the precision of the stored data. If the length is given, it will be ignored. For example, "salary, double, 10, 2" and "salary, double, 2" produce the same field. |
| Integer | 4 | N/A | 4-byte long integer values from -2,147,483,648 to 2,147,483,647. |
| ShortDate | 3 | N/A | 3-byte date field. This type supports the same range of dates as a standard date field. |
| Image | 10 | N/A | Variable-length memo field containing binary image data. The size of each field is limited to 4 GB. The binary image data is actually stored in a separate file, called a memo file, to reduce table bloat. If using the Advantage CA-Visual Objects RDDs, Advantage Client Engine APIs must be used to set and retrieve the image data. Most non-Advantage applications will interpret this data as a text memo field with a short text identifier. |
| Binary | 10 | N/A | Variable-length memo field containing binary data. The size of each field is limited to 4 GB. The binary data is actually stored in a separate file, called a memo file, to reduce table bloat. If using the Advantage CA-Visual Objects RDDs, Advantage Client Engine APIs must be used to set and retrieve the binary data. Most non-Advantage applications will interpret this data as a text memo field with a short text identifier. |

Visual FoxPro DBF Table Data Types

In addition to the standard DBF types, the following types can be used when using the ADS\_VFP table type (Visual FoxPro driver). These are fully compatible with Visual FoxPro.

|  |  |  |  |
| --- | --- | --- | --- |
| Type | Length | Decimals | Description |
| Double | 8 | 0-20 | 8-byte IEEE floating point value in the range 1.7E +/-308 (15 digits of precision). The decimal value affects NTX indexes and the use of the field in expressions. It does not affect the precision of the stored data. If the length is given, it will be ignored. For example, "salary, double, 10, 2" and "salary, double, 2" produce the same field. |
| Integer | 4 | N/A | 4-byte long integer values from -2,147,483,648 to 2,147,483,647. |
| Binary | 4 | N/A | Variable-length field containing binary (Blob) data. The size of each Blob is limited to 4 GB. The binary data is stored in the FPT memo file associated with the table. |
| Money | 8 | 4 implied | Currency data stored internally as a 64-bit integer, with 4 implied decimal digits from -922,337,203,685,477.5807 to +922,337,203,685,477.5807. The Money data type will not lose precision. |
| TimeStamp | 8 | N/A | DateTime value containing year, month, day, hour, minute, and second. Note that the timestamp value can contain milliseconds, but Visual FoxPro always rounds to the nearest second. Unlike ADI index keys, VFP TimesStamp index keys do not contain the millisecond portion of the value. |
| Character NoCPTrans | 1 to 65534 | N/A | Fixed-length character field that is stored entirely in the table. The NoCPTrans (binary) option indicates that ANSI/OEM translations will not be performed on the data. Note that if you want the table to be compatible with Visual FoxPro, you should limit the field length to 254 or less. |
| Autoinc | 4 | N/A | 4-byte read-only positive integer value from 0 to 4,294,967,296 that is unique for each record in the table. A starting value and the increment value can be supplied when creating the table. |
| Memo NoCPTrans | 4 | N/A | Variable-length memo field containing character data. The size of each field is limited to 4 GB. The NoCPTrans (binary) option indicates that the ANSI/OEM translations will not be performed on the data. |
| Varchar | 1 to 254 | N/A | This field type allows variable length character data to be stored up to the maximum field length, which is specified when the table is created. It is similar to a character field except that the exact same data will be returned when it is read without extra blank padding on the end. |
| Varchar NoCPTrans | 1 to 254 | N/A | This is the same as a VarChar except that no ANSI/OEM translations will be performed on the data. |
| Varbinary | 1 to 254 | N/A | Variable length binary data. The maximum length of data that can be stored in the field is specified when the table is created. |
| NChar | 1 to 32500 | N/A | Fixed length Unicode character field that is stored entirely in the table. The length specified for the field is the number of UTF16 code units or characters. The internal storage uses UTF16 encoding so the number of bytes occupied by the field in each record is 2 times the specified length. |
| NVarChar | 1 to 32500 | N/A | Variable length Unicode character data. The field is stored entirely in the table. The maximum length of the data that can be stored in the field is specified when the table is created. The internal storage uses UTF16 encoding so the number of bytes occupied by the field in each record is 2 times the specified length plus 2 bytes for the length. |
| NMemo | 9 | N/A | Variable length Unicode memo field. The maximum length of data that can be stored in the field is 4GB. Since UTF16 is used as the internal storage, the number of UTF16 code units is limited to 2G. The data is stored in a separate file, called a memo file. |
| LongInt | 8 | N/A | 8-byte long integer values from -9,223,372,036,854,775,807 to 9223372036854775807. This type is supported in DBF file formats but not index-able in NTX format |
| GUID | 16 | N/A | 16-byte raw data representing a GUID. This type is supported in DBF file formats but not index-able in NTX format. |

Note When creating Visual FoxPro (VFP) tables, you can specify that a specific field allows NULL values. To do this, include "NULL" in the table creation string. If it is for an Advantage Client Engine API such as AdsCreateTable, include it as an additional comma delimited item. The same can be done with the NoCPTrans option. For example, the table creation string "c,char,10,null,nocptrans; i,integer,null;" specifies a table with two fields that can hold NULL values and with no codepage translations performed on the character field. With SQL, the options are provided after the field type. The equivalent SQL field definition would be "(c char(10) null nocptrans, i integer null )".