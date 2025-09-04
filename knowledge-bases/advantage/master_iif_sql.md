IIF




Advantage Database Server 12  

IIF

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IIF  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - IIF Advantage SQL Engine master\_Iif\_sql Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| IIF  Advantage SQL Engine |  |  |  |  |

The IIF scalar evaluates a boolean expression and returns one of two possible result expressions. The IIF lets you use IF ... THEN ... ELSE logic in SQL statements.

Syntax

IIF ( <boolean\_expression> , <true\_expression> , <false\_expression> )

Parameters

|  |  |
| --- | --- |
| <boolean\_expression> | A boolean expression that evaluates to true or false. |
| <true\_expression> | An expression or value to be returned when <boolean\_expression> is true. |
| <false\_expression> | An expression or value to be returned when <boolean\_expression> is false. |

Return Values

When <boolean\_expression> evaluates to true then the evaluation of <true\_expression> is returned. Conversely, when <boolean\_expression> evaluates to false then the evaluation of <false\_expression> is returned.

Remarks

IIF() is a logical conversion function. It provides a mechanism to evaluate a condition within an SQL statement. With this ability you can convert a logical expression to another data type. The true and false expressions must be of compatible types. Similarly the IIF return value must be compatible within the encompassing SQL statement.

Examples

A. Simple data type conversion using IIF

SELECT name, IIF ( married = TRUE, 'Married', 'Not Married' ) FROM employees

B. Calculate the difference between the number of married persons and the number of unmarried persons.

SELECT SUM( IIF( married = TRUE, 1, -1 )) FROM employees

See Also

[CASE()](master_case.htm)