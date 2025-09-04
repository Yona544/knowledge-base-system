AdsGetHandleType




Advantage Database Server 12  

TAdsTable.AdsGetHandleType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetHandleType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetHandleType Advantage TDataSet Descendant ade\_Adsgethandletype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetHandleType  Advantage TDataSet Descendant |  |  |  |  |

Returns the type of a given Advantage Client Engine handle.

Syntax

type TAdsHandleTypes = ( htTABLE, htINDEX );

 

function AdsGetHandleType( hObj : ADSHANDLE ) : TAdsHandleTypes;

Parameter

|  |  |
| --- | --- |
| hObj | Handle of either a table or an index order. |

Description

Possible types returned are htTABLE for table handles and htINDEX for index order handles.

Example

AdsTable1.Active := TRUE;

eAdsHandleType := AdsTable1.AdsGetHandleType( AdsTable1.GetAceOrderHandle );

See Also

[AdsGetIndexHandle](ade_adsgetindexhandle.htm)

[AdsGetIndexHandleByOrder](ade_adsgetindexhandlebyorder.htm)