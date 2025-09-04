LoadParamsFromDictionary




Advantage Database Server 12  

TAdsStoredProc.LoadParamsFromDictionary

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsStoredProc.LoadParamsFromDictionary  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsStoredProc.LoadParamsFromDictionary Advantage TDataSet Descendant ade\_Loadparamsfromdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsStoredProc.LoadParamsFromDictionary  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.htm)

Reads parameter information from the Advantage Data Dictionary.

Syntax

procedure LoadParamsFromDictionary;

Description

LoadParamsFromDictionary populates the [Params](ade_params_tadsstoredproc.htm) property with the parameter information associated with the procedure in the Advantage Data Dictionary. If the StoredProcName property is assigned when the TAdsStoredProc is attached to an open TAdsConnection component (for example, at design-time) this procedure is called automatically.

Use this procedure if you are configuring a new TAdsStoredProc instance at run-time, and would like to have the Params property automatically populated, as opposed to writing the code to configure the parameters.