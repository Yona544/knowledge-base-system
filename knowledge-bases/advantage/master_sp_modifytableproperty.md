sp\_ModifyTableProperty




Advantage Database Server 12  

sp\_ModifyTableProperty

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ModifyTableProperty  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ModifyTableProperty Advantage SQL Engine master\_Sp\_modifytableproperty Advantage SQL > System Procedures > Procedures > sp\_ModifyTableProperty / Dear Support Staff, |  |
| sp\_ModifyTableProperty  Advantage SQL Engine |  |  |  |  |

Sets one table property in the data dictionary.

Syntax

sp\_ModifyTableProperty(

TableName,CHARACTER,200,

Property,CHARACTER,200,

Value,MEMO,

ValidationOption,CHARACTER,25,

FailTable,CHARACTER,515 )

sp\_ModifyTableProperty(

TableName,CHARACTER,200,

Property,CHARACTER,200,

Value,NMEMO,

ValidationOption,CHARACTER,25,

FailTable,CHARACTER,515 )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name of the table in the database to set the property. |
| Property (I) | Name of table property to set. See Remarks for possible values. |
| Value (I) | Value to store in the data dictionary. |
| ValidationOption (I) | If the property is a constraint on records in the table, the ValidationOption parameter specifies the type of validation to perform on existing records in the table. See Remarks for possible values. |
| FailTable (I) | If the property specified is a constraint on records in the table, and validation is to be performed on existing records in the table, this parameter specifies the name of the file to save the records that are deleted from the table due to the new constraint. If this parameter is NULL, the records will be saved in a table named "savefail.adt" in the same directory as the table. If a path is specified, it must be a fully qualified UNC path or a relative path from the data dictionary. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either Property is not a valid table property index, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | The table specified by TableName cannot be located in the data dictionary. |

Remarks

sp\_ModifyTableProperty sets one property for the specified table in the database. The new property overwrites the existing property in the data dictionary. The following are the valid property names.

