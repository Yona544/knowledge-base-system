2196 Column not found in GROUP BY clause




Advantage Database Server 12  

2196 Column not found in GROUP BY clause

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2196 Column not found in GROUP BY clause  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2196 Column not found in GROUP BY clause Advantage Error Guide error\_2196\_column\_not\_found\_in\_group\_by\_clause Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2196 Column not found in GROUP BY clause  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine expected to find the specified column in the GROUP BY clause.

Solution: If you use an aggregate function and a non-aggregated column name in a SELECT statement, then you must use a GROUP BY clause. For example, an application will get this error if it executes this statement: "SELECT lastname, COUNT(lastname) FROM employee".

The statement must also include the clause "GROUP BY lastname". In addition, if a GROUP BY clause is used, then every column that is not in an aggregate function in the SELECT list must be included in the GROUP BY clause.