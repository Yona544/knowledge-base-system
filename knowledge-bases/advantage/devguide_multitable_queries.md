Multitable Queries




Advantage Database Server 12  

     Multitable Queries

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Multitable Queries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Multitable Queries Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Multitable\_Queries Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Multitable Queries / Dear Support Staff, |  |
| Multitable Queries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The queries covered so far in this chapter have all involved a single table. However, in the world of relational databases, your data is typically distributed across two or more related tables. Queries that include two or more tables make use of joins or unions. The following sections describe joins and unions.

   
NOTE: Any time you execute a query that contains a join of any type, the result is a static cursor.  
 

Creating Table Joins in the WHERE Clause

The simplest mechanism for defining a join is to define the relationship between two or more fields in two or more tables in the WHERE clause. For example, consider the following query:

SELECT Count(INVOICE."Invoice No") AS "Count of Invoices",  
    INVOICE."Employee ID", RTRIM(EMPLOYEE."First Name") +   
    ' ' + RTRIM(EMPLOYEE."Last Name") AS "Full Name"  
  FROM INVOICE, EMPLOYEE  
  WHERE INVOICE."Employee ID" = EMPLOYEE."Employee Number"  
  GROUP BY 2, 3

This query joins records in the EMPLOYEE table to those in the INVOICE table based on the fields that uniquely identify the employee. Those fields are the Employee ID field in the INVOICE table and the Employee Number field in the EMPLOYEE table. By selecting those records where these fields match in the WHERE clause, we effectively produce a join. Figure 12-6 depicts the result set produced by this query.

This type of join is called an inner join. With an inner join, the result set only includes records for which the same values appear in both tables for those fields involved in the join. With respect to this query, it means that only employees associated with at least one invoice in the INVOICE table, and whose Employee Number appears in the EMPLOYEE table, will be selected to the result set. Any employee whose number does not appear in the INVOICE table will not appear in the result set, nor will employees whose Employee ID appears in the INVOICE table, but whose Employee ID does not appear in the Employee Number field of the EMPLOYEE table.

Figure 12-6: A query with a WHERE clause join

 

   
NOTE: Anytime you join data from two or more tables using either the WHERE clause or the JOIN keyword (described next), appropriate indexes can have a dramatic impact on query performance.  
 

Using JOIN

In addition to using a WHERE clause to produce an inner join, you can join data from two or more tables in records of your result using the JOIN keyword. With JOIN, you can create both inner and outer joins.

You create an inner join by preceding the JOIN keyword by the keyword INNER, followed by a table that you want to JOIN, and then listing the field associations following the ON keyword. For example, the following query creates the same inner join as that shown in the preceding query using a WHERE clause:

SELECT Count(INVOICE."Invoice No") AS "Count of Invoices",   
  INVOICE."Employee ID",   
  RTRIM(EMPLOYEE."First Name") +   
  ' ' + RTRIM(EMPLOYEE."Last Name") AS "Full Name"   
  FROM INVOICE   
  INNER JOIN EMPLOYEE ON   
    INVOICE."Employee ID" = EMPLOYEE."Employee Number"   
  GROUP BY INVOICE."Employee ID",   
    RTRIM(EMPLOYEE."First Name") + ' ' +   
    RTRIM(EMPLOYEE."Last Name")

Because inner joins defined in the WHERE clause tend to be shorter in length, those queries tend to be used more often than those that employ the INNER JOIN keywords. By comparison, outer joins cannot be accomplished using the WHERE clause. Instead, you use the OUTER JOIN keywords. When you define an outer join, records can be included in the result set even when there is no match between the tables being joined.

Advantage supports three types of outer joins: LEFT, RIGHT, and FULL. Use a LEFT OUTER JOIN to include all records from the left-side table even when there are no corresponding records in the right-side table. Use a RIGHT OUTER JOIN to include all records from the right-side table even when there are no corresponding records in the left-side table. FULL OUTER JOIN includes records from both tables, whether or not  there are matching records in the opposing table.

The following query demonstrates a LEFT OUTER JOIN.

SELECT Count(INVOICE.[Invoice No]) AS [Count of Invoices],  
  EMPLOYEE.[Employee Number], RTRIM(EMPLOYEE.[First Name]) +  
    ' ' + RTRIM(EMPLOYEE.[Last Name]) AS [Full Name]  
  FROM EMPLOYEE  
  LEFT OUTER JOIN   
    INVOICE ON INVOICE.[Employee ID] =   
      EMPLOYEE.[Employee Number]  
  GROUP BY EMPLOYEE.[Employee Number], [Full Name]

This query counts the number of invoices found in the INVOICE table for all employees, not just those employees whose employee numbers appear in the INVOICE table. A count of 0 is returned for those employees listed in the EMPLOYEE table for whom no corresponding records appear in the INVOICE table, as seen in Figure 12-7.

Figure 12-7: The results of a LEFT OUTER JOIN

   
NOTE: Advantage 8 introduced RIGHT OUTER JOIN and FULL OUTER JOIN operations.  
 

An in-depth look at the various types of joins is beyond the scope of this book. For more information on how and when to use the various types of joins, refer to any number of introductory books on the SQL language.

Using UNION

You use UNION to combine records from two result sets with a similar structure (same number of fields and similar data types for the corresponding fields) into one result set. Each result set is produced by a SELECT statement that may be from one or more tables. When using UNION, only distinct records are retrieved to the result set. If you use UNION ALL, duplicate records are not suppressed. Consider the following query:

SELECT [Employee ID],   
  'Has Sales' AS [Sales Status]  
  FROM INVOICE  
  UNION SELECT [Employee Number],   
      'No Sales' AS [Sales Status]  
    FROM EMPLOYEE  
    WHERE [Employee Number] NOT IN  
      (SELECT [Employee ID] FROM INVOICE)

This query will return the employee identification number from both the INVOICE and the EMPLOYEE tables. Those employees associated with at least one invoice in the INVOICE table will have the string "Has Sales" associated with their records in the result set, while those without corresponding entries in the INVOICE table will display the string "No Sales." The result set returned by this query is shown in Figure 12-8.

Figure 12-8: Two result sets combined using UNION

   
NOTE: You cannot use MEMO or BLOB fields in queries that use the UNION keyword, except in the case of UNION ALL.