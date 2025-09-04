7071 File is too large to be opened with the given settings




Advantage Database Server 12  

7071 File is too large to be opened with the given settings

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7071 File is too large to be opened with the given settings  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7071 File is too large to be opened with the given settings Advantage Error Guide error\_7071file\_is\_too\_large\_to\_be\_opened\_with\_the\_given\_settings Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7071 File is too large to be opened with the given settings  Advantage Error Guide |  |  |  |  |

Problem: An open table greater than 4GB in size was attempted with compatibility locking. Due to lock offsets required to implement record locking that can be shared across applications (either non-Advantage applications or applications that use Advantage Local Server), the table cannot be opened.

Solution: If you are using Advantage Database Server, open the table with [proprietary locking](master_advantage_proprietary_locking.htm). With Advantage Local Server, it is necessary to open the table in exclusive mode.

Note For information about table sizes with each operating system, see [Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.htm).