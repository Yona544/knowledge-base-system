2145 Unable to ORDER BY this column




Advantage Database Server 12  

2145 Unable to ORDER BY this column

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2145 Unable to ORDER BY this column  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2145 Unable to ORDER BY this column Advantage Error Guide error\_2145\_unable\_to\_order\_by\_this\_column Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2145 Unable to ORDER BY this column  Advantage Error Guide |  |  |  |  |

This error is returned when the SQL engine is not able to supported the ORDER BY clause of the SQL statement. The following are some possible causes and solutions.

Problem: If the ORDER BY is used in a SELECT statement that defines a cursor in an SQL script, or that is a value subquery, then there are additional restriction on the columns in the ORDER BY  clause. For example, the column cannot be from a system table.

Solution: Use table expression to create an intermediate result set and then SELECT ... ORDER BY... on the intermediate result.

Example:

// This script returns 2145 error

DECLARE Columns CURSOR AS

       SELECT \*

       FROM System.Columns

       WHERE field\_default\_value is not null

       ORDER BY [Parent];

OPEN Columns;

// Rewrite to this to avoid error

DECLARE Columns CURSOR AS

       SELECT \* FROM

          ( SELECT \*

            FROM System.Columns

            WHERE field\_default\_value is not null ) t

       ORDER BY [Parent];

OPEN Columns;

Problem: The ORDER BY clause contained a column that cannot be ordered (e.g., memo, binary, or character field longer than 1024 characters).

Solution: Use only fixed-length fields that are 1024 characters or less in the ORDER BY clause.