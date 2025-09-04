INDEX SCAN




Advantage Database Server 12  

INDEX SCAN

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| INDEX SCAN  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - INDEX SCAN Advantage SQL Engine master\_Index\_scan Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| INDEX SCAN  Advantage SQL Engine |  |  |  |  |

A table is being scanned in indexed order using a [scope](master_index_scopes_ranges.htm). This is generally the most efficient method for returning a subset of rows from a table predicating on restrictions on column values in the table. For example, suppose the restriction is "customer\_id = 222" and an index exists on the customer\_id column in the table, a scope with the top value of 222 and a bottom value of 222 can be applied using the index to quickly limit the set of rows returned. For this operator,

|  |  |
| --- | --- |
| · | •   The StatementText contains the following information about the table and the index: |

|  |  |
| --- | --- |
| · | •   Table Name |

|  |  |
| --- | --- |
| · | •   Table Alias |

|  |  |
| --- | --- |
| · | •   Tag Name |

If the query engine determines that a new index is needed to optimize the query the "Tag Name" will be "Temp".

|  |  |
| --- | --- |
| · | •   The Arguments column lists any restrictions that are optimized using the index. |

|  |  |
| --- | --- |
| · | •   The Warning column may indicate that no existing index is available to optimize restriction and the Advantage SQL engine must build an index each time the statement is executed. |

See Also

[How Indexes are Used by ORDER BY Clauses](master_how_indexes_are_used_by_order_by_clauses.htm)