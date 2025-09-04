TRANSFORM()




Advantage Database Server 12  

TRANSFORM()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TRANSFORM()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - TRANSFORM() Advantage Concepts master\_Transform Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TRANSFORM()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts any value into a formatted character string.

|  |  |
| --- | --- |
| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

TRANSFORM(<exp>, <cSayPicture>) à cFormatString

Parameters

|  |  |
| --- | --- |
| <exp> | The value to be formatted. This expression can be any valid data type except array, code block, and NIL. |
| <cSayPicture> | A string of picture and template characters that describes the format of the returned character string. |

Return Values

TRANSFORM() converts <exp> to a formatted character string as defined by <cSayPicture>.

Remarks

TRANSFORM() is a conversion function that formats character, date, logical, and numeric values according to a specified picture string that includes a combination of picture function and template strings.

A picture function string specifies formatting rules that apply to the TRANSFORM() return value as a whole, rather than to particular character positions within <exp>. The function string consists of the @ character, followed by one or more additional characters, each of which has a particular meaning (see table below). If a function string is present, the @ character must be the leftmost character of the picture string, and the function string must not contain spaces. A function string may be specified alone or with a template string. If both are present, the function string must precede the template string, and the two must be separated by a single space.

TRANSFORM() Functions

Function Action

 

B Displays numbers left-justified

C Displays CR after positive numbers

D Displays date in TAdsSettings.DateFormat format

E Displays date in British format

R Nontemplate characters are inserted

X Displays DB after negative numbers

Z Displays zeros as blanks

( Encloses negative numbers in parentheses

! Converts alphabetic characters to uppercase

 

A picture template string specifies formatting rules on a character-by-character basis. The template string consists of a series of characters, some of which have special meanings (see table below). Each position in the template string corresponds to a position in the value of the <exp> argument. Because TRANSFORM() uses a template, it can insert formatting characters such as commas, dollar signs, and parentheses.

Characters in the template string that have no assigned meaning are copied literally into the return value. If the @R picture function is used, these characters are inserted between characters of the return value; otherwise, they overwrite the corresponding characters of the return value. A template string may be specified alone or with a function string. If both are present, the function string must precede the template string, and the two must be separated by a single space.

TRANSFORM() Templates

Template Action

 

A,N,X,9,# Displays digits for any data type

L Displays logicals as "T" or "F"

Y Displays logicals as "Y" or "N"

! Converts an alphabetic character to uppercase

$ Displays a dollar sign in place of a leading

space in a numeric

\* Displays an asterisk in place of a leading space

in a numeric

. Specifies a decimal point position

, Specifies a comma position

Note This function is not supported as an SQL scalar.

Note Memo, binary, and image fields are not supported in this Advantage Expression Engine function. If memo, binary, or image fields are used with this expression engine function, the Advantage Expression Engine will be unable to evaluate the expression.

Example

This example formats a number into a currency format using a template:

TRANSFORM(123456, "$999,999") // Result: $123,456

This example formats a character string using a function:

TRANSFORM("to upper", "@!") // Result: TO UPPER

See Also

[PAD()](master_pad.htm)

[STR()](master_str.htm)

[UPPER()](master_upper.htm)