---
title: Ade Adsregistercallbackfunction
slug: ade_adsregistercallbackfunction
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsregistercallbackfunction.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9fc25cb6c5fefb6dd7c5c137bf8fc0530cb7e1ee
---

# Ade Adsregistercallbackfunction

AdsRegisterCallbackFunction

TAdsTable/TAdsQuery.AdsRegisterCallbackFunction

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsRegisterCallbackFunction  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md)

Registers a callback function that the Advantage Client Engine can call during long operations for the purpose of cancellation or progress updates.

type TCallbackFunction = function( usPercent: Word;

ulCallbackID: Longint ): Longint; stdcall;

 

procedure AdsRegisterCallbackFunction( Value: TCallbackFunction;

ulCallbackID: Longint );

| Value | Pointer to a function to be called during long operations that can support callback functionality. The first parameter to the TCallbackFunction, usPercent, will contain the percentage of the current operation that is complete. The second parameter to the TCallbackFunction, ulCallbackID, will contain an ID for the thread that is making the current callback. This ID is the same value as passed to AdsRegisterCallbackFunction through its ulCallbackID parameter. |
| ulCallbackID | An identification number to assign to this instance of registering the function. This is the callback ID that will be registered and consequently passed to the function pointed to by TCallbackFunction during callbacks. |

Description

AdsRegisterCallbackFunction directs the Advantage client to call the registered function during operations that support callback functionality. See [Callback Functionality](master_callback_functionality.md)for a list of functions/methods that support this feature.

A non-zero return value from the registered user function will cause the Advantage client to signal the current operation to abort. If an index creation operation is aborted by returning a non-zero value from the callback function, the indexes may be left in an unknown and incomplete state.

The registered callback function will not be called if it goes out of scope. The Advantage client will verify that it is a valid function pointer before calling it. The Advantage client uses exception handling when calling the user-supplied function to trap errors that may occur.

Note The registered callback function should not make any calls to Advantage methods or Advantage Client Engine APIs. If it does, it is possible to get error code 6619 "Communication Layer is busy".

The callback function is thread-specific and will be used for all applicable operations that are made on the thread in which the callback function is registered. If, for example, an application registers two different callback functions for two different threads and each thread then creates an index, the Advantage client will call the appropriate registered function for each thread.

It is also possible to use the same callback function for all threads by taking advantage of the callback ID when registering the callback function. Threads can do this by passing integer values (such as their thread IDs) through the ulCallbackID parameter when they register the callback function. All calls by the Advantage client to the registered callback function will then be made with the callback ID they were originally registered with. This allows the applications callback function to handle the callbacks for any number of threads based on the callback ID passed to it. The ability to differentiate within the callback function based on the callback ID is useful for applications that arent multi-threaded as well.

Note AdsRegisterCallbackFunction combines the functionality of the now obsolete TAdsQuery.AdsRegisterSQLAbortFunc and TAdsTable/TAdsQuery.AdsRegisterProgressCallback methods. Mixing usage of TAdsTable/TAdsQuery.AdsRegisterCallbackFunction with the obsolete TAdsTable/TAdsQuery.AdsRegisterProgressCallback or TAdsQuery.AdsRegisterSQLAbortFunc methods will result in the function registered with AdsRegisterCallbackFunction being called by the Advantage client and any other registered functions being cleared.

 

Note The syntax of the callback function to be registered must match the prototype defined by TCallbackFunction correctly. It is important that the callback function uses the Windows API style "stdcall" calling convention.

 

CAUTION When using Advantage Local Server, the thread that calls the users registered callback function is the same thread that is performing the server operations (e.g., index creation, query execution, etc.). Because of this, it is important the applications registered callback function be as efficient as possible. For example, the callback function should not block and wait for user input because that would stop the Advantage Local Server progress until the callback function returns.

Example

{\* this is the callback function we will register with Advantage.

\* NOTE: The global \*ThreadID variables are set in the Execute methods

\* of TMyThread1 and TMyThread2.

\*}

function MyCallbackFunc( usPercent: Word;

ulCallbackID: Longint ): Longint; stdcall;

begin

 

{\* If the callback ID is the same as the global thread then this

  \* callback is for showing progress information for an index creation.

  \*}

if gulBuildThreadID = ulCallbackID then

begin

  Form1.ProgressBar1.Position := usPercent;

  Result := 0;

end;

 

 {\* If the gbCancelQuery global variable is set, then a cancel has

\* been requested. Check to see if the global gulQueryThreadID

\* is set and that it is the same as our callback. If it is then

\* this thread is being targeted for cancellation.

\*}

 if gbCancelQuery then

 begin

   if gulQueryThreadID = ulCallbackID then

   Result := 1;

 end;

 

end;

 

 

procedure TMyThread1.Execute;

begin

{\* Register MyCallbackFunc for our callback function \*}

AdsTable1.AdsRegisterCallbackFunction( @MyCallbackFunc, TMyThread1.ThreadID );

 

{\* Set the global gulBuildThreadID to the value used as the Callback ID

  \* passed to AdsRegisterCallbackFunction.

  \*}

gulBuildThreadID := TMyThread1.ThreadID;

 

{\* Create a new index, it is possible for this to take a long time \*}

AdsTable1.AdsCreateIndex( '', strTag, strExpr, '', '', [optCOMPOUND] );

 

{\* Clear the callback function for this thread \*}

AdsTable1.AdsClearCallbackFunction;

end;

 

 

procedure TMyThread2.Execute;

begin

 {\* Register MyCallbackFunc for our callback function \*}

FOwnerForm.AdsQuery1.AdsRegisterCallbackFunction( @MyCallbackFunc, TMyThread2.ThreadID );

 

 {\* Set the global gulQueryThreadID to the value used as the Callback ID

  \* passed to AdsRegisterCallbackFunction.

  \*}

 gulQueryThreadID := TMyThread2.ThreadID;

 

 {\* Prepare and execute a query, this could potentially take a long time \*}

 FOwnerForm.AdsQuery1.SQL.Clear;

 FOwnerForm.AdsQuery1.SQL.Add( FOwnerForm.Edit1.Text );

 FOwnerForm.AdsQuery1.Active := TRUE;

 

 {\* Clear the callback function for this thread \*}

 FownerForm.AdsQuery1.AdsClearCallbackFunction;

end;

 

Note For more detailed examples go to the Delphi section of the Downloads area on the Advantage Developer Zone web site, (http://DevZone.AdvantageDatabase.com).

See Also

[AdsClearCallbackFunction](ade_adsclearcallbackfunction.md)

[AdsCreateIndex](ade_adscreateindex.md)

[AdsReindex](ade_adsreindex.md)
