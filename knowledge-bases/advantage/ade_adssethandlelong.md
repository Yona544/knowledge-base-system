AdsSetHandleLong




Advantage Database Server 12  

TAdsTable.AdsSetHandleLong

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetHandleLong  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetHandleLong Advantage TDataSet Descendant ade\_Adssethandlelong Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetHandleLong  Advantage TDataSet Descendant |  |  |  |  |

Sets a long value for the given handle

Syntax

procedure AdsSetHandleLong( ulHandle : Longint );

Description

Sets a long value that will be associated with the given handle and available to the user for the life of the handle. The value stored is at the user's discretion. The Advantage Client Engine does not use the value for any operation, but simply stores it. If the value is a memory reference (e.g., a pointer to an application-specific structure), the application is responsible for freeing the memory.

Example

procedure TForm1.RegisterHandle( lNewID : Longint );

begin

AdsTable1.AdsSetHandleLong( lNewID );

end;

See Also

[AdsGetHandleLong](ade_adsgethandlelong.htm)