Building Multi-threaded Applications with TAdsQuery and TAdsTable




Advantage Database Server 12  

Building Multi-Threaded Applications with TAdsQuery and TAdsTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Building Multi-Threaded Applications with TAdsQuery and TAdsTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Building Multi-Threaded Applications with TAdsQuery and TAdsTable Advantage TDataSet Descendant ade\_Building\_multi\_threaded\_applications\_with\_tadsquery\_and\_tadstable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Building Multi-Threaded Applications with TAdsQuery and TAdsTable  Advantage TDataSet Descendant |  |  |  |  |

Both TAdsTable and TAdsQuery are safe to use in multi-threaded applications. Starting with version 2.6, table and query handles may be used across threads. For example, a TAdsQuery may be dropped on to a TDataModule (owned by the main application thread) and used within a secondary thread to execute a query. Unlike the BDE, TSession is not used in any part of the Advantage TDataSet Descendant solution. The table or query component is simply referenced or created in the TThread.Execute body.

The TAdsConnection.AdsServerTypes property allows the Advantage server type (Remote, Local, Internet) to be associated with a specific connection. This is useful when the application uses more than one server type. TAdsConnection components may be created either in the main thread by placing them on a TForm or TDataModule, or in the TThread.Execute body.

When building multi-threaded applications, it is important to note that all requests to any table or index associated to a single connection are synchronized. If multiple threads try to use a single connection simultaneously, all threads but one will be paused until the one has completed its task. If that task takes a long time, such as a lengthy SQL query or building an index, the other threads may be paused for an unacceptable time. To prevent threads from being paused, use separate TAdsConnection instances for any TAdsTable or TAdsQuery instances that will be used to perform operations that may take considerable time.

The following Advantage extended methods work on a thread level rather than globally.

[AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.htm)

[AdsGetLastError](ade_adsgetlasterror.htm)

[AdsClearCallbackFunction](ade_adsclearcallbackfunction.htm)

For example, if Thread A performs an operation on a TAdsTable instance and an error occurs, then only Thread A may call AdsGetLastError to retrieve the information for that error.

When assigning AdsConnections to AdsDataSet components, Advantage uses the following search order (with respect to the TAdsDataSet and all available TAdsConnections):

|  |  |
| --- | --- |
| 1. | Matching Name, ThreadID, Owner |

|  |  |
| --- | --- |
| 2. | Matching Name, ThreadID |

|  |  |
| --- | --- |
| 3. | Matching Name, Owner |

|  |  |
| --- | --- |
| 4. | Matching Name |