7115 Unable to obtain OS file lock




Advantage Database Server 12  

7115 Unable to obtain OS file lock

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7115 Unable to obtain OS file lock  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7115 Unable to obtain OS file lock Advantage Error Guide error\_7115\_unable\_to\_lock\_file Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7115 Unable to obtain OS file lock  Advantage Error Guide |  |  |  |  |

Problem: Advantage server failed to obtain a lock on a file from OS. This error is returned by Advantage Local Server or Advantage Database Server with compatibility lock mode. In such environment, a lock requirement on an index file or a memo file can only be fully satisfied by obtaining a lock on the file from the OS. If the OS lock request fails for any reason, Advantage will retry the lock request for about 2 minutes. If the lock cannot be obtained after 2 minutes, the 7115 error is returned. A known case for this error is when the file is hosted on a Linux server and the Advantage process does not have sufficient permission to obtain the lock.

Solution: The problem can be avoided by using Advantage database server with proprietary locking when possible. If using compatibility locking or local server on Linux, make sure that the user (Advantage user on remote server) has read and write permission to the files.