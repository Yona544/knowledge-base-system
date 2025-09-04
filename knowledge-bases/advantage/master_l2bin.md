L2BIN()




Advantage Database Server 12  

L2BIN()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| L2BIN()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - L2BIN() Advantage Concepts master\_L2bin Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| L2BIN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a long integer numeric value to a character string formatted as a 32-bit binary integer.

|  |  |
| --- | --- |
| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

L2BIN( <nLongInteger> ) --> cBinaryInteger

Parameters

|  |  |
| --- | --- |
| <nLongInteger> | A long integer numeric value to be converted. Decimal digits are truncated. |

Return Values

L2BIN() returns a four-byte character string containing a 32-bit binary integer.

Remarks

L2BIN() is a low-level file function that converts a long integer numeric value to a character string formatted as a 32-bit binary integerleast significant byte first.

See Also

[I2BIN()](master_i2bin.htm)

[CHR()](master_chr.htm)