Testing a View




Advantage Database Server 12  

     Testing a View

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Testing a View  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Testing a View Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Testing\_a\_View Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 6 - Views > Testing a View / Dear Support Staff, |  |
| Testing a View  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You test a view by opening it, or by querying it. Either way, the result set created by the view is returned. Both of these techniques are demonstrated in this section.

Opening a View

Use the following steps to open a view in a Table Browser:

If the VIEWS node of the DemoDictionary connection is not already expanded, expand it.

Double-click the Employee Tab view. (Alternatively, right-click the view in the Connection Repository and select Open.) The view is executed, and the result set that it returns is displayed in the Table Browser, as shown in Figure 6-2.

Figure 6-2: The result set returned by the Employee Tab view

Notice that the Salary field, which was not included in the SELECT clause of the query, is not in this view.

This view is an editable view. For example, if you wanted to change the department code for one of the employees, you could do so from this view using the Table Browser. Any changes that you write to the view will be applied directly to the underlying table from which the records were obtained.

Querying a View

Views are often used in the FROM clause of SQL queries in client applications, and in other views. In both of these situations, the view itself is being treated as though it were a table in your database.

Use the following steps to demonstrate querying a view:

With DemoDictionary as the active connection, select Tools | SQL Utility from the Advantage Data Architect's main menu.

Enter the following SELECT statement in the SQL pane of the SQL Utility:

SELECT \* FROM [Employee Tab]

Click the Execute button or press F5 to execute this query. The query result is returned, as shown in Figure 6-3.

Figure 6-3: The result set returned by querying a view