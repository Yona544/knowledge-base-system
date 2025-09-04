---
title: Ade Gettableproperty
slug: ade_gettableproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_gettableproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8c777b2f803bf8ae5a0ec815e52820a9e59d812b
---

# Ade Gettableproperty

GetTableProperty

TAdsDictionary.GetTableProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetTableProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Retrieves one table property into the supplied buffer from the data dictionary.

Syntax

TAdsDictionary.GetTableProperty( strTableName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 );

Parameters

| strTableName | Name of the table in the database to retrieve the property. |
| usPropertyID | Index of the table property to retrieve. See Remarks for allowed values. |
| pvProperty | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen | On input, it specifies the size of the buffer pointed by pvProperty. On output, it returns the length of property stored in the buffer. |

Remarks

TAdsDictionary.GetTableProperty retrieves one table property of the specified table property from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and usPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | The function returns the table description in pvProperty. |
| ADS\_DD\_USER\_DEFINED\_PROP | The function returns the user defined table property in pvProperty. |
| ADS\_DD\_TABLE\_VALIDATION\_EXPR | The function returns the tables record level validation expression. The validation expression is returned as a NULL terminated string. If no record level validation expression is defined in the data dictionary, the function returns  AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See Advantage Data Dictionary User Permissions for more information. |
| ADS\_DD\_TABLE\_VALIDATION\_MSG | The function returns the error message that will be returned when a record in the table is being modified in such a manner that the record will fail to pass the record level constraint. It is returned as a NULL terminated string. This property can only be retrieved by users with administrative permissions. See Advantage Data Dictionary User Permissions for more information. |
| ADS\_DD\_TABLE\_PRIMARY\_KEY | The function returns the key name of the tables primary key. The key name is returned as a NULL terminated string. The maximum length of the key name is ADS\_MAX\_OBJECT\_NAME\_LEN. If no primary key is defined for the table, the functions return AE\_PROPERTY\_NOT\_SET error. |
| ADS\_DD\_TABLE\_TYPE | The function returns the type of the base table. The table type is returned as a 2-byte (UNSIGNED16) number with the following possible values: ADS\_NTX, ADS\_CDX, ADS\_VFP, and ADS\_ADT. |
| ADS\_DD\_TABLE\_FIELD\_COUNT | The function returns the number of fields or columns in the table. The field count is returned as a 2 byte (UNSIGNED16) number. |
| ADS\_DD\_TABLE\_ENCRYPTION | The function returns the encryption state of the database table in pvProperty. The value returned in pvProperty is a 2-byte value. It is non-zero if the database table is encrypted. |
| ADS\_DD\_TABLE\_DEFAULT\_INDEX | Gets the default index to be used by the table. For optimized performance the default index is initially not set, indicating no default index should be used. The Advantage Client Engine does not use the default index directly. Client front-ends can call this API to retrieve the index name, and then take the appropriate actions to implement default index functionality. |
| ADS\_DD\_TABLE\_IS\_RI\_PARENT | The function returns a boolean value indicating if the table in question is a parent in a referential integrity rule. This property can only be retrieved by users with administrative permissions. See Advantage Data Dictionary User Permissions for more information. |
| ADS\_DD\_TABLE\_AUTO\_CREATE | The function returns the auto-creation flag of the table in pvProperty. The flag is returned as a 2-byte (UNSIGNED16) number. If the number is non-zero, the table will be automatically created by the ADS if the table cannot be found at the specified location. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_TABLE\_PERMISSION\_LEVEL | Returns in pvProperty a 2-byte integer (UNSIGNED16) indicating the tables access permission level. The table permission level determines how column permission are enforced for the table. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. The table permission level can be one of the following three values:  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_1: If the user does not have read permission to a column in the table, reading the value of the column by the user will not cause an error. Instead, NULL value is always returned on the column that the user does not have read permission. Filtering the table (using scope, filter, SQL WHERE clause) on the column that the user does not have permission is allowed. This level is most compatible with other shared file access databases such as Paradox.  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_2: This is the default table permission level in Advantage. Reading of a column in the table that the user does not have read permission does not cause an error condition. Instead, NULL value is always returned on the column that user does not have read permission. However, filtering the table (using scope, filter, SQL WHERE clause) on the column that the user does not have permission will return an error.  ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_3: This is the most restricted table permission level. Direct access to the table is not allowed. The table can only be access using SQL statements. If the SQL statement contains a column that the user does not have the proper access to, an error will be returned. In other words, the user must have read permission to all columns in the SELECT, WHERE, HAVING, and ORDER BY clause of the SQL statement. This level is most compatible with other client server database such as MS SQL Server. |
| ADS\_DD\_TABLE\_FIELD\_COUNT | The function returns the number of fields or columns in the table. The field count is returned as a 2 byte (UNSIGNED16) number. |
| ADS\_DD\_TABLE\_AUTO\_CREATE | Returns in pvProperty a 2-byte integer (UNSIGNED16) indicating whether this particular table and any indexes associated with it are automatically created should the files be missing when an open occurs. The returned value is FALSE if files are not to be re-created and TRUE if they should be. The default for this property is FALSE. |
| ADS\_DD\_TABLE\_MEMO\_BLOCK\_SIZE | Returns in pvProperty a 2-byte integer (UNSIGNED16) containing the value auto-creation functionality will use for the memo block size of the memo file should this table need to be re-created. AE\_PROPERTY\_NOT\_SET will be returned if the property has not been set, in which case auto-creation will use the default memo block based on the table type. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_TABLE\_ENCRYPTION | The function returns the encryption state of the database table in pvProperty. The value returned in pvProperty is a 2-byte value. It is non-zero if the database table is encrypted. |

Example

procedure GetTablePropertyExample;

var

usLength : UNSIGNED16;

oAdsDictionary : TAdsDictionary;

aucProperty : array[ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

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

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetTableProperty( 'salesreps',

ADS\_DD\_TABLE\_PRIMARY\_KEY,

@aucProperty,

usLength );

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetTableProperty( 'salesreps',

ADS\_DD\_TABLE\_DEFAULT\_INDEX,

@aucProperty,

usLength );

 

 

 

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

 

end;

See Also

[SetTableProperty](ade_settableproperty.md)

[SetFieldProperty](ade_setfieldproperty.md)

[GetFieldProperty](ade_getfieldproperty.md)
