---
title: Devguide Calling A User Defined Function
slug: devguide_calling_a_user_defined_function
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_calling_a_user_defined_function.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 415a88e25686059ae5eefd7a1a6f87aa66f7c200
---

# Devguide Calling A User Defined Function

Calling a User Defined Function

     Calling a User Defined Function

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Calling a User Defined Function  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You call a user defined function from within a SQL statement or an Advantage SQL script. User defined function calls can appear anywhere an Advantage SQL scalar function can appear.

Use the following steps to demonstrate calling the RandomRange user defined function:

1.        With the DemoDictionary connection active and connected, select Tools | SQL Utility or click the Test Queries button from the Advantage Data Architect toolbar to display the SQL Utility.

| 2. | Enter the following script into the SQL pane: |

SELECT Math.RandomRange(1, 10) as Rank,  
    [Customer ID]  
  FROM CUSTOMER

3.        Click the Execute Query button on the SQL Utility toolbar. The query will execute, and the result set, including the random values calculated by the RandomRange user defined function, will be displayed on the Data page of the Result pane. Your SQL Utility should look something like that shown in Figure 13-4.

Figure 13-4: A user defined function is used to randomly rank customers in a SELECT statement

4.        Close the SQL Utility when you are done.

 

In the next chapter you will learn how to access metadata, as well as perform maintenance tasks on your data dictionary using SQL.
