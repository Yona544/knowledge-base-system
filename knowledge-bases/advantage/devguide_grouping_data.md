Grouping Data




Advantage Database Server 12  

     Grouping Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Grouping Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Grouping Data Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Grouping\_Data Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Grouping Data / Dear Support Staff, |  |
| Grouping Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Grouping data is necessary when you want to perform operations across one or more records. There are two primary types of operations that you perform across records. The first involves selecting the unique values, or combination of values, across all records in a table. The second involves calculating simple descriptive statistics.

Selecting Unique Values

You select unique values using the DISTINCT keyword. For example, if you want to know which employees are responsible for one or more sales appearing in the ITEMS table, you follow the SELECT keyword with the DISTINCT keyword, which you then follow with the list of fields or expressions for which you want unique values. For example, consider the following query:

SELECT DISTINCT [Employee ID] FROM INVOICE

This query produces a table that has only one instance of each Employee ID that appears in the table.

You can use DISTINCT with any combination of fields or expressions, in which case the result set will contain one column for each field or expression, and one record for each unique combination of those field values. For example, the following query selects each unique combination of the Employee ID and Customer ID fields:

SELECT DISTINCT [Employee ID], [Customer ID] FROM INVOICE

Of course, you can use WHERE clauses like those shown earlier in this chapter to select the distinct data from some subset of records from one or more tables.

   
NOTE: You cannot use MEMO or BLOB fields in the SELECT list of DISTINCT queries, although you can use them in the WHERE clause. Also, queries that use the DISTINCT keyword always return a static cursor.  
 

Using TOP

The TOP keyword permits you to select some, but not all, of the records associated with the SELECT. You use TOP by immediately following the SELECT keyword by the TOP keyword. TOP is followed by an integer, which will either define the number of records you want returned or the percent of the overall number of records that you want returned. When selecting a percent of the records, follow the integer with the PERCENT keyword.

The following query returns only the first five of the records from the INVOICE table:

SELECT TOP 5 \* FROM ITEMS

This next query returns the top five percent of the records from the ITEMS table:

SELECT TOP 5 PERCENT \* FROM ITEMS

The TOP keyword is often associated with queries that calculate statistics across records (described next). For example, using TOP you can calculate which employees are responsible for the top ten percent of sales, or which five customers are responsible for the most purchases.

   
NOTE: Beginning with Advantage 8.1, TOP can be used in subqueries.  
 

Calculating Simple Descriptive Statistics

Another operation that you can perform across records is the calculation of simple statistics. Advantage SQL, like most other SQL languages, supports five descriptive statistics: average (AVG), count (COUNT), maximum (MAX), minimum (MIN), and total (SUM).

Each of these statistical functions takes a single parameter, which can be any field or expression that can appear in the SELECT list. These functions return an expression appropriate for the function. For example, the following query returns a result set that calculates the sum of the Quantity field in the ITEMS table:

SELECT SUM(Quantity) FROM ITEMS

In this query, the sum of a single field was requested. However, there is no reason why you cannot perform the operation on an expression, as shown in the following query, which calculates the total value of items purchased in the ITEMS table:

SELECT SUM(Quantity \* Price) FROM ITEMS

The COUNT function is slightly different from the other functions in that it can accept the reserved words ALL or DISTINCT and a field or expression, or the \* character. When passed the \* character as an argument, COUNT calculates the number of records. For example, the following query returns the number of records in the INVOICE table:

SELECT COUNT(\*) FROM INVOICE

When you want to count the unique non-null values in a field (or expression), use DISTINCT. For example, the following query selects the number of unique Employee ID values from the INVOICE table:

SELECT COUNT(DISTINCT [Employee ID]) FROM INVOICE

Use the ALL keyword to count all non-null values in the field (or expression). Actually, ALL is the default value, so the following statement counts the total number of non-null values in the Employee ID field of the INVOICE table:

SELECT COUNT([Employee ID]) FROM INVOICE

   
NOTE: A query that includes one or more aggregate functions always returns a static cursor.  
 

Using GROUP BY

Instead of calculating the preceding statistics across all records, you might want to calculate the statistics separately for groups of records. For example, rather than calculating the number of records in the invoice table, you might want to calculate the number of invoice records for each employee. In order to do this, you need to group by employee.

