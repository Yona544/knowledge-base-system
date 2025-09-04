sp\_ModifyGroupProperty




Advantage Database Server 12  

sp\_ModifyGroupProperty

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ModifyGroupProperty  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ModifyGroupProperty Advantage SQL Engine master\_Sp\_modifygroupproperty Advantage SQL > System Procedures > Procedures > sp\_ModifyGroupProperty / Dear Support Staff, |  |
| sp\_ModifyGroupProperty  Advantage SQL Engine |  |  |  |  |

Sets one property associated with a database user group in the data dictionary.

Syntax

sp\_ModifyGroupProperty(

GroupName,CHARACTER,100,

Property,CHARACTER,200,

Value,MEMO )

Parameters

|  |  |
| --- | --- |
| GroupName (I) | Name of the database user group object to set the associated property. |
| Property (I) | Name of a database user group property to set. See Remarks for allowed values. |
| Property (I) | Value to be stored in the property. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Possible causes for the error is that the pucUserGroupName does not specify a valid user group in the database. |

Remarks

sp\_ModifyGroupProperty sets one property associated with the specified user group. The new property overwrites the existing property in the data dictionary. The following are the valid values of Property and the expected values.

|  |  |
| --- | --- |
| usPropertyID | Description |
| COMMENT | Stores a new description for the user group. |

Example

After making a connection to the database, store a new description for the user group "Managers".

EXECUTE PROCEDURE sp\_ModifyGroupProperty(

Managers ,

COMMENT,

Managers of the Data Product Division. );

See Also

[sp\_CreateGroup](master_sp_creategroup.htm)

[sp\_DropGroup](master_sp_dropgroup.htm)

[sp\_CreateUser](master_sp_createuser.htm)

[sp\_DropUser](master_sp_dropuser.htm)

[sp\_AddUserToGroup](master_sp_addusertogroup.htm)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.htm)