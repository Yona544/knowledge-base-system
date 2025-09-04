7055 Field size mismatch




Advantage Database Server 12  

7055 Field size mismatch

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7055 Field size mismatch  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7055 Field size mismatch Advantage Error Guide error\_7055\_field\_size\_mismatch Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7055 Field size mismatch  Advantage Error Guide |  |  |  |  |

Problem: A Copy To or Append From operation was attempted where the source table and the destination table contained numeric fields with the same name, but of different width or number of decimals.

Solution: Do not use source and destination tables that contain numeric fields with the same name but different width or decimals before attempting the Copy To or Append From operations.