STR()




Advantage Database Server 12  

STR()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| STR()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - STR() Advantage Concepts master\_Str Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| STR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a numeric expression to a character string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes (the 3 parameter version is supported in SQL) |
| Supported in Navigational: | Yes |

Syntax

STR(<nNumber>, [<nLength>], [<nDecimals>]) à cNumber

Parameters

|  |  |
| --- | --- |
| <nNumber> | The numeric expression to be converted to a character string. |
| <nLength> | The length of the character string to return, including decimal digits, decimal point, and sign. |
| <nDecimals> | The number of decimal places to return. |

Return Values

STR() returns <nNumber> formatted as a character string. If the optional length and decimal arguments are not specified, STR() returns the character string according to the following rules:

Results of STR() when optional nLength and nDecimals arguments are not specified:

|  |  |
| --- | --- |
| Expression | Return Value Length |
| Field Variable | Field length plus decimals (Note: This is Clipper-compatible, but differs from the FoxPro standard. FoxPro defaults to a length of 10 for fields if the nLength value is not specified) |
| Expressions/constants | Minimum of 10 digits plus decimals |
| VAL() | Minimum of 3 digits |
| MONTH()/DAY() | 3 digits |
| YEAR() | 5 digits |
| RECNO() | 7 digits |

Remarks

STR() is a numeric conversion function that converts numeric values to character strings. It is commonly used to concatenate numeric values to character strings. STR() has applications displaying numbers, creating codes such as part numbers from numeric values, and creating index keys that combine numeric and character data.

The inverse of STR() is VAL(), which converts character numbers to numerics.

Note If <nLength> is less than the number of whole number digits in <nNumber>, STR() returns asterisks instead of the number.

 

Note If <nLength> is less than the number of decimal digits required for the decimal portion of the returned string, the number is rounded to the available number of decimal places.

 

Note If <nLength> is specified but <nDecimals> is omitted (no decimal places), the return value is rounded to an integer.

See Also

[TRANSFORM()](master_transform.htm)

[VAL()](master_val.htm)