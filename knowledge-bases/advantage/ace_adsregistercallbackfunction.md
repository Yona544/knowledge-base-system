AdsRegisterCallbackFunction




Advantage Database Server 12  

AdsRegisterCallbackFunction

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRegisterCallbackFunction  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRegisterCallbackFunction Advantage Client Engine ace\_Adsregistercallbackfunction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRegisterCallbackFunction  Advantage Client Engine |  |  |  |  |

Registers a callback function that the Advantage Client Engine can call during long operations for the purpose of cancellation or progress updates.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRegisterCallbackFunction(UNSIGNED32 (WINAPI \*lpfnCallback)  (UNSIGNED16 usPercent,  UNSIGNED32 ulCallbackID ),  UNSIGNED32 ulCallbackID); |

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRegisterCallbackFunction101(UNSIGNED32 (WINAPI \*lpfnCallback)  (UNSIGNED16 usPercent,  SIGNED64 qCallbackID ),  SIGNED64 qCallbackID); |

Parameters

|  |  |
| --- | --- |
| UNSIGNED32 (WINAPI \*lpfnCallback)  ( UNSIGNED16 usPercent,  UNSIGNED32 ulCallbackID ) | Pointer to a function to be called during long operations that can support callback functionality. The first parameter to the lpfnCallback function, usPercent, will contain the percentage of the current operation that is complete. The second parameter to the lpfnCallback function, ulCallbackID, will contain an ID for the thread that is making the current callback. This ID is the same value as passed to AdsRegisterCallbackFunction through its ulCallbackID parameter. The unsigned 32-bit return value indicates whether the current database operation should be aborted. A non-zero return value will abort the operation. |
| ulCallbackID (I) | Identification number to assign to this instance of registering the function. This is the callback ID that will be registered and consequently passed to the function pointed to by lpfnCallback during callbacks. |

|  |  |
| --- | --- |
| UNSIGNED32 (WINAPI \*lpfnCallback)  ( UNSIGNED16 usPercent,  SIGNED64 qCallbackID ) | Pointer to a function to be called during long operations that can support callback functionality. The first parameter to the lpfnCallback function, usPercent, will contain the percentage of the current operation that is complete. The second parameter to the lpfnCallback function, qCallbackID, will contain an ID for the thread that is making the current callback. This ID is the same value as passed to AdsRegisterCallbackFunction101 through its qCallbackID parameter. The signed 64-bit return value indicates whether the current database operation should be aborted. A non-zero return value will abort the operation. |
| qCallbackID (I) | Identification number to assign to this instance of registering the function. This is the callback ID that will be registered and consequently passed to the function pointed to by lpfnCallback during callbacks. |

Remarks

AdsRegisterCallbackFunction directs the Advantage Client Engine to call the registered function during operations that support callback functionality. For details about callback functionality, and for a list of functions/methods that support callback functionality, see [Callback Functionality](master_callback_functionality.htm).

A non-zero return value from the registered user function will cause the Advantage Client Engine to signal the current operation to abort. If an index creation operation is aborted by returning a non-zero value from the callback function, the indexes may be left in an unknown and incomplete state.

The registered callback function will not be called if it goes out of scope. The Advantage Client Engine will verify that it is a valid function pointer before calling it. The Advantage Client Engine uses exception handling when calling the user-supplied function to trap errors that may occur.

Note The registered callback function should not make any Advantage Client Engine calls. If it does it is possible to get error code 6619, "Communication Layer is busy".

The callback function is thread-specific and will be used for all applicable operations that are made on the thread in which the callback function is registered. If, for example, an application registers two different callback functions for two different threads and each thread then creates an index, the Advantage Client Engine will call the appropriate registered function for each thread.

It is also possible to use the same callback function for all threads by taking advantage of the callback ID when registering the callback function. Threads can do this by passing integer values (such as their thread IDs) through the ulCallbackID parameter when they register the callback function. All calls by the Advantage Client Engine to the registered callback function will then be made with the callback ID they were originally registered with. This allows the applications callback function to handle the callbacks for any number of threads based on the callback ID passed to it. The ability to differentiate within the callback function based on the callback ID is useful for applications that arent multi-threaded as well.

AdsRegisterCallbackFunction combines the functionality of the now obsolete AdsRegisterSQLAbortFunc and AdsRegisterProgressCallback APIs. Mixing usage of AdsRegisterCallbackFunction with the obsolete [AdsRegisterProgressCallback](ace_adsregisterprogresscallback.htm) or [AdsRegisterSQLAbortFunc](ace_adsregistersqlabortfunc.htm) APIs will result in the function registered with AdsRegisterCallbackFunction being called by the Advantage Client Engine and any other registered functions being cleared.

