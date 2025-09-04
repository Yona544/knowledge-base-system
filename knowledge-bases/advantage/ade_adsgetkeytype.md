AdsGetKeyType




Advantage Database Server 12  

TAdsTable.AdsGetKeyType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetKeyType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetKeyType Advantage TDataSet Descendant ade\_Adsgetkeytype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetKeyType  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine data type of the evaluated index keys.

Syntax

type TAdsExpressionTypes = ( etLOGICAL, etNUMERIC, etDATE, etSTRING, etRAW );

 

function AdsGetKeyType : TAdsExpressionTypes;

Description

Returns the data type of the key as evaluated by the Advantage Client Engine. Possible key types are etSTRING, etNUMERIC, etDATE, etRAW, and etLOGICAL. etRAW is returned for any index that uses the binary concatenation operator ";" and for indexes created on time, timestamp, and raw fields.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

AdsTable1.IndexName := 'Tag1';

eKeyType := AdsTable1.AdsGetKeyType;

{ eKeyType equals etString }

 

AdsTable1.AdsCreateIndex( '', 'Tag2', 'DeptNum', '', '', [] );

AdsTable1.IndexName := 'Tag2';

eKeyType := AdsTable1.AdsGetKeyType;

{ eKeyType equals etNUMERIC }

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsGetIndexExpr](ade_adsgetindexexpr.htm)

[AdsGetKeyLength](ade_adsgetkeylength.htm)

[AdsOpenIndex](ade_adsopenindex.htm)