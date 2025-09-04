Expression Engine Performance




Advantage Database Server 12  

Expression Engine Performance

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Expression Engine Performance  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Expression Engine Performance Advantage Concepts master\_Expression\_engine\_performance Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Expression Engine Performance  Advantage Concepts |  |  |  |  |

When the Advantage server builds an index, the operation is performed using one thread on the server. The thread is not relinquished until index building is complete. If the number of indexes being built at any one time is equal to the number of threads configured with the Advantage server, other Advantage users' operations will be held off until an index creation completes. A thread is then released and other operations may be executed. If operations are being held off, increase the thread count. See the Advantage Database Server guide for information about how to change the Advantage server thread count parameter.