---
title: Ade Getdatabaseproperty
slug: ade_getdatabaseproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getdatabaseproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 333ece11bc116a5ea74d6a7171904cd9cde1f260
---

# Ade Getdatabaseproperty

GetDatabaseProperty

TAdsDictionary.GetDatabaseProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetDatabaseProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.GetDatabaseProperty( usPropertyID : UNSIGNED16;

pvProperty : pointer;

var usBufferLength : UNSIGNED16 );

Parameters

| usPropertyID | Index of a database property to retrieve. See Remarks for allowed values. |
| pvProperty | Pointer to the buffer where the property is to be copied into. |
| usBufferLength | On input, it specifies the size of the buffer pointed to by pvProperty. On output, it returns the length of property copied into the buffer. |

Remarks

TAdsDictionary.GetProperty retrieves one database property from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Returns the database description in pvProperty. |
| ADS\_DD\_DEFAULT\_TABLE\_PATH | Returns in the pvProperty the default path for creating new tables. The path is a full qualified UNC path. If this property is not set, the default table path is the same directory as the data dictionary. |
| ADS\_DD\_TEMP\_TABLE\_PATH | Returns in the pvProperty the default path for creating temporary tables. The path is a full qualified UNC path. If this property is not set, the default temporary table path is the same as the default table path. |
| ADS\_DD\_LOG\_IN\_REQUIRED | Returns in the pvProperty a 2-byte (UNSIGNED16) integer that indicates whether an anonymous user connection is allowed to the database. The returned value is zero if the anonymous user is allowed to make a connection to the database. Otherwise the database does not allow an anonymous connection. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_VERIFY\_ACCESS\_RIGHTS | Returns in the pvProperty a 2-byte (UNSIGNED16) integer that indicates whether the Advantage Database Server enforces the users access rights when working with objects in the database. Permissions can be defined for tables, columns, views, stored procedures and links. If the returned value for this property is zero, the Advantage Database Server does not enforce the user access rights. A non-zero value is returned if the Advantage Database Server enforces the user access rights. See [TAdsDictionary.GrantPermissions](ade_grantpermissions_tadsdictionary.md) for more information. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD | Returns in pvProperty the table encryption password that is used to encrypt all encrypted tables in the data dictionary. This property can only be retrieved when by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_ENCRYPT\_NEW\_TABLE | Returns in pvProperty a 2-byte (UNSIGNED16) integer that indicates whether the table will be automatically encrypted when being added or created in the data dictionary. This property can only be by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_DATA\_ENCRYPTION\_TYPE | Returns in pvProperty a 4-byte (UNSIGNED32) integer that contains the type of encryption that is used for newly encrypted tables. This property is set when the dictionary is created. Possible values include ADS\_ENCRYPTION\_RC4 (3), ADS\_ENCRYPTION\_AES128 (5), and ADS\_ENCRYPTION\_AES256 (6). It is possible to change the encryption type with the system procedure [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md). |
| ADS\_DD\_VERSION\_MAJOR | Returns the user major version property. On input, the usBufferLength should be equal to or greater than 2. See [TAdsDictionary.SetDatabaseProperty](ade_setdatabaseproperty.md) for more info. |
| ADS\_DD\_VERSION\_MINOR | Returns the user minor version property. On input, the usBufferLength should be equal to or greater than 2. See [TAdsDictionary.SetDatabaseProperty](ade_setdatabaseproperty.md) for more info. |
| ADS\_DD\_ENCRYPTED | This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_FTS\_DELIMITERS | Returns in pvProperty the Full Text Search (FTS) delimiter characters for the data dictionary. |
| ADS\_DD\_FTS\_NOISE | Returns in pvProperty the default Full Text Search (FTS) noise words for the data dictionary. |
| ADS\_DD\_FTS\_DROP\_CHARS | Returns in pvProperty the default Full Text Search (FTS) drop characters for the data dictionary. |
| ADS\_DD\_FTS\_CONDITIONAL\_CHARS | Returns in pvProperty the default Full Text Search (FTS) conditional drop characters for the data dictionary. |
| ADS\_DD\_LOGINS\_DISABLED | Returns in pvProperty a 2-btye (UNSIGNED16) integer that indicates if the database is currently allowing logins. See [Disabling Database Logins](master_disabling_database_logins.md) for more details. |
| ADS\_DD\_LOGINS\_DISABLED\_ERRSTR | Returns in pvProperty a string that is currently being used when denying database logins (if the ADS\_DD\_LOGINS\_DISABLED property is TRUE). |
| ADS\_DD\_ENCRYPTED | Returns in the pvProperty parameter a 2-byte (UNSIGNED16) integer that indicates if the data dictionary itself (.add file) is encrypted. If the returned value is zero the data dictionary is not encrypted. If the returned value is one the data dictionary is encrypted. Only the ADSSYS user and users authorized to modify the database are allowed to retrieve this property. |
| ADS\_DD\_ENCRYPT\_INDEXES | Returns in pvProperty a 2-byte (UNSIGNED16) integer that indicates whether indexes on encrypted tables will be encrypted. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_ENCRYPT\_COMMUNICATION | Returns in pvProperty a 2-byte (UNSIGNED16) integer that indicates whether all communication between the Advantage Database Server and client programs will be encrypted. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |

Example

Getting the database comment.

procedure GetDatabasePropertyExample;

var

oAdsDictionary : TAdsDictionary;

aucProperty : array[ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

usBufferLength : UNSIGNED16;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_LOCAL];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\*

\* The CreateDictionary call leaves an ADSSYS connection open. We will get

\* the comments with this connection

\*}

 

usBufferLength := ADS\_DD\_MAX\_PROPERTY\_LEN:

oAdsDictionary.GetDatabaseProperty( ADS\_DD\_COMMENT,

@aucProperty,

usBufferLength );

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

end;

See Also

[CreateDictionary](ade_createdictionary.md)

[SetDatabaseProperty](ade_setdatabaseproperty.md)
