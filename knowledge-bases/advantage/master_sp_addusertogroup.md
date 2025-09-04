sp\_AddUserToGroup




Advantage Database Server 12  

sp\_AddUserToGroup

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_AddUserToGroup  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_AddUserToGroup Advantage SQL Engine master\_Sp\_addusertogroup Advantage SQL > System Procedures > Procedures > sp\_AddUserToGroup / Dear Support Staff, |  |
| sp\_AddUserToGroup  Advantage SQL Engine |  |  |  |  |

Makes a database user member of a user group.

Syntax

sp\_AddUserToGroup(

UserName,CHARACTER,50,

GroupName,CHARACTER,100 )

Parameters

|  |  |
| --- | --- |
| UserName (I) | Name of the database user object that will become a member of the user group. |
| GroupName (I) | Name of the database user group object to make the user a member of. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Either the GroupName does not specify a valid user group in the database or the UserName does not specify a valid database user. |
| AE\_ALREADY\_MEMBER\_OF\_GROUP | The user is already a member of the specified user group. |

Remarks

sp\_AddUserToGroup makes the user a member of the specified user group. Once the user is a member of the user group, the user inherits rights to all objects that the user group has. If the user groups object access rights changes, the users inherited rights will change accordingly. A user can be member of multiple user groups. The users effective right to a database object (table, view or stored procedure) is the summation of all inherited rights the user have from all user groups that the user is a member of.

Example

After making a connection to the database, add user "rsmith" to the user group "Managers". If the "Managers" has read and write rights to the table "employees", the user "rsmith" will now have rights to open the "employees" table for read and write purpose.

EXECUTE PROCEDURE sp\_AddUserToGroup(

rsmith,

Managers );

See Also

[sp\_CreateGroup](master_sp_creategroup.htm)

[sp\_DropGroup](master_sp_dropgroup.htm)

[sp\_CreateUser](master_sp_createuser.htm)

[sp\_DropUser](master_sp_dropuser.htm)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.htm)