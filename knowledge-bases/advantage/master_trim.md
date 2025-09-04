TRIM()




Advantage Database Server 12  

TRIM()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TRIM()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - TRIM() Advantage Concepts master\_Trim Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TRIM()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that removes trailing spaces from a character string. The [SQL version](master_trim_sql_scalar.htm) can optionally trim a specific string from another string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

Navigational:

 TRIM(<cString>) à cTrimString

 

SQL:

 TRIM( [[ LEADING | TRAILING | BOTH [ str1 ] FROM ] | [ str1 FROM ]] cString )

 

Parameters

|  |  |
| --- | --- |
| <cString> | The character string to be copied without trailing spaces. |
| <str1> | Optional string to trim from cString (as opposed to space characters). |

Return Values

A copy of the given string with characters trimmed.

Remarks

The navigational version of TRIM and the SQL version differ in semantics.

Navigational:

When TRIM() is used in a navigational environment (e.g., when setting filters directly on a table), it behaves the same as RTRIM().  It removes trailing spaces from the string.

SQL:

When TRIM() is used in SQL statements, it can be used in a number of different forms.  An important difference from the navigational version is that the default behavior of TRIM() with SQL is to remove both leading and trailing spaces like ALLTRIM(). The behavior can be controlled with the alternative forms of the syntax.

Note If trim functions are used in an index expression for the purposes of optimizing SQL statements, the LTRIM, RTRIM, and ALLTRIM scalars should be used.  When TRIM() is used in SQL statements, it will not be optimized by indexes.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[PAD()](master_pad.htm)

[RTRIM()](master_rtrim.htm)

[LTRIM()](master_ltrim.htm)

[ALLTRIM()](master_alltrim.htm)

[SUBSTR()](master_substr.htm)

[SQL TRIM()](master_trim_sql_scalar.htm)