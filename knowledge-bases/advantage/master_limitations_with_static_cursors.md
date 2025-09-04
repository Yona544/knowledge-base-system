Limitations with Static Cursors




Advantage Database Server 12  

Limitations with Static Cursors

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Limitations with Static Cursors  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Limitations with Static Cursors Advantage SQL Engine master\_Limitations\_with\_static\_cursors Advantage SQL > SQL Performance > Limitations with Static Cursors / Dear Support Staff, |  |
| Limitations with Static Cursors  Advantage SQL Engine |  |  |  |  |

Advantage can optimize most SQL queries very well. There are a few types of queries that cannot be fully optimized, however. One class of statements are those that use scalar functions in the WHERE clause that cannot be mapped to an index. See [Indexes With Expressions](master_indexes_with_expressions.htm) for details on which scalars can be mapped to index expressions. For example,

SELECT \* FROM table WHERE COS( angle ) < 0

This query will result in a static cursor and will not be optimized by the SQL engine.

Another type of query that cannot be optimized is one that uses the LIKE operator with patterns that begin with the wildcard character. For example,

SELECT \* FROM employee WHERE lastname LIKE '%ins%'

This query requires the examination of all records because it is not feasible to index on all potential substrings of a character field.

In addition, some SQL statements cannot be fully optimized due to the nature of the SQL processing involved. For example, consider the following statement:

SELECT \* FROM smalltable a, largetable b WHERE ((a.empid < 5 ) OR ( b.lastname > 'Q' )) AND a.empid = b.empid

Assuming "smalltable" has fewer records than "largetable", "smalltable" will be placed first and used as the pivot table. The OR condition will be used to optimize the processing of "largetable" but will not be used when processing the smaller table. Each record of "smalltable" must be examined by this query because it is not possible to eliminate any records from that table without also examining each potential corresponding record of "largetable".

The optimization of the logical OR operator in the WHERE clause is dependent on every expression in the OR condition. An OR condition cannot be optimized using only part of the OR condition. It is optimized only if all expressions involved in the OR condition can be optimized. For example, the OR condition "Expr1 OR ( Expr2 AND Expr3 )" involves three expressions and the condition is only optimized if all three expressions can be optimized individually. The Advantage SQL engine can optimize an OR condition using available indexes only if all column references in the OR condition are from one table. The following is an example of an OR condition that can be optimized:

SELECT SUM( volume ) FROM orders WHERE salesid = 102 OR salesid = 103

The following is an example of an OR condition that cannot be optimized:

SELECT \* FROM orders, products WHERE orders.productID = product.productID OR orders.salesID = '102'

See [Subqueries](master_subqueries.htm) for information about optimization of static cursors that contain subqueries.