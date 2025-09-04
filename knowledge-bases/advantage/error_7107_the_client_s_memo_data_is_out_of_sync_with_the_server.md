7107 The client's memo data is out of sync with the server




Advantage Database Server 12  

7107 The client's memo data is out of sync with the server

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7107 The client's memo data is out of sync with the server  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7107 The client's memo data is out of sync with the server Advantage Error Guide error\_7107\_the\_client\_s\_memo\_data\_is\_out\_of\_sync\_with\_the\_server Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7107 The client's memo data is out of sync with the server  Advantage Error Guide |  |  |  |  |

Problem: Advantage server detected a mismatch between the client's expected memo or blob data length and the amount of actual available data. This error is possible with the Advantage thin clients, such as JDBC driver, when live/updateable result set (cursor) is used.

Solution: Refresh the client's record data after receiving this error to make it in sync with the server. To avoid this error, use static cursor.