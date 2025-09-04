AdsClearFilter




Advantage Database Server 12  

TAdsTable.AdsClearFilter

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsClearFilter  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsClearFilter Advantage TDataSet Descendant ade\_Adsclearfilter Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsClearFilter  Advantage TDataSet Descendant |  |  |  |  |

Clears the current filter expression in a given table.

Syntax

procedure AdsClearFilter;

Description

AdsClearFilter will remove the current filter from the specified table, allowing records that previously had not passed the filter to become visible again.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetFilter( 'LastName = "S" .AND. EMPID > 50' );

AdsTable1.First;

{ The row is filtered if LastName does not begin with S or if EMPID not greater than 50 }

{. . . your code here . . .}

 

AdsTable1.AdsClearFilter;

See Also

[AdsGetFilter](ade_adsgetfilter.htm)

[AdsSetFilter](ade_adssetfilter.htm)