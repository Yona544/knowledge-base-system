How Indexes are Used in Joins




Advantage Database Server 12  

How Indexes are Used in Joins

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| How Indexes are Used in Joins  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - How Indexes are Used in Joins Advantage SQL Engine master\_How\_indexes\_are\_used\_in\_joins Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| How Indexes are Used in Joins  Advantage SQL Engine |  |  |  |  |

With joins, indexes are used in much the same fashion for optimization. For example, the query "select \* from customer left outer join orders on customer.id = orders.custid where customer.id = 22" is optimized most efficiently if indexes exist on the "id" field in the customer table and the "custid" field in the orders table. This is because the "id" index can be used to efficiently find "customer.id = 22". The SQL engine then uses the "custid" index on the orders table to find the matching record(s) for the join.