5208 AE\_KEY\_CANNOT\_BE\_NULL




Advantage Database Server 12  

5208 AE\_KEY\_CANNOT\_BE\_NULL

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5208 AE\_KEY\_CANNOT\_BE\_NULL  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5208 AE\_KEY\_CANNOT\_BE\_NULL Advantage Error Guide error\_5208\_ae\_key\_cannot\_be\_null Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5208 AE\_KEY\_CANNOT\_BE\_NULL  Advantage Error Guide |  |  |  |  |

Problem: A field value was modified such that it resulted in a NULL key value, but the index does not allow NULL values. This can happen with candidate indexes created on Visual FoxPro tables.

Solution: Change the data so that it does not result in a NULL key value or cancel the update.