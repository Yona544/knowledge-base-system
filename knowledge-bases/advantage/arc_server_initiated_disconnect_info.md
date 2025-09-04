Server Initiated Disconnect Info




Advantage Database Server 12  

Server Initiated Disconnect Info

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Server Initiated Disconnect Info |  |  | Feedback on: Advantage Database Server 12 - Server Initiated Disconnect Info arc\_Server\_initiated\_disconnect\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Server Initiated Disconnect Info |  |  |  |  |

A normal client disconnect consists of two steps initiated by the client: 1) the semaphore connection file is closed, and 2) a disconnect request is made. If a client PC crashes, is turned off without first logging off the network, or if the network goes down, a normal disconnect will not occur. The Advantage Database Server "watch dog" thread identifies the client is gone and disconnects the client automatically. This can also occur on a busy network when step 2 above is not immediately serviced after step 1 occurs.