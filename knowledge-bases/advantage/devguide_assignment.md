Assignment




Advantage Database Server 12  

     Assignment

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Assignment  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Assignment Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Assignment Advantage Developer's Guide > Part II - Advantage SQL > Chapter 13 - SQL Scripting Language > Assignment / Dear Support Staff, |  |
| Assignment  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Variables are assigned a value using the assignment operator, = (the equals sign), where the variable name appears on the left-hand side of the assignment operator, and an expression whose value is being assigned appears on the right. An assignment statement can optionally be preceded by the SET keyword.

The expression can be any valid expression supported by Advantage, and may include literals, PSM variables, scalar functions, user defined functions, and operators.

The expression can also be a SELECT statement enclosed in parentheses if the SELECT statement returns a single field of one record. In this case, the value returned by the SELECT statement must be compatible with the variable type.

The following demonstrates several variable declarations and assignments:

DECLARE ProdName String, @Price Double;  
@Price = 1199.00;  
ProdName = (SELECT "Product Name" FROM Products   
  WHERE "Retail Price" = @Price);

There is a special case of assignment that pertains only to cursors. A cursor may be assigned its SELECT statement as part of its declaration. This is done by following the cursor data type with the AS keyword followed by a SELECT statement. The following is an example of a cursor declaration that includes assignment:

DECLARE CustTab Cursor AS SELECT \* FROM CUSTOMER;

The assignment of a SQL SELECT statement to a cursor can also be performed from the OPEN call for a cursor. Using OPEN to assign the cursor SELECT statement is described later in this section.