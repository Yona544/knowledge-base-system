AdsDDRemoveRefIntegrity




Advantage Database Server 12  

AdsDDRemoveRefIntegrity

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDRemoveRefIntegrity  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDRemoveRefIntegrity Advantage Client Engine ace\_Adsddremoverefintegrity Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDRemoveRefIntegrity  Advantage Client Engine |  |  |  |  |

Removes a referential integrity (RI) constraint from the data dictionary.

Syntax

UNSIGNED32 AdsDDRemoveRefIntegrity( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucRIName );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | The data dictionary connection. |
| pucRIName | Name of the RI constraint in the data dictionary to be removed. |

Description

AdsDDRemoveRefIntegrity will remove a RI constraint from the data dictionary.

The parent and child table must not be opened, so that the Advantage Client Engine can temporarily open the parent and the child tables exclusively. This function will temporarily open all tables exclusively that are in the data dictionary and that interlink with these tables through other RI constraints.

ALTER TABLE permissions are required on both related tables to remove a relation from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetCode = AdsDDRemoveRefIntegrity( hDD, "salesreps.rep\_office to offices.office" );

See Also

[AdsDDGetRefIntegrityProperty](ace_adsddgetrefintegrityproperty.htm)

[AdsDDCreateRefIntegrity](ace_adsddcreaterefintegrity.htm)

[sp\_DropReferentialIntegrity](master_sp_dropreferentialintegrity.htm)