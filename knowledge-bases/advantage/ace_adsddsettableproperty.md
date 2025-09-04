AdsDDSetTableProperty




Advantage Database Server 12  

AdsDDSetTableProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDSetTableProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDSetTableProperty Advantage Client Engine ace\_Adsddsettableproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDSetTableProperty  Advantage Client Engine |  |  |  |  |

Sets one table property in the data dictionary.

Syntax

UNSIGNED32 AdsDDSetTableProperty( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucTableName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen,

UNSIGNED16 usValidateOption,

UNSIGNED8 \*pucFailTable );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucTableName (I) | Name of the table in the database to set the property. |
| usPropertyID (I) | Index of a table property to set. See Remarks for possible values. |
| pvProperty (I) | Pointer to the property value to store in the data dictionary. |
| usPropertyLen (I) | Length of the property value pointed to by the pvProperty parameter. |
| usValidateOption (I) | If the property specified by usPropertyID is a constraint on records in the table, the usValidateOption parameter specifies the type of validation to perform on existing records in the table. This parameter is ignored otherwise. See Remarks for possible values. |
| pucFailTable (I) | If the property specified by usPropertyID is a constraint on records in the table, and validation is to be performed on existing records in the table, this parameter specifies the name of the file to save the records that are deleted from the table due to the new constraint. If this parameter is NULL, the records will be saved in a table named "savefail.adt" in the same directory as the table. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either usPropertyID is not a valid table property index, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | The table specified by pucTableName cannot be located in the data dictionary. |

Remarks

AdsDDSetTableProperty sets one property for the specified table in the database. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

ALTER permissions on the table are required to modify data dictionary table properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the table description. The pvProperty is expected to be NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or empty string, the table description is removed. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined table property. If pvProperty is NULL, the user defined table property is removed. User defined property is set, read, and interpreted by the application. It is not used by the Advantage Database Server. |
| ADS\_DD\_TABLE\_VALIDATION\_EXPR | Sets a new record level validation expression for the table. pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. To remove an existing record level validation expression for the table, use NULL or an empty string as pvProperty. The usValidateOption can be used to indicate how the existing records in the table should be validated. Setting this property requires the table to be opened and validated. |
| ADS\_DD\_TABLE\_VALIDATION\_EXPR\_W | Sets a new record level validation expression for the table. pvProperty is expected to be a NULL terminated UTF-16 string. usPropertyLen is the length of the string including the NULL terminator. To remove an existing record level validation expression for the table, use NULL or an empty string as pvProperty. The usValidateOption can be used to indicate how the existing records in the table should be validated. Setting this property requires the table to be opened and validated. |
| ADS\_DD\_TABLE\_VALIDATION\_MSG | Sets an error message that will be returned when a record in the table is being modified in such a manner that the record will fail to pass the record level constraint. pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_TABLE\_PRIMARY\_KEY | Sets the tables primary key. pvProperty is expected to be a NULL terminated string specifying the name of one of the indexes associated with the table. usPropertyLen is the length of the string including the NULL terminator. To remove an existing primary key for the table, use NULL or an empty string as pvProperty. The primary key of the table can be used as the default ordering of the records in the table or used to support referential integrity within the database. |
| ADS\_DD\_TABLE\_ENCRYPTION | Encrypt/decrypt the database table. pvProperty is expected to be a pointer to a 2 byte value and usPropertyLen is expected to be 2. If the 2 byte value pointed to by pvProperty is non-zero, the database table will be fully encrypted. If the table is an ADT table, the field header of the table will also be encrypted. If the 2 byte value pointed to by pvProperty is zero, the database table will be decrypted. |
| ADS\_DD\_TABLE\_DEFAULT\_INDEX | Sets the default index to be used by the table. For optimized performance the default index is initially not set, indicating no default index should be used. The Advantage Client Engine does not use the default index directly. Client front-ends must implement a call to [AdsDDGetTableProperty](ace_adsddgettableproperty.htm) to retrieve the index name, and then take the appropriate actions to implement default index functionality. |
| ADS\_DD\_TABLE\_PERMISSION\_LEVEL | Sets the table permission verification level. The table permission level determines how column permissions are enforced on this table. pvProperty is expected to be a pointer to a 2 byte value and usPropertyLen is expected to be 2. The 2 byte value pointed to by pvProperty can be one of the following values:  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_1: If the user does not have read permission to a column in the table, reading the value of the column by the user will not cause an error. Instead, a NULL value is returned on the column that the user does not have read permission to. Filtering the table (using a scope, filter, or SQL WHERE clause) on a column that the user does not have permission to is allowed. This permission level is most compatible with other shared file access databases such as Paradox.  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_2: This is the default table permission level in Advantage. Reading of a column in the table that the user does not have read permission to does not cause an error condition. Instead, a NULL value is always returned on the column that user does not have read permission to. However, filtering a table (using a scope, filter, or SQL WHERE clause) on the column that the user does not have permission to will return an error.  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_3: This is the most restrictive table permission level. Direct access to the table is not allowed. The table can only be accessed using SQL statements. If the SQL statement contains a column that the user does not have the proper access to, an error will be returned. In other words, the user must have read permission to all columns in the SELECT, WHERE, HAVING, and ORDER BY clauses of an SQL statement. This level is most compatible with other client server database such as MS SQL Server. |
| ADS\_DD\_TABLE\_AUTO\_CREATE | Changes whether or not the specified table and/or any associated indexes are automatically created. If the value is True and the table and/or associated indexes do not exist when the table is opened, the missing files will be automatically created. This property is a Boolean value and by default is set to False (turned off). pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. If the integer pointed to by the pvProperty is zero or NULL, the property is set to False. Otherwise the property is set to True. |
| ADS\_DD\_TABLE\_MEMO\_BLOCK\_SIZE | Sets the size of memo blocks that auto-creation functionality should use when re-creating a missing table and its associated memo file. pvProperty is expected to be a 2-byte integer value. usPropertyLen is expected to be 2 in order to set the property. The integer pointed to by pvProperty is expected to be a valid memo block size as described in [AdsCreateTable](ace_adscreatetable.htm). An invalid value will generate an AE\_INVALID\_MEMO\_BLOCK\_SIZE error. Passing in 0 for usLength or NULL for pvProperty will unset this property and Advantage will auto-create the table using the default memo block size for this particular table type. |
| ADS\_DD\_TABLE\_CACHING | Changes the table caching mode.  Database ALTER permissions are required to modify this setting.  This property is used to enable or disable caching of table data in the caching system.  Please read [Table Data Caching](master_table_data_caching.htm) before enabling this feature.  pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer.  usPropertyLen is expected to be 2.    ADS\_TABLE\_CACHE\_NONE:  The default setting.  No caching of table reads or writes is done.    ADS\_TABLE\_CACHE\_READS: This mode will cause the caching system to keep sections of the table in memory for faster read access.  When caching reads, updates to the table are still written to the physical disk.    ADS\_TABLE\_CACHE\_WRITES: This mode will turn on read caching and will cause the caching system to keep updates to the table in memory as long as there is enough memory to do so.  Updates may be kept in memory until the table is closed at which time all cached updates will be written to disk. |
| ADS\_DD\_TABLE\_TXN\_FREE | Changes whether or not the specified table is treated as a [transaction-free table](master_transaction_free_tables.htm).  This property is a Boolean value set to False by default.  pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer.  If the integer pointed to by pvProperty is zero or NULL, the property is set to False. Otherwise the property is set to True.  Configuring this property requires exclusive access to the table. |
| ADS\_DD\_TABLE\_WEB\_DELTA | Changes whether updates to the table should be tracked to support the delta query in the Advantage Web service. This property is a Boolean value set to False by default. pvProperty is expected to be a pointer to a 2 byte (UNSIGNED16) integer. The table must meet a few requirements in order for this property to be set to True: it must have a rowversion column, and it must have either a primary key or a unique index defined. If this property is set to True for any table in the data dictionary, ADS will create a GetTombstones table in the data dictionary to track the deleted rows. See [Advantage Web Platform Delta Operations](web_delta_operations.htm) for additional information. |
| ADS\_DD\_TABLE\_CONCURRENCY\_ENABLED | This property is used to enable [optimistic concurrency](master_optimistic_concurrency.htm) on the table when used with the Advantage Web Platform. This property is a Boolean value set to False by default. pvProperty is expected to be a pointer to a 2 byte (UNSIGNED16) integer.The table must have a rowversion column in order to be able to set this property to True. Note that if you ALTER a table and remove the rowversion field, this property will be reset to False. |

