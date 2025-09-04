7013 Advantage server file access error




Advantage Database Server 12  

7013 Advantage server file access error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7013 Advantage server file access error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7013 Advantage server file access error Advantage Error Guide error\_7013\_advantage\_server\_file\_access\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7013 Advantage server file access error  Advantage Error Guide |  |  |  |  |

Problem 1: The user does not have sufficient access rights to open the specified file.

Solution 1: If you are using the Advantage Database Server for Windows, and your data files are located on a drive using NTFS, that PCs "system" group must have full access to the share that contains the data in order for the Advantage Database Server service to have access to that data. Note that it must be that PCs system group that has full access, not the domains system group.

Problem 2: The file(s) is marked read-only.

Solution 2: Remove the read-only attribute on the file(s).