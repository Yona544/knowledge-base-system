---
title: Ade Adsregisterprogresscallback
slug: ade_adsregisterprogresscallback
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsregisterprogresscallback.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4e5c9c567a5b4429554ec404750ee507e0b13dc0
---

# Ade Adsregisterprogresscallback

AdsRegisterProgressCallback

TAdsTable/TAdsQuery.AdsRegisterProgressCallback

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsRegisterProgressCallback  Advantage TDataSet Descendant |  |  |  |  |

Provides a callback function that the Advantage Client Engine can call during long index operations.

Note This API still functions as before, but is now obsolete. It is suggested that you use [AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.md) as it works better with threads and has more complete functionality.

Syntax

type TProgressCallback = function( usPercent: Word ): Longint ; stdcall;

 

procedure AdsRegisterProgressCallback( Value : TProgressCallback );

Parameter

| Value | Pointer to a function to be called during index builds. usPercent will contain the percentage of the current operation that is complete. |

Description

AdsRegisterProgressCallback makes the Advantage Client Engine call the given function during index builds or reindexing to provide a measure of progress.

The Advantage client will call the registered callback function for the first time approximately two seconds after the server begins the operation it was registered for. The callback function will be called approximately every two seconds thereafter until the operation completes or is cancelled. At either of these points, one final call to the callback function is made with a value of 100 contained in usPercent.

A non-zero return value from the registered user function will cause the Advantage Client Engine to send an abort signal to the server to stop the current operation.

Note The user must be aware that this function will not be called if it goes out of scope. The Advantage Client Engine will verify that it is a valid function pointer before calling it. The Advantage Client Engine uses exception handling when calling the user-supplied function to trap errors that may occur.

 

Note The registered function should not make any Advantage Client Engine calls. If it does, it is possible to get error code 6619 "Communication layer is busy".

Example

function MyCallbackFunc( usPercent: Word ): Longint ; stdcall;

begin

if ( gbCancelRequested ) then

Result := 1

else

Result := 0;

end;

 

procedure TForm1.RegisterButtonClick(Sender: TObject);

begin

AdsTable1.AdsRegisterProgressCallback( @MyCallbackFunc );

end;

 

procedure TForm1.ClearButtonClick(Sender: TObject);

begin

AdsTable1.AdsClearProgressCallback;

end;

See Also

[AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.md)

[AdsClearCallbackFunction](ade_adsclearcallbackfunction.md)

[AdsCreateIndex](ade_adscreateindex.md)

[AdsReindex](ade_adsreindex.md)
