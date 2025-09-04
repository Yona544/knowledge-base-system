AdsGetHandleLong




Advantage Database Server 12  

TAdsTable.AdsGetHandleLong

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetHandleLong  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetHandleLong Advantage TDataSet Descendant ade\_Adsgethandlelong Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetHandleLong  Advantage TDataSet Descendant |  |  |  |  |

Returns the long value for this handle set with a call to AdsSetHandleLong.

Syntax

function AdsGetHandleLong : Longint;

Description

Returns the value set for this handle in a previous call to AdsSetHandleLong. This function allows one value to be stored for this handle. The value stored is up to the users discretion. The Advantage Client Engine does not use the value for any operation, but simply stores it. The value is readable for as long as the handle is valid.

Example

function TForm1.GetHandle( oTable : TAdsTable ) : Longint;

begin

Result := oTable.AdsGetHandleLong;

end;

See Also

[AdsSetHandleLong](ade_adssethandlelong.htm)