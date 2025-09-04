Overview of Advantage SQL Queries




Advantage Database Server 12  

 

     Overview of Advantage SQL Queries

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Overview of Advantage SQL Queries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Overview of Advantage SQL Queries Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Overview\_of\_Advantage\_SQL\_Queries Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > Overview of Advantage SQL Queries / Dear Support Staff, |  |
| Overview of Advantage SQL Queries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage SQL statements are text-based commands that you use to instruct Advantage to perform some operation. Examples of operations that you can perform with Advantage SQL include creating and destroying (dropping) tables, adding or removing (dropping) indexes, inserting data into a table, deleting records from a table, updating data in one or more records in a table, adding permissions for users or groups, and selecting records to return to your client application, to name a few. When used with ADS, these instructions are performed entirely on the server.

Many of the data access mechanisms for Advantage provide alternative ways of requesting these same operations. For example, in Delphi, you can perform all of the preceding tasks using the Advantage TDataSet Descendant components. Similarly, any development environment that can directly access the ACE (Advantage Client Engine) APIsuch as Visual Basic 6, Delphi, Visual C++, C++Builder, and the likecan perform these tasks through the functions of the ACE API. (Refer to the Advantage help for information on the ACE API.)

While some data access mechanisms permit you to manipulate data using means other than SQL, Advantage SQL is the common denominator. Specifically, SQL can be used with every data access mechanism that Advantage supports (except with the Advantage Clipper RDDs). For example, ODBC (open database connectivity) is a SQL-based standard for creating client/server applications. Any language that supports ODBC can be an effective tool for writing client applications that use Advantage, even if that language cannot use the ACE API.

When used with ADS, Advantage SQL statements are executed on the remote database server. If you are using ALS (Advantage Local Server), the queries are executed on the client machine. To put this another way, only with ADS do you get the full benefits of distributed computing with SQL queries.

Although ALS does not provide a client application with the benefit of executing SQL statements on the server, there are still situations in which SQL is better suited or even required with ALS:

•        With some of the Advantage data access mechanisms, SQL provides the only mechanism for executing stored procedures.

|  |  |
| --- | --- |
| • | SQL provides a mechanism for joining tables from multiple data dictionaries with a single connection. |

|  |  |
| --- | --- |
| • | SQL reduces the amount of coding required to perform some complex tasks, especially if these tasks involve multiple tables. |

|  |  |
| --- | --- |
| • | SQL makes code more portable to other RDBMS (relational database management systems). |

|  |  |
| --- | --- |
| • | Since Advantage 7.1, you can control almost every aspect of your database, including tables, indexes, users, groups, views, triggers, publications and subscriptions, user-defined functions, and even your data dictionary properties, through SQL. |

SQL is a parsimonious language for performing many tasks. Even environments that support alternative ways of working with Advantage data can exploit the powerful nature of Advantage SQL. For example, even though Delphi developers find the TAdsTable immensely useful, there are many times when using Advantage SQL through a TAdsQuery component performs a task more efficiently.

Advantage SQL queries consist of table references, field references, aliases, keywords, literals, operators, SQL scalar functions, user defined functions, comments, and parameters. Each of these is discussed in the following sections.

   
NOTE: In this book, we have adopted a convention of showing SQL keywords and table names in uppercase and field names with initial capital letters. However, with the exception of character string literals, SQL statements are not case-sensitive. SELECT \* FROM Customer, select \* from CUSTOMER, and select \* FROM Customer are equivalent. The exception to this rule is in Linux, which is a case-sensitive operating system. In Linux, table names are case-sensitive, which is why we use uppercase for table references since they match our sample database filenames.