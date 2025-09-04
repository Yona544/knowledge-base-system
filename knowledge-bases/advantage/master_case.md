CASE




Advantage Database Server 12  

CASE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CASE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - CASE Advantage SQL Engine master\_Case Advantage SQL > Supported SQL Grammar > CASE / Dear Support Staff, |  |
| CASE  Advantage SQL Engine |  |  |  |  |

The CASE expression evaluates a list of conditions and returns one value from multiple possible result expressions. The CASE expressions let you use IF ... THEN ... ELSE logic in SQL statements.

CASE has two formats:

|  |  |
| --- | --- |
| · | The simple CASE function compares an expression to a set of simple expressions to determine the result. |

|  |  |
| --- | --- |
| · | The searched CASE function evaluates a set of Boolean expressions to determine the result. |

Both formats support an optional ELSE argument.

Syntax

The BNF syntax of CASE expression can be found in [Advantage SQL Grammar](master_advantage_sql_grammar.htm).

Simple CASE function:

CASE input\_expression

 WHEN when\_expression THEN result\_expression

 [ ...n ]

 [ELSE else\_result\_expression]

END

 

Searched CASE function:

CASE

 WHEN Boolean\_expression THEN result\_expression

 [ ...n ]

 [ELSE else\_result\_expression]

END

 

Arguments

input\_expression is the expression evaluated when using the simple CASE format. input\_expression can be any valid Advantage SQL expression.

when\_expression is the expression to which input\_expression is compared when using the simple CASE format. when\_expression can be any valid Advantage SQL expression. The data types of the input\_expression and each when\_expression must be the same or must be an implicit conversion.

...n is a placeholder indicating that multiple WHEN Boolean\_expression THEN result\_expression, or multiple WHEN when\_expression THEN result\_expression clauses can be used.

result\_expression is the expression whose value is to be the result of the CASE expression when the input\_expression equals the when\_expression, or when the Boolean\_expression evaluates to TRUE. result\_expression can be any valid Advantage SQL expression.

else\_result\_expression is the value to be returned if no Boolean\_expression evaluates to TRUE or no when\_expression equals the input\_expression. If this argument is omitted and no comparison operation evaluates to TRUE, CASE returns NULL. the else\_result\_expression can be any valid Advantage SQL expression.

Boolean\_expression is the expression evaluated using the searched CASE format. Boolean\_expression can be any valid Boolean expression.

 

Result Types

Returns the highest precedence type from the set of types in result\_expression and the optional else\_result\_expression. The data types of all result\_expression and the else\_result\_expression must be either identical or compatible.

Result Values

Simple CASE function:

|  |  |
| --- | --- |
| · | Evaluates the input\_expression |

|  |  |
| --- | --- |
| · | In the order specified, compare the input\_expression with the when\_expression for each WHEN clause. |

|  |  |
| --- | --- |
| · | Returns the value of the result\_expression of the first WHEN clause where the input\_expression equals the when\_expression. |

|  |  |
| --- | --- |
| · | If no value is returned from any WHEN clauses, the value of the else\_result\_expression is returned if the ELSE clause is specified. If there is no ELSE clause, NULL is returned. |

Searched CASE function:

|  |  |
| --- | --- |
| · | Evaluates, in the order specified, the Boolean\_expression for each WHEN clause. If the Boolean\_expression evaluates to TRUE, the value of the result\_expression is returned. |

|  |  |
| --- | --- |
| · | If no Boolean\_expression evaluates to TRUE, the value of the else\_result\_expression is returned if the ELSE clause is specified. If there is no ELSE clause, NULL is returned. |

Examples

A. Use a SELECT statement with a simple CASE function

This example uses the CASE function to alter the display of the marriage status of the employees to make them more understandable.

SELECT Lastname + firstname As "Employee Name",

CASE married

WHEN True THEN 'Married'

WHEN False THEN 'Single'

ELSE 'Not yet known'

END As "Marital status"

FROM Employee

WHERE DateOfBirth >= '1970-03-31'

ORDER BY 2

 

Here is the result set:

Employee Name Marital Status

------------------- -------------------------

Smith John Married

Coles Becky Not yet known

Holmes Monique Single

Brown Terry Single

 

B. Use a SELECT statement with a searched CASE function

This example displays the current vacation earning schedule of the employees based on how long the employee has been working for the company.

SELECT Lastname + firstname As "Employee Name",

 CASE

   WHEN TimestampDiff( SQL\_TSI\_YEAR, CURR\_DATE(), DateOfHire ) >= 10 THEN 7

   WHEN TimestampDiff( SQL\_TSI\_YEAR, CURR\_DATE(), DateOfHire ) >= 5 THEN 6.66

   ELSE 5

 END As "Vacation Hours Earned This period"

FROM Employee

ORDER BY 2 DESC

 

Here is the result set:

Employee Name Vacation Hours Earned this Period

--------------------- ---------------------------------

Schmidt Kathy 7.00

Wilkins Becky 6.66

Wong Wesley 5

Schmidt Mark 5

See Also

[IIF](master_iif_sql.htm)