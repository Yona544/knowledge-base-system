ShowDeleted




Advantage Database Server 12  

TAdsSettings.ShowDeleted

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsSettings.ShowDeleted  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsSettings.ShowDeleted Advantage TDataSet Descendant ade\_Showdeleted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsSettings.ShowDeleted  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.htm)

Defines whether deleted records are visible when using DBF tables.

Syntax

property ShowDeleted: Boolean;

Description

If True, deleted records in DBF tables will be visible. The default value is True. Deleted records still physically exist inside DBF tables so they can be returned to client applications.

Deleted controls whether the Advantage Database Server filters out records that are marked for deletion in DBF tables. If Deleted is False, then the server will filter the deleted records, and the client will never "see" those records. This call also affects all currently connected servers and all server connections that are made after the call.

This property has no effect when using ADT tables because records that are deleted can never be retrieved by the application.