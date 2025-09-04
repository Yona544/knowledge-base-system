AdsClearProgressCallback




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsClearProgressCallback

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsClearProgressCallback  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsClearProgressCallback Advantage TDataSet Descendant ade\_Adsclearprogresscallback Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsClearProgressCallback  Advantage TDataSet Descendant |  |  |  |  |

Clears the progress callback registered using AdsRegisterProgressCallback.

Note This API still functions as before, but is now obsolete. It is suggested that you use [AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.htm) and [AdsClearCallbackFunction](ade_adsclearcallbackfunction.htm) instead, as they work better with threads and have more complete functionality.

Syntax

procedure AdsClearProgressCallback;

Description

AdsClearProgressCallback will make the Advantage Client Engine stop calling the registered callback function. The progress callback is used to indicate progress while an Advantage server is building an index.

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

[AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.htm)

[AdsClearCallbackFunction](ade_adsclearcallbackfunction.htm)

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsReindex](ade_adsreindex.htm)