---
title: Ace Adsddgetdatabaseproperty
slug: ace_adsddgetdatabaseproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgetdatabaseproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a335cefc10a9d31fc28a1baa5a0bf80904c87098
---

# Ace Adsddgetdatabaseproperty

AdsDDGetDatabaseProperty

AdsDDGetDatabaseProperty

Advantage Client Engine

| AdsDDGetDatabaseProperty  Advantage Client Engine |  |  |  |  |

Retrieves one database property from the data dictionary into the supplied buffer.

Syntax

UNSIGNED32 AdsDDGetDatabaseProperty( ADSHANDLE hDBConn,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hDBConn (I) | Handle of database connection). |
| usPropertyID (I) | Index of a database property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| \*pusPropertyLen (I/O) | On input, it specifies the size of the buffer pointed to by pvProperty. On output, it returns the length of property stored in the buffer. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid database property, or the specified property is not retrievable. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and \*pusPropertylen. |

Remarks

AdsDDGetDatabaseProperty retrieves one database property from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Returns the database description in pvProperty. |
| ADS\_DD\_VERSION\_MAJOR | Returns the user major version property. On input, the \*pusPropertyLength should be equal to or greater than 2. See [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md) for more info. |
| ADS\_DD\_VERSION\_MINOR | Returns the user minor version property. On input, the \*pusPropertyLength should be equal to or greater than 2. See [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md) for more info. |
| ADS\_DD\_USER\_DEFINED\_PROP | Returns the user defined database property. |
| ADS\_DD\_DEFAULT\_TABLE\_PATH | Returns in the pvProperty the default path for creating new tables. The path is a fully qualified UNC path. If this property is not set, the default table path is the same directory as the data dictionary. |
| ADS\_DD\_TEMP\_TABLE\_PATH | Returns in the pvProperty the default path for creating temporary tables. The path is a fully qualified UNC path. If this property is not set, the default temporary table path is the same as the default table path. |
| ADS\_DD\_LOG\_IN\_REQUIRED | Returns in the pvProperty a 2-byte (UNSIGNED16) integer that indicates whether anonymous user connection is allowed to the database. The returned value is zero if anonymous user is allowed to make connection to the database. Otherwise the database does not allow an anonymous connection. See [AdsConnect60](ace_adsconnect60.md) for more information. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_VERIFY\_ACCESS\_RIGHTS | Returns in the pvProperty a 2-byte (UNSIGNED16) integer that indicates whether the Advantage Database Server enforces the users access rights when opening a database table or view or executing a stored procedure. The returned value is zero if the Advantage Database Server does not enforce the user access rights. A non-zero value is returned if the Advantage Database Server enforces the user access rights. See [AdsConnect60](ace_adsconnect60.md) and [AdsOpenTable](ace_adsopentable.md) for more information. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD | Returns in pvProperty the table encryption password that is used to encrypt all encrypted tables in the data dictionary. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_ENCRYPT\_NEW\_TABLE | Returns in pvProperty a 2-byte (UNSIGNED16) integer that indicates whether the table will be automatically encrypted when being added or created in the data dictionary. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_DATA\_ENCRYPTION\_TYPE | Returns in pvProperty a 4-byte (UNSIGNED32) integer that contains the type of encryption that is used for newly encrypted tables. This property is set when the dictionary is created. Possible values include ADS\_ENCRYPTION\_RC4 (3), ADS\_ENCRYPTION\_AES128 (5), and ADS\_ENCRYPTION\_AES256 (6). It is possible to change the encryption type with the system procedure [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md). |
| ADS\_DD\_FTS\_DELIMITERS | Returns in pvProperty the Full Text Search (FTS) delimiter characters for the data dictionary. |
| ADS\_DD\_FTS\_NOISE | Returns in pvProperty the default Full Text Search (FTS) noise words for the data dictionary. |
| ADS\_DD\_FTS\_DROP\_CHARS | Returns in pvProperty the default Full Text Search (FTS) drop characters for the data dictionary. |
| ADS\_DD\_FTS\_CONDITIONAL\_CHARS | Returns in pvProperty the default Full Text Search (FTS) conditional drop characters for the data dictionary. |
| ADS\_DD\_ENCRYPTED | This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_LOGINS\_DISABLED | Returns in pvProperty a 2-btye (UNSIGNED16) integer that indicates if the database is currently allowing logins. See [Disabling Database Logins](master_disabling_database_logins.md) for more details. |
| ADS\_DD\_LOGINS\_DISABLED\_ERRSTR | Returns in pvProperty a string that is currently being used when denying database logins (if the ADS\_DD\_LOGINS\_DISABLED property is TRUE). |
| ADS\_DD\_ENCRYPTED | Returns in the pvProperty parameter a 2-byte (UNSIGNED16) integer that indicates if the data dictionary itself (.add file) is encrypted. If the returned value is zero the data dictionary is not encrypted. If the returned value is one the data dictionary is encrypted. Only the ADSSYS user and users authorized to modify the database are allowed to retrieve this property. |
| ADS\_DD\_ENCRYPT\_INDEXES | Returns in pvProperty a 2-byte (UNSIGNED16) integer that indicates whether indexes on encrypted tables will be encrypted. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_ENCRYPT\_COMMUNICATION | Returns in pvProperty a 2-byte (UNSIGNED16) integer that indicates whether all communication between the Advantage Database Server and client programs will be encrypted. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_QUERY\_VIA\_ROOT | Returns in pvProperty a 4-byte (UNSIGNED32) integer that indicates whether passthrough queries are allowed through the [root dictionary](master_root_dictionary.md). Valid values are a combination (bitmask) of ADS\_DD\_QVR\_OPT\_QUERY (0x01) and ADS\_DD\_QVR\_OPT\_PROCEDURE (0x02). The first value indicates that passthrough queries are allowed. The second value indicates that passthrough procedure calls are allowed. This property is checked by the Advantage Web Platform when queries and procedure calls are made "through" the root dictionary to another dictionary. If the value is not set, then the request is denied. This property was introduced primarily for use by the Web Administrator Utility. |

Example

After making a connection to the database, retrieve the description of the database.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = sizeof( aucMessage );

AdsDDGetDatabaseProperty( hDD, ADS\_DD\_COMMENT, aucMessage, &usBuffSize ) ;

AdsDisconnect( hDD );

See Also

[AdsDDCreate](ace_adsddcreate.md)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md)

[AdsConnect60](ace_adsconnect60.md)

[AdsDDCreateUser](ace_adsddcreateuser.md)

[AdsDDDeleteUser](ace_adsdddeleteuser.md)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[system.dictionary](master_system_dictionary.md)
