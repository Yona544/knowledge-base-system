Selecting Record Subsets from Views




Advantage Database Server 12  

 

     Selecting Record Subsets from Views

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Selecting Record Subsets from Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Selecting Record Subsets from Views Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Selecting\_Record\_Subsets\_from\_Views Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 6 - Views > Selecting Record Subsets from Views / Dear Support Staff, |  |
| Selecting Record Subsets from Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You learned at the beginning of this chapter that views look like tables to client applications. This similarity extends to SQL queries that you can execute against views. In particular, the use of WHERE clauses to select a subset of records from a view can be very powerful.

Consider the Sales by Employee view that you created in the preceding section. That view produces a total of sales for each employee. However, what if you were interested in the sales by employees who are in the Sales and Marketing department? Or, what if you were interested in the sales of a specific employee? Using a SQL SELECT statement, you can query the Sales by Employee view, using a WHERE clause to return only those records of interest.

For example, consider the following query:

SELECT SEmp.[Employee ID], SEmp.[Last Name],  
    SEmp.[First Name], SEmp.[Total Sales]  
  FROM [Sales by Employee] SEmp, EMPLOYEE Emp  
  WHERE SEmp.[Employee ID] = Emp.[Employee Number] AND  
    Emp.[Department Code] = 108

This query uses the totals calculated by the Sales by Employee view, and then uses a WHERE clause to select only those employees whose department code is 108, the Sales and Marketing department.

The preceding query was a bit involved, since it was necessary to link from the view to the EMPLOYEE table in order to select those employees from the specific department. If the selection can be made based on data in the view itself, the SQL SELECT statement would be considerably shorter.

For example, imagine that you want to get the total sales for a specific employee. If you can perform your selection based on the employee's ID, first name, last name, or any combination of those field values, the query can reference the view alone. For example, the following query returns the sales totals for the employee associated with employee ID 89:

SELECT [Employee ID], [First Name], [Last Name],   
    [Total Sales]  
  FROM [Sales by Employee]  
  WHERE [Employee ID] = 89