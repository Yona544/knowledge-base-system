2194 Unable to perform DISTINCT operation on some of the columns




Advantage Database Server 12  

2194 Unable to perform DISTINCT operation on some of the columns

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2194 Unable to perform DISTINCT operation on some of the columns  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2194 Unable to perform DISTINCT operation on some of the columns Advantage Error Guide error\_2194\_unable\_to\_perform\_distinct\_operation\_on\_some\_of\_the\_columns Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2194 Unable to perform DISTINCT operation on some of the columns  Advantage Error Guide |  |  |  |  |

Problem: The DISTINCT operation cannot be performed on some columns in the result set. DISTINCT operation will fail if the query contains any of the following column types in the result set: character or binary columns that are larger than 1 KB, or MEMO, BLOB, or VARCHAR columns.

Solution: Adjust the SELECT list so it does not include any offending column.