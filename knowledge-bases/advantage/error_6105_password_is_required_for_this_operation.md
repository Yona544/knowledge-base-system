6105 Password is required for this operation




Advantage Database Server 12  

6105 Password is required for this operation

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6105 Password is required for this operation  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6105 Password is required for this operation Advantage Error Guide error\_6105\_password\_is\_required\_for\_this\_operation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6105 Password is required for this operation  Advantage Error Guide |  |  |  |  |

Problem: Advantage CA-Clipper applications require that encryption be enabled via the correct password in order to update an encrypted record. This error is returned if an attempt is made to modify an encrypted record without encryption having been enabled.

Solution: Use the AX\_SetPassword function to enable encryption before attempting to modify the encrypted record.