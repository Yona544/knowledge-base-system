AdsDDRemoveView




Advantage Database Server 12  

AdsDDRemoveView

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDRemoveView  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDRemoveView Advantage Client Engine ace\_Adsddremoveview Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDRemoveView  Advantage Client Engine |  |  |  |  |

Removes a VIEW from an Advantage Data Dictionary. See [Advantage SQL Engine](master_advantage_sql_engine.htm) for more specific VIEW documentation.

Syntax

UNSIGNED32 AdsDDRemoveView( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucName );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Dictionary connection handle |
| pucName (I) | Name of the VIEW to remove |

Remarks

AdsDDRemoveView will remove a view from an [Advantage Data Dictionary](master_advantage_data_dictionary.htm).

DROP permissions on the view are required to remove a view from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

AdsDDRemoveView( hConn, "myview" );

See Also

[AdsDDAddView](ace_adsddaddview.htm)

[AdsDDGetViewProperty](ace_adsddgetviewproperty.htm)

[AdsDDSetViewProperty](ace_adsddsetviewproperty.htm)