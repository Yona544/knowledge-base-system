System Stored Procedures




Advantage Database Server 12  

 

     System Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| System Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       System Stored Procedures Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_System\_Stored\_Procedures Advantage Developer's Guide > Part II - Advantage SQL > Chapter 14 - System Management and Metadata > System Stored Procedures / Dear Support Staff, |  |
| System Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While you can create a data dictionary, as well as many of the objects it contains, there are limits to what you can do with Advantage SQL. For example, you can create a data dictionary, and you can create a table in a data dictionary, but there are no commands in Advantage SQL to add a free table to a data dictionary.

The reason for this relates to standards. For the most part, Advantage SQL is designed to conform to most of the ANSI (American National Standards Institute) SQL/92 standard. No database vendor complies 100 percent with this standard, but all try to support most of it, and Advantage is no different.

The problem with conforming to standards is that they discourage customization, such as the introduction of new base keywords. While CREATE, GRANT, and INVOKE are part of the SQL/92 specification, there are no base keywords such as ADD and REMOVE.

In order to maintain a close conformance with ANSI SQL/92 and still be able to handle the many necessary data dictionary maintenance tasks through SQL, Advantage chose to implement these tasks by using stored procedures built into ADS and ALS.

The number of available system stored procedures has increased dramatically since they were first introduced in Advantage 7. Consider this, in Advantage 7.0 there were 17 system stored procedures. In Advantage 8.1, there are 102. Depending of the version of Advantage you are using, there may be additional system stored procedures. Query the system.systemprocedures table, mentioned earlier in this chapter, for a current list of the available procedures.

With these system stored procedures, in combination with the system tables and SQL statements that were discussed in both this chapter and in Chapter 12, you can perform every kind of configuration and maintenance operation that you need for your data dictionaries entirely using SQL statements. In earlier versions of Advantage, it was sometimes necessary to resort to the Advantage client engine (ACE) in order to perform some of the more advanced tasks, such as changing a user's password.

Due to the large number of system stored procedures in Advantage, providing detailed information about each one is not possible in this chapter. Instead, the remaining sections of this chapter are categorized by the system stored procedure type. In each section you will find a general description of the associated tasks, as well as a list of the system stored procedures that apply.

But first, let's discuss how to create a well-formed stored procedure invocation using SQL.