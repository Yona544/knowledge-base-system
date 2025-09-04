7092 The index is not Advantage compatible




Advantage Database Server 12  

7092 The index is not Advantage compatible

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7092 The index is not Advantage compatible  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7092 The index is not Advantage compatible Advantage Error Guide error\_7092\_the\_index\_is\_not\_advantage\_compatible Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7092 The index is not Advantage compatible  Advantage Error Guide |  |  |  |  |

Problem: Advantage has detected that the index was not built with an Advantage-compatible format. This problem can occur if the original index was built with the CA-Clipper 5.3 DBFCDX RDD, which does not create FoxPro-compatible indexes.

Solution: Rebuild the index with Advantage. For example, open the table with Advantage Data Architect and click the re-index button, or choose Re-Index from the Table menu.

If you get this error when using the Advantage proprietary table format (.ADT/.ADI), report the error to Advnatage [Technical Support](master_technical_support_u_s__and_canada.htm).