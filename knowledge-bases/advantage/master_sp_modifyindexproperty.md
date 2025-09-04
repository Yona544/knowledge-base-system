sp\_ModifyIndexProperty




Advantage Database Server 12  

sp\_ModifyIndexProperty

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ModifyIndexProperty  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ModifyIndexProperty Advantage SQL Engine master\_Sp\_modifyindexproperty Advantage SQL > System Procedures > Procedures > sp\_ModifyIndexProperty / Dear Support Staff, |  |
| sp\_ModifyIndexProperty  Advantage SQL Engine |  |  |  |  |

Modifies an existing index in the data dictionary.

Syntax

sp\_ModifyIndexProperty(

TableName,CHARACTER,200,

IndexName,CHARACTER,200,

Property,CHARACTER,200,

Value,Memo )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name of the table containing the index order. |
| IndexName (I) | Name of the existing index to modify. |
| Property (I) | Name of an index property to set. See Remarks for allowed values./ |
| Value (I) | Property value to set. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | This error will be returned if the table or index name provided cannot be found in the dictionary. |
| AE\_INVALID\_PROPERTY\_ID | This error is returned if the property ID supplied is invalid for an index. |

Remarks

This procedure modifies an existing index. The following are the valid values of Property and the expected value in Value. Once an index description has been set in the dictionary, it can be retrieved by querying the system.indexes virtual table, or via the API AdsDDGetIndexProperty.

ALTER permission on the table containing the index being modified is required to modify data dictionary index properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

|  |  |
| --- | --- |
| usPropertyID | Description |
| COMMENT | Stores a new description for the index order. |

Example

After making a connection to the data dictionary, set a new description for the index "field1" that is built on table "table1":

EXECUTE PROCEDURE sp\_ModifyIndexProperty(

'Table1',

'Field1',

'COMMENT',

'This is a new description for this index' );

See Also

[system.indexes](master_system_indexes.htm)

AdsDDGetIndexProperty (in the Advantage Client Engine)

AdsDDSetIndexProperty (in the Advantage Client Engine)