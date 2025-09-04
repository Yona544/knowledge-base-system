Why Create Indexes?




Advantage Database Server 12  

     Why Create Indexes?

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Why Create Indexes?  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Why Create Indexes? Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Why\_Create\_Indexes\_ Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 3 - Defining Indexes > Why Create Indexes? / Dear Support Staff, |  |
| Why Create Indexes?  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are two reasons for creating an index order. The first is to provide a meaningful view of the records in a table. The views may be related to the order of a tables records, or they may be related to the specific contents of individual records. The second reason is related to database performance.

The physical order of records in a table, sometimes called the natural order, is rarely very useful. The natural order is a consequence of the order in which the records were added in conjunction with records that were deleted. For example, when using ADT tables, a newly added record may be placed in a position where a previously deleted record appeared.

Using index orders, you can provide many different and meaningful orderings for your records. For example, there may be times when you may want to access your customer table in order of the customer ID number. At other times, you may want to work with your customer records sorted by the customers last name. Both of these orders are possible by creating one index order that organizes records by customer ID, and another that orders records by customer last name. The order in which the customer table records appear depends on which of these two indexes is currently active.

Index orders that are based on the contents of individual records can be used to work with a subset of records from a table. For example, you may have a table that contains records for employees, both past and present. One of the fields in this table may indicate the status of the employeewhether the employee is a current employee or a former employee. If you regularly want to work only with current employees, you can create an index order that ignores former employees. When that index order is active, the table will appear to contain only records for current employees.

As noted earlier in this section, the second reason to create an index order is to enable high-performance operations on your data. Imagine, for instance, that you need to work with a record where the customer ID number is 10304. If you have an index order whose index key expression is based on the customer ID field, Advantage will located the record using this index order. Specifically, it will locate the record by first searching for the customer ID in the keys of this index order, and then use the keys pointer to the record to retrieve the data. In other words, the underlying table is not even touched until the server knows which record it needs to read. This approach is much faster than if the server had to read every record in the table looking for the particular customer ID.

While the preceding example considered the location of a single record, these indexes also allow groups of records to be quickly identified. For example, if you have an index key expression based on the customer tables last name field, you can quickly locate all customers whose last name begins with a given letter, such as T. Likewise, if you have an index on the city name field, you can very quickly obtain a list of customers who reside in a particular city, New York City, for example. In both of these cases, Advantage can quickly find the appropriate customer records by reading the keys of the associated index orders, which is always faster than reading the individual customer records.

It is this second characteristic of index ordersthe identification of record locations using the indexes directlythat is the source of Advantages blinding performance.

Heres another way to look at it. If you design your indexes correctly, Advantage will provide you with the best performance possible. On the other hand, if you fail to define indexes based on how your application needs to work with its data, your applications performance will suffer. For example, if you do not have an index order whose index key expression is based on the city name field, searching for customers who live in New York City will be significantly slower.

Dont let the significance of indexes worry you too much. The Table Designer in the Advantage Data Architect makes it easy for you to create field-specific indexes, which are the most common as far as performance is concerned.