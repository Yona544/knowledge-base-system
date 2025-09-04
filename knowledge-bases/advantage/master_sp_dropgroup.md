sp\_DropGroup




Advantage Database Server 12  

sp\_DropGroup

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropGroup  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropGroup Advantage SQL Engine master\_Sp\_dropgroup Advantage SQL > System Procedures > Procedures > sp\_DropGroup / Dear Support Staff, |  |
| sp\_DropGroup  Advantage SQL Engine |  |  |  |  |

Delete a user group object from the database.

Syntax

sp\_DropGroup( GroupName,CHARACTER,100 )

Parameters

|  |  |
| --- | --- |
| GroupName (I) | Name of the user group object to delete. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the GroupName is not a valid user group name in the database. |

Remarks

sp\_DropGroup removes an existing user group from the database. All references to the user group by the database users are removed from the data dictionary.

Example

After making a connection to the database, delete the user group named "Managers" from the database.

EXECUTE PROCEDURE sp\_DropGroup( Managers );

See Also

[sp\_CreateGroup](master_sp_creategroup.htm)

[sp\_ModifyGroupProperty](master_sp_modifygroupproperty.htm)

[sp\_CreateUser](master_sp_createuser.htm)

[sp\_DropUser](master_sp_dropuser.htm)

[sp\_AddUserToGroup](master_sp_addusertogroup.htm)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.htm)