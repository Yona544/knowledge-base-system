2191 Invalid Data Type




Advantage Database Server 12  

2191 Invalid Data Type

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2191 Invalid Data Type  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2191 Invalid Data Type Advantage Error Guide error\_2191\_union\_statement\_can\_only\_be\_ordered\_by\_ordinal\_number Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2191 Invalid Data Type  Advantage Error Guide |  |  |  |  |

Problem: The data type of an expression in the SQL statement is not valid in the specified context.

Solution: Use Cast() or Convert() function to force the expression into the required type.

Problem: Incompatible data types are given to the UNION statements, IFNULL, IIF, or CASE expressions. For example: "SELECT 1 FROM system.iota UNION SELECT 'abc' FROM system.iota" will resulted in 2191 error because the integer value in the first SELECT is not compatible with the string value in the second SELECT for the purpose of the UNION. Similarly, "SELECT IIF( bVal, 1, 'abc' ) FROM system.iota" will also return 2191 error.

Solution: Use Cast() or Convert() function to force the expressions into the compatible type.

Note: In version 8.0 and earlier releases, the error 2191 means "UNION statement can only be ordered by ordinal number". The problem and solution for this error are below.

Problem: The combined result set of the UNION statement can be ORDER BY ordinal numbers only. Individual queries in the UNION statement cannot be sorted with the ORDER BY clause. For example, "SELECT lastname, firstname FROM table1 UNION SELECT lastname, firstname FROM table2 ORDER BY lastname" is not valid because the ORDER BY is not specified with ordinal number.

Solution: Adjust the ORDER BY clause in the UNION statement to use ordinal number columns.