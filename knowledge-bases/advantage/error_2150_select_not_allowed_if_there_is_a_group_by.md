2150 SELECT \* not allowed if there is a GROUP BY




Advantage Database Server 12  

2150 SELECT \* not allowed if there is a GROUP BY

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2150 SELECT \* not allowed if there is a GROUP BY  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2150 SELECT \* not allowed if there is a GROUP BY Advantage Error Guide error\_2150\_select\_not\_allowed\_if\_there\_is\_a\_group\_by Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2150 SELECT \* not allowed if there is a GROUP BY  Advantage Error Guide |  |  |  |  |

Problem: An SQL statement used the \* token in a SELECT list when a GROUP BY clause was specified.

Solution: You must specifically name the columns in the SELECT list when a GROUP BY clause is used. The wildcard \* token is not allowed in that context.