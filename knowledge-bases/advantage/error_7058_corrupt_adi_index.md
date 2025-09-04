7058 Corrupt ADI index




Advantage Database Server 12  

7058 Corrupt ADI index

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7058 Corrupt ADI index  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7058 Corrupt ADI index Advantage Error Guide error\_7058\_corrupt\_adi\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7058 Corrupt ADI index  Advantage Error Guide |  |  |  |  |

Problem: The current ADI index file contains corrupt or invalid data. It is possible that the index file was created with a version of Advantage Database Server greater than the version you are currently using. For example, if Advantage Database Server 7.0 or greater is used to build a full text search (FTS) index, it is not possible to open that index file with prior versions of Advantage.

Solution: Rebuild the index.