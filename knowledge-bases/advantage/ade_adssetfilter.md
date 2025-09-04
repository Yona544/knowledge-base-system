AdsSetFilter




Advantage Database Server 12  

TAdsTable.AdsSetFilter

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetFilter  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetFilter Advantage TDataSet Descendant ade\_Adssetfilter Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetFilter  Advantage TDataSet Descendant |  |  |  |  |

Sets a filter on the given table.

Syntax

procedure AdsSetFilter( strFilter : String );

Parameter

|  |  |
| --- | --- |
| strFilter | Expression given as a pascal-style string. If there is an existing filter on the given table, it is replaced with the new filter. This affects subsequent record movements other than AdsGotoRecord. |

Description

Setting a filter through AdsSetFilter allows only the records that pass the filter expression to be visible. The filter expression must result in a boolean True or False. After setting a filter, the table may still be positioned on a record that does not pass the filter. To activate the filter, perform an AdsGotoTop or some other movement function.

See [Advantage Expression Engine](master_advantage_expression_engine.htm) for a list of functions supported by Advantage Expression Engine.

Note AdsSetFilter does not utilize the Advantage Optimized Filters functionality. It is recommended you use the native Delphi properties (Filter and Filtered) to set a filter. If you must use an Advantage specific API, the [AdsSetAOF](ade_adssetaof.htm) function is recommended.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetFilter( 'LastName = "S" .AND. EMPID > 50' );

 

{. . .your code here. . .}

 

strFilter := AdsTable1.AdsGetFilter;

See Also

[AdsClearFilter](ade_adsclearfilter.htm)

[AdsGetFilter](ade_adsgetfilter.htm)