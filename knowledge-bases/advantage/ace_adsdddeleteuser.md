AdsDDDeleteUser




Advantage Database Server 12  

AdsDDDeleteUser

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDDeleteUser  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDDeleteUser Advantage Client Engine ace\_Adsdddeleteuser Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDDeleteUser  Advantage Client Engine |  |  |  |  |

Delete a user object from the database.

Syntax

UNSIGNED32 AdsDDDeleteUser( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucUserName );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucUserName (I) | Name of the user object to delete. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucUserName is not a valid user name in the database. |

Remarks

AdsDDDeleteUser removes an existing user from the database. Once the user is removed from the database, any future connection attempts to the database using the specified user name will fail with authentication error. Any existing connections by the user will still be valid. However, those connections may not be able to open table or execute SQL statement if the database is set up to verify the users access rights. If the database is not set up to verify the users access rights, those connection can still open table and execute SQL statement. See [AdsSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm) for information on setting up user access rights verification.

DROP permissions on the user are required to delete a data dictionary user. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, delete the user named "User1" from the database.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDDeleteUser( hDD, "User1" );

See Also

[AdsDDCreateUser](ace_adsddcreateuser.htm)

[AdsDDGetUserProperty](ace_adsddgetuserproperty.htm)

[AdsDDSetUserProperty](ace_adsddsetuserproperty.htm)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.htm)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.htm)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.htm)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.htm)

[AdsDDGrantPermission](ace_adsddgrantpermission.htm)

[AdsDDRevokePermission](ace_adsddrevokepermission.htm)

[sp\_DropUser](master_sp_dropuser.htm)