7047 Invalid bits set in the deleted byte




Advantage Database Server 12  

7047 Invalid bits set in the deleted byte

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7047 Invalid bits set in the deleted byte  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7047 Invalid bits set in the deleted byte Advantage Error Guide error\_7047\_invalid\_bits\_set\_in\_the\_deleted\_byte Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7047 Invalid bits set in the deleted byte  Advantage Error Guide |  |  |  |  |

Problem: The "deleted" byte, which is the first byte in a table record that is used to indicate whether the record is marked for deletion or not, has bits set that are invalid for that byte. The previous log file entry contains the record number of the record that has invalid bits in its "deleted" byte.

Solution: Clear the invalid bits in the "deleted" byte. Open the table exclusively via a non-Advantage driver. Then loop through all records in the table re-marking all records for deletion that are currently marked for deletion and recalling all records that are not currently marked for deletion.