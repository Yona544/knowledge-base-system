Live Cursors Versus Static Cursors




Advantage Database Server 12  

     Live Cursors Versus Static Cursors

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Live Cursors Versus Static Cursors  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Live Cursors Versus Static Cursors Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Live\_Cursors\_Versus\_Static\_Cursors Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > Live Cursors Versus Static Cursors / Dear Support Staff, |  |
| Live Cursors Versus Static Cursors  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You use SQL SELECT statements to retrieve data from the database server to your client application. When you execute a SELECT statement, Advantage produces one of two types of cursors: a live cursor or a static cursor. Which type of cursor Advantage produces has implications for both performance and features.

Creating Live Cursors

A live cursor is one that maps directly to an Advantage table. If the live cursor does not include all records in the table being queried, the live cursor is produced by Advantage by creating an AOF (Advantage Optimized Filter). (Selecting fewer than all records means that a WHERE clause is included in the SELECT statement.)

Advantage will first attempt to build the AOF using existing indexes. If all of the necessary indexes already exist for the table, Advantage is able to quickly build an AOF. These AOFs are referred to as fully optimized AOFs, and they are one of the primary sources of Advantage's speed.

If the WHERE clause can make use of one or more indexes, and some, but not all, of the indexes that Advantage requires are present, the AOFs will be partially optimized based on the existing indexes. These AOFs are referred to as partially optimized filters. Advantage will then have to explicitly read the records that match the optimized part of the AOF to determine whether or not they match the non-optimized part of the filter expression.

Imagine that you have a CUSTOMER table that includes both Last Name and City fields. Imagine further that you have an index on Last Name, but not on City. If your filter expression is Last Name = "Green" and City = "Chicago", the AOF will be partially optimized. Advantage will use the Last Name filter to quickly select all Greens, but then must read every one of these identified customers in order to determine whether or not they live in Chicago.

If no indexes currently exist to assist in satisfying the WHERE clause, the AOF is a non-optimized filter. With a non-optimized filter, Advantage must read every record in the entire table to determine whether or not it passes the filter expression. As you can imagine, this results in the slowest performance of the three AOF types.

Once the AOF has been constructed, Advantage begins returning records to the client. The number of records returned depends on the size of the result set, the size of individual records, the number of records requested by the application, and the requirements of the client. Advantage will usually return to the client the number of records configured in the record cache setting (or a single record if the application requested only the first record in the result set). The default record cache setting is 10 or however many records fit into a transmission burst, whichever is smaller. A transmission burst is 22K bytes with IP, and 8K bytes with IPX.

   
NOTE: See the ADS help for information on changing the record cache size.  
 

If the returned records do not satisfy the client's needsfor example, if the client application is attempting to populate a grid that can display more records than that received in the first transmissionanother transmission, and then another, if necessary, is returned until the client is satisfied. This process is repeated each time the client navigates to another part of the result set, as well as each time the query is executed.

From a performance perspective, whether or not an optimized AOF can be created affects how quickly live cursors are returned. This is why it is important to create indexes on those expressions that will be used regularly to select data from your tables.

Using Live Cursors

The primary benefit of a live cursor is that it can be updated, just like a table. Furthermore, when another client changes the contents of the underlying table, those changes are immediately reflected in the AOF. For example, newly inserted records that meet the WHERE clause become part of the live cursor, and will be received by the client the next time the client application requests data from the region of the AOF where the record was inserted. This may occur due to normal navigation, or be the result of an explicit refresh.

But there are two specific situations where live cursors based on AOFs do not have automatic access to newly posted data. With ALS, AOFs are not updated each time data changes. As a result, with ALS, an AOF may become obsolete on a client, returning data that no longer meets the WHERE clause. The second situation is when you are using compatibility locking to share DBF files with non-Advantage applications. In these cases, Advantage is not the sole application that is accessing those files, and once again, the AOF may become obsolete. For these situations, you need to re-execute the query to create a current AOF.

Creating Static Cursors

Static cursors are created automatically any time Advantage cannot create a live cursor. This happens when the SELECT statement selects more than simple columns from a single table, contains the DISTINCT or TOP keyword or an aggregate function in the SELECT clause, contains a GROUP BY or HAVING clause, includes a subquery (discussed later in this section), or includes either a BLOB field or the LIKE operator in the WHERE clause. Another element that will prevent a live cursor is the use of a user defined function or any scalar function in an expression in the WHERE clause other than the functions listed in Table 11-6.

 

|  |  |  |
| --- | --- | --- |
| ABS | BIT\_LENGTH | CHAR |
| CHARACTER\_LENGTH | CHAR\_LENGTH | CONCAT |
| CONTAINS | CURDATE | CURRENT\_DATE |
| CURRENT\_TIME | CURTIME | IFNULL |
| IIF | ISNULL | LCASE |
| LEFT | LENGTH | LOCATE(x, y) |
| LOWER | LTRIM | NOW |
| OCTET\_LENGTH | PI | POSITION |
| POWER | RIGHT | RTRIM |
| SPACE | SUBSTRING | UCASE |
| UPPER |  |  |

Table 11-6: WHERE Clause Scalar Functions Compatible with Live Cursors

Even if your SELECT statement would not otherwise create a static cursor, you can specifically request a static cursor when you create your SQL statement. Simply include the {static} directive immediately following the SELECT keyword to request a static cursor. For example, the following query produces a static cursor, even though Advantage would normally create a live cursor:

SELECT {static} \* FROM INVOICE

While a live cursor is a filtered view of a table based on AOF, a static cursor is actually a new, temporary table constructed by (and managed by) the server. While this temporary table may take a while to create, Advantage will begin returning records to the client before this temporary table is completely populated. As a result, there are rare situations where static cursors will make records available to the client faster than when live cursors are used. In most cases, using live cursors is faster because no temporary files will be created.

This behavior of static cursorsreturning results before the temporary table is completely filledis obvious if you first obtain a static cursor on a large result set and then attempt to navigate to the last record. Going to the last record is something that can only be accomplished once the static cursor is completely populated. Consequently, if you obtain a static cursor and then immediately attempt to move to the last record, there will often be a noticeable delay while Advantage awaits the population of the temporary table prior to returning the last record.

SQL statements that cause a static cursor to be fully populated include the use of aggregate functions in your query, such as MIN, MAX, and COUNT, as well as including an ORDER BY clause.

This discussion is not meant to imply that static cursors are not optimized. Indeed, whenever possible, Advantage will employ indexes and use other optimization techniques to identify the records that must be copied to the temporary table.

In Advantage 8.1, static cursors are cached in memory as much as possible. No physical temporary file is created for a static cursor until Advantage needs the memory for other purposes. As a result, static cursors that return a small result set are exceptionally fast.

Using Static Cursors

From the standpoint of client applications, there are only two differences between using a live cursor and a static cursor. The first is that a static cursor is readonly. You cannot make changes to the result set created using a static cursor. (The exception is static, client-side cursors in ADO, ActiveX data objects, which provide a mechanism to generate SQL updates to the underlying tables.) By comparison, you can insert, delete, and update records using a live cursor.

The second difference is that static cursors do not automatically reflect changes that have been posted to the underlying table. Recall that a static cursor actually points to a temporary table on the server. Consequently, if another client inserts a record into a table from which you selected a static cursor, the record is inserted into the destination table but not into the temporary table. If you want to see changes made to the underlying table, you have to re-execute the query, which causes Advantage to rebuild the temporary table.