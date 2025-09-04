sp\_DropUser




Advantage Database Server 12  

sp\_DropUser

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropUser  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropUser Advantage SQL Engine master\_Sp\_dropuser Advantage SQL > System Procedures > Procedures > sp\_DropUser / Dear Support Staff, |  |
| sp\_DropUser  Advantage SQL Engine |  |  |  |  |

Delete a user object from the database.

Syntax

sp\_DropUser( UserName,CHARACTER,50 )

Parameters

|  |  |
| --- | --- |
| UserName (I) | Name of the user object to delete. |

Special Return Codes

AE\_INVALID\_OBJECT\_NAME Possible cause for the error is that the UserName is not a valid user name in the database.

Remarks

sp\_DropUser removes an existing user from the database. Once the user is removed from the database, any future connection attempts to the database using the specified user name will fail with authentication error. Any existing connections by the user will still be valid. However, those connections may not be able to open table or execute SQL statement if the database is set up to verify the users access rights. If the database is not set up to verify the users access rights, those connection can still open table and execute SQL statement. See [sp\_ModifyDatabase](master_sp_modifydatabase.htm) for information on setting up user access rights verification.

Example

After making a connection to the database, delete the user named "User1" from the database.

EXECUTE PROCEDURE sp\_DropUser( User1 );

See Also

[sp\_CreateUser](master_sp_createuser.htm)

[sp\_DropUser](master_sp_dropuser.htm)

[sp\_ModifyUserProperty](master_sp_modifyuserproperty.htm)

[sp\_CreateGroup](master_sp_creategroup.htm)

[sp\_DropGroup](master_sp_dropgroup.htm)

[sp\_AddUserToGroup](master_sp_addusertogroup.htm)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.htm)