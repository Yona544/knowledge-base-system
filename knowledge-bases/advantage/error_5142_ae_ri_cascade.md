5142 AE\_RI\_CASCADE




Advantage Database Server 12  

5142 AE\_RI\_CASCADE

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5142 AE\_RI\_CASCADE  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5142 AE\_RI\_CASCADE Advantage Error Guide error\_5142\_ae\_ri\_cascade Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5142 AE\_RI\_CASCADE  Advantage Error Guide |  |  |  |  |

Problem: The record update or delete failed because an existing referential integrity rule caused cascaded updates, and subsequent updates failed. The row that failed to update is a child in a different referential integrity rule. The updates produced a foreign key from the data in this row that does not have a corresponding key in the parent table. Note that these RI rules may cause cascaded updates: ADS\_DD\_RI\_CASCADE, ADS\_DD\_RI\_SETNULL, and ADS\_DD\_RI\_SET\_DEFAULT.

Solution: When this error occurs, retrieve the text error message that accompanies the error code. That text will include information about the row and RI rule that caused the failure.