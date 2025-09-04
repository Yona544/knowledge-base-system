AdsClearSQLAbortFunc




Advantage Database Server 12  

TAdsQuery.AdsClearSQLAbortFunc

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.AdsClearSQLAbortFunc  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.AdsClearSQLAbortFunc Advantage TDataSet Descendant ade\_Adsclearsqlabortfunc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.AdsClearSQLAbortFunc  Advantage TDataSet Descendant |  |  |  |  |

Clears the SQL abort callback function registered using AdsRegisterSQLAbortFunc.

Note This API still functions as before, but is now obsolete. It is suggested that you use [AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.htm) and [AdsClearCallbackFunction](ade_adsclearcallbackfunction.htm) instead, as they work better with threads and have more complete functionality.

Syntax

procedure AdsClearSQLAbortFunc;

Description

AdsClearSQLAbortFunc will make the Advantage Client Engine stop calling the registered callback function. AdsRegisterSQLAbortFunc is used to abort an SQL query.

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

[AdsRegisterSQLAbortFunc](ade_adsregistersqlabortfunc.htm)