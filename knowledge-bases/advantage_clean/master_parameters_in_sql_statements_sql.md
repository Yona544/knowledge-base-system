---
title: Master Parameters In Sql Statements Sql
slug: master_parameters_in_sql_statements_sql
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_parameters_in_sql_statements_sql.htm
source: Advantage CHM
tags:
  - master
checksum: 1837eb045cdf0e88376eb4e68191912a961a5158
---

# Master Parameters In Sql Statements Sql

Parameters in SQL Statements

Parameters in SQL Statements

Advantage SQL Engine

| Parameters in SQL Statements  Advantage SQL Engine |  |  |  |  |

Advantage Streamline SQL engine supports unnamed parameters in SQL statements. Named parameters are supported through the Advantage Client Engine API. The main advantage of using parameters in SQL statements is that the statements will be prepared (parsed and semantic verified) once and then different values of the parameters can be used to execute the query many times without needing to prepare the statement again. A sample SQL statement with parameters is the following:

INSERT INTO Table1 VALUES ( ?, ?, ? )

This statement may be prepared once and executed multiple times with different values for the three parameters.

Parameters are also useful for avoiding the issue of incompatible date, time, and currency format in different regions in the world. For example, instead of formatting a date value into a standard format string that the SQL engine recognizes, a parameter can be used to set the date value directly. For example,

UPDATE Table1 SET date\_column = '1999-12-01'

The above statement requires the string value in the ANSI standard date format. Using a parameter, the statement can be written as

UPDATE Table1 SET date\_column = ?

Then the date value of the parameter may be set using the API specific to individual client development environment.

However, there are several issues that need to be kept in mind when using parameters in SQL statements.

Data Type and Precision

Because the data type and precision of a parameter is not known until the query is executed, the SQL engine uses the following rules to determine the data type and precision of the parameter during query preparation. If the data type and precision of the parameter cannot be determined using the rules, a 2123 (ERR\_UNKNOWNTYPE) will be returned.

| 1. | If a parameter is used in a binary algebraic or Boolean expression, and one side of the expression is a parameter, then the data type, precision, and scale of the parameter will be set to be the same as the data type, precision and scale of the other side of the expression in general, except when the data type is character. When the data type is character, the parameter will have a minimum precision of 1024. If the expression is unary or if both side of the expression are parameters, then the data type cannot be determine and an error will be returned. A sample statement that will lead to this error is "SELECT \* FROM table1 WHERE id = - ?". In this case, the parameter is used in an unary expression. If the implied data type, precision, or scale is not the desired value, or if the query engine cannot determine the data type of the parameter, the Cast() and Convert() scalar functions can be used to force the parameter into the desired data type, precision or scale. |

| 2. | If a parameter is used as an argument to a scalar function, the data type of the parameter will be set to be the same data type specified for the argument. |

| .b. | If the argument can be different numeric data types (integer, numeric or double), the double data type will generally be used. |

| .c. | If the arguments data type is a precision numeric data type other than integer, the parameters data type will be precision numeric data type with precision of 15 and scale of 4. |

| .d. | If the arguments data type is character, the parameters data type will be character with precision 1024. |

| .e. | If the argument may be date, time, or timestamp, the parameters data type will be timestamp. |

| .f. | The CAST and CONVERT scalar function can be used to cast the parameter into the specific data type and precision. |

| .g. | Several scalar functions do not currently support implicit data type assignment of parameters. These include TimestampAdd, TimestampDiff, Week, Case, Coalesce, Ifnull, and Isnull. When parameters are to be used in these functions, the type of the parameters must be set explicitly using the Cast scalar function. |

In general, if the parameters data type cannot be determined implicitly by the SQL engine, or if a specific data type is needed in case of multiple compatible data types, the CAST scalar function can be used to force the parameter into a specific data type during query preparation. The following example uses the Cast scalar to calculate the Round of a precision numeric value:

SELECT Round( Cast( ? AS SQL\_MONEY ), 2 ) FROM system.iota

The column in the result set will be the money type a precision numeric data. A similar example without the Cast will result in a column of the double type an approximated numeric data:

SELECT Round( ?, 2 ) FROM system.iota

Since the precision of the parameter is determined at the preparation time, a data truncation error will be returned if the value supplied for the parameter is longer than the precision of the parameter.

Optimization

Currently, Advantage SQL engine determines the query execution plan during the query preparation time. The query execution plan is very dependant on the restriction in the WHERE clause of the SQL statement. If there are parameters in the WHERE clause, and since the actual parameter values are not known at the preparation time, the SQL engine will use a heuristic to determine the optimal execution plan, specifically which tables will be used as the driver tables during query execution. The heuristic used at query preparation time may not lead to the most optimal execution plan depending on the actual parameter values supplied at query execution time.

This optimization issue will only affect queries that involve more than one table. Therefore, it only affects SELECT queries.

If using parameters in the WHERE clause of an SQL statement generates a less than optimal query execution plan, the problem can be avoided by using the actual values in the SQL statement (as opposed to parameters).
