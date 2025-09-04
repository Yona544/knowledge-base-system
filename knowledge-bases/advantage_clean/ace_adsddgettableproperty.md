---
title: Ace Adsddgettableproperty
slug: ace_adsddgettableproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgettableproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 202d06c2844256e2de86746b050475f0e0b124f1
---

# Ace Adsddgettableproperty

AdsDDGetTableProperty

AdsDDGetTableProperty

Advantage Client Engine

| AdsDDGetTableProperty  Advantage Client Engine |  |  |  |  |

Retrieves one table property from the data dictionary into the supplied buffer.

Syntax

UNSIGNED32 AdsDDGetTableProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucTableName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucTableName (I) | Name of the table in the database to retrieve the property. |
| usPropertyID (I) | Index of the table property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| \*pusPropertyLen (I/O) | On input, specifies the size of the buffer pointed by pvProperty. On output, returns the length of property stored in the buffer. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid table property, or the specified property cannot be retrieved. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and \*pusPropertyLen. |

Remarks

AdsDDGetTableProperty retrieves one table property of the specified database table from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | The function returns the table description in pvProperty. |
| ADS\_DD\_USER\_DEFINED\_PROP | The function returns the user defined table property in pvProperty. |
| ADS\_DD\_TABLE\_VALIDATION\_EXPR | The function returns the tables record level validation expression. The validation expression is returned as a NULL terminated string. If no record level validation expression is defined in the data dictionary, the function returns an AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data as ANSI encoded text. |
| ADS\_DD\_TABLE\_VALIDATION\_EXPR\_W | The function returns the tables record level validation expression. The validation expression is returned as a NULL terminated string. If no record level validation expression is defined in the data dictionary, the function returns an AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data as UTF-16 encoded text. |
| ADS\_DD\_TABLE\_VALIDATION\_MSG | The function returns the error message that will be returned when a record in the table is being modified in such a manner that the record will fail to pass the record level constraint. It is returned as a NULL terminated string. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_TABLE\_PRIMARY\_KEY | The function returns the index name of the tables primary key. The index name is returned as a NULL terminated string. The maximum length of the index name is ADS\_MAX\_OBJECT\_NAME\_LEN. If no primary key is defined for the table, the functions return an AE\_PROPERTY\_NOT\_SET error. |
| ADS\_DD\_TABLE\_TYPE | The function returns the type of the base table. The table type is returned as a 2 byte (UNSIGNED16) number with the following possible values: ADS\_NTX, ADS\_CDX, ADS\_VFP, and ADS\_ADT. |
| ADS\_DD\_TABLE\_FIELD\_COUNT | The function returns the number of fields or columns in the table. The field count is returned as a 2 byte (UNSIGNED16) number. |
| ADS\_DD\_TABLE\_ENCRYPTION | The function returns the encryption state of the database table in pvProperty. The value returned in pvProperty is a 2-byte value. It is non-zero if the database table is encrypted. |
| ADS\_DD\_TABLE\_DEFAULT\_INDEX | Gets the default index to be used by the table. For optimized performance the default index is initially not set, indicating no default index should be used. The Advantage Client Engine does not use the default index directly. Client front-ends can call this API to retrieve the index name, and then take the appropriate actions to implement default index functionality. |
| ADS\_DD\_TABLE\_IS\_RI\_PARENT | The function returns a boolean value indicating if the table in question is a parent in a referential integrity rule. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_TABLE\_AUTO\_CREATE | Returns in pvProperty a 2-byte integer (UNSIGNED16) indicating whether this particular table and any indexes associated with it are automatically created should the files be missing when an open occurs. The returned value is False if files are not to be re-created and True if they should be. The default for this property is False. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_TABLE\_PERMISSION\_LEVEL | Returns in pvProperty a 2-byte integer (UNSIGNED16) indicating the tables access permission level. The table permission level determines how column permissions are enforced for the table. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. The table permission level can be one of the following three values:  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_1: If the user does not have read permission to a column in the table, reading the value of the column by the user will not cause an error. Instead, NULL value is always returned on the column that the user does not have read permission. Filtering the table (using scope, filter, SQL WHERE clause) on the column that the user does not have permission is allowed. This level is most compatible with other shared file access databases such as Paradox.  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_2: This is the default table permission level in Advantage. Reading of a column in the table that the user does not have read permission does not cause an error condition. Instead, NULL value is always returned on the column that user does not have read permission. However, filtering the table (using scope, filter, SQL WHERE clause) on the column that the user does not have permission will return an error.  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_3: This is the most restricted table permission level. Direct access to the table is not allowed. The table can only be access using SQL statements. If the SQL statement contains a column that the user does not have the proper access to, an error will be returned. In other words, the user must have read permission to all columns in the SELECT, WHERE, HAVING, and ORDER BY clause of the SQL statement. This level is most compatible with other client server database such as MS SQL Server. |
| ADS\_DD\_TABLE\_MEMO\_BLOCK\_SIZE | Returns in pvProperty a 2-byte integer (UNSIGNED16) containing the value auto-creation functionality will use for the memo block size of the memo file should this table need to be re-created. AE\_PROPERTY\_NOT\_SET will be returned if the property has not been set, in which case auto-creation will use the default memo block based on the table type. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_TABLE\_CACHING | Returns in pvProperty a 2-byte integer (UNSIGNED16) containing the caching mode of the table.  Database ALTER permissions are required to read this property.  By default, the table caching mode is ADS\_TABLE\_CACHE\_NONE.  If read caching is enabled for the specified table, ADS\_TABLE\_CACHE\_READS will be returned.  If write caching is enabled, ADS\_TABLE\_CACHE\_WRITES will be returned.  Please read [Table Data Caching](master_table_data_caching.md) for more information. |
| ADS\_DD\_TABLE\_TXN\_FREE | Returns in pvProperty a 2-byte integer (UNSIGNED16) indicating whether this particular table is treated as a [transaction-free table](master_transaction_free_tables.md) or not.  The returned value is true if the updates to this table performed during a transaction are excluded from the transaction, and false otherwise.  The default for this property is False. |
| ADS\_DD\_TABLE\_CONCURRENCY\_ENABLED | Returns in pvProperty a 2-byte integer (UNSIGNED16) indicating whether this table is enabled for [optimistic concurrency](master_optimistic_concurrency.md). |

Example 1

After making a connection to the database, retrieve the number of fields in the "Customer Information" table.

AdsDDOpen( "n:\\MyData\\myData.ADD", NULL, &hDD );

usBufferSize = sizeof( usFieldCount );

AdsDDGetTableProperty( hDD, "Customer Information", ADS\_DD\_TABLE\_FIELD\_COUNT,

&usFieldCount, &usBuffSize ) ;

AdsDDClose( hDD );

Example 2

After making a database connection as an anonymous user, retrieve the description of the "Customer Information" table.

AdsConnect60( "n:\\MyData\\MyData.ADD", ADS\_REMOTE\_SERVER, NULL, NULL, ADS\_DEFAULT,

&hConn ));

usBufferSize = sizeof( acTableDescription );

AdsDDGetTableProperty( hConn, "Customer Information", ADS\_DD\_COMMENT,

acTableDescription, &usBuffSize ) ;

AdsDisconnect( hConn );

See Also

[AdsDDSetTableProperty](ace_adsddsettableproperty.md)

[AdsDDSetFieldProperty](ace_adsddsetfieldproperty.md)

[AdsDDGetFieldProperty](ace_adsddgetfieldproperty.md)

[AdsConnect60](ace_adsconnect60.md)

[system.tables](master_system_tables.md)
