ADT Field Types and Specifications




Advantage Database Server 12  

ADT Field Types and Specifications

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADT Field Types and Specifications  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ADT Field Types and Specifications Advantage Concepts master\_Adt\_field\_types\_and\_specifications Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADT Field Types and Specifications  Advantage Concepts |  |  |  |  |

The following are the field data types available in ADT tables. Note that the length and format of some fields are different than their DBF table equivalents. The following data types that are available in DBF tables are not available in ADT tables: ShortDate, General, and Picture.

|  |  |  |  |
| --- | --- | --- | --- |
| Type | Length | Available in DBF Table | Description |
| Character | 1 to 65530 | Yes | Fixed-length character field that is stored entirely in the table. |
| CICharacter | 1 to 65530 | No | Case insensitive fixed-length character field that is stored entirely in the table. |
| Date | 4 | Yes | 4-byte integer containing a Julian date. |
| Logical | 1 | Yes | 1-byte logical (Boolean) field. Recognized values for True are 1, T, t, Y, and y. |
| Memo | 9 (No compression)  16 (Compressed) | Yes | Variable-length memo field containing character data. The size of each field is limited to 4 GB. The memo data is actually stored in a separate file, called a memo file, to reduce table bloat. The data stored in this field type may be optionally compressed. |
| Double | 8 | VFP, Extended | 8-byte IEEE floating point value in the range 1.7E +/-308 (15 digits of precision). The decimal value affects the use of the field in expressions. It does not affect the precision of the stored data. If the length is given, it will be ignored. For example, "salary, double, 10, 2" and "salary, double, 2" produce the same field. |
| Integer | 4 | VFP, Extended | 4-byte integer values from --2,147,483,647 to 2,147,483,647. |
| LongInt | 8 | Yes | 8-byte long integer values from -9,223,372,036,854,775,807 to 9223372036854775807. This type is  supported in DBF file formats but not index-able in NTX format. |
| Numeric | 2 to 32 (Decimal: 0 to Length-2) | Yes | Fixed-length (exact ASCII representation) numeric. One byte is reserved for the sign of the numeric value. If the decimal value is not zero, one additional byte is used for the decimal point. |
| Image | 9 | Extended | Variable-length memo field containing binary image data. The size of each field is limited to 4 GB. The binary image data is actually stored in a separate file, called a memo file, to reduce table bloat.  If using the Advantage CA-Visual Objects RDDs, Advantage Client Engine APIs must be used to set and retrieve the image data. |
| Binary | 9 (No compression)  16 (Compressed) | VFP, Extended | Variable-length memo field containing binary data. The size of each field is limited to 4 GB. The binary data is actually stored in a separate file, called a memo file, to reduce table bloat. The data stored in this field type may be optionally compressed.  If using the Advantage CA-Visual Objects RDDs, Advantage Client Engine APIs must be used to set and retrieve the binary data. |
| ShortInt | 2 | No | 2-byte short integer value from -32,767 to 32,767. |
| Time | 4 | No | 4-byte integer internally stored as the number of milliseconds since midnight. |
| TimeStamp | 8 | VFP | 8-byte value where the high order 4 bytes are an integer containing a Julian date, and the low order 4 bytes are internally stored as the number of milliseconds since midnight. If using the Advantage CA-Visual Objects RDDs, this is a string type. |
| AutoIncrement | 4 | VFP | 4-byte read-only positive integer value from 0 to 4,294,967,296 that is unique for each record in the table. |
| Raw | 1 to 65530 | No | Fixed-length, data-typeless raw data field. If using the Advantage CA-Visual Objects RDDs, Advantage Client Engine APIs must be used to set and retrieve the raw data. |
| GUID | 16 | Yes | 16-byte raw data representing a GUID. |
| CurDouble | 8 | No | Currency data stored internally as an 8-byte IEEE floating-point value in the range 1.7E +/-308 (15 digits of precision). The decimal value affects the use of the field in expressions. It does not affect the precision of the stored data. If the length is given, it will be ignored. For example, "salary, CurDouble, 10, 2" and "salary, CurDouble, 2" produce the same field. |
| Money | 8 | VFP | Currency data stored internally as a 64-bit integer, with 4 implied decimal digits from -922,337,203,685,477.5807 to +922,337,203,685,477.5807. The Money data type will not lose precision. |
| ModTime | 8 | No | 8-byte value where the high order 4 bytes are an integer containing a Julian date, and the low order 4 bytes are internally stored as the number of milliseconds since midnight. If using the Advantage CA-Visual Objects RDDs, this is a string type. The value of this field is automatically updated with the current date and time each time a record is updated. |
| RowVersion | 8 | No | An 8-byte unsigned integer unique for each record in the table that is automatically incremented each time a record is updated. |
| VarChar | 1 to 65000 | VFP | This field type allows variable length character data to be stored up to the maximum field length, which is specified when the table is created. It is similar to a character field except that the exact same data will be returned when it is read without extra blank padding on the end. If you are creating this field using the Advantage Client Engine API directly (e.g., AdsCreateTable), you must specify the type as "VarCharFox" to avoid legacy compatibility issues with an older obsolete varchar field type. |
| VarBinary | 1 to 65000 | VFP | Variable length binary data. The maximum length of data that can be stored in the field is specified when the table is created. This is similar to the Raw field type except that the true length of the data is stored internally in the record. |
| NChar | 1 to 32500 | Yes | Fixed length Unicode character field that is stored entirely in the table. The length specified for the field is the number of UTF16 code units or characters. The internal storage uses UTF16 encoding so the number of bytes occupied by the field in each record is 2 times the specified length. |
| NVarChar | 1 to 32500 | Yes | Variable length Unicode character data. The field is stored entirely in the table. The maximum length of the data that can be stored in the field is specified when the table is created. The internal storage uses UTF16 encoding so the number of bytes occupied by the field in each record is 2 times the specified length plus 2 bytes for the length. |
| NMemo | 9 (No compression)  16 (Compressed) | Yes | Variable length Unicode memo field. The maximum length of data that can be stored in the field is 4GB. Since UTF16 is used as the internal storage, the number of UTF16 code units is limited to 2G. The data is stored in a separate file, called a memo file. The data stored in this field type may be optionally compressed. |

Note The Memo, Binary, and NMemo field types may optionally stored data compressed to reduce size of the memo file. To specify the field to be compressed using the Advantage Client Engine API such as AdsCreateTable, include the option "COMPRESSED" as an additional comma delimited item. For example, the table creation string "i,integer;m,memo,compressed;" specifies a table with a integer field and a memo field that stores the data in compressed format. With SQL, the option is provided after the field type. The equivalent SQL CREATE TABLE statement would be "CREATE TABLE x ( i integer, m memo compressed )".