SessionName




Advantage Database Server 12  

SessionName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SessionName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - SessionName Advantage TDataSet Descendant ade\_Sessionname Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SessionName  Advantage TDataSet Descendant |  |  |  |  |

The Advantage TDataSet Descendant does not support the concept of a session, nor does it need one. With a BDE dataset, the applications database connections, drivers, cursors, queries, and so on, are maintained within the context of one or more BDE sessions. This provides the ability to cross the multi-threaded boundaries with a BDE dataset. In Advantage, no "session" is necessary in order for all connections, tables, and index handles to be available across all threads.