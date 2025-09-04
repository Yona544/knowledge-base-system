Scopes, Seeks, and AOFs




Advantage Database Server 12  

     Scopes, Seeks, and AOFs

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Scopes, Seeks, and AOFs  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Scopes, Seeks, and AOFs Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Scopes\_Seeks\_and\_AOFs Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 3 - Defining Indexes > Scopes, Seeks, and AOFs / Dear Support Staff, |  |
| Scopes, Seeks, and AOFs  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Another performance-related issue concerns how indexes are used. Some operations, such as scopes (ranges) and seeks (single record locates), are performed directly on indexes. Other operations, such as filtering, involve special bitmap filters that are referred to as Advantage Optimized Filters, or AOFs.

Lets start by considering scopes and seeks, which in the terminology of the Advantage TDataSet Descendant for Delphi are called ranges and findkeys. A scope is a subset of records, based on an index order. A seek is the selection of a given record in a table, based on an index order.

Both scopes and seeks use indexes directly, and provide the highest attainable level of performance. Before you can set a scope or perform a seek, you must make the index that will be used for the operation the active index. This directs Advantage to use the keys of the active index for the operation.

For example, if you have an index whose index expression consists of two fields, last name and first name, you can select this index and then set a scope to include all records where the last name is Smith. This operation uses the index directly to set the scope. This same index could be used to select all customers whose last name is Jones and whose first name begins with the letters A through G. Again, this scope uses the active index directly.

   
NOTE: The Locate and Lookup methods of the Advantage TDataSet Descendant do not require you to explicitly set an index before their call. These methods are special in that they are smart enough to use available indexes for optimization, if present.  
 

Not all Advantage developers can use scopes and seeks. For example, if your only interface to Advantage is through SQL, such as when you are using an ODBC or Java JDBC driver, you have no way to execute scopes and seeks. Scopes and seeks are available to developers who can use the Advantage Client Engine API, the Advantage Clipper RDD, the Advantage OLE DB Provider (seeks only), the Advantage .NET Data Provider (through the AdsExtendedReader class), the Advantage Visual Objects RDD, and the Advantage TDataSet Descendant.

On the other hand, even if you cannot create scopes and seeks manually, Advantage might be creating them for you. For example, a SQL SELECT statement including a WHERE clause may set a scope in order to satisfy the WHERE clause, but only if the appropriate index is available. If a scope cannot be used, Advantage will try to create an AOF instead.

AOFs are bitmap filters that are created from available indexes in order to create filtered views of a table. Unlike the use of scopes and seeks, where you as the developer must specifically choose the index, AOFs are constructed at runtime based on the available indexes. Once constructed, they can be used by multiple client applications to select one or more records based on a filter. AOFs are never faster than a scope, but they are often much faster than if an optimized AOF cannot be created.

Each bit in an AOF corresponds to a record in a table. If an AOF is fully optimized, a bit that is set means that the corresponding table record passes the filter, and a clear bit means that the record does not. These values are then used to retrieve the filtered records from the table.

If an AOF is partially optimized or not optimized, a set bit in the AOF means that the record might be in the filter, and a clear bit means that it is not. In these cases, Advantage must read each record associated with a set bit in order to determine whether or not to include the record in the filtered set.

You may recall that earlier in this chapter in the section "Testing Indexes," you entered a filter expression and a green circle appeared. When the circle is green, Advantage is using a fully optimized AOF. If the circle is red, the AOF is not optimized. If a partially optimized AOF can be created, a yellow circle appears. As a result, the Set Filter feature of the Table Browser is an invaluable tool for verifying that your indexes are providing Advantage with the information it needs.

Recall that a given index order can be based on one or more expressions in the index key expression. The first expression of a multipart expression index (or the only expression in a simple expression index) is always available to contribute to an optimized AOF. For example, if you have an index on Last Name;First Name, comparisons involving the Last Name field produce optimized AOFs based on this index. (The same is true if the index expression is simply Last Name.)

If there are two or more expressions in the index key expression, the remaining expressions may or may not participate in an AOF, depending on the comparison being made in the filter or WHERE clause. If the comparison performs a strict equality comparison, and makes use of the AND operator, two or more fields in a comparison can make use of the corresponding two or more expressions in the index key expression. For example, the index based on Last Name;First Name may produce optimized AOFs if your comparison looks something like the following:

Last Name='Jones' AND First Name = 'Frank'

However, partial matches or range comparisons can only make use of the first field of a multiexpression index key expression. As a result, the following comparison will produce only a partially optimized AOF even though there is a Last Name;First Name index:

Last Name = 'Jones' AND First Name = 'F\*'

Since the first field of an index does contribute to the creation of optimized AOFs, if you have one index on Last Name, and another index on First Name, then the preceding expression does produce an optimized AOF.

   
NOTE: You can test this yourself using the Set Filter feature of the Table Browser. Add an index for Last Name;First Name and test the two preceding filters. Then add a First Name index and test them again. With just the Last Name;First Name index available, only the first filter will be fully optimized. After adding the First Name index, both will be optimized.  
 

There is more to AOFs than we have space to describe here. As a result, for more details concerning AOFs, and what you can do to ensure that your application will use optimized AOFs, we suggest that you refer to the Advantage documentation.