The syntax of the callback function to be registered must match the prototype defined as the first parameter of AdsRegisterCallbackFunction correctly. Specifically, be sure to define it as a WINAPI function.

The AdsRegisterCallbackFunction101 function is provided for 64 bit platforms so that a valid 64 bit pointer may be used as the callback ID.  Both the original (32 bit) and the new (64 bit) versions of this API behave the same except for the size of the callback ID value.

Linux Note Linux users should not use the WINAPI declaration in the declaration of their callback function. In linux your callback function should be of the form: UNSIGNED32 MyCallbackFunction( UNSIGNED16 usPercent, UNSIGNED32 ulCallbackID ).

 

CAUTION When using Advantage Local Server, the thread that calls the users registered callback function is the same thread that is performing the server operations (e.g., index creation, query execution, etc.). Because of this, it is important the applications registered callback function be as efficient as possible. For example, the callback function should not block and wait for user input because that would stop the Advantage Local Server progress until the callback function returns.

Example

/\*

\* This is the callback function we will register with

\* the Advantage Client Engine

\*/

UNSIGNED32 WINAPI MyCallbackFunction( UNSIGNED16 usPercentDone, UNSIGNED32 ulCallbackID ){

/\*

\* DoProgress() registered its index creation with a callback ID of 1.

\* If the index creation takes longer than 2 seconds to complete, the

\* Advantage Client Engine will call this function with a 1 passed in

\* for ulCallbackID and progress information in usPercentDone.

\*/

if ( ulCallbackID == 1 )

{

printf( "Thread %d\n", ulCallbackID );

printf( " Percent Complete: %d\n", usPercentDone );

return 0;

}

/\*

\* DoQueryCancel() registered its query with a callback ID of 2. \* If the query takes longer than 2 seconds to complete, the \* Advantage Client Engine will call this function with a 2 passed in \* for ulCallbackID. Percentage information is provided for long query

\* operations. gbCancelQuery is a global variable that determines

\* whether to cancel this query. \*/

if ( ulCallbackID == 2 )

{

if ( gbCancelQuery == TRUE )

{

printf( "Thread %d\n", ulCallbackID );

printf( " Query has been cancelled.\n" );

return 1;

}

else

{

printf( "Thread %d\n", ulCallbackID );

printf( " Percent Complete: %d\n", usPercentDone );

return 0; }

}

 

return 0;

 

} /\* MyCallbackFunction \*/

 

UNSIGNED32 DoQueryCancel( void )

{ ADSHANDLE hConnect;

ADSHANDLE hSQL;

ADSHANDLE hCursor;

UNSIGNED32 ulRetVal;

 

ulRetVal = AdsConnect( "x:\\data", &hConnection );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Create SQL Statement Handle to be used \*/

ulRetVal = AdsCreateSQLStatement( hConnect, &hSQL );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Prepare a statement handle to be executed with a named parameter \*/

ulRetVal = AdsPrepareSQL( hSQL, "SELECT \* FROM a, b WHERE a.pnum = b.pnum" );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\*

\* Register a callback function. This function will serve to cancel the

\* query should a global variable be set by some external function. It

\* will also report a long querys progress.

\*/

ulRetVal = AdsRegisterCallbackFunction( MyCallbackFunction, 2 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Execute the SQL statement \*/

ulRetVal = AdsExecuteSQL( hSQL, &hCursor );

 

/\* Clear the callback function for this thread \*/

AdsClearCallbackFunction();

 

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

} /\* DoQueryCancel \*/

 

UNSIGNED32 DoProgress( void )

{

ADSHANDLE hTable;

ADSHANDLE hIndex;

UNSIGNED32 ulRetVal;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "x:\\data\\test.dbf", "test", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE couldn't open table" );

return ulRetVal;

}

 

/\*

\* Register a callback function. This function will be called with

\* progress information during long indexing operations.

\*/

ulRetVal = AdsRegisterCallbackFunction( MyCallbackFunction, 1 );

 

if ( ulRetVal != AE\_SUCCESS )

printf( "Error %d when attempting to register callback function.\n",

ulRetVal );

 

/\* create an index \*/

ulRetVal = AdsCreateIndex( hTable, "x:\\data\\test", "test",

"firstname", NULL, NULL, ADS\_DEFAULT, &hIndex );

 

/\* Clear the callback function for this thread \*/

AdsClearCallbackFunction();

 

AdsCloseTable( hTable );

 

return ulRetVal;

} /\* DoProgress \*/

 

See Also

[AdsClearCallbackFunction](ace_adsclearcallbackfunction.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsReindex](ace_adsreindex.htm)