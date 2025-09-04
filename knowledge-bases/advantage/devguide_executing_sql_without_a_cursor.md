Executing SQL Without a Cursor




Advantage Database Server 12  

     Executing SQL Without a Cursor

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Executing SQL Without a Cursor  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Executing SQL Without a Cursor Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Executing\_SQL\_Without\_a\_Cursor Advantage Developer's Guide > Part II - Advantage SQL > Chapter 13 - SQL Scripting Language > Executing SQL Without a Cursor / Dear Support Staff, |  |
| Executing SQL Without a Cursor  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Cursors are essential if you want to read data from one or more fields of one or more records. However, many different kinds of SQL statements do not return a result set. These include common tasks such as inserting or deleting records, as well as data definition language (DDL) statements such as ALTER, CREATE, and DROP.

In most cases, you can execute statements like these by simply including them in your Advantage SQL script. For example, the following script segment creates a temporary table named #MYTABLE:

DECLARE MyCursor CURSOR;  
CREATE TABLE #MYTABLE (Message CICHAR(255));  
//statements follow that insert data into #MYTABLE

But what if you did not know in advance the name of the table that you wanted to create. In this case, you cannot include the CREATE TABLE statement directly in your script, because that statement must include the literal name of your table. For those statements where you must assemble your SQL at runtime, you use the EXECUTE IMMEDIATE statement.

EXECUTE IMMEDIATE is followed by a string value that contains the SQL you want to execute. This SQL can be a literal string, but you will nearly always follow EXECUTE IMMEDIATE with a string variable that holds your SQL.

The following is a simple SQL stored procedure that creates a table whose name is not known until runtime. In this case, the stored procedure is passed a single character field in the input table. That field is named TabName, and it contains the name of the table that the stored procedure will create:

DECLARE TempName String, SQLStmt String;  
TempName = (SELECT TabName FROM \_\_input);  
SQLStmt = 'CREATE TABLE ' + TempName +   
  '(Message CICHAR(255))';  
EXECUTE IMMEDIATE SqlStmt;