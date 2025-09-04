GetAceOrderHandle




Advantage Database Server 12  

TAdsTable/TAdsQuery.GetAceOrderHandle

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.GetAceOrderHandle  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.GetAceOrderHandle Advantage TDataSet Descendant ade\_Getaceorderhandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.GetAceOrderHandle  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine index order handle.

Syntax

function GetAceOrderHandle : ADSHANDLE ;

Description

GetAceOrderHandle returns the Advantage Client Engine index handle of the active index. If no index is active, GetAceOrderHandle returns the Advantage Client Engine table or cursor handle. GetAceOrderHandle is only useful if you are going to call Advantage Client Engine functionality directly that is prototyped in ACE.PAS. Please refer to the ADSFUNC.PAS source file for examples of how this method is used.

Example

ACE.AdsGotoTop( AdsTable1.GetAceOrderHandle );