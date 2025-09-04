How Indexes are Used by ORDER BY Clauses




Advantage Database Server 12  

How Indexes are Used by ORDER BY Clauses

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| How Indexes are Used by ORDER BY Clauses  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - How Indexes are Used by ORDER BY Clauses Advantage SQL Engine master\_How\_indexes\_are\_used\_by\_order\_by\_clauses Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| How Indexes are Used by ORDER BY Clauses  Advantage SQL Engine |  |  |  |  |

Existing indexes may be used to sort live cursors when the index expression matches the expression in the ORDER BY clause. For example, "select \* from employee order by lastname" will result in a live cursor that will use an index built on lastname if one exists. If such an index does not exist, a temporary one will be created by the server and deleted when the cursor is closed. If a specific query is common, it probably makes sense to create a permanent index on the field or fields used in the ORDER BY clause.