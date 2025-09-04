---
title: Ace Adsddsetdatabaseproperty
slug: ace_adsddsetdatabaseproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddsetdatabaseproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e128d07f3eda5a64030ef5706fce4e1d1f205035
---

# Ace Adsddsetdatabaseproperty

AdsDDSetDatabaseProperty

AdsDDSetDatabaseProperty

Advantage Client Engine

| AdsDDSetDatabaseProperty  Advantage Client Engine |  |  |  |  |

Sets one database property in the data dictionary.

Syntax

UNSIGNED32 AdsDDSetDatabaseProperty( ADSHANDLE hAdminConn, UNSIGNED16 usPropertyID,

VOID \*pvProperty, UNSIGNED16 usPropertyLen );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| usPropertyID (I) | Index of a database property to set. See below for possible values. |
| pvProperty (I) | Pointer to the property to be stored in the data dictionary. |
| usPropertyLen (I) | Length of the property pointed to by the pvProperty parameter. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid database property index, or the specified property cannot be modified. |
| AE\_NO\_TABLE\_ENCRYPTION\_PASSWORD | This error is returned when setting the ADS\_DD\_ENCRYPT\_NEW\_TABLE property to True and the databases table encryption password property, ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD, has not been set. |

Remarks

AdsDDSetDatabaseProperty sets one database property in the data dictionary. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

ALTER DATABASE permission is required to modify any database property. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

| UsPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the database description. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_VERSION\_MAJOR | Sets the user defined major version property of the data dictionary. This property is intended for storing a value associated with the major version of the user's dictionary. The user version property is set, read, and interpreted by the application. The Advantage Database Server does not currently use it internally. This value can be used by the application developer to determine when the Advantage "database upgrade" functionality needs to be used. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The "database upgrade" functionality will be available for application developers to create and execute the code necessary to upgrade the files and/or definitions in the version "1.0" database to the version "1.1" database. The default value for this property, if it has never been set, is 0. If pvProperty is NULL, the user version property value will be removed. |
| ADS\_DD\_VERSION\_MINOR | Sets the user defined minor version property of the data dictionary. This property is intended for storing a value associated with the minor version of the user's dictionary. The user version property is set, read, and interpreted by the application. The Advantage Database Server does not currently use it internally. This value can be used by the application developer to determine when the Advantage "database upgrade" functionality needs to be used. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The "database upgrade" functionality will be available for application developers to create and execute the code necessary to upgrade the files and/or definitions in the version "1.0" database to the version "1.1" database. The default value for this property, if it has never been set, is 0. If pvProperty is NULL, the user version property value will be removed. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined database property. If pvProperty is NULL, the user defined database property will be removed. User defined property is set, read, and interpreted by the application. It is not used by the Advantage Database Server. Example use of a user defined database property will be to store the version of the database tables. |
| ADS\_DD\_DEFAULT\_TABLE\_PATH | Changes the default path for creating new tables. If pvProperty is NULL or an empty string, new tables will be created in the same directory as the data dictionary. No verification of the validity of the path is made. If the default table path is set to an invalid path, subsequent attempts to create new tables in this data dictionary will fail. |
| ADS\_DD\_TEMP\_TABLE\_PATH | Changes the path for creating temporary tables. If pvProperty is NULL or an empty string, a temporary table will be created in the same directory as the normal tables. Advantage Database Server and Advantage Local Server create temporary tables and indexes when executing SQL statements. |
| ADS\_DD\_ADMIN\_PASSWORD | Changes the ADSSYS password of the database. If pvProperty is NULL or an empty string, the data dictionary is re-set to not require a password for the ADSSYS user. |
| ADS\_DD\_LOG\_IN\_REQUIRED | Changes whether an anonymous user connection to the database is allowed. This property is a Boolean value. It is defaulted to False when the data dictionary is created. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. If the integer pointed to by the pvProperty is zero, the property is set to False. Otherwise the property is set to True. If this property is set to False, an anonymous connection to the database with no user name and no password is allowed. Otherwise a user name and password is required to make a database connection to the data dictionary. See [AdsConnect60](ace_adsconnect60.md) for more information. |
| ADS\_DD\_VERIFY\_ACCESS\_RIGHTS | This property determines whether the Advantage Database Server will enforce the users access rights when opening a database table or view or executing a stored procedure. This property is a Boolean value. It is defaulted to False when the data dictionary is created. pvProperty is expected to be a pointer to a 2 byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. If the integer pointed to by the pvProperty is zero, the property is set to False. Otherwise the property is set to True. If this property is set to False, the Advantage database server does not verify the users access rights when opening a database table or view or when executing a stored procedure. The implication is that all users have full rights to all objects in the database. If this property is set to True, the users access rights are verified. See [AdsDDGrantPermission](ace_adsddgrantpermission.md) and [AdsDDRevokePermission](ace_adsddrevokepermission.md) for more information on object access rights. Note that an anonymous user does not have any rights to objects in the database. If the database is set up to verify user access rights, an anonymous user can make a connection to the database but he cannot open any table or view or execute any stored procedure. See [AdsConnect60](ace_adsconnect60.md) and [AdsOpenTable](ace_adsopentable.md) for more information. |
| ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD | This property sets the encryption password for the database tables when using default encryption. This property is not used if the dictionary has [AES encryption](master_encryption.md) enabled. Setting this property does not encrypt any table in the data dictionary. It only sets the password that all database tables in the data dictionary will be encrypted with. The pvProperty should be a pointer to a NULL terminated string. The usPropertyLen should be the length of the password including the NULL terminator. If pvProperty is NULL or a pointer to an empty string, the function will remove the database encryption password from the data dictionary and, as a side effect, sets the database property ADS\_DD\_ENCRYPT\_NEW\_TABLE to False. Setting and removing this property requires that all database tables in the data dictionary not be encrypted. If there are encrypted table(s) in the data dictionary, this function will fail with error AE\_DD\_REQUEST\_NOT\_COMPLETED. Once this property is set, individual tables in the data dictionary can be encrypted by calling [AdsDDSetTableProperty](ace_adsddsettableproperty.md) and setting the table property ADS\_DD\_TABLE\_ENCRYPTION to True. |
| ADS\_DD\_ENCRYPT\_NEW\_TABLE | This property determines whether a new table added or created in the in the data dictionary should be encrypted. This property is a Boolean value. It is defaulted to False when the data dictionary is created. pvProperty is expected to be a pointer to a 2 byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. When this property is set to True, all tables added or created into the database will be automatically encrypted. Setting this property has no effect on existing tables in the database. If this property is set to False, new table added or created in the data dictionary will not be encrypted. When setting this property to True, the database property ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD must be set. |
| ADS\_DD\_ENABLE\_INTERNET | This property enables/disables the Internet access for the data dictionary. If it is disabled, no users will be allowed to connect from the Internet. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Expected values are True and False. For more information see [Advantage Internet Server](master_advantage_internet_server_overview.md). |
| ADS\_DD\_INTERNET\_SECURITY\_LEVEL | This is the security level for communications between the Advantage Database Server and the clients when they are communicating over the Internet. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. The values are ADS\_DD\_LEVEL\_0, ADS\_DD\_LEVEL\_1, ADS\_DD\_LEVEL\_2. For more information, see [Internet Security Levels](master_internet_security_levels.md). |
| ADS\_DD\_MAX\_FAILED\_ATTEMPTS | This is the maximum number of failed Internet login attempts a user can have. Once the user has reached this number, their Internet access will be shut off. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. For more information on this setting, see [Maximum Failed Login Attempts](master_maximum_failed_login_attempts.md). |
| ADS\_DD\_ENFORCE\_MAX\_FAILED\_LOGINS | This property enables/disables the enforcement of the max failed login attempts limit for all remote server connections.  If disabled, the ADS\_DD\_MAX\_FAILED\_ATTEMPTS limit only applies to Advantage Internet Connections (AIS).  If enabled the ADS\_DD\_MAX\_FAILED\_ATTEMPTS limit applies to remote and internet connections.  If enabled, ADS will disable the login of any user that exceeds the maximum failed attempts.  To enable the login of that user a database admin should use [sp\_ModifyUserProperty](master_sp_modifyuserproperty.md) or [AdsDDSetUserProperty](ace_adsddsetuserproperty.md) to disable their LOGINS\_DISABLED property.  pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Expected values are True and False. |
| ADS\_DD\_FTS\_DELIMITERS | Changes the default Full Text Search (FTS) delimiter characters for the data dictionary. When new FTS indexes are created with the default delimiters, these will be used as the defaults for the new index. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_FTS\_NOISE | Changes the default Full Text Search (FTS) noise words for the data dictionary. When new FTS indexes are created with the default noise words, these will be used as the defaults for the new index. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_FTS\_DROP\_CHARS | Changes the default Full Text Search (FTS) drop characters for the data dictionary. When new FTS indexes are created with the default drop characters, these will be used as the defaults for the new index. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_FTS\_CONDITIONAL\_CHARS | Changes the default Full Text Search (FTS) conditional drop characters for the data dictionary. When new FTS indexes are created with the default conditional drop characters, these will be used as the defaults for the new index. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_LOGINS\_DISABLED | Enables/disables logins to the database. Logins can be disabled in order to perform database maintenance in which you do not want new users connecting to the database. See [Disabling Database Logins](master_disabling_database_logins.md) for more details. Only an administrative user can set this property. |
| ADS\_DD\_LOGINS\_DISABLED\_ERRSTR | Used to specify a custom error string to return when database logins are attempted and the database is currently not accepting new connections (see ADS\_DD\_LOGINS\_DISABLED property above). Only an administrative user can set this property. |
| ADS\_DD\_DISABLE\_DLL\_CACHING | This property enables/disables the DLL caching functionality for the data dictionary. If it is disabled, DLL caching will not take place. By default it is enabled. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Expected values are True and False. For more information see [DLL Caching](master_dll_caching.md). |
| ADS\_DD\_ENCRYPT\_INDEXES | This property determines whether indexes on dictionary bound ADT tables should be encrypted. This property is a Boolean value. It is defaulted to False when the data dictionary is created. pvProperty is expected to be a pointer to a 2 byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. When this property is set to True, all encrypted tables must be re-indexed for the property to take effect. If this property is set to False, indexes on encrypted tables will remain encrypted until the table is re-indexed. When setting this property to True, the database property ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD must be set. |
| ADS\_DD\_ENCRYPT\_COMMUNICATION | This property determines whether all communication between the Advantage Database Server and Advantage-enabled client applications is encrypted. This property is a Boolean value. It is defaulted to False when the data dictionary is created. pvProperty is expected to be a pointer to a 2 byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Using this specifies that the [default encryption](master_communications_encryption.md) be used. To use Transport Layer Security (TLS) communications, specify a [CommType property](ace_adsconnect101.md) of TLS. |
| ADS\_DD\_QUERY\_VIA\_ROOT | This property specifies whether passthrough queries are allowed through the [root dictionary](master_root_dictionary.md). Valid values are a combination (bitmask) of ADS\_DD\_QVR\_OPT\_QUERY (0x01) and ADS\_DD\_QVR\_OPT\_PROCEDURE (0x02). The first value indicates that passthrough queries are allowed. The second value indicates that passthrough procedure calls are allowed. This property is checked by the Advantage Web Platform when queries and procedure calls are made "through" the root dictionary to another dictionary. If the value is not set, then the request is denied. This property was introduced primarily for use by the Web Administrator Utility. pvProperty is expected to be a pointer to a 4 byte (UNSIGNED32) integer. usPropertyLen is expected to be 4. |

Example

After making a connection to the database, change the description of the database. Then change the data dictionary to require a password for administrative access.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = (UNSIGNED16)strlen( aucMessage ) + 1;

AdsDDSetDatabaseProperty( hDD, ADS\_DD\_COMMENT, aucMessage, usBufferSize ) ;

AdsDDSetDatabaseProperty( hDD, ADS\_DD\_ADMIN\_PASSWORD,

"Secret", 7 /\* length of "Secret" plus 1 \*/ );

AdsDisconnect( hDD );

 

/\* This will fail because administrative password is required now. \*/

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

 

/\* This will succeed because correct password is given \*/

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", "Secret", ADS\_DEFAULT, &hDD );

See Also

[AdsDDCreate](ace_adsddcreate.md)

[AdsConnect60](ace_adsconnect60.md)

[AdsDDGetDatabaseProperty](ace_adsddgetdatabaseproperty.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsDDCreateUser](ace_adsddcreateuser.md)

[AdsDDDeleteUser](ace_adsdddeleteuser.md)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[sp\_ModifyDatabase](master_sp_modifydatabase.md)
