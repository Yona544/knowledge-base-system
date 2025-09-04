GetAceConnectionHandle




Advantage Database Server 12  

TAdsTable/TAdsQuery.GetAceConnectionHandle

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.GetAceConnectionHandle  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.GetAceConnectionHandle Advantage TDataSet Descendant ade\_Getaceconnectionhandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.GetAceConnectionHandle  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine connection handle.

Syntax

function GetAceConnectionHandle : ADSHANDLE ;

Description

GetAceConnectionHandle returns the active connection handle, which is the connection handle being used by the specified dataset instance. If no table or cursor is open or no connection exists, the Advantage Client Engine connection handle returned will not be valid. GetAceConnectionHandle is only useful if you are going to call Advantage Client Engine functionality directly that is prototyped in ACE.PAS. Please refer to the ADSFUNC.PAS source file to see examples of how this method is used.

Example

ACE.AdsBeginTransaction( AdsTable1.GetAceConnectionHandle );