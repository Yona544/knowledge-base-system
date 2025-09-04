AdsGetIndexExpr




Advantage Database Server 12  

TAdsTable.AdsGetIndexExpr

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetIndexExpr  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetIndexExpr Advantage TDataSet Descendant ade\_Adsgetindexexpr Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetIndexExpr  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the index key expression of this index order.

Syntax

function AdsGetIndexExpr : String;

Description

The index expression returned by AdsGetIndexExpr is the expression evaluated against records in the table to generate index keys. This expression can evaluate to a numeric value, a string value, a date, or a logical.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

AdsTable1.IndexName := 'Tag1';

 

strExpression := AdsTable1.AdsGetIndexExpr;

{ strExpression equals LASTNUM;DEPTNUM }

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsIsExprValid](ade_adsisexprvalid.htm)

[AdsOpenIndex](ade_adsopenindex.htm)