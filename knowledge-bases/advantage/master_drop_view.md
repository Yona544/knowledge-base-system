DROP VIEW




Advantage Database Server 12  

DROP VIEW

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DROP VIEW  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - DROP VIEW Advantage SQL Engine master\_Drop\_view Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DROP VIEW  Advantage SQL Engine |  |  |  |  |

Deletes a view from the database

Syntax

DROP VIEW <view-name>

 

Remarks

CASCADE, RESTRICT not supported.

Views are supported through the use of the [Advantage Data Dictionary](master_advantage_data_dictionary.htm). DROP VIEW statements must be executed on a valid dictionary connection, and from the dictionary administrator account.

Example(s)

DROP VIEW GoodCustomers

 

See Also

[sp\_ModifyViewProperty](master_sp_modifyviewproperty.htm)