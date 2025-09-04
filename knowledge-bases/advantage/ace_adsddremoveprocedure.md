AdsDDRemoveProcedure




Advantage Database Server 12  

AdsDDRemoveProcedure

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDRemoveProcedure  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDRemoveProcedure Advantage Client Engine ace\_Adsddremoveprocedure Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDRemoveProcedure  Advantage Client Engine |  |  |  |  |

Remove a stored procedure definition from the data dictionary.

Syntax

UNSIGNED32 AdsDDRemoveProcedure( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucName );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Data dictionary connection handle. |
| pucName (I) | The stored procedure data dictionary name to remove from the data dictionary. |

Remarks

This function may be used to remove a stored procedure definition from the Advantage Data Dictionary. Other methods of removing stored procedures are the "DROP PROCEDURE" SQL syntax or by using Advantage Data Architect.

DROP permissions are required on the stored procedure to remove it from the data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

See Also

[AdsDDAddProcedure](ace_adsddaddprocedure.htm)

[AdsDDGetProcedureProperty](ace_adsddgetprocedureproperty.htm)

[AdsDDSetProcedureProperty](ace_adsddsetprocedureproperty.htm)