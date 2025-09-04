TABLE SCAN




Advantage Database Server 12  

TABLE SCAN, AOF SCAN

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TABLE SCAN, AOF SCAN  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - TABLE SCAN, AOF SCAN Advantage SQL Engine master\_Table\_scan Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TABLE SCAN, AOF SCAN  Advantage SQL Engine |  |  |  |  |

This row indicates the table is being scanned in natural order.  If the operator is TABLE SCAN, it means the entire table will be read because all the data is required or because the associated filter cannot be optimized. If the operator is AOF SCAN, then it indicates that a filter has been applied and is either fully or partially optimized. For example, if there is an applicable restriction such as join condition on this table, an Advantage Optimized Filter is applied to the table before the table is scanned. This row contains the following information:

|  |  |
| --- | --- |
| · | The StatementText contains information about the table being scanned including the table name and alias. |

|  |  |
| --- | --- |
| · | The Arguments column lists any restrictions that are applicable to this table along with optimization details described below. |

|  |  |
| --- | --- |
| · | The Warning column may indicate that restrictions on this table are not optimized, (i.e., the AOF being applied on the table is not fully optimized.) |

 

The Arguments column contains details about the AOF that is applied to the table. Some of the information supplied can help understand the optimization process. The individual filter segments of the AOF are listed in the order they are evaluated (if applicable) along with the index that is used to optimize the segment.  In addition, estimates and actual key counts are given if applicable.

Following is an example of the Arguments column text. In this example, the filter has five segments which are listed along with the index name that was chosen to optimize them.

The first segment (entry=4000) shows that the index named ENTRY is being used and that an estimated 10,998 keys would be read to resolve that portion of the filter and that 11,043 keys were actually read. Advantage uses the estimates to order the segment evaluation. In the following example, the last three segments were not evaluated because Advantage used the estimates (and index page sizes) to determine that it would be more costly to evaluate the remaining AOF segments than to read the records that passed the filtering of the first two segments. If a segment is not evaluated, the value is given as NA (not available). The very last segment in the example (date < STOD(20100427)) indicates that there was no index available to optimize the segment and, thus, the Estimate is also given as NA (not available). Note that even if an index is available, the Estimate may not be computed because it may not be necessary or because there are not enough rows in the table to warrant the estimation.

 

 AOF<entry = 4000 AND type = 0 AND comp = 100 AND processed = .T. AND date < STOD('20100427')>

 ====================

 AOF Optimization Details:

  Index: ENTRY, Expr: entry=4000, Estimate: 10998, Actual: 11043

  Index: TYPE, Expr: type=0, Estimate: 161722, Actual: 162393

  Index: PROCESSED, Expr: processed=.T., Estimate: 2744082, Actual: NA

  Index: COMP, Expr: comp=100, Estimate: 9623468, Actual: NA

  Index: <none>, Expr: date<STOD('20100427'), Estimate: NA, Actual: NA

 ====================

Note: The [LIKE](master_using_the_like_operator.htm) operator cannot be optimized or used in an AOF expression. Therefore when the SQL engine optimizes an SQL statement containing multiple operators such as a LIKE operator and an equality comparision operator (=), the portion with the equality operator will be optimized with an AOF expression, and the LIKE operator will be evaluated as a non-optimized filter.  But since it is not given to the AOF engine, the LIKE operator will not appear in the AOF SCAN results.

See Also

[AOF Optimization](master_aof_optimization.htm)

[SQL Execution Plan](master_sql_execution_plan.htm)