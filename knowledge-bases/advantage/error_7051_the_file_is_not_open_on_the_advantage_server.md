7051 The file is not open on the Advantage server




Advantage Database Server 12  

7051 The file is not open on the Advantage server

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7051 The file is not open on the Advantage server  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7051 The file is not open on the Advantage server Advantage Error Guide error\_7051\_the\_file\_is\_not\_open\_on\_the\_advantage\_server Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7051 The file is not open on the Advantage server  Advantage Error Guide |  |  |  |  |

Problem: The file specified in an Advantage Management API is not currently open on the Advantage server.

Solution: Specify a file that is open on the Advantage server. The file name should be specified using the path that corresponds to the client making the Advantage Management API call. Look up the associated 7051 error in the Advantage error log file, and verify the filename in that log entry is what you expect it to be.