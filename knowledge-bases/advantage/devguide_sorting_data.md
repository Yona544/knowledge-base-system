Sorting Data




Advantage Database Server 12  

     Sorting Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Sorting Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Sorting Data Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Sorting\_Data Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Sorting Data / Dear Support Staff, |  |
| Sorting Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Unless you specifically request that the records returned by the SELECT statement are sorted, a query will return records in the natural order of the table. As discussed in Chapter 3, this order is affected by the order in which records are entered and deleted, and has nothing to do with the data contained in those records.

To sort the results in a result set, add an ORDER BY clause to your SQL statement. ORDER BY clauses can be constructed in one of two ways. You can specify the ORDER BY columns either by name or by number. For example, the following SELECT statement will return the records of the PRODUCTS table ordered by the Description field:

SELECT \* FROM [PRODUCTS] ORDER BY [Description]

If you want to sort by two or more fields, separate the field names with commas. Also, the default order direction is an ascending sort order, from lowest to highest. You can follow your field name with DESC to sort in descending order, if you like. (You can also use the keyword ASC, but since ascending is the default order, this keyword has no effect.) The following query demonstrates a two-field sort where the Invoice Date field is sorted in descending order:

SELECT "Invoice No", "Employee ID",  
  "Invoice Date", "Date Payment Received"  
  FROM INVOICE  
  ORDER BY "Employee ID", "Invoice Date" DESC

Actually, the ORDER BY clause can be any valid expression except those that use MEMO or BLOB fields. While the following example is obviously a meaningless sort order, it demonstrates the level of flexibility that you have when selecting which fields or expressions to order by:

SELECT "Invoice No", "Customer ID", "Invoice Date"  
  FROM INVOICE  
  ORDER BY 100 - "Employee ID"

Instead of using field names or expressions in the ORDER BY clause, if the fields or expressions that you want to sort by appear in the SELECT list, you can simply supply numerals that refer to the positions of the fields or expressions that you want to sort by. Just as you do when sorting by name, these numerals are separated by commas if you want to sort by more than one column, and can be followed by the DESC or ASC keywords. For example, the following query produces the same result set as did an earlier query in this section:

SELECT "Invoice No", "Employee ID",  
  "Invoice Date", "Date Payment Received"  
  FROM INVOICE  
  ORDER BY 2, 3 DESC

You can even sort by position when using the \* (select all) symbol, as shown here:

SELECT \* FROM CUSTOMER ORDER BY 3, 2

   
NOTE: The performance of queries that include ORDER BY clauses can be dramatically improved by the presence of one or more appropriate indexes.