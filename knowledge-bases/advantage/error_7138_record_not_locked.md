7138 Record Not Locked




Advantage Database Server 12  

7138 Record Not Locked

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7138 Record Not Locked  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7138 Record Not Locked Advantage Error Guide error\_7138\_record\_not\_locked Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7138 Record Not Locked  Advantage Error Guide |  |  |  |  |

Problem: The client sent an unlock request for a record that the server no longer had locked.

Solution: In most situations this is an acceptable error, and is only noted as a warning. If, however, this error is encountered along with other unexpected behavior, contact your Advantage technical support provider.

Acceptable Situations:

|  |  |
| --- | --- |
| 1. | A failed referential integrity update that was deleting records. |

|  |  |
| --- | --- |
| 2. | An AFTER DELETE or INSTEAD OF DELETE trigger returns an error. |