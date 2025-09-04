2121 Column not found




Advantage Database Server 12  

2121 Column not found

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2121 Column not found  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2121 Column not found Advantage Error Guide error\_2121\_column\_not\_found Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2121 Column not found  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine could not find a specified column. For example, a SELECT statement referred to a column that does not exist.

Solution: Verify that the columns referenced in the SQL statement all exist in the table. Also verify that you are using the correct alias on column names. For example, if you use an alias on a table name, you must use that alias with the column name rather than the table name. Example: "SELECT a.field FROM mytable a". The alias "a" is used on "mytable". "SELECT mytable.field FROM mytable a" is not correct.