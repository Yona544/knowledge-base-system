How Indexes are used by UPDATE, DELETE, and INSERT




Advantage Database Server 12  

How Indexes are Used by UPDATE, DELETE, and INSERT

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| How Indexes are Used by UPDATE, DELETE, and INSERT  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - How Indexes are Used by UPDATE, DELETE, and INSERT Advantage SQL Engine master\_How\_indexes\_are\_used\_by\_update\_delete\_and\_insert Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| How Indexes are Used by UPDATE, DELETE, and INSERT  Advantage SQL Engine |  |  |  |  |

DELETE and UPDATE statements also make use of indexes in much the same way when those statements have WHERE clauses. For example, the statement "update employee set salary = salary \* 1.05 where empid = 525" can be evaluated very efficiently if an index exists on the field "empid". If such an index does not exist, the server must read each record to determine which record matches the WHERE clause. If the index does exist, the associated AOF (and thus the SQL query) will be evaluated very quickly.

The efficiency of INSERT statements is not affected by the existence of indexes.