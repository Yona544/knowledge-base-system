GetProcedureNames




Advantage Database Server 12  

TAdsConnection.GetProcedureNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetProcedureNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetProcedureNames Advantage TDataSet Descendant ade\_Getprocedurenames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetProcedureNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Retrieves a list of stored procedures from an Advantage Data Dictionary.

Syntax

procedure GetProcedureNames( poList : TStrings );

Description

GetProcedureNames retrieves a list of Advantage Extended Procedures from the Advantage Data Dictionary referenced by the TAdsConnection component. If the TAdsConnection component does not reference an Advantage Data Dictionary the procedure returns without modifying the list. See [Accessing an Advantage Data Dictionary](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.htm) for more details on associating a TAdsConnection component with an Advantage Data Dictionary.