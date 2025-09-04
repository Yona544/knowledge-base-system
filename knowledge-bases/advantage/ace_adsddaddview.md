AdsDDAddView




Advantage Database Server 12  

AdsDDAddView

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDAddView  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDAddView Advantage Client Engine ace\_Adsddaddview Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDAddView  Advantage Client Engine |  |  |  |  |

Adds a VIEW to an Advantage Data Dictionary. See [Views](master_views.htm) for more specific VIEW information.

Syntax

UNSIGNED32 AdsDDAddView( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucName,

UNSIGNED8 \*pucComments,

UNSIGNED8 \*pucSQL );

 

UNSIGNED32 AdsDDAddView100( ADSHANDLE hAdminConn,

                           UNSIGNED8 \*pucName,

                           UNSIGNED8 \*pucComments,

                           WCHAR     \*pwcSQL );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Dictionary connection handle. |
| pucName (I) | Name of the new VIEW object to create. |
| pucComments (I) | Optional comments. |
| pucSQL (I) | SQL SELECT statement definition of the VIEW. |

Remarks

AdsDDAddView will add a new view to an Advantage Data Dictionary. Once created the view can be referenced in SQL statements or opened directly with a call to [AdsOpenTable](ace_adsopentable.htm).

CREATE VIEW permissions are required to add a view to a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note AdsDDAddView can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

AdsDDAddView( hConn, "myview", "test comment", "select \* from customers where

credit\_limit > 50000" );

See Also

[AdsDDRemoveView](ace_adsddremoveview.htm)

[AdsDDGetViewProperty](ace_adsddgetviewproperty.htm)

[AdsDDSetViewProperty](ace_adsddsetviewproperty.htm)