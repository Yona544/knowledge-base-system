CREATE VIEW




Advantage Database Server 12  

CREATE VIEW

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CREATE VIEW  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - CREATE VIEW Advantage SQL Engine master\_Create\_view Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CREATE VIEW  Advantage SQL Engine |  |  |  |  |

Creates a new view in the database

Syntax

CREATE VIEW <view-name> AS SELECT <select-spec>

Remarks

SELECT statement can not have an ORDER BY clause. Views are by definition virtual base tables, which are unordered.

Views are supported through the use of the [Advantage Data Dictionary](master_advantage_data_dictionary.htm). CREATE VIEW statements must be executed on a valid dictionary connection, and from the dictionary administrator account.

Example(s)

CREATE VIEW GoodCustomers AS SELECT cust\_name from customers where credit\_limit > 50000

See Also

[sp\_ModifyViewProperty](master_sp_modifyviewproperty.htm)