Defining groups within a table is performed using the GROUP BY keywords. You follow the GROUP BY keywords with a list of one or more fields or expressions. The statistic is then calculated once for each unique combination of the values within the group. For example, the following query returns the number of invoices associated with each employee:

SELECT COUNT(\*) FROM INVOICE GROUP BY [Employee ID]

There is one problem with this query, however. As you can see from the result set that this query returns (shown in Figure 12-3), although the statistics were calculated, there is no way to know for which employee each calculation applies.

In order to display which employee each count is associated with, you would need to include the "Employee ID" field in the SELECT list.

Figure 12-3: Calculating the number of invoices by Employee ID

Another problem with this query is that the values that are calculated appear using a default name in the result set, which in this case is EXPR. As you learned earlier in this chapter, you can assign a name to a column returned in the result set using the AS keyword. Using AS to assign a meaningful name to calculated columns is especially important when you are calculating both statistics and expressions. The following is an improved version of the preceding query:

SELECT COUNT(\*) AS "Count of Invoices", "Employee ID"   
  FROM INVOICE   
  GROUP BY "Employee ID"

This query produces the result set shown in Figure 12-4.

Figure 12-4: Field aliases permit you to assign result set column names

When you include fields or expressions in the SELECT list, other than aggregate functions, you must also include those fields and expressions in the GROUP BY list. This requirement is obvious if you consider the following illegal SQL statement:

//The following query is illegal, and generates an error  
SELECT COUNT(\*) AS "Invoice Count", "Employee ID",   
    "Customer ID"  
  FROM INVOICE   
  GROUP BY "Employee ID"

Consider what this query is asking. It is instructing Advantage to calculate the number of invoices for each Employee ID, and to include the Customer ID in the result set. The problem is that each employee likely made sales to two or more customers. Since the result set will have only one record for each employee (by virtue of Employee ID being the only field in the GROUP BY clause), there is no way to include the one or more Customer IDs. If you want to see the customer that each employee made a sale to, you must also include the Customer ID field in the GROUP BY clause, as shown in the following query:

SELECT COUNT(\*) AS "Invoice Count", "Employee ID",  
    "Customer ID"   
  FROM INVOICE   
  GROUP BY "Employee ID", "Customer ID"

This query produces the result set shown in Figure 12-5.

Figure 12-5: A query with a GROUP BY clause

Similar to ORDER BY, you can also use the column ordinal numbers instead of column names in the GROUP BY clause. The following query produces the same result as the preceding one:

SELECT COUNT(\*) AS "Invoice Count", "Employee ID",   
  "Customer ID"   
  FROM INVOICE   
  GROUP BY 2, 3

   
NOTE: You cannot use MEMO or BLOB fields in the GROUP BY clause, although you can use them in the WHERE clause. Also, queries that include GROUP BY always return a static cursor.  
 

All of the preceding examples calculate the resulting statistic based on all of the records in the table. If you want to calculate the statistic across some, but not all of the records, you have two options. One option is to use a WHERE clause.

As you learned earlier in this chapter, WHERE clauses limit the SELECT operation to those records for which the WHERE Boolean expression evaluates to True. For example, the following query counts the number of invoices entered between January 1st and December 31st, 2004, assuming that your date format is set to mm/dd/ccyy:

SELECT COUNT(\*) FROM INVOICE  
  WHERE "Invoice Date" BETWEEN '1/1/2004' AND '12/31/2004'

Using HAVING

Another way to limit which records are considered is to use a HAVING clause. Unlike a WHERE clause, which is used to select records based on values and expressions related to individual records, you use a HAVING clause to base the selection on statistics calculated across records, as defined by the GROUP BY clause. For example, consider the following query:

SELECT Count("Invoice No") AS "Count of Invoices",   
    "Employee ID"  
  FROM INVOICE  
  GROUP BY "Employee ID"  
  HAVING COUNT("Invoice No") > 10

This query calculates the total number of invoices associated with each employee, but only for those employees responsible for more than ten invoices. Employees with ten or fewer sales are ignored.

   
NOTE: Queries that employ a HAVING clause always return a static cursor. Also, beginning with Advantage 8, you can use field aliases in a HAVING clause.