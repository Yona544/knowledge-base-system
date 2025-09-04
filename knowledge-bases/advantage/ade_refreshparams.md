RefreshParams




Advantage Database Server 12  

TAdsStoredProc.RefreshParams

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsStoredProc.RefreshParams  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsStoredProc.RefreshParams Advantage TDataSet Descendant ade\_Refreshparams Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsStoredProc.RefreshParams  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.htm)

Refreshes parameter data stored in TAdsStoredProc.Params

Syntax

property RefreshParams : string;

Description

RefreshParams is a property that can be used at design-time to refresh the information stored in the [TAdsStoredProc.Params](ade_params_tadsstoredproc.htm) collection. To force the TAdsStoredProc instance to re-read parameter information from the data dictionary, simply click on the ellipsis in the Object Inspector.

Note Refreshing the parameter data will clear all customizations you may have made to parameters. If customer parameters have been added, or if parameter properties have been modified, it is recommended you make all subsequent modifications manually, and avoid the use of this property.

See Also

[LoadParamsFromDictionary](ade_loadparamsfromdictionary.htm)

[Params](ade_params_tadsstoredproc.htm)