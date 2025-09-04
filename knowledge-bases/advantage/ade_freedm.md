FreeDM




Advantage Database Server 12  

TAdsAEPSessionMgr.FreeDM

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsAEPSessionMgr.FreeDM  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsAEPSessionMgr.FreeDM Advantage TDataSet Descendant ade\_Freedm Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsAEPSessionMgr.FreeDM  Advantage TDataSet Descendant |  |  |  |  |

[TAdsAEPSessionMgr](ade_tadsaepsessionmgr.htm)

Destroys a data module stored in the session manager.

Syntax

procedure FreeDM( id : integer )

Parameters

The id parameter is the unique value used to identify this data module in a previous call to the AddDM method.

Description

Call FreeDM to free the memory associated with a data module stored with a previous call to If you would like to close tables or perform other clean-up actions do so in the data modules OnDestroy event.

Example

function Shutdown( ulConnectionID: UNSIGNED32;

pucUserName: PChar;

pucPassword: PChar

): UNSIGNED32; stdcall; // Do not change the prototype.

begin

 

Result := AE\_SUCCESS;

 

if assigned( AEPSessionMgr ) then

AEPSessionMgr.FreeDM( ulConnectionID );

 

end;

See Also

[AddDM](ade_adddm.htm)

[GetDM](ade_getdm.htm)