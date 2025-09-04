6036 Encryption password does not exist




Advantage Database Server 12  

6036 Encryption password does not exist

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6036 Encryption password does not exist  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6036 Encryption password does not exist Advantage Error Guide error\_6036\_encryption\_password\_does\_not\_exist Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6036 Encryption password does not exist  Advantage Error Guide |  |  |  |  |

Problem: An encryption password did not exist in a work area and an operation requiring an encryption password was issued. Currently, functions that require encryption passwords are AX\_DBFEncrypt() and AX\_DBFDecrypt().

Solution: Make sure an encryption password is set in the work area before attempting a function requiring an encryption password.