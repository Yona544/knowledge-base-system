6104 Invalid Password




Advantage Database Server 12  

6104 Invalid Password

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6104 Invalid Password  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6104 Invalid Password Advantage Error Guide error\_6104\_invalid\_password Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6104 Invalid Password  Advantage Error Guide |  |  |  |  |

Problem: The CA-Clipper RDD AX\_SetPassword function failed because the password given does not match the one used to encrypt the records in the current table.

Solution: Make sure the correct password is supplied to the function. Advantage allows one password per table. The encryption information is stored in the table header when the password is set on the table for the first time. The password is stored in encrypted form and it cannot be retrieved if forgotten.