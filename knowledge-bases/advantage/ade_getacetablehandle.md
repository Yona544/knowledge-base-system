GetAceTableHandle




Advantage Database Server 12  

TAdsTable/TAdsQuery.GetAceTableHandle

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.GetAceTableHandle  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.GetAceTableHandle Advantage TDataSet Descendant ade\_Getacetablehandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.GetAceTableHandle  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine table or cursor handle.

Syntax

function GetAceTableHandle : ADSHANDLE ;

Description

GetAceTableHandle returns the current open table or cursor handle. If the table or cursor is closed, the Advantage Client Engine handle returned will not be valid. GetAceTableHandle is only useful if you are going to call Advantage Client Engine functionality directly that is prototyped in ACE.PAS. Please refer to the ADSFUNC.PAS source file for examples of how this method is used.

Example

ACE.AdsGotoTop( AdsTable1.GetAceTableHandle );