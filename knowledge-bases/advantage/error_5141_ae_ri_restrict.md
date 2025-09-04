5141 AE\_RI\_RESTRICT




Advantage Database Server 12  

5141 AE\_RI\_RESTRICT

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5141 AE\_RI\_RESTRICT  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5141 AE\_RI\_RESTRICT Advantage Error Guide error\_5141\_ae\_ri\_restrict Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5141 AE\_RI\_RESTRICT  Advantage Error Guide |  |  |  |  |

Problem: The record update or delete failed because an existing referential integrity rule is set to RESTRICT. The row that failed to update may be a child in a different referential integrity rule that was enforced do to cascades.

Solution: When this error occurs, retrieve the text error message that accompanies the error code. That text will include information about the row and RI rule that caused the failure.