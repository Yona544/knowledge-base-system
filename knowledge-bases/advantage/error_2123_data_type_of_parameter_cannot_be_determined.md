2123 Data type of parameter cannot be determined




Advantage Database Server 12  

2123 Data type of parameter cannot be determined

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2123 Data type of parameter cannot be determined  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2123 Data type of parameter cannot be determined Advantage Error Guide error\_2123\_data\_type\_of\_parameter\_cannot\_be\_determined Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2123 Data type of parameter cannot be determined  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine was not able to determine the data type of a parameter within the query. See [Parameters in SQL Statements](master_parameters_in_sql_statements_sql.htm) for more information.

Solutions:

|  |  |
| --- | --- |
| 1. | Make sure you do not have a query of the form "SELECT \* FROM mytable where ? = ?". One of the parameters must be specified so that the data type can be determined. |

|  |  |
| --- | --- |
| 2. | Use the Cast scalar function to explicitly specify the data type of the parameter. |