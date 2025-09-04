PADC()




Advantage Database Server 12  

PADC()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| PADC()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - PADC() Advantage Concepts master\_Padc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| PADC()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that pads character, date, and numeric values with a fill character.

|  |  |
| --- | --- |
| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

PADC(<exp>, <nLength>, [<cFillChar>]) à cPaddedString

Parameters

|  |  |
| --- | --- |
| <exp> | A character, numeric, or date value to be padded with a fill character. |
| <nLength> | The length of the character string to be returned. |
| <cFillChar> | The character with which to pad <exp>. If not specified, the default is a space character. |

Return Values

PADC() returns the result of <exp> as a character string padded with <cFillChar> to a total length of <nLength>.

Remarks

PADC() is a character function that pads character, date, and numeric values with a fill character to create a new character string of a specified length. PADC() centers <exp> within <nLength> adding fill characters to the left and right sides. If the length of <exp> exceeds <nLength>, all of the PAD() functions truncate cPaddedString to <nLength>.

PADC() is the inverse of the ALLTRIM(), RTRIM(), and LTRIM() functions which trim leading and trailing space from character strings.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. This function is not supported within SQL statements.

Note Memo, binary, and image fields are not supported in this Advantage Expression Engine function. If memo, binary, or image fields are used with this expression engine function, the Advantage Expression Engine will be unable to evaluate the expression.

See Also

[RTRIM()](master_rtrim.htm)