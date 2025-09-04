AdsGetLastError




Advantage Database Server 12  

TAdsTable.AdsGetLastError

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetLastError  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetLastError Advantage TDataSet Descendant ade\_Adsgetlasterror Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetLastError  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the result of the last Advantage Client Engine function call.

Syntax

function AdsGetLastError( var strError : String ) : Longint;

Parameter

|  |  |
| --- | --- |
| strError | Returns the error string corresponding to return value. It will be similar to the string return by AdsGetErrorString but may have information specific to the error instance such as table names. |

Description

The error code returned by this function will be the same as the one returned by the last Advantage Client Engine function call. The first action of each Advantage Client Engine function is to clear the previous error if there is one. Thus, a call to AdsGetLastError is valid only for the most recent function call as opposed to the most recently occurring error. If no error occurred on the last Advantage Client Engine function call, a 0 (zero) is returned.

Example

procedure TForm1.ShowLastAdvantageError( oTable : TAdsTable );

var

strError : string;

lErrorCode : longint;

begin

lErrorCode := oTable.AdsGetLastError( strError );

if ( lErrorCode <> 0 ) then

Application.MessageBox( pchar(strError), 'Advantage Error', 0 );

end;

See Also

[AdsGetErrorString](ade_adsgeterrorstring.htm)

[AdsShowError](ade_adsshowerror.htm)