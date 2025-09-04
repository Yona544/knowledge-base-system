2210 Invalid index option




Advantage Database Server 12  

2210 Invalid index option

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2210 Invalid index option  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2210 Invalid index option Advantage Error Guide error\_2210\_invalid\_index\_option Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2210 Invalid index option  Advantage Error Guide |  |  |  |  |

Problem: An option in a CREATE INDEX statement was not valid.

Solution: Verify that the options specified in the CREATE INDEX statement are valid. If you specified options for creating a full text search index, verify that the keyword CONTENT is provided. If the CONTENT keyword is provided, verify that the UNIQUE and DESC keywords are not specified.