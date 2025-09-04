6031 No memo file




Advantage Database Server 12  

6031 No memo file

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6031 No memo file  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6031 No memo file Advantage Error Guide error\_6031\_no\_memo\_file Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6031 No memo file  Advantage Error Guide |  |  |  |  |

Problem: A memo file (DBT or FPT file) does not exist and an operation that requires a memo file was issued. Currently, functions that require a memo file to exist are AX\_BLOB2File() and AX\_File2BLOB().

Solution: Make sure the table being used also has a memo file before attempting an operation that requires a memo file.