AdsRegisterSQLAbortFunc




Advantage Database Server 12  

AdsRegisterSQLAbortFunc

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRegisterSQLAbortFunc  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRegisterSQLAbortFunc Advantage Client Engine ace\_Adsregistersqlabortfunc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRegisterSQLAbortFunc  Advantage Client Engine |  |  |  |  |

Provides a callback function that the Advantage Client Engine can call to abort long SQL operations.

Note This API still functions as before, but is now obsolete. It is suggested you use [AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.htm) as it works better with threads and has more complete functionality.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRegisterSQLAbortFunc(UNSIGNED32(WINAPI \*lpfnCallback) () ); |

Parameters

|  |  |
| --- | --- |
| \*lpfnCallback (I) | Pointer to a function to be called during SQL query execution. |

Remarks

AdsRegisterSQLAbortFunc directs the Advantage Client Engine to call the given function during SQL query execution to abort the query if so desired. A non-zero return value from the registered user function will cause the Advantage Client Engine to send an abort signal to the server to abort the current query.

The Advantage Client Engine will call the registered callback function for the first time approximately two seconds after the server begins the operation it was registered for. The callback function will be called approximately every two seconds thereafter until the operation completes or is cancelled.

The registered function should not make any Advantage Client Engine calls. If it does, it is possible to get error code 6619 "Communication Layer is busy".

This function will not be called if it goes out of scope. The Advantage Client Engine will verify that it is a valid function pointer before calling it. The Advantage Client Engine uses exception handling when calling the user-supplied function to trap errors that may occur.

The registered function applies to all connections in the current thread. Therefore, if Query 1 is being run on Connection 1 that is running in Thread 1, and Query 2 is being run on Connection 2 that is running in Thread 2, they can each have their own SQL Abort functions because AdsRegisterSQLAbortFunc works per thread. In addition, because each query has two connections in its individual thread, the queries can be literally happening concurrently with their own SQL Abort functions.

See Also

[AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.htm)

[AdsClearCallbackFunction](ace_adsclearcallbackfunction.htm)

[AdsClearSQLAbortFunc](ace_adsclearsqlabortfunc.htm)