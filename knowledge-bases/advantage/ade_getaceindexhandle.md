GetAceIndexHandle




Advantage Database Server 12  

TAdsTable/TAdsQuery.GetAceIndexHandle

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.GetAceIndexHandle  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.GetAceIndexHandle Advantage TDataSet Descendant ade\_Getaceindexhandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.GetAceIndexHandle  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine index handle.

Syntax

function GetAceIndexHandle : ADSHANDLE ;

Description

GetAceIndexHandle returns the current Advantage Client Engine index handle. If no index is active, then 0 is returned. GetAceIndexHandle is only useful if you are going to call Advantage Client Engine functionality directly that is prototyped in ACE.PAS. Please refer to the ADSFUNC.PAS source file for examples of how this method is used.

Example

ACE.AdsGotoTop( AdsTable1.GetAceIndexHandle );