2215 Invalid options in CREATE TABLE statement




Advantage Database Server 12  

2215 Invalid options in CREATE statement

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2215 Invalid options in CREATE statement  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2215 Invalid options in CREATE statement Advantage Error Guide error\_2215\_invalid\_options\_in\_create\_table\_statement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2215 Invalid options in CREATE statement  Advantage Error Guide |  |  |  |  |

An invalid option is specified in the CREATE statement. The error text should contain more information about the specific error. For example: the following CREATE TABLE statement returns the error because it specified both options to create a temporary table and a database table.

CREATE TABLE #Table1 ( id integer, name char(20) ) IN DATABASE

The # prefix before the table name specifies that the table is a temporary table while the IN DATABASE clause specifies that the table should be added into the data dictionary. An error is returned because the two options are mutually exclusive.

The error may also be returned when invalid options are specified in a CREATE INDEX, a CREATE FUNCTION, a CREATE PACKAGE statement or other CREATE statement.