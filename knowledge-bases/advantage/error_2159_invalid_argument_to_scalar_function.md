2159 Invalid argument to scalar function




Advantage Database Server 12  

2159 Invalid argument to scalar function

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2159 Invalid argument to scalar function  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2159 Invalid argument to scalar function Advantage Error Guide error\_2159\_invalid\_argument\_to\_scalar\_function Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2159 Invalid argument to scalar function  Advantage Error Guide |  |  |  |  |

Problem: An SQL statement specified an incorrect argument for a scalar function.

Solution: Refer to the [Advantage SQL](master_advantage_sql_engine.htm) documentation for information about the scalar function you are trying to use.

Problem: A parameter is used in an SQL scalar function that supports multiple data types. For example, the IIF() and ISNULL() may take different data types as input and return as output different types of values. If the query engine was not able to determine the type of the parameter, the 2159 error will be returned. A sample statement that may return 2159 error is "SELECT IIF( id = 1, :param1, :param2 ) FROM table1". The query engine is not able to determine the type of the resulting column until the execution time and will return 2159 error instead.

Solution: Use explicit CAST() or CONVERT() on the parameter(s) so there is no ambiguity to the data type. The above sample statement may be changed to the following to avoid the error: "SELECT IIF( id = 1, CAST( :param1 AS SQL\_CHAR(20)), :param2 AS SQL\_CHAR(20))) FROM table1".