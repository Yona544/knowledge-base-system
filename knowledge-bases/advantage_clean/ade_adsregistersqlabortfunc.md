---
title: Ade Adsregistersqlabortfunc
slug: ade_adsregistersqlabortfunc
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsregistersqlabortfunc.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 7139d58225304a56618ea9200c0e23001a95e7e1
---

# Ade Adsregistersqlabortfunc

AdsRegisterSQLAbortFunc

TAdsQuery.AdsRegisterSQLAbortFunc

Advantage TDataSet Descendant

| TAdsQuery.AdsRegisterSQLAbortFunc  Advantage TDataSet Descendant |  |  |  |  |

Provides a callback function that the Advantage Client Engine can call to abort long SQL operations.

Note This API still functions as before, but is now obsolete. It is suggested that you use [AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.md) as it works better with threads and has more complete functionality.

Syntax

type TSQLAbortFunc = function: Longint ; stdcall;

 

procedure AdsRegisterSQLAbortFunc( Value : TSQLAbortFunc );

Parameter

| Value | Pointer to a function to be called during SQL query execution. |

Description

AdsRegisterSQLAbortFunc directs the Advantage Client Engine to call the given function during SQL query execution to abort the query if so desired. A non-zero return value from the registered user function will cause the Advantage Client Engine to send an abort signal to the server to abort the current query.

The Advantage client will call the registered callback function for the first time approximately two seconds after the server begins the operation it was registered for. The callback function will be called approximately every two seconds thereafter until the operation completes or is cancelled.

Note The registered function should not make any Advantage Client Engine calls. If it does, it is possible to get error code 6619 "Communication Layer is busy".

 

This function will not be called if it goes out of scope. The Advantage Client Engine will verify that it is a valid function pointer before calling it. The Advantage Client Engine uses exception handling when calling the user-supplied function to trap errors that may occur.

 

The registered function applies to all connections in the current thread. Therefore, if Query 1 is being run on Connection 1 which is running in Thread 1, and Query 2 is being run on Connection 2 which is running in Thread 2, they can each have their own SQL Abort functions because AdsRegisterSQLAbortFunc works per thread. And since there are two connections each in its own thread, the queries can be literally happening concurrently with their own SQL Abort functions.

Example

function MySQLAbortFunc : Longint ; stdcall;

begin

if ( gbCancelRequested ) then

Result := 1

else

Result := 0;

end;

 

procedure TForm1.RegisterButtonClick(Sender: TObject);

begin

AdsQuery1.AdsRegisterSQLAbortFunc( @MySQLAbortFunc );

end;

 

procedure TForm1.ClearButtonClick(Sender: TObject);

begin

AdsQuery1.AdsClearSQLAbortFunc;

end;

See Also

[AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.md)

[AdsClearCallbackFunction](ade_adsclearcallbackfunction.md)

[AdsClearSQLAbortFunc](ade_adsclearsqlabortfunc.md)
