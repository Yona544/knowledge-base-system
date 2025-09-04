I2BIN()




Advantage Database Server 12  

I2BIN()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| I2BIN()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - I2BIN() Advantage Concepts master\_I2bin Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| I2BIN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts an integer numeric value to a character string formatted as a binary integer.

|  |  |
| --- | --- |
| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

I2BIN( <nInteger> ) à cBinaryInteger

Parameters

|  |  |
| --- | --- |
| <nInteger> | An integer numeric value to be converted. Decimal digits are truncated. |

Return Values

I2BIN() returns a two-byte character string containing a 16-bit binary integer.

Remarks

I2BIN() is a low-level file function that converts an integer numeric value to a character string formatted as a binary integerleast significant byte first.

See Also

[CHR()](master_chr.htm)

[L2BIN()](master_l2bin.htm)