---
title: Master Sp Modifydatabase
slug: master_sp_modifydatabase
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_modifydatabase.htm
source: Advantage CHM
tags:
  - master
checksum: f1cfd35bfad2eb537c04d9a554a487d0c311d413
---

# Master Sp Modifydatabase

sp\_ModifyDatabase

sp\_ModifyDatabase

Advantage SQL Engine

| sp\_ModifyDatabase  Advantage SQL Engine |  |  |  |  |

Sets one database property in the data dictionary.

Syntax

sp\_ModifyDatabase(

Property,CHARACTER,200,

Value,MEMO )

Parameters

| Property (I) | Name of a database property to set. See below for possible values. |
| Value (I) | Property to be stored in the data dictionary. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in Property is not a valid database property index, or the specified property cannot be modified. |
| AE\_NO\_TABLE\_ENCRYPTION\_PASSWORD | This error is returned when setting the ENCRYPT\_NEW\_TABLE property to True and the databases table encryption password property, ENCRYPT\_TABLE\_PASSWORD, has not been set. |

Remarks

sp\_ModifyDatabase sets one database property in the data dictionary. The new property overwrites the existing property in the data dictionary. The following are the valid values of Property.

| Property | Description |
| COMMENT | Changes the database description. |
| VERSION\_MAJOR | Sets the user defined major version property of the data dictionary. This property is intended for storing a value associated with the major version of the user's dictionary. The user version property is set, read, and interpreted by the application. The Advantage Database Server does not currently use it internally. The default value for this property, if it has never been set, is 0. If a value of NULL is used, the user version property value will be removed. |
| VERSION\_MINOR | Sets the user defined minor version property of the data dictionary. This property is intended for storing a value associated with the minor version of the user's dictionary. The user version property is set, read, and interpreted by the application. The Advantage Database Server does not currently use it internally. The default value for this property, if it has never been set, is 0. If a value of is NULL is used, the user version property value will be removed. |
| DEFAULT\_TABLE\_PATH | Changes the default path for creating new tables. If the value is NULL or an empty string, new tables will be created in the same directory as the data dictionary. No verification of the validity of the path is made. If the default table path is set to an invalid path, subsequent attempts to create new tables in this data dictionary will fail. The path must be a fully qualified UNC path or a relative path from the data dictionary. |
| TEMP\_TABLE\_PATH | Changes the path for creating temporary tables. If the value is NULL or an empty string, a temporary table will be created in the same directory as the normal tables. Advantage Database Server and Advantage Local Server create temporary tables and indexes when executing SQL statements. The path must be a fully qualified UNC path or a relative path from the data dictionary. |
| ADMIN\_PASSWORD | Changes the administrative password of the database. If the value is NULL or an empty string, the data dictionary is re-set to not require an administrative password to maintain the data dictionary. |
| LOG\_IN\_REQUIRED | Changes whether an anonymous user connection to the database is allowed. The default is False when the data dictionary is created. If the integer pointed to by the pvProperty is zero, the property is set to False. Otherwise the property is set to True. If this property is set to False, anonymous connection to the database with no user name and no password is allowed. Otherwise a user name and password is required to make a database connection to the data dictionary. See AdsConnect60 for more information. |
| VERIFY\_ACCESS\_RIGHTS | This property determines whether the Advantage Database Server will enforce the users access rights when opening a database table or view or executing a stored procedure. This property is a Boolean value. It is defaulted to False when the data dictionary is created. If this property is set to False, the Advantage database server does not verify the users access rights when opening a database table or view or when executing a stored procedure. The implication is that all users have full rights to all objects in the database. If this property is set to True, the users access rights are verified. Note that an anonymous user does not have any rights to objects in the database. If the database is set up to verify user access rights, an anonymous user can make a connection to the database but he cannot open any table or view or execute any stored procedure. |
| ENCRYPT\_TABLE\_PASSWORD | This property sets the encryption password for the database tables for use with default encryption. It is not used when using AES encryption.   Refer to the [encryption overview](master_encryption.md) for more information. Setting this property does not encrypt any table in the data dictionary. It only sets the password that all database tables in the data dictionary will be encrypted with. If the value is NULL or a pointer to an empty string, the function will remove the database encryption password from the data dictionary and, as a side effect, sets the database property ENCRYPT\_NEW\_TABLE to False. Setting and removing this property requires that all database tables in the data dictionary not be encrypted. If there are encrypted table(s) in the data dictionary, this function will fail with error AE\_DD\_REQUEST\_NOT\_COMPLETED. Once this property is set, calling sp\_ModifyTableProperty and setting the table property TABLE\_ENCRYPTION to True can encrypt individual tables in the data dictionary. |
| ENCRYPT\_NEW\_TABLE | This property determines whether a new table added or created in the in the data dictionary should be encrypted. This property is a Boolean value. It is set to False when the data dictionary is created. When this property is set to True, all tables added or created into the database will be automatically encrypted. Setting this property has no effect on existing tables in the database. If this property is set to False, new table added or created in the data dictionary will not be encrypted. When setting this property to True, the database property ENCRYPT\_TABLE\_PASSWORD must be set. |
| ENABLE\_INTERNET | This property enables/disables the Internet access for the data dictionary. If it is disabled, no users will be allowed to connect from the Internet. Expected values are True and False. For more information see [Advantage Internet Server](master_advantage_internet_server.md). |
| INTERNET\_SECURITY\_LEVEL | This is the security level for communications between the Advantage Database Server and the clients when they are communicating over the Internet. The values are 0, 1, 2. For more information, see [Internet Security Levels](master_internet_security_levels.md). |
| MAX\_FAILED\_ATTEMPTS | This is the maximum number of failed Internet login attempts a user can have. For more information on this setting, see [Maximum Failed Login Attempts](master_maximum_failed_login_attempts.md). |
| ENFORCE\_MAX\_FAILED\_LOGINS | This property enables/disables the enforcement of the max failed login attempts limit for all remote server connections.  If disabled, the MAX\_FAILED\_ATTEMPTS limit only applies to Advantage Internet Connections (AIS).  If enabled the MAX\_FAILED\_ATTEMPTS limit applies to remote and internet connections.  If enabled, ADS will disable the login of any user that exceeds the maximum failed attempts.  To re-enable the login of that user, a database admin should use [sp\_ModifyUserProperty](master_sp_modifyuserproperty.md) or [AdsDDSetUserProperty](ace_adsddsetuserproperty.md) to disable their LOGINS\_DISABLED property.  Expected values are 'True' and 'False'. |
| LOGINS\_DISABLED | This property disables/enables database logins. Expected values are True and False. See [Disabling Database Logins](master_disabling_database_logins.md) for more details. |
| LOGINS\_DISABLED\_MSG | This is the custom error string that will be returned to clients attempting database connections when database logins are disabled. See LOGINS\_DISABLED above and [Disabling Database Logins](master_disabling_database_logins.md) for more details. |
| FTS\_NOISE\_WORDS | Changes the default Full Text Search (FTS) noise words for the data dictionary. When new FTS indexes are created with the default noise words, these will be used as the defaults for the new index. |
| FTS\_DELIMITERS | Changes the default Full Text Search (FTS) delimiter characters for the data dictionary. When new FTS indexes are created with the default delimiters, these will be used as the defaults for the new index. |
| FTS\_DROP\_CHARS | Changes the default Full Text Search (FTS) drop characters for the data dictionary. When new FTS indexes are created with the default drop characters, these will be used as the defaults for the new index. |
| FTS\_CONDITIONAL\_CHARS | Changes the default Full Text Search (FTS) conditional drop characters for the data dictionary. When new FTS indexes are created with the default conditional drop characters, these will be used as the defaults for the new index. |
| ENCRYPT\_INDEXES | This property determines whether indexes on dictionary bound ADT tables should be encrypted. This property is a Boolean value. It is defaulted to False when the data dictionary is created. When this property is set to True, all encrypted tables must be re-indexed for the property to take effect. If this property is set to False, indexes on encrypted tables will remain encrypted until the table is re-indexed. When setting this property to True, the database property ENCRYPT\_TABLE\_PASSWORD must be set. |
| ENCRYPT\_COMMUNICATION | This property determines whether all communication between the Advantage Database Server and Advantage-enabled client applications is encrypted. This property is a Boolean value. It is defaulted to False when the data dictionary is created. |
| DISABLE\_DLL\_CACHING | This property disables/enables DLL caching. Expected values are True and False. See [DLL Caching](master_dll_caching.md) for more details. |
| QUERY\_VIA\_ROOT | This property specifies whether passthrough queries are allowed through the [root dictionary](master_root_dictionary.md). Valid values are a combination (bitmask) of ADS\_DD\_QVR\_OPT\_QUERY (0x01) and ADS\_DD\_QVR\_OPT\_PROCEDURE (0x02). The first value indicates that passthrough queries are allowed. The second value indicates that passthrough procedure calls are allowed. This property is checked by the Advantage Web Platform when queries and procedure calls are made "through" the root dictionary to another dictionary. If the value is not set, then the request is denied. This property was introduced primarily for use by the Web Administrator Utility. |

Example

After making a connection to the database, change the description of the database.

EXECUTE PROCEDURE sp\_ModifyDatabase(

COMMENT,

This is my data dictionary );

See Also

[system.dictionary](master_system_dictionary.md)
