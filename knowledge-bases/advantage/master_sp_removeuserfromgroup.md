sp\_RemoveUserFromGroup




Advantage Database Server 12  

sp\_RemoveUserFromGroup

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_RemoveUserFromGroup  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_RemoveUserFromGroup Advantage SQL Engine master\_Sp\_removeuserfromgroup Advantage SQL > System Procedures > Procedures > sp\_RemoveUserFromGroup / Dear Support Staff, |  |
| sp\_RemoveUserFromGroup  Advantage SQL Engine |  |  |  |  |

Removes a database user from the specified user group.

Syntax

sp\_RemoveUserFromGroup(

UserName,CHARACTER,50,

GroupName,CHARACTER,100 )

Parameters

|  |  |
| --- | --- |
| UserName (I) | Name of the database user object to remove from the user groups membership. |
| GroupName (I) | Name of the database user group object to remove the users membership. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Either the GroupName does not specify a valid user group in the database or the UserName does not specify a valid database user. |
| AE\_NOT\_MEMBER\_OF\_GROUP | The user is not a member of the specified user group. |

Remarks

sp\_RemoveUserFromGroup removes the user from the membership of the specified user group. Once the user is removed from the membership of the user group, the user loses all object access rights that he inherited from the user group.

Example

After making a connection to the database, remove user "rsmith" from the user group "Managers". If the only rights the user has to the table "employees" are inherited from the "Managers" user group, the user "rsmith" will now have no rights to the "employees" table after being removed from the user group.

EXECUTE PROCEDUE sp\_RemoveUserFromGroup(

rsmith,

Managers )

See Also

[sp\_CreateGroup](master_sp_creategroup.htm)

[sp\_DropGroup](master_sp_dropgroup.htm)

[sp\_CreateUser](master_sp_createuser.htm)

[sp\_DropUser](master_sp_dropuser.htm)

[sp\_AddUserToGroup](master_sp_addusertogroup.htm)