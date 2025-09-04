7111 The temporary table is in use




Advantage Database Server 12  

7111 The temporary table is in use

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7111 The temporary table is in use  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7111 The temporary table is in use Advantage Error Guide error\_7111\_the\_temporary\_table\_is\_in\_use Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7111 The temporary table is in use  Advantage Error Guide |  |  |  |  |

Problem: The temporary table is already in use. There are two possible causes for this error:

|  |  |
| --- | --- |
| a. | An attempt was made to open a temporary table as a regular table using the table path directly when the temporary table is already in use. Or |

|  |  |
| --- | --- |
| b. | An attempt was made to open a temporary table when the table has already been opened as a regular table using the table path directly. |

Solution: Avoid opening temporary tables as regular tables.