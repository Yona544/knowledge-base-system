sp\_ModifyUserProperty




Advantage Database Server 12  

sp\_ModifyUserProperty

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ModifyUserProperty  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ModifyUserProperty Advantage SQL Engine master\_Sp\_modifyuserproperty Advantage SQL > System Procedures > Procedures > sp\_ModifyUserProperty / Dear Support Staff, |  |
| sp\_ModifyUserProperty  Advantage SQL Engine |  |  |  |  |

Sets one property associated with a database user in the data dictionary.

Syntax

sp\_ModifyUserProperty(

UserName,CHARACTER,50,

Property,CHARACTER,200,

Value,Memo )

Parameters

|  |  |
| --- | --- |
| UserName (I) | Name of the database user object to set the associated property. |
| Property (I) | Name of a database user property to set. See Remarks for allowed values. |
| Value (I) | Property value to set. |

Special Return Codes

AE\_INVALID\_OBJECT\_NAME Possible cause for the error is that the UserName does not specify a valid user name in the database.

Remarks

sp\_ModifyUserProperty sets one user property associated with the specified user. The new property overwrites the existing property in the data dictionary. The current connected users must have the ALTER permission to the user named by UserName to successfully execute this stored procedure. The following are the valid values of Property and the expected value in Value. If a regular user makes the connection, the only property that may be set is USER\_PASSWORD for the same user who made the connection.

|  |  |
| --- | --- |
| usPropertyID | Description |
| COMMENT | Stores a new description for the user. |
| USER\_PASSWORD | Sets a new password for this user. The user password is used by the Advantage Database Server or the Advantage Local Server to authenticate a user when he makes a connection to the database. See AdsConnect60 for more information on database connections. To allow the user to connect without a password, specify NULL or an empty string. The maximum length of the password is 20 characters. USER\_PASSWORD can be used to set the administrator password by specifying the ADSSYS as the user name. Although this property can be used to change the current connected user password (i.e. using [User()](master_miscellaneous_functions.htm) as the UserName parameter), this stored procedure does not provide facility for supply the existing password. Thus it will only work if the current user is set up to not require old password when changing its own password. Otherwise, the stored procedure [sp\_ChangeCurrentUserPassword()](master_sp_changecurrentuserpassword.htm) which provides the facility to supply the existing password should be used to change the current user's password. |
| ENABLE\_INTERNET | This property enables/disables the Internet access for the user. If it is disabled, the user will be allowed to connect from the Internet. Expected values are True and False. For more information see Advantage Internet Server. |
| LOGINS\_DISABLED | This property enables/disables the database login for the user. If it is enabled, the user will not be allowed to login to the database. Expected values are True and False. |
| REQUIRE\_OLD\_PASSWORD | This property controls whether existing password is required when the specified user changes its own password. Expected values are True and False. |
| USER\_DEFINED\_PROP | Changes the user defined user property. |

Note When the database is created, it is default to allow anonymous user to make database connection with no user name and no password. Setting the LOG\_IN\_REQUIRED database property to True will disable the anonymous user connections and improve the database security. See [sp\_ModifyDatabase](master_sp_modifydatabase.htm) for more information.

Example

After making a connection to the database, set a new password for user

User1.

 

EXECUTE PROCEDURE sp\_ModifyUserProperty(

User1,

USER\_PASSWORD,

Super secret );

See Also

[sp\_CreateUser](master_sp_createuser.htm)

[sp\_ModifyDatabase](master_sp_modifydatabase.htm)

[sp\_DropUser](master_sp_dropuser.htm)

[sp\_ModifyUserProperty](master_sp_modifyuserproperty.htm)

[sp\_CreateGroup](master_sp_creategroup.htm)

[sp\_DropGroup](master_sp_dropgroup.htm)

[sp\_AddUserToGroup](master_sp_addusertogroup.htm)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.htm)