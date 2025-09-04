7150 Collation Is Corrupt




Advantage Database Server 12  

7150 Collation Is Corrupt

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7150 Collation Is Corrupt  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7150 Collation Is Corrupt Advantage Error Guide error\_7150\_collation\_is\_corrupt Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7150 Collation Is Corrupt  Advantage Error Guide |  |  |  |  |

Problem: An attempt to load a [dynamic collation](master_collation_support.htm) failed because the information in the collation repository did not contain the expected data.

Solution: When Advantage loads a dynamic collation from the repository (adscollate.adt and adscollate.adm), it verifies that the information is consistent. If it finds a problem with the collation information, it will log this error. To resolve this error, you will need to replace adscollate.adt and adscollate.adm with valid copies of the files.