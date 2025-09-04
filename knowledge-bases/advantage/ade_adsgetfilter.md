AdsGetFilter




Advantage Database Server 12  

TAdsTable.AdsGetFilter

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetFilter  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetFilter Advantage TDataSet Descendant ade\_Adsgetfilter Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetFilter  Advantage TDataSet Descendant |  |  |  |  |

Returns the current filter expression for the given table.

Syntax

function AdsGetFilter : String;

Description

AdsGetFilter returns the current filter expression for the specified table. Note that the case of the expression returned is not guaranteed to be identical to the filter expression that was set.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetFilter( 'LastName = "S" .AND. EMPID > 50' );

 

{. . .your code here. . .}

 

strFilter := AdsTable1.AdsGetFilter;

See Also

[AdsClearFilter](ade_adsclearfilter.htm)

[AdsSetFilter](ade_adssetfilter.htm)