The usValidateOption parameter is used only when usPropertyID is ADS\_DD\_TABLE\_VALIDATION\_EXPR. It specifies how the function should validate existing records in the table. Once the record level constraint is successfully set for the database table, the Advantage Database Server will always validate any new records added to the table and any modification to existing records in the table. The following are the allowed values for usValidateOption.

|  |  |
| --- | --- |
| usValidateOption | Description |
| ADS\_NO\_VALIDATE | Do not perform any validation on existing records in the table. Only verify that the record level constraint expression is valid. CAUTION: Using this option can logically corrupt tables and is strongly discouraged. If an index is available on the field in question, validating constraints is a quick operation and should always be performed. |
| ADS\_VALIDATE\_APPEND\_FAIL | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table and appended to the table specified by pucFailTable or to the default fail table if pucFailTable is NULL. |
| ADS\_VALIDATE\_WRITE\_FAIL | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table. The fail table will be created to save all records that are removed from the original table. |
| ADS\_VALIDATE\_NO\_SAVE | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table. The deleted records are not saved and will be lost. |
| ADS\_VALIDATE\_RETURN\_ERROR | Perform validation on existing records in the table. If there are existing records in the table not meeting the new constraint, an error will be returned by the function. The table will not be modified. If the error is returned the new constraint will not be set. |

Example

After making a connection to the database, change the record level constraint of the "Customer Information" table. The records not meeting the new record level constraint are saved in "deleted.adt" in the same directory as the data dictionary.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

sprintf( aucExpr, "Not Empty( Customer ID ) " );

AdsDDSetTableProperty( hDD, "Customer Information",

ADS\_DD\_TABLE\_VALIDATION\_EXPR, aucExpr,

(UNSIGNED16)( strlen( aucExpr ) + 1 ),

ADS\_VALIDATE\_WRITE\_FAIL, "deleted.adt" );

AdsDisconnect( hDD );

See Also

[AdsDDGetTableProperty](ace_adsddgettableproperty.htm)

[AdsDDSetFieldProperty](ace_adsddsetfieldproperty.htm)

[AdsDDGetFieldProperty](ace_adsddgetfieldproperty.htm)

[sp\_ModifyTableProperty](master_sp_modifytableproperty.htm)