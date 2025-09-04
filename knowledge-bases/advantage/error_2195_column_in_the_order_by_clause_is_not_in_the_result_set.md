2195 Column in the ORDER BY clause is not in the result set




Advantage Database Server 12  

2195 Column in the ORDER BY clause is not in the result set

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2195 Column in the ORDER BY clause is not in the result set  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2195 Column in the ORDER BY clause is not in the result set Advantage Error Guide error\_2195\_column\_in\_the\_order\_by\_clause\_is\_not\_in\_the\_result\_set Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2195 Column in the ORDER BY clause is not in the result set  Advantage Error Guide |  |  |  |  |

Problem: In certain cases, the ORDER BY clause cannot contain columns that are not in the result set. Two such cases are: 1) a UNION statement and 2) an ORDER BY clause containing any column that is an expression. For example, "SELECT lastname FROM table1 UNION SELECT lastname FROM table2 ORDER BY 1, firstname" is not valid because the column firstname is not in the result set. "SELECT UCASE( lastname ) FROM table1 ORDER BY 1, firstname" is not valid because the ordinal number 1 in the ORDER BY clause specifies an expression column and firstname column is not in the result set.

Solution: Adjust the ORDER BY clause so it conforms to the restriction.