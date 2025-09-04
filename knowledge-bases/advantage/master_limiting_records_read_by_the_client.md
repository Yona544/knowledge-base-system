Limiting Records Read by the Client




Advantage Database Server 12  

Limiting Records Read by the Client

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Limiting Records Read by the Client  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Limiting Records Read by the Client Advantage SQL Engine master\_Limiting\_records\_read\_by\_the\_client Advantage SQL > SQL Performance > Limiting Records Read by the Client / Dear Support Staff, |  |
| Limiting Records Read by the Client  Advantage SQL Engine |  |  |  |  |

Another way to increase performance is by not pulling all the records of the result set back to the client, if it is not necessary. This decision might be based on the underlying development tool. If there is a way for the application to limit the rowset from all being returned, that will help performance.

A specific example is in the use of client-side cursors. ADO (ActiveX Data Objects) supports both client-side and server-side cursors. When an application requests a client-side cursor through ADO, it reads the entire rowset as soon as it is opened. While there are certain benefits to this for some applications, it can be expensive for large tables especially if only part of the rowset is actually needed. With server-side cursors, the data is read only as needed.