---
title: Master Callback Functionality
slug: master_callback_functionality
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_callback_functionality.htm
source: Advantage CHM
tags:
  - master
checksum: df6327fcacd25d163f96c9602e25d6caad71b07f
---

# Master Callback Functionality

Callback Functionality

Callback Functionality

Advantage Concepts

| Callback Functionality  Advantage Concepts |  |  |  |  |

The Advantage Database Server and Advantage Local Server are both capable of callback functionality. Callback functionality provides a way for the client to keep track of any progress the server has made as well as allowing cancellation support for applications using Advantage. This is especially helpful in applications that execute lengthy operations, both for the feedback on current progress and the ability to stop an operation that is taking too long.

Callback functionality is supported in the Advantage Client Engine API as well as the Advantage TDataSet Descendant. Any Advantage database operation that is capable of using callback functionality will have a note stating so in its Help documentation. These functions are generally supported because they are capable of taking significant amounts of time to complete due to very large datasets, complex computations, considerable disk I/O, or combinations of these.

Callback Functions

All applications written to support callback functionality must have a callback function. This function is written by the developer and must be registered within the Advantage Client Engine before any operations that support callbacks can access this functionality. Once a callback function is registered, the Advantage Client Engine will call that function directly whenever it receives progress information from the server, passing the servers information to the application. Callback functions are also required to have a return value. This value is passed back to the Advantage Client Engine, which uses it as a flag to let the server know whether to continue its current operation or to abort the operation. Once an operation has completed, the callback function should typically be cleared.

Callback functions for the Advantage Client Engine API and the Advantage TDataSet Descendant work similarly. For instance, a prototype for a Delphi callback function might look like this:

 

type TCallbackFunction = function( usPercentDone: Word; ulCallbackID: Longint ): Longint; stdcall;

 

Where a C/C++ application using the Advantage Client Engine API might look like this:

 

UNSIGNED32 WINAPI MyCallbackFunction( UNSIGNED16 usPercentDone,UNSIGNED32 ulCallbackID )

 

Both return 32-bit integers and have two parameters consisting of a 16-bit integer and a 32-bit integer. Both also use the stdcall and WINAPI calling conventions that control the order in which parameters are read and who cleans up the stack. This should not affect the developer, however, as long as the callback function is declared with the same calling conventions.

As mentioned above, the return value is used as a flag for the Advantage server signifying whether or not to continue the operation for which the callback function is registered. Non-zero values will cause the server to abort that operation. For example, if a callback function was registered before executing a query, and at some point the callback function is called and returns a non-zero value, the server will stop executing the query and return a 7209 error to the client. This error signifies that the server was told to abort its operation. Similar errors are returned to the client from the server when other types of operations are aborted. More detail on these is discussed below.

The two parameters in the callback function are input parameters. When the Advantage Client Engine calls the callback function, it passes values in through these parameters. The usPercentDone parameter will contain progress information. This is how much progress the server has completed for its current operation. The second parameter, ulCallbackID, is a means for the Advantage Client Engine to pass information to the applications callback function. This can be used in many different ways, but is primarily used for identifying which operation is making the callback. More detail on the usage of this parameter is provided below.

Registering and Clearing the Callback Function

Registering and clearing the callback function is simple. In both the Advantage Client Engine API and the Advantage TDataSet Descendant, the Advantage function used to register a callback function is named AdsRegisterCallbackFunction. Specific information about AdsRegisterCallbackFunction can be found in the respective Help files for the development environments mentioned previously. To clear a registered callback function, see AdsClearCallbackFunction.

There are three main parts to registering a callback function for a particular database operation. These include:

- Registering the applications callback function using AdsRegisterCallbackFunction

- Calling the Advantage function that the callback function was registered for (the database operation that will be reporting progress or that might need canceling)

- Clearing the applications callback function using AdsClearCallbackFunction after the operation has completed or been canceled

