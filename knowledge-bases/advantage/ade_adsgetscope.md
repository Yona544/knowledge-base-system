AdsGetScope




Advantage Database Server 12  

TAdsTable.AdsGetScope

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetScope  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetScope Advantage TDataSet Descendant ade\_Adsgetscope Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetScope  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the specified scope from the given index order.

Syntax

type TAdsScopeOptions = ( soTOP, soBOTTOM );

 

function AdsGetScope( eScopeOption : TAdsScopeOptions ) : String;

Parameter

|  |  |
| --- | --- |
| eScopeOption | Indicates which scope value to retrieve. |

Description

AdsGetScope returns the indicated scope setting in the form of an index key. The value sent in a call to AdsSetScope was converted to a valid index key by the Advantage Client Engine. It may be necessary to convert the key to another form to make it useful. For example, when an application sets a scope on a date index, the Advantage Client Engine converts the date value to match the key data type. For a CDX or ADI index, this would be an 8-byte Julian date representation.

Example

AdsTable1.Active := TRUE;

AdsTable1.IndexName := 'LastName' ;

AdsTable1.SetRange( ['Adams'], ['Smith'] );

 

strScopeValue := AdsTable1.AdsGetScope( soTop );

{strScopeValue equals 'Adams '}

See Also

[AdsClearScope](ade_adsclearscope.htm)

[AdsSetScope](ade_adssetscope.htm)