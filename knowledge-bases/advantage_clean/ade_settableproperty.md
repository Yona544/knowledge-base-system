---
title: Ade Settableproperty
slug: ade_settableproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_settableproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ab34c1902686e67bab8ecf8115a5664e5bc757de
---

# Ade Settableproperty

SetTableProperty

TAdsDictionary.SetTableProperty

Advantage TDataSet Descendant

| TAdsDictionary.SetTableProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Sets one table property in the data dictionary.

Syntax

TAdsDictionary.SetTableProperty( strTableName : string;

usPropertyID : UNSIGNED16;

pvProperty : pointer;

usPropertyLen : UNSIGNED16;

usValidateOption : UNSIGNED16;

strFailTable : string);

Parameters

| strTableName | Name of the table in the database to set the property. |
| usPropertyID | Index of a table property to set. See Remarks for possible values. |
| strProperty | Pointer to the property value to stored in the data dictionary. |
| usValidateOption (I) | If the property specified by usPropertyID is a constraint on records in the table, the usValidateOption parameter specifies the kind of validation to perform on existing records in the table. This parameter is ignored otherwise. See Remarks for possible values. |
| strFailTable (I) | If the property to set is a constraint on records in the table, and validation is to be performed on existing records in the table, this parameter specifies the name of the file to save the records that are deleted from the table due to the new constraint. If this parameter is NULL, the records will be saved in a table named "savefail.adt" in the same directory as the table. |
| usPropertyLen (I) | The size of the property pointed to by pvProperty. |

Remarks

SetTableProperty sets one property of the specified table in the database. The new property overwrites the existing property in the data dictionary. The properties can only be set when the TAdsDictionary is opened by a user with ALTER permissions on the table. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the table description. The pvProperty is expected to be NULL terminated string. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined table property. If pvProperty is NULL, the user defined table property is removed. User defined property is set, read, and interpreted by the application. It is not used by the Advantage Database Server. |
| ADS\_DD\_TABLE\_VALIDATION\_EXPR | Sets a new record level validation expression for the table. pvProperty is expected to be a NULL terminated string. To remove existing record level validation expression for the table, use empty string as pvProperty. The usValidateOption can be used to indicate how the existing records in the table should be validated. |
| ADS\_DD\_TABLE\_VALIDATION\_MSG | Sets an error message that will be returned when a record in the table is being modified in such a manner that the record will fail to pass the record level constraint. pvProperty is expected to be a NULL terminated string. |
| ADS\_DD\_TABLE\_PRIMARY\_KEY | Sets the tables primary key. pvProperty is expected to be a NULL terminated string specifying the name of one of the keys associated with the table. To remove existing primary key for the table, use empty string as pvProperty. The primary key of the table can be used as the default ordering of the records in the table or used to support referential integrity within the database. |
| ADS\_DD\_TABLE\_ENCRYPTION | Encrypt/decrypts the database table. pvProperty is expected to be a pointer to a 2 byte value and usPropertyLen is expected to be 2. If the 2-byte value pointed to by pvProperty is non-zero, the database table will be fully encrypted. If the table is an ADT table, the field header of the table will also be encrypted. If the 2-byte value pointed to by pvProperty is zero, the database table will be decrypted. |
| ADS\_DD\_TABLE\_DEFAULT\_INDEX | The [default index](ade_defaultindex.md) for the table. Set the same way as the primary key property. |
| ADS\_DD\_TABLE\_PERMISSION\_LEVEL | Sets the table permission verification level. The table permission level determines how column permissions are enforced on this table. pvProperty is expected to be a pointer to a 2 byte value and usPropertyLen is expected to be 2. The 2 byte value pointed to by pvProperty can be one of the following values:  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_1: If the user does not have read permission to a column in the table, reading the value of the column by the user will not cause an error. Instead, a NULL value is returned on the column that the user does not have read permission to. Filtering the table (using a scope, filter, or SQL WHERE clause) on a column that the user does not have permission to is allowed. This permission level is most compatible with other shared file access databases such as Paradox.  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_2: This is the default table permission level in Advantage. Reading of a column in the table that the user does not have read permission to does not cause an error condition. Instead, a NULL value is always returned on the column that user does not have read permission to. However, filtering a table (using a scope, filter, or SQL WHERE clause) on the column that the user does not have permission to will return an error.  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_3: This is the most restrictive table permission level. Direct access to the table is not allowed. The table can only be accessed using SQL statements. If the SQL statement contains a column that the user does not have the proper access to, an error will be returned. In other words, the user must have read permission to all columns in the SELECT, WHERE, HAVING, and ORDER BY clauses of an SQL statement. This level is most compatible with other client server database such as MS SQL Server. |
| ADS\_DD\_TABLE\_AUTO\_CREATE | Changes whether or not the specified table and/or any associated indexes are automatically created. If the value is True and the table and/or associated indexes do not exist when the table is opened, the missing files will be automatically created. This property is a Boolean value and by default is set to False (turned off). pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usLength is expected to be 2. If the integer pointed to by the pvProperty is zero or NULL, the property is set to False. Otherwise the property is set to True. |
| ADS\_DD\_TABLE\_MEMO\_BLOCK\_SIZE | Sets the size of memo blocks that auto-creation functionality should use when re-creating a missing table and its associated memo file. pvProperty is expected to be a 2-byte integer value. usLength is expected to be 2 in order to set the property. The integer pointed to by pvProperty is expected to be a valid memo block size as described in [AdsCreateTable](ade_adscreatetable.md). An invalid value will generate an AE\_INVALID\_MEMO\_BLOCK\_SIZE error. Passing in 0 for usLength or NULL for pvProperty will unset this property and Advantage will auto-create the table using the default memo block size for this particular table type. |

