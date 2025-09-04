AdsDDAddUserToGroup




Advantage Database Server 12  

AdsDDAddUserToGroup

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDAddUserToGroup  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDAddUserToGroup Advantage Client Engine ace\_Adsddaddusertogroup Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDAddUserToGroup  Advantage Client Engine |  |  |  |  |

Makes a database user member of a user group.

Syntax

UNSIGNED32 AdsDDAddUserToGroup( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucGroupName,

UNSIGNED8 \*pucUserName );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucGroupName (I) | Name of the database user group object to make the user a member of. |
| pucUserName (I) | Name of the database user object that will become a member of the user group. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Either the pucGroupName does not specify a valid user group in the database or the pucUserName does not specify a valid database user. |
| AE\_ALREADY\_MEMBER\_OF\_GROUP | The user is already a member of the specified user group. |

Remarks

AdsDDAddUserToGroup makes the user a member of the specified user group. Once the user is a member of the user group, the user inherits rights to all objects that the user group has. If the user groups object access rights changes, the users inherited rights will change accordingly. A user can be member of multiple user groups. The users effective right to a database object (table, view or stored procedure) is the summation of all inherited rights the user have from all user groups that the user is a member of.

ALTER permissions on the user group are required to add a user to a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, add user "rsmith" to the user group "Managers". If the "Managers" has read and write rights to the table "employees", the user "rsmith" will now have rights to open the "employees" table for read and write purpose.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDAddUserToGroup( hDD, "Managers", "rsmith" );

AdsDisconnect( hDD );

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "rsmith", NULL, ADS\_DEFAULT, &hConn );

AdsOpenTable( hConn, "employees", NULL, ADS\_DEFAULT, ADS\_DEFAULT, ADS\_DEFAULT,

ADS\_DEFAULT, ADS\_DEFAULT, &hTable );

See Also

[AdsDDCreateUser](ace_adsddcreateuser.htm)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.htm)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.htm)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.htm)

[sp\_AddUserToGroup](master_sp_addusertogroup.htm)