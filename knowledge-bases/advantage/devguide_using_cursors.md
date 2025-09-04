Using Cursors




Advantage Database Server 12  

     Using Cursors

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Cursors  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Using Cursors Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Using\_Cursors Advantage Developer's Guide > Part II - Advantage SQL > Chapter 13 - SQL Scripting Language > Using Cursors / Dear Support Staff, |  |
| Using Cursors  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A cursor is a data type that can point to the readonly, forward-navigating result set returned by a SELECT or EXECUTE PROCEDURE statement. Once active, a cursor can be used to read the individual fields of the result set.

There are four steps to using a cursor. They are:

Declaring a cursor variable.

Opening the cursor.

Fetching one or more records from the cursor.

Closing the cursor.

Declaring and assigning a SQL SELECT statement to a cursor is discussed earlier in this section. Activating and using a cursor is discussed in the following sections.

Opening a Cursor

Before you can use a cursor, you must open it. You do this using the OPEN keyword followed by the name of the cursor variable.

If a cursor already has a SQL SELECT statement assigned to it, that statement is executed when the cursor is opened.

For example, the following statements declare and execute a SQL SELECT statement, returning a cursor to the result set:

DECLARE CustTab CURSOR as SELECT \* FROM CUSTOMER;  
OPEN CustTab;

You can also assign or change the SELECT statement associated with a cursor with the OPEN keyword. This permits you to use a single cursor variable to execute many different SELECT statements.

To assign a new SELECT statement to a cursor while opening it, follow the name of the cursor with the AS keyword and then the SELECT statement. This is demonstrated in the following example:

DECLARE CustTab CURSOR;  
OPEN CustTab AS SELECT \* from CUSTOMER;

If you have an open cursor, you must close it before you can open it again, whether or not you change the SELECT statement in the OPEN operation.

Fetching Data

Once you have executed a query by opening a cursor, you must first fetch a record before you can access the data. You fetch a record by calling the FETCH keyword followed by the name of your open cursor.

FETCH is similar to a function that returns a Boolean value. If the first time you call FETCH it returns False, the result set is empty. If it returns True, the cursor points to the first record in the result set.

If there is more than one record in your result set, you can call FETCH repeatedly. Each additional time FETCH returns True, the cursor advances one record in the result set. Once FETCH returns False, there are no more records in the result set.

Reading a Field

Anytime FETCH returns True, your cursor is pointing to a record in the result set. To read individual field values, you use dot notation with the cursor. Specifically, you follow the cursor variable name with a dot (or period) followed by the name of the field or field alias.

If a field name in your table contains spaces, special characters, or includes reserved words, you must delimit the field name with double quotation marks or square braces.

For example, if you have a field named Customer ID, you can read that field using code similar to the following:

DECLARE CustId Integer;  
DECLARE CustTab Cursor AS SELECT \* from CUSTOMER;  
OPEN CustTab;  
TRY  
  IF FETCH CustTab then  
    CustId = CustTab."Customer ID";  
  END;  
FINALLY  
  CLOSE CustTab;  
END;  
//ready to work with the Customer ID value

If your SELECT statement selects fields not actually in the table, such as an expression, you must assign an alias to those fields if you want to refer to them using the cursor. You then use the alias to refer to the field. This is demonstrated in the following code:

DECLARE CustOrder Double, CustID Integer;  
DECLARE CustTab Cursor AS   
  SELECT [Customer ID], Rand() as Random   
    FROM CUSTOMER ORDER BY Random;  
OPEN CustTab;  
TRY  
  IF FETCH CustTab THEN  
    CustOrder = CustTab.Random;  
    CustID = CustTab.[Customer ID];  
  END;  
FINALLY  
  CLOSE CustTab;  
END;

Closing a Cursor

Close a cursor when you are through with it. If you want, you can re-open a cursor after closing it. Doing so re-executes the query associated with the cursor, or executes the new SQL statement assigned to the cursor in the OPEN statement.