The usValidateOption parameter is used only when usPropertyID is ADS\_DD\_TABLE\_VALIDATION\_EXPR. It specifies how the existing records in the table should be validated. New records added to the table will always be validated against the record level constraint. Modified existing records will always be validated against the record level constraint also. The following are the allowed values for usValidateOption.

| usValidateOption | Description |
| ADS\_NO\_VALIDATE | Do not perform any validation on existing records in the table. |
| ADS\_VALIDATE\_APPEND\_FAIL | Perform validation on existing records in the table. Records fail to meet the new constraint will be permanently deleted from the table and appended to the table specified by strFailTable or to the default fail table if strFailTable is empty string. |
| ADS\_VALIDATE\_WRITE\_FAIL | Perform validation on existing records in the table. Records fail to meet the new constraint will be permanently deleted from the table. The fail table will be created to save all records that are removed from the original table. |
| ADS\_VALIDATE\_NO\_SAVE | Perform validation on existing records in the table. Records fail to meet the new constraint will be permanently deleted from the table. The deleted records are not saved and will be lost. |
| ADS\_VALIDATE\_RETURN\_ERROR | Perform validation on existing records in the table. If there are existing records in the table not meeting the new constraint, an error will be returned by the function. Table will not be modified. If the error is returned the new constraint will not be set. |

Example

procedure SetTablePropertyExample;

var

usLength : UNSIGNED16;

oAdsDictionary : TAdsDictionary;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

{\* now we are going to add a couple tables from our sample tables \*}

oAdsDictionary.AddTable( 'salesreps',

'd:\demo\salesreps.adt',

'',

'customers table',

ttAdsADT,

ANSI );

 

usLength := length( 'empl\_num' ) + 1;

oAdsDictionary.SetTableProperty( 'salesreps',

ADS\_DD\_TABLE\_PRIMARY\_KEY,

pChar( 'empl\_num' ),

usLength,

ADS\_NO\_VALIDATE,

'' );

 

usLength := length( 'manager' ) + 1;

oAdsDictionary.SetTableProperty( 'salesreps',

ADS\_DD\_TABLE\_DEFAULT\_INDEX,

pChar( 'manager' ),

usLength,

ADS\_NO\_VALIDATE,

'' );

 

 

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

end;

See Also

[GetTableProperty](ade_gettableproperty.md)

[SetFieldProperty](ade_setfieldproperty.md)

[GetFieldProperty](ade_getfieldproperty.md)
