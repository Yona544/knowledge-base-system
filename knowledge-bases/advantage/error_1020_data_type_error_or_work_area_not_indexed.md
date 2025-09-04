1020 Data Type Error or Work Area not Indexed




Advantage Database Server 12  

1020 Data Type Error or Work Area not Indexed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1020 Data Type Error or Work Area not Indexed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 1020 Data Type Error or Work Area not Indexed Advantage Error Guide error\_1020\_data\_type\_error\_or\_work\_area\_not\_indexed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 1020 Data Type Error or Work Area not Indexed  Advantage Error Guide |  |  |  |  |

Problem 1: An invalid data type was assigned to a field in a table.

Solution 1: Correct the program. If assigning a value to a field in a table from some variable, make sure the variable has been initialized (i.e., is not NIL).

Problem 2: An operation, such as a Seek, was performed in the work area, but there was no index active.

Solution 2: Make sure that an index has been made active before performing the operation.