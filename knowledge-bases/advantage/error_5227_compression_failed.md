5227 Compression Failed




Advantage Database Server 12  

5227 Compression Failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5227 Compression Failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5227 Compression Failed Advantage Error Guide Error\_5227\_compression\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5227 Compression Failed  Advantage Error Guide |  |  |  |  |

Problem: Error was encountered when compression or decompressing data.

Solution: The likely cause for this problem is attempting to updated a compressible blob field in chunks. Unlike regular blob field, compressed blob field can only be updated in whole. Other cause for this error is corrupted memo file.