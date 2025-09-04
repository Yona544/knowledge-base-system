SQL Literals




Advantage Database Server 12  

SQL Literals

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Literals  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - SQL Literals Advantage SQL Engine master\_Sql\_literals Advantage SQL > Supported SQL Grammar > SQL Literals / Dear Support Staff, |  |
| SQL Literals  Advantage SQL Engine |  |  |  |  |

The following types of literals (constant values) can be used in Advantage SQL statements.

Character String

A sequence of characters enclosed in single quotes. In versions 7.0 and earlier, the maximum length of a string literal is 1024. In versions 7.1 and later, there is no specific limit on character literal length; they can be arbitrarily long. To represent a single quote itself within a character string literal, use two adjacent single quotes (e.g., 'Mark''s text'). Note that character string literals cannot be enclosed in double quotes; those are reserved for delimiting identifiers such as field or table names that have non-standard characters or are reserved keywords.

Numeric

A sequence of digits proceeded by an optional sign (+/-) and with an optional decimal point. In addition, scientific notation can be used. The following are examples of valid numeric literals: 7, 3.14159, -5, 2.6e-4. Note that the decimal point must be represented by a period. A comma is not recognized as a valid decimal point.

The numeric literal may be interpreted as either exact numeric or approximate numeric (see [Exact Numeric vs Approximate Numeric](master_exact_numeric_vs_approximate_numeric.htm)) using the following rules:

|  |  |
| --- | --- |
| 1. | Numeric literals in scientific notation are always interpreted approximate numeric. |

|  |  |
| --- | --- |
| 2. | Numeric literals with no decimal point are interpreted as exact numeric Integer type, unless its value exceeds the range supported by a 4-byte integer. When the value exceeds the range of a 4-byte integer, the numeric literal will be interpreted as either an exact numeric Numeric type or an approximate numeric according to rule 3 and 4. |

|  |  |
| --- | --- |
| 3. | If a numeric literal cannot be interpreted as an approximate numeric using rule 1 or an Integer using rule 2, it will be interpreted as an exact numeric Numeric type unless the precision of the numeric literal (number of digits) exceeds the maximum supported numeric precision (i.e., 30 in current implementation). The precision of the exact numeric will be the number of digits in the numeric literal and the scale of the numeric will be the number of digits after the decimal point. |

|  |  |
| --- | --- |
| 4. | All other numeric literals are interpreted as approximate numeric. The internal representation of approximate numeric is IEEE Double. |

For example:

-5, 5, 1000, 1234567890 : Exact numeric Integer

1234567890123, 1.23, -1.000 : Exact numeric Numeric

2.6e-4, 1.234567890123456789012345678901234, 98765432109876543210987654321099 : Approximate numeric Double

How the numeric literal values are written in the SQL statement and interpreted by the SQL engine affects the outcome of the algebraic expression using the numeric literals. If a specific type is desired, the [Convert()](master_miscellaneous_functions.htm#convert) and [Cast()](master_miscellaneous_functions.htm#cast) scalar can be used to obtain the value in the required type. See [Exact Numeric vs Approximate Numeric](master_exact_numeric_vs_approximate_numeric.htm) for more detail.

Logical

Represented by numeric values 0 and 1. In addition, the reserved keywords FALSE and TRUE can be used as aliases for 0 and 1 respectively.

Date

A Date literal may be specified as DATE'YYYY-MM-DD' or simply as 'YYYY-MM-DD', where the string inside the quotes must be conforming to either the ANSI date format, YYYY-MM-DD, or a custom date format specified in the client side application via the "set date format" operation. For example, DATE'1999-12-31' is a valid date literal. Although the DATE prefix is optional, its presence allows the SQL parser and semantic checker to follow a slightly more efficient path. If the prefix is omitted, Advantage SQL engine will interpret the string literal as a date literal depending on the context. For example, if ADateColumn is a date data type column in ATable, this SQL statement, SELECT ... FROM ATable WHERE ADateColumn > '1999-12-31', is valid and the SQL engine will automatically convert the String literal to Date literal. If custom date format is to be used, how to set it depends on the client application. With the Advantage Client Engine API or Advantage OLE DB Provider, the date format for an application can be specified via the AdsSetDateFormat API. With Advantage TDataSet Descendant applications, the date format for an application can be specified via the TAdsSettings.DateFormat property. If the ANSI style format (YYYY-MM-DD) and the format specified through the client's "set date format" operation are in conflict, the ANSI format is assumed. For example, if the client format was 'YYYY-DD-MM', the date '1999-01-22' will be interpreted as January 22, 1999.

Time

A Time literal may be specified as TIME'HH:MM', 'HH:MM', TIME'HH:MM:SS', or 'HH:MM:SS'. Additionally, the 'am' or 'pm' can be included on the end if 12-hour time formats are desired. If the am/pm indicator is not present, it is assumed that the time is in 24-hour format. Although the TIME prefix is optional, it allows the SQL parser and semantic checker to follow a slightly more efficient code path. If the prefix is not present, the Advantage SQL engine will interpret the string literal as a time literal depending on the context. The following are examples of valid time literals: TIME'01:05', '01:05', '10:30 am', TIME'06:25:15 pm', '18:25:15', '14:00'.

Timestamp

A Timestamp literal may be specified as TIMESTAMP'YYYY-MM-DD HH:MM:SS.mmm' or 'YYYY-MM-DD HH:MM:SS.mmm'. The milliseconds, mmm, at the end is optional. The date portion and the time portion may be separated with either a space character or the character 'T'. The time portion of timestamp literals must be in 24-hour time and must include the seconds value. The date portion must conform to either the ANSI date format, YYYY-MM-DD or a custom date format specified in the client side application via the "set date format" operation. Although the TIMESTAMP prefix is optional, its presence allows the the SQL parser and semantic checker to follow a slightly more efficient path. If the prefix is not present, the SQL engine will interpret the string as a Timestamp literal depending on the context. The following are examples of valid timestamp literals: TIMESTAMP'1999-01-22T01:30:00', '1999-01-22 01:30:00', and '2000-12-31 23:59:59.999'.

Binary String Literals

A binary string literal is a series of hexadecimal characters, the digits 0-9 and uppercase and lowercase letters A-F.  Binary string literals must be prefixed with x and contain an even number of hexadecimal characters to the right of the prefix.  Spaces can be inserted between hexadecimal characters to improve readability and will be ignored.  The integer value 42 can be represented with the following binary string literals, x00 00 00 2A or x0000002A.  An unlimited number of characters may follow the x prefix. See [Functions to Convert Hexadecimal Values](master_functions_to_convert_hexadecim.htm).

GUID Literals

A GUID literal may be specified either as a string literal in the "registry format" with or without braces, i.e. 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' or '{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}', or as binary string literals, i.e. x'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'. The SQL engine will interpret the literal values based on the context.