|  |  |
| --- | --- |
| Property | Description |
| COMMENT | Changes the table description. |
| TABLE\_VALIDATION\_EXPR | Sets a new record level validation expression for the table. To remove an existing record level validation expression for the table, use NULL or an empty string as the value. The ValidationOption can be used to indicate how the existing records in the table should be validated. Setting this property requires the table to be opened and validated. |
| TABLE\_VALIDATION\_MSG | Sets an error message that will be returned when a record in the table is being modified in such a manner that the record will fail to pass the record level constraint. |
| TABLE\_PRIMARY\_KEY | Sets the tables primary key. Value is the name of one of the indexes associated with the table. To remove an existing primary key for the table, use NULL or an empty string. The primary key of the table can be used as the default ordering of the records in the table or used to support referential integrity within the database. |
| TABLE\_ENCRYPTION | Encrypt/decrypt the database table. Pass in TRUE to encrypt the table and FALSE to decrypt the table. If the table is an ADT table, the field header of the table will also be encrypted. |
| TABLE\_DEFAULT\_INDEX | Sets the default index to be used by the table. For optimized performance the default index is initially not set, indicating no default index should be used. The Advantage Client Engine does not use the default index directly. Client front-ends must implement a call to AdsDDGetTableProperty to retrieve the index name, and then take the appropriate actions to implement default index functionality. |
| TABLE\_PERMISSION\_LEVEL | Sets the table permission verification level. The table permission level determines how column permissions are enforced on this table. The value is expected to be an integer representing the permission level.  Permission Level 1: If the user does not have read permission to a column in the table, reading the value of the column by the user will not cause an error. Instead, a NULL value is returned on the column that the user does not have read permission to. Filtering the table (using a scope, filter, or SQL WHERE clause) on a column that the user does not have permission to is allowed. This permission level is most compatible with other shared file access databases such as Paradox. Pass in 1 as the value to the system procedure.  Permission Level 2: This is the default table permission level in Advantage. Reading of a column in the table that the user does not have read permission to does not cause an error condition. Instead, a NULL value is always returned on the column that user does not have read permission to. However, filtering a table (using a scope, filter, or SQL WHERE clause) on the column that the user does not have permission to will return an error. Pass in 2 as the value to the system procedure.  Permission Level 3: This is the most restrictive table permission level. Direct access to the table is not allowed. The table can only be accessed using SQL statements. If the SQL statement contains a column that the user does not have the proper access to, an error will be returned. In other words, the user must have read permission to all columns in the SELECT, WHERE, HAVING, and ORDER BY clauses of an SQL statement. This level is most compatible with other client server database such as MS SQL Server. Pass in 3 as the value to the system procedure. |
| TABLE\_AUTO\_CREATE | Changes whether or not the specified table and/or any associated indexes are automatically created. If the value is True and the table and/or associated indexes do not exist when the table is opened, the missing files will be automatically created. This property is False by default (turned off). |
| TABLE\_MEMO\_BLOCK\_SIZE | Sets the size of memo blocks that auto-creation functionality should use when re-creating a missing table and its associated memo file. Passing in NULL will unset this property and Advantage will auto-create the table using the default memo block size for this particular table type. |
| TABLE\_TRANS\_FREE | Changes whether or not the specified table is treated as a [transaction-free table](master_transaction_free_tables.htm).  If the value is True, all updates to the table when a transaction is active will be excluded from the scope of the transaction.  This property is False by default. |
| TABLE\_CACHING | This property is used to enable or disable caching of table data in the caching system.  Please read [Table Data Caching](master_table_data_caching.htm) before enabling this feature.  Value is expected to be 1 (CACHE\_READS), 2 (CACHE\_WRITES), or 0 (CACHE\_NONE). |
| TABLE\_WEB\_DELTA | This property is used to enable tracking updates to the table to support the delta query in the Advantage Web service. This property is False by default. See [Advantage Web Platform Delta Operations](web_delta_operations.htm) for additional information. The table must have a rowversion column and a primary key or unique index to support this function. |
| TABLE\_CONCURRENCY\_ENABLED | This property is used to enable [optimistic concurrency](master_optimistic_concurrency.htm) on the table when used with the Advantage Web Platform. This property is False by default.The table must have a rowversion field in order to be able to set this property to True. Note that if you ALTER a table and remove the rowversion field, this property will be reset to False. |

The ValidateOption parameter is used only when Property is TABLE\_VALIDATION\_EXPR. It specifies how the function should validate existing records in the table. Once the record level constraint is successfully set for the database table, the Advantage Database Server will always validate any new records added to the table and any modification to existing records in the table. The following are the allowed values for ValidateOption.

|  |  |
| --- | --- |
| ValidateOption | Description |
| NO\_VALIDATE | Do not perform any validation on existing records in the table. Only verify that the record level constraint expression is valid. CAUTION: Using this option can logically corrupt tables and is strongly discouraged. If an index is available on the field in question, validating constraints is a quick operation and should always be performed. |
| APPEND\_FAIL | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table and appended to the table specified by FailTable or to the default fail table if FailTable is NULL. |
| WRITE\_FAIL | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table. The fail table will be created to save all records that are removed from the original table. |
| NO\_SAVE | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table. The deleted records are not saved and will be lost. |
| RETURN\_ERROR | Perform validation on existing records in the table. If there are existing records in the table not meeting the new constraint, an error will be returned by the function. The table will not be modified. If the error is returned the new constraint will not be set. |

Example

After making a connection to the database, change the record level constraint of the "Customer Information" table. The records not meeting the new record level constraint are saved in "deleted.adt" in the same directory as the data dictionary.

EXECUTE PROCEDURE sp\_ModifyTableProperty(

Customer Information,

TABLE\_VALIDATION\_EXPR,

Not Empty( Customer ID ),

VALIDATE\_WRITE\_FAIL,

deleted.adt );

 

Enable table to track updates to support the delta query in the Advantage Web service:

EXECUTE PROCEDURE sp\_ModifyTableProperty(

ORDERS,

TABLE\_WEB\_DELTA,

True,

NULL,

NULL );

 

 

See Also

[system.tables](master_system_tables.htm)

[sp\_ModifyFieldProperty](master_sp_modifyfieldproperty.htm)