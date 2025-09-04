AdsShowError




Advantage Database Server 12  

TAdsTable.AdsShowError

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsShowError  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsShowError Advantage TDataSet Descendant ade\_Adsshowerror Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsShowError  Advantage TDataSet Descendant |  |  |  |  |

Displays a message box for the last error (if there was one).

Syntax

procedure AdsShowError( strCaption : String );

Parameter

|  |  |
| --- | --- |
| strCaption | The title for the message box. Can be an empty string. |

Description

AdsShowError will display a message box containing the last error message. The message displayed is identical to the error message available from AdsGetErrorString. This function is useful during development or debugging for viewing error messages immediately after the error occurred.

Example

procedure TForm1.Button5Click(Sender: TObject);

begin

try

AdsTable2.open;

except

{$ifdef DEBUG}

AdsTable2.AdsShowError( 'table open' );

{$else}

{\* put your release code error handling here \*}

{$endif}

end;

end;

See Also

[AdsGetErrorString](ade_adsgeterrorstring.htm)

[AdsGetLastError](ade_adsgetlasterror.htm)