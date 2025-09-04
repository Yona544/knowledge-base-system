Small Result Sets with Large Tables




Advantage Database Server 12  

Small Result Sets with Large Tables

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Small Result Sets with Large Tables  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Small Result Sets with Large Tables Advantage SQL Engine master\_Small\_result\_sets\_with\_large\_tables Advantage SQL > SQL Performance > Small Result Sets with Large Tables / Dear Support Staff, |  |
| Small Result Sets with Large Tables  Advantage SQL Engine |  |  |  |  |

Generally, performance of SQL queries that result in live cursors can be improved by maintaining a permanent index to be used with an ORDER BY clause. However, there is a case where it is more efficient to allow Advantage to build a temporary index. That situation is when the resulting rowset is very small in relation to the base table size. In that case, the index on the base table would be used and potentially a lot of time can be spent traversing the larger index. If a temporary index was used, the index would be built on the resulting rowset, and only those records would be represented in the index. Logic has been added to the Advantage SQL Query engine that may automatically build a temporary index on the result sets that are small compared to the base table size.

Experimentation will help determine when a temporary index should be used. A temporary index can be forced by having the ORDER BY clause be for an order that does not cause an existing, permanent index to be used.

For example, if the query "select \* from employee where empid < 500 order by lastname" is performed on a table that contains 1,000,000 records, the following can be done to potentially increase performance:

|  |  |
| --- | --- |
| · | •   An index on empid will allow the Cursor AOF to rapidly select the correct records. |

|  |  |
| --- | --- |
| · | •   An index on lastname could slow down the ORDER BY if the result set size was above the limit used by the Advantage SQL Query engine. |

|  |  |
| --- | --- |
| · | •   If an index on lastname existed, the ORDER BY clause could be "order by lastname, firstname" so that a temporary new index on lastname+firstname is used instead of the existing index on lastname. |