ISNULL()




Advantage Database Server 12  

ISNULL()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ISNULL()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ISNULL() Advantage Concepts master\_Isnull Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ISNULL()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that determines if the result of an expression is NULL.

|  |  |
| --- | --- |
| Supported in SQL: | No Use alternative syntax:   <field> IS NULL |
| Supported in Navigational: | Yes |

Syntax

ISNULL(<exp>) à lNull

Parameters

<exp>  An expression of any data type.

Return Values

This function returns True if the given expression evaluates to NULL; it returns False otherwise.

Remarks

For ADT tables, this function is equivalent to [EMPTY()](master_empty.htm). For CDX and NTX table types, this function will always return False because those table types do not support NULL values. For Visual FoxPro (VFP) tables, this returns True if the given expression evaluates to a NULL value; it returns False otherwise (even if the result evaluates to an empty value). NULL and empty are not equivalent when dealing with VFP tables.

See Also

[EMPTY()](master_empty.htm)