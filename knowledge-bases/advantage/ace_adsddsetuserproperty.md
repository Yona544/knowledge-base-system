AdsDDSetUserProperty




Advantage Database Server 12  

AdsDDSetUserProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDSetUserProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDSetUserProperty Advantage Client Engine ace\_Adsddsetuserproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDSetUserProperty  Advantage Client Engine |  |  |  |  |

Sets one property associated with a database user in the data dictionary.

Syntax

UNSIGNED32 AdsDDSetUserProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucUserName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen );

Parameters

|  |  |
| --- | --- |
| hDBConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucUserName (I) | Name of the database user object to set the associated property. |
| usPropertyID (I) | Index of a database user property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property is stored. |
| usPropertyLen (I) | The size of the property specified by the pvProperty. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucUserName does not specify a valid user name in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid database user property ID, or the specified property cannot be set. |
| AE\_PERMISSION\_DENIED | The current connected user does not have permission to modify the property of the named user. |

Remarks

AdsDDSetUserProperty sets one user property associated with the specified user. The new property overwrites the existing property in the data dictionary.

ALTER permissions on the user are required to modify data dictionary user properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the user. The pvProperty is expected to be NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or empty string, the user description is removed. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined user property. If pvProperty is NULL, the user defined user property is removed. User defined property is set, read, and interpreted by the application. It is not used by the Advantage Database Server or the Advantage Local Server. |
| ADS\_DD\_USER\_PASSWORD | Sets a new password for this user. The user password is used by the Advantage Database Server or the Advantage Local Server to authenticate a user when he makes a connection to the database. See [AdsConnect60](ace_adsconnect60.htm) for more information on database connections. pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. To allow the user to connect without a password, specify NULL or an empty string as pvProperty. The maximum length of the password not including the NULL terminator is 20 characters. If usPropertyLen is longer than 21, the first 20 character will be used as the password. ADS\_DD\_USER\_PASSWORD can be used to set the administrator password by specifying the ADSSYS as the user name.  Although this property can be used to change the current connected user password, there is no facility for supplying the existing password. Thus it will only work if the current user is set up to not require old password when changing its own password. To supply existing password, use the  ADS\_DD\_CURRENT\_USER\_PASSWORD property and provide  the old password in the pucUserName parameter. Alternative, the [sp\_ChangeCurrentUserPassword](master_sp_changecurrentuserpassword.htm) may be used instead. |
| ADS\_DD\_ENABLE\_INTERNET | This property enables/disables the Internet access for the user. If it is disabled, the user will be allowed to connect from the Internet. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Expected values are True and False. For more information see [Advantage Internet Server](master_advantage_internet_server_overview.htm). A user cannot change this setting for themselves. Only a separate user with ALTER permissions for this user can change this property. |
| ADS\_DD\_LOGINS\_DISABLED | This property enables/disables the database login for the user. If it is enabled, the user will not be allowed to login to the database. The default setting is disabled (the user is allowed to login). pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Expected values are True and False. |
| ADS\_DD\_REQUIRE\_OLD\_PASSWORD | This property controls whether existing password is required when the specified user changes its own password. Expected values are True and False. The default setting is TRUE, meaning that existing password is require when user changes its own password. |
| ADS\_DD\_CURRENT\_USER\_PASSWORD | This property can be used for the connected user to change its own password. When this property is specified, the pvProperty property parameter is expected to be the new password, and the pucUserName is expected to be the existing password. |

Note When the database is created, by default it allows anonymous users to make a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)) with no user name and no password. Setting the ADS\_DD\_LOG\_IN\_REQUIRED database property to True will disable the anonymous user connections and improve the database security. See [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm) for more information.

Example

After making a connection to the database, set a new password for user User1.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDSetUserProperty( hDD, "User1", ADS\_DD\_USER\_PASSWORD, "Super secret", 13 );

See Also

[AdsConnect60](ace_adsconnect60.htm)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm)

[AdsDDCreateUser](ace_adsddcreateuser.htm)

[AdsDDGetUserProperty](ace_adsddgetuserproperty.htm)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.htm)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.htm)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.htm)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.htm)

[AdsDDGrantPermission](ace_adsddgrantpermission.htm)

[AdsDDRevokePermission](ace_adsddrevokepermission.htm)

[sp\_ModifyUserProperty](master_sp_modifyuserproperty.htm)

[sp\_ChangeCurrentUserPassword](master_sp_changecurrentuserpassword.htm)