Examples are included in the AdsRegisterCallbackFunction documentation. There is also a demonstration written in Delphi for using callback functionality available in the Delphi section of the Downloads page on the Advantage Developer Zone Web site, (http://DevZone.AdvantageDatabase.com).

Caveats of Using Callback Functionality

- The Advantage server only reports progress to the client approximately every 2 seconds. If the database operation takes less than 2 seconds to complete, no progress callback information will be returned to the client.

- The Advantage Client Engine will call the registered callback function immediately upon receiving progress information from the server.

- When using Advantage Local Server, it is important for the callback function written by the developer to be as efficient as possible. This is because the thread that is performing the database operation is the same thread that executes the callback function every 2 seconds. This behavior does not occur with Advantage Database Servers due to their client/server nature.

- Registering a callback function will have no effect on the speed of that operation. Therefore, application performance will not suffer when using callback functionality.

- If callback functionality is used during the creation of an index, and that index creation operation is aborted by returning a non-zero value from the callback function, the indexes may be left in an unknown and incomplete state.

- In most cases there is no guarantee that a callback to the registered callback function will be made with 0 in the percentage parameter when the operation begins or 100 in the percentage parameter when the operation finishes. It is up to the developer to initialize percentages to 0 before beginning a database operation and then handle final progress information upon the operation completing.

- Two other register callback functions exist for registering callback functions, AdsRegisterProgressCallback and AdsRegisterSQLAbortFunc. These functions are considered obsolete and should not be used. They are still maintained for backwards compatibility. Should one of these functions be used to register a callback function, and then AdsRegisterCallbackFunction is used as well, the obsolete register function will have its callback function automatically cleared. Calling one of the obsolete register functions will not clear a callback function registered with AdsRegisterCallbackFunction.

Operations Supporting Callback Functionality

The following tables outline the functions that currently support callback functionality as well as any special behavioral notes.

| Advantage Client Engine API | Special Behavior Notes\* |
| AdsCreateIndex | 1 |
| AdsReindex | 1 |
| AdsPackTable | 1,2 |
| AdsExecuteSQL | 4 |
| AdsExecuteSQLDirect | 4 |
| AdsGotoBookmark | 3,4 |
| AdsGotoBookmark60 | 3,4 |
| AdsGotoBottom | 3,4 |
| AdsGetRecordCount | 3,4 |
| AdsSkip | 3,4 |
| AdsCopyTable | 5 |
| AdsCopyTableContents | 5 |
| AdsConvertTable | 5 |

| Advantage TDataSet Descendant | Special Behavior Notes\* |
| TAdsTable/TAdsQuery.AdsCreateIndex | 1 |
| TAdsTable.AdsReindex | 1 |
| TAdsTable.AdsPackTable | 1,2 |
| TAdsQuery.ExecSQL | 4 |
| TAdsQuery.ExecSQLScript | 4 |
| TAdsTable.AdsGotoBookmark | 3,4 |
| TAdsTable/TAdsQuery.GotoBookmark | 3,4 |
| TAdsTable.AdsGotoBottom | 3,4 |
| TAdsTable/TAdsQuery.Last | 3,4 |
| TAdsTable.AdsGetRecordCount | 3,4 |
| TAdsTable.RecordCount | 3,4 |
| TAdsTable.AdsSkip | 3,4 |
| TAdsTable/TAdsQuery.Next | 3,4 |
| TAdsTable/TAdsQuery.Prior | 3,4 |
| TAdsTable/TAdsQuery.AdsCopyTable | 5 |
| TAdsTable/TAdsQuery.AdsCopyTableContents | 5 |
| TAdsTable/TAdsQuery.AdsConvertTable | 5 |

\* Special Behavior Notes

| 1. | This operation is guaranteed to return 100 in the percent parameter upon completion. |

| 2. | This operations callback functionality is only available during its index build portion. |

| 3. | This operation only has callback functionality when registered for use with a static cursor that is not fully populated. |

| 4. | See the section below on Callback Functionality with Queries. |

| 5. | See the section below on Callback Functionality with Copy Table Operations. |

Callback Functionality with Index Creation

When registering a callback function for creating a compound index (the index file contains multiple index orders), progress wont be reported over the entire file. Instead, progress information will advance towards 100 for each individual index order within the compound index, starting over for each additional index that is built. If an index creation operation is aborted by returning a non-zero value from the callback function, the indexes may be left in an unknown and incomplete state.

Callback Functionality with Queries

Providing progress information for a query is a complicated process. Queries are often non-deterministic in nature and calculating the length of time a query will take is often impossible until the query has completed, hardly useful by that point. Advantages query engine attempts to estimate how much of the query is complete throughout its execution. Optimizations within the query engine can lead to erratic progress information as short-circuiting eliminates unneeded processing. The 2-second pause between callbacks will smooth out most of this behavior, but slow progress followed by sudden completion, or the alternative, fast progress followed by relatively slow progress can still occur.

Callback functionality for queries will behave differently depending on the type of query and the resulting cursor type.

As far as progress functionality is concerned, there are 3 types of resulting cursors:

- Live cursors

- Static cursors that are not fully populated when the query is first executed

- Static cursors that are fully populated when the query is first executed

Queries that result in a live cursor are always fast except when they contain an ORDER BY clause. An ORDER BY clause can cause an index to be built on the resulting record set if no existing applicable index exists, and depending on the number of records in the resulting cursor, it could take a significant amount of time.

Advantage can optimize many static cursors by not fully populating them when the query is first executed. The server can often send records in a static cursor a few at a time to the client without having to populate the entire cursor, thus saving time and cutting down on network traffic. Should the client perform an operation that requires further populating the result set, it will let the server know and make a request for those records. This static cursor optimization means the original "execute SQL query" operation will return relatively quickly, and the last progress callback from the server (if there even was one) will report only a portion of the total progress as being complete. This is because populating the static cursor with records is the most expensive part of a query, and hence progress is tied mostly to the populating of the cursor. Record movement operations on the resulting dataset will cause further cursor population to occur, increasing the callback progress value until the entire cursor has been populated.

Some static cursors will be fully populated when the SQL query is first executed. These static cursors will report all their progress in the "execute SQL query" operation. Some static cursors are fully populated when the query is first executed because in order for the query to finish, the server must calculate every record that belongs in the cursor. This is usually associated with sorting the records within the cursor since the server cannot determine the final order until the cursor has been fully populated.

Progress information coupled with cancellation functionality allows one the ability to quickly recognize a query is taking an excessive amount of time, in which case it can be cancelled.

Callback Functionality with Copy Table Operations

The copy table operations, AdsCopyTable, AdsCopyTableContents, and AdsConvertTable, support callback functionality. This allows progress information to be provided when copying large data sets. A special note about using this functionality is when the data set being copied is a cursor from a query. If it is a static cursor that isnt fully populated, doing a copy table operation will result in the percentage information advancing towards 100 while the cursor is populated before beginning the copy. When the cursor is fully populated, the percentage information will start over at 0 and advance towards 100 for a second time while the records are copied to the destination table.

AdsCopyTable and AdsConvertTable create destination tables from scratch. Therefore, should these operations be canceled while performing their copy operation, any destination table that was created will be deleted.

AdsCopyTableContents appends records from a source table to a pre-existing destination table. Therefore, if AdsCopyTableContents is canceled during its copy table operation, it will not delete the destination table. However, the destination table will contain whatever records were copied to it before the copy operation was aborted.

Usage of the Callback ID Parameter and Threads

The callback ID parameter in AdsRegisterCallbackFunction is used to differentiate between separately registered database operations making callbacks to the same registered callback function. The following are examples of how the callback ID can be used:

Example 1

A developer can have several different callback functions registered based on the operation type. If the operation is an index creation, a function (e.g., MyIndexBuildCallback) can be registered before beginning any index creation operations. Alternatively, another function (e.g., MyQueryCallback) can be registered before any SQL query is executed, or any operation is performed that might cause a partially populated static cursor to be populated further. In this particular example, there is no need for the callback ID parameter as separate callback functions are registered for different operations.

Example 2

Expanding on Example 1, consider if the developers application is multi-threaded. It is possible for multiple threads to execute multiple queries concurrently. In this case, when a thread is about to execute a query and registers MyQueryCallback with AdsRegisterCallbackFunction, a unique number (e.g., the threads ID) can be passed in AdsRegisterCallbackFunctions callback ID parameter. From then on until MyQueryCallback is cleared via AdsClearCallbackFunction, the callback ID that MyQueryCallback was registered with will be passed to MyQueryCallback through its callback ID parameter. This way MyQueryCallback can tell which thread is making the callback even if two separate queries are executing in separate threads and are making callbacks to MyQueryCallback at the same time.

Example 3

Expanding even further, lets say the developer only wants to register one callback function called MyCallbackFunction. This single callback function can be used for all callbacks in the application, and functionality will change based on many different factors at the time MyCallbackFunction is called. Because the callback ID parameter is a 4-byte integer, it can be used to pass a pointer. The developer can define a structure that contains all the information relative to the callback function, fill in the data before registering MyCallbackFunction, and then pass a pointer to the structure rather than a single number in the callback ID parameter. Then when MyCallbackFunction is called, it can access the structure for the information on how it should behave for this particular callback. There is a specific demonstration written in Delphi that shows how to do this in the Delphi section of the Downloads page on the Advantage Developer Zone Web site, (http://DevZone.AdvantageDatabase.com).

Error Codes

The following error codes will be returned to the client whenever a user cancels an operation that supports callback functionality:

7089 The index creation was aborted by the user.

7090 The copy table operation was aborted by the user.

7209 The query was aborted by the user.
