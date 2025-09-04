7144 Collation Repository Not Found




Advantage Database Server 12  

7144 Collation Repository Not Found

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7144 Collation Repository Not Found  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7144 Collation Repository Not Found Advantage Error Guide error\_7144\_collation\_repository\_not\_found Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7144 Collation Repository Not Found  Advantage Error Guide |  |  |  |  |

Problem: Advantage was not able to find the collation repository that stores the [dynamic collations](master_collation_support.htm).

Solution: The collation repository is an ADT table named adscollate.adt with an associated memo file named adscollate.adm. It should reside in the same directory as the Advantage Database Server binary image (e.g., ads.exe, libadsd.so, etc.). When using Advantage Local Server, adscollate.adt must be found in the path (normally it would be in the same directory as the adslocal.cfg file).