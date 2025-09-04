7039 File already open




Advantage Database Server 12  

7039 File already open

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7039 File already open  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7039 File already open Advantage Error Guide error\_7039\_file\_already\_open Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7039 File already open  Advantage Error Guide |  |  |  |  |

A sharing mode mismatch has occurred. Another user or connection has the file in question opened with a conflicting sharing mode.

Problem1: The user attempted to open a table or an index file for EXCLUSIVE use when another user already had the file open in SHARED mode.

Solution1: Determine which user(s) has the specified file open in SHARED mode and have that user(s) close the file before attempting to open the file for EXCLUSIVE use.

Problem2: The user attempted to open a table or an index file for SHARED use when another user already had the file open in EXCLUSIVE mode.

Solution2: Determine which user(s) has the specified file open in EXCLUSIVE mode and have that user(s) close the file before attempting to open the file

Problem3: The user attempted to open a table or an index file for EXCLUSIVE use when another user already had the file open in EXCLUSIVE mode.

Solution3: Determine which user(s) has the specified file open in EXCLUSIVE mode and have that user(s) close the file before attempting to open the file.

Problem4: The user attempted to open an index file that was already open on another table.

Solution4: A single index file can only be associated with one table. The error log's MORE\_INFO field will contain the name of the original table that opened the index.