AdsGetIndexCondition




Advantage Database Server 12  

TAdsTable.AdsGetIndexCondition

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetIndexCondition  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetIndexCondition Advantage TDataSet Descendant ade\_Adsgetindexcondition Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetIndexCondition  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the conditional index expression of this index order if one exists.

Syntax

function AdsGetIndexCondition : String;

Description

A conditional expression is a logical expression that filters the records placed in an index order. Only records that pass the conditional expression are in the index order. If records that do not pass the conditional expression are modified such that they pass the condition, a key is added to the index for that record. If an updated record no longer passes the condition, any associated key is removed from the index.

If no index condition exists, AdsGetIndexCondition will return an empty string.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'EmpId>50', '', [] );

AdsTable1.IndexName := 'Tag1';

 

strCondition := AdsTable1.AdsGetIndexCondition;

{ strCondition equals EMPID>50 }

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsOpenIndex](ade_adsopenindex.htm)