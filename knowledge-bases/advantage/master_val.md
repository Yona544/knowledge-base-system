VAL()




Advantage Database Server 12  

VAL()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| VAL()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - VAL() Advantage Concepts master\_Val Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| VAL()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a character number to numeric type.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

VAL(<cNumber>) à nNumber

Parameters

<cNumber> The character expression to be converted.

Return Values

VAL() returns <cNumber> converted to a numeric value including decimal digits.

Remarks

VAL() is a character conversion function that converts a character string containing numeric digits to a numeric value. When VAL() is executed, it evaluates <cNumber> until a second decimal point, the first non-numeric character, or the end of the expression is encountered. Leading spaces are ignored. As with all other functions that round, digits between zero and four are rounded down, and digits between five and nine are rounded up.

VAL() is the opposite of STR() and TRANSFORM(), which convert numeric values to character strings.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[ROUND()](master_round.htm)

[STR()](master_str.htm)

[TRANSFORM()](master_transform.htm)