AdsIsExprValid




Advantage Database Server 12  

TAdsTable.AdsIsExprValid

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsIsExprValid  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsIsExprValid Advantage TDataSet Descendant ade\_Adsisexprvalid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsIsExprValid  Advantage TDataSet Descendant |  |  |  |  |

Determines if a filter or index expression is valid.

Syntax

function AdsIsExprValid( strExpression : String ) : Boolean;

Parameter

|  |  |
| --- | --- |
| strExpression | Expression to check. |

Description

AdsIsExprValid tests whether an expression can be handled by the Advantage Expression Engine. If not, the return value will be False. If the expression is not valid, an application can call AdsGetLastError to retrieve the specific error code that will indicate why the expression is not valid. Note that if the table type is not ttAdsADT and the expression contains the binary concatenation operator (e.g., 'lastname;firstname') or data types that are specific to ADT tables, then the return value will be False.

Example

strExpression := 'LastName < "C" AND DeptNum < 60 AND Left( FirstName, 1 ) == "A"';

if (AdsTable1.AdsIsExprValid( strExpression )) then

AdsTable1.AdsSetFilter( strExpression );

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsLocate](ade_adslocate.htm)

[AdsSetFilter](ade_adssetfilter.htm)