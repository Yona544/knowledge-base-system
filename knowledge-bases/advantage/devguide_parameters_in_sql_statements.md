Parameters in SQL Statements




Advantage Database Server 12  

     Parameters in SQL Statements

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Parameters in SQL Statements  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Parameters in SQL Statements Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Parameters\_in\_SQL\_Statements Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > Parameters in SQL Statements / Dear Support Staff, |  |
| Parameters in SQL Statements  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A parameterized query is one that includes one or more parameters. A parameter is a placeholder for a value in the WHERE clause of SELECT, UPDATE, or DELETE queries. The value of a parameter does not need to be defined until just before the query is executed by the client application, permitting you to define the query at design time and then customize which records it will affect at runtime.

In addition to permitting you to create customizable query templates, parameterized queries offer potential performance benefits as well. Specifically, if you need to execute a parameterized query more than once, even when one or more of the parameter values change, the query will generally execute faster upon repeated execution.

There are two sources of this performance benefit. The first is that Advantage need only parse and check the syntax of the query the first time it is executed. So long as the SQL statement being executed is unchanged, excluding the values of the parameters, subsequent executions do not need parsing and syntax checking. Second, upon repeated execution of a parameterized query, only the parameter values need to be sent to the server. The remainder of the query does not, having already been sent during a previous execution.

There are two types of parameters that can appear in a parameterized query: named parameters and positional parameters. Named parameters are identified by a placeholder that appears as a text label preceded by a colon. For instance, in the following SQL statement, the parameter is named custparam:

SELECT [City], [State] FROM [CUSTOMER]  
  WHERE [Customer ID] = :custparam

Positional parameters do not have labels. Instead, they are represented by a question mark (?). The following SQL statement is similar to the preceding one, except that it uses a positional parameter rather than a named parameter:

SELECT [City], [State] FROM [CUSTOMER]  
  WHERE [Customer ID] = ?

In order to execute a parameterized query, it is necessary to supply a value for each parameter in the query prior to the execution of the query. How this is done depends on the development environment you are writing your client applications in. Using parameterized queries, and assigning values to parameters at runtime, is described for each of the ADS-supported data access mechanisms in the later chapters of this book. Refer to the chapter that discusses the data access mechanism you want to use for details.