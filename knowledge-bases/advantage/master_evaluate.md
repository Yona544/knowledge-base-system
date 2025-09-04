EVALUATE




Advantage Database Server 12  

EVALUATE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EVALUATE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - EVALUATE Advantage SQL Engine master\_Evaluate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EVALUATE  Advantage SQL Engine |  |  |  |  |

The row represents the evaluation of the WHERE clause or HAVING clause in an SQL statement. The evaluation is performed on the result of a child operation. For this operator,

|  |  |
| --- | --- |
| · | •   The StatementText column indicates which clause is being executed. |

|  |  |
| --- | --- |
| · | •   The Arguments column provides the information on the expression being evaluated. |

|  |  |
| --- | --- |
| · | •   More than one child may have this row as the parent row. The child with the lowest value in the NodeID column supplies the simple values in the expression. Any child rows with the higher values in the NodID column contain execution plans for subqueries in the expression. |

|  |  |
| --- | --- |
| · | •   The Warning column may indicate that a [correlated subquery](master_subqueries.htm) is part of the evaluation clause and may contribute to poor performance. |

See Also

[How Indexes are Used by the WHERE Clause](master_how_indexes_are_used_by_the_where_clause.htm)