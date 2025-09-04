7038 Invalid record number




Advantage Database Server 12  

7038 Invalid record number

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7038 Invalid record number  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7038 Invalid record number Advantage Error Guide error\_7038\_invalid\_record\_number Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7038 Invalid record number  Advantage Error Guide |  |  |  |  |

Problem: Attempted to read a record and the record number is greater than the number of records in the file. This error often results from using an index that contains more keys than the table has records. This can occur if a Pack or Zap is performed on the table when the index file(s) was closed.

Solution: Reposition to a valid record number. Reindex the index(es) that contain more keys than the table has records.