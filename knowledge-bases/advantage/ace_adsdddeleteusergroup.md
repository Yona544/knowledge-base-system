AdsDDDeleteUserGroup




Advantage Database Server 12  

AdsDDDeleteUserGroup

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDDeleteUserGroup  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDDeleteUserGroup Advantage Client Engine ace\_Adsdddeleteusergroup Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDDeleteUserGroup  Advantage Client Engine |  |  |  |  |

Delete a user group object from the database.

Syntax

UNSIGNED32 AdsDDDeleteUserGroup( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucGroupName );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucGroupName (I) | Name of the user group object to delete. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucGroupName is not a valid user group name in the database. |

Remarks

AdsDDDeleteUserGroup removes an existing user group from the database. All references to the user group by the database users are removed from the DD.

DROP permissions on the user group are required to delete a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, delete the user group named "Managers" from the database.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDDeleteUserGroup( hDD, "Managers" );

See Also

[AdsDDCreateUser](ace_adsddcreateuser.htm)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.htm)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.htm)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.htm)

[AdsDDGrantPermission](ace_adsddgrantpermission.htm)

[AdsDDRevokePermission](ace_adsddrevokepermission.htm)

[sp\_DropGroup](master_sp_dropgroup.htm)