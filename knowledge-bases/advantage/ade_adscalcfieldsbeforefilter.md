AdsCalcFieldsBeforeFilter




Advantage Database Server 12  

TAdsTable.AdsCalcFieldsBeforeFilter

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsCalcFieldsBeforeFilter  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsCalcFieldsBeforeFilter Advantage TDataSet Descendant ade\_Adscalcfieldsbeforefilter Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsCalcFieldsBeforeFilter  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Sets when calculated and lookup fields should be populated when using the OnFilterRecord event.

Syntax

property AdsCalcFieldsBeforeFilter: Boolean default False;

Description

This setting specifies when calculated and lookup fields should be populated when using the OnFilterRecord event. The default value is false, which means the overhead of calculating these fields will not happen until after the OnFilterRecord event has been fired. With this behavior, if the record is filtered out you will save the time it would have taken to populate the calculated fields.

If your OnFilterRecord event uses any of your calculated or lookup fields to perform its task, then you should set the AdsCalcFieldsBeforeFilter property to true.