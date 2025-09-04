6634 The inter-process communications (IPC) object is no longer valid




Advantage Database Server 12  

6634 The inter-process communications (IPC) object is no longer valid

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6634 The inter-process communications (IPC) object is no longer valid  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6634 The inter-process communications (IPC) object is no longer valid Advantage Error Guide error\_6634\_the\_inter\_process\_communications\_ipc\_object\_is\_no\_longer\_valid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6634 The inter-process communications (IPC) object is no longer valid  Advantage Error Guide |  |  |  |  |

Problem: This error indicates that the connection to the server has been lost while using inter-process communications. The communications channel has been given to another client.

Solution: Close the connection and open a new one. It is expected that this error would only occur if the server was stopped and restarted while the client was still running.