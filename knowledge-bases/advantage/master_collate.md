COLLATE()




Advantage Database Server 12  

COLLATE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| COLLATE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - COLLATE() Advantage Concepts master\_Collate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| COLLATE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function used to coerce a string value to a specific column-level collation language.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

Navigational Syntax:

COLLATE( <cString>, <collation\_lang> ) -> <cString>

 

SQL Syntax:

<cstring> COLLATE <collation\_lang> -> <cString>

 

Parameters

|  |  |
| --- | --- |
| <cString> | The character string to coerce. |
| <collation\_lang> | The column-level collation language to coerce to. |

Return Values

COLLATE returns the string value <cString> with its coercion type changed to COERCION\_EXPLICIT and its collation language changed to <collation\_lang).

Remarks

<collation\_lang> can be one of the following values, and must be surrounded by single quotes:

|  |  |
| --- | --- |
| ads\_default\_cs | case sensitive |
| ads\_default\_ci | case insensitive |

When using collate() in navigational access, the <collation\_lang> must be a string literal with one of the values above. If it is not a string literal or not one of the values above, an 3x25 error may be returned.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

Example

Navigational:

collate( csfield, ads\_default\_ci )

SQL:

SELECT \* FROM table WHERE field collate ads\_default\_ci = 'value';

See Also

[Comparison Operators and Coercion](master_case_insensitive_field_type.htm#comparison_operators_and_coercion)