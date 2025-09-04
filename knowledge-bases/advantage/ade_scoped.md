Scoped




Advantage Database Server 12  

TAdsTable/TAdsQuery.Scoped

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.Scoped  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.Scoped Advantage TDataSet Descendant ade\_Scoped Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.Scoped  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm)

Specifies whether Scoping is active for a dataset.

Syntax

property Scoped: Boolean;

Description

Check Scoped to determine whether or not indexed dataset scoping is in effect. If Scoped is True, then scoping is active. To apply Scope conditions specified in the ScopeEnd/ScopeBegin property, set Scoped to True.

Note TAdsTable's and TAdsQuerys Scope and range are two different ways of filtering records in the table. They are mutually exclusive. If there is an active range on the dataset, trying to set the Scope property to True will raise an exception.

Ranges are implemented internally as scopes. Ranges provide a very useful means to automatically produce the value necessary to set the scope. For this reason, use of ranges is easier and more versatile.