7057 Record update failed




Advantage Database Server 12  

7057 Record update failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7057 Record update failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7057 Record update failed Advantage Error Guide error\_7057\_record\_update\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7057 Record update failed  Advantage Error Guide |  |  |  |  |

Problem: The key value produced from this record was not unique, and the index for the current table has the UNIQUE property.

Solution: Replace the key value field(s) with a unique value(s). If this is not possible, cancel the operation. When using the Advantage Client Engine API directly, call AdsCancelUpdate. When using the Advantage TDataSet Descendant, use the TTable.Cancel method.