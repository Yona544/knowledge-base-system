7073 The maximum number of memo blocks has been reached




Advantage Database Server 12  

7073 The maximum number of memo blocks has been reached

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7073 The maximum number of memo blocks has been reached  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7073 The maximum number of memo blocks has been reached Advantage Error Guide error\_7073\_the\_maximum\_number\_of\_memo\_blocks\_has\_been\_reached Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7073 The maximum number of memo blocks has been reached  Advantage Error Guide |  |  |  |  |

Problem: The number of blocks in the memo file has reached the 4,294,967,296 block (4 GB) limit.

Solution 1: Create a new table with the same structure as the table in question, but with a larger memo block size. Copy all data from the old table into the new table. See documentation in your client help file for more information on choosing a memo block size.

Solution 2: It is possible that memo blocks can be orphaned in memo files. Packing the table will free these orphaned blocks and allow them to be used again.