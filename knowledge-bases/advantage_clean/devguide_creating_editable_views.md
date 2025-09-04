---
title: Devguide Creating Editable Views
slug: devguide_creating_editable_views
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_editable_views.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 61cd72e9894dbdede3617f4d7e48286c712fb8cb
---

# Devguide Creating Editable Views

Creating Editable Views

 

     Creating Editable Views

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating Editable Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

An editable view is one that can be used to edit data in the underlying table. In short, an editable view is one where the SQL SELECT statement used to create the view produces an editable result set.

SQL SELECT statements that produce editable result sets select data from only one table or view. If selecting from a table, there must be a one-to-one correspondence between the individual records and columns in the query result set and the table being queried. In other words, you cannot use SQL keywords like DISTINCT, UNION, or GROUP BY, and only a list of one or more fields, or all fields (using the \* operator), may appear in the SELECT clause. Similarly, you cannot use aggregate functions, SQL scalar functions, user defined functions, or subqueries in the fields list of a SELECT query if you want to edit the results.

If your view selects from a view, the view being queried must produce an editable result set in order for the view to be editable.

The following steps show you how to create a simple, editable view using the sample files you have been working with in preceding chapters:

Open the DemoDictionary connection in the Connection Repository, if it is not already open.

Right-click the VIEWS node and select Create. The View dialog box is displayed, as shown in Figure 6-1.

At the Name field, enter Employee Tab.

Enter the following SQL statement in the SQL section:

SELECT "Employee Number", "First Name", "Last Name",  
  "Department Code"  
FROM EMPLOYEE

Select the Description tab and enter the following description: View of EMPLOYEE table without the Salary field.

Click OK to create the view.

Figure 6-1: The View dialog box

   
NOTE: If you add one or more INSTEAD OF triggers to a view, it can be edited even if the view is otherwise non-editable. These triggers take responsibility for applying any edits to the view to the underlying tables. Creating triggers is discussed in Chapter 8.
