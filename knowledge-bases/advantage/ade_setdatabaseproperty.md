SetDatabaseProperty




Advantage Database Server 12  

TAdsDictionary.SetDatabaseProperty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.SetDatabaseProperty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.SetDatabaseProperty Advantage TDataSet Descendant ade\_Setdatabaseproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.SetDatabaseProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Sets one database property in the data dictionary.

Syntax

TAdsDictionary.SetProperty( usPropertyID : UNSIGNED16;

pvProperty : pointer;

usPropertyLen : UNSIGNED16 );

Parameters

|  |  |
| --- | --- |
| usPropertyID | Index of a database property to set. See below for possible values. |
| pvProperty | Pointer to the property to stored in the data dictionary. |
| usPropertyLen | The size of the data pointed to by pvProperty. |

Remarks

The properties can only be set when the TAdsDictionary is open by a user with ALTER DATABASE permissions. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

The following are the valid values of usPropertyID and the expected value in strProperty.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the database description. |
| ADS\_DD\_DEFAULT\_TABLE\_PATH | Changes the default path for creating new tables. If strProperty is NULL or empty string, new tables will be created in the same directory as the data dictionary. |
| ADS\_DD\_ ADMIN\_PASSWORD | Changes the administrative password of the database. The administrative password is required to open the data dictionary for administrative access. If strProperty is empty string, the data dictionary is re-set to not requiring administrative password to maintain the data dictionary. |
| ADS\_DD\_TEMP\_TABLE\_PATH | Changes the path for creating temporary tables. If pvProperty is NULL or an empty string, temporary table will be created in the same directory as the normal tables. Advantage Database Server and Advantage Local Server creates temporary tables and indexes when executing SQL statements. |
| ADS\_DD\_LOG\_IN\_REQUIRED | Changes whether an anonymous user connection to the database is allowed. This property is a Boolean value. It is defaulted to FALSE when the data dictionary is created. pvProperty is expected to be a pointer to a 2 byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. If the integer pointed to by the pvProperty is zero, the property is set to FALSE. Otherwise the property is set to TRUE. If this property is set to FALSE, anonymous connection to the database with no user name and no password is allowed. Otherwise a user name and password is required to make a database connection to the data dictionary. |
| ADS\_DD\_VERIFY\_ACCESS\_RIGHTS | This property determines whether the Advantage Database Server will enforce the users access rights when opening a database table or view or executing a stored procedure. This property is a Boolean value. It is defaulted to FALSE when the data dictionary is created. pvProperty is expected to be a pointer to a 2 byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. If the integer pointed to by the pvProperty is zero, the property is set to FALSE. Otherwise the property is set to TRUE. If this property is set to FALSE, the Advantage Database Server does not verify the users access rights when opening a database table or view or when executing a stored procedure. The implication is that all users have full rights to all objects in the database. If this property is set to TRUE, the users access rights are verified. See [SetObjectAccessRights](ade_setobjectaccessrights.htm) for more information on object access rights. Note: An anonymous user does not have any rights to objects in the database. If the database is set up to verify user access rights, an anonymous user can make a connection to the database but he cannot open any table or view or execute any stored procedure. |
| ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD | This property sets the encryption password for the database tables when using default encryption. This property is not used if the dictionary has [AES encryption](master_encryption.htm) enabled. Setting this property does not encrypt any table in the data dictionary. It only sets the password that all database tables in the data dictionary will be encrypted with. The pvProperty should be a pointer to a NULL terminated string. The usPropertyLen should be the length of the password including the NULL terminator. If pvProperty is NULL or a pointer to an empty string, the function will remove the database encryption password from the data dictionary and, as a side effect, sets the database property ADS\_DD\_ENCRYPT\_NEW\_TABLE to False. Setting and removing this property requires that all database tables in the data dictionary not be encrypted. If there are encrypted table(s) in the data dictionary, this function will fail with error AE\_DD\_REQUEST\_NOT\_COMPLETED. Once this property is set, individual tables in the data dictionary can be encrypted by calling AdsDDSetTableProperty and setting the table property ADS\_DD\_TABLE\_ENCRYPTION to True. |
| ADS\_DD\_ENCRYPT\_NEW\_TABLE | This property determines whether a new table added or created in the data dictionary should be encrypted. This property is a Boolean value. It is defaulted to False when the data dictionary is created. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. When this property is set to True, all tables added or created into the database will be automatically encrypted. Setting this property has no effect on existing tables in the database. If this property is set to False, a new table added or created in the data dictionary will not be encrypted. When setting this property to True, the database property ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD must be set. |
| ADS\_DD\_ENABLE\_INTERNET | This property enables/disables the Internet access for the data dictionary. If it is disabled, no users will be allowed to connect from the Internet. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Expected values are True and False. For more information see [Advantage Internet Server](master_advantage_internet_server.htm). |
| ADS\_DD\_INTERNET\_SECURITY\_LEVEL | This is the security level for communications between the Advantage Database Server and the clients when they are communicating over the Internet. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. The values are ADS\_DD\_LEVEL\_0, ADS\_DD\_LEVEL\_1, ADS\_DD\_LEVEL\_2. For more information on the different security levels, see [Internet Security Levels](master_internet_security_levels.htm). |
| ADS\_DD\_MAX\_FAILED\_ATTEMPTS | This is the maximum number of failed Internet login attempts a user can have. Once the user has reached this number, their Internet access will be shut off. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. For more information on this setting, see [Maximum Failed Login Attempts](master_maximum_failed_login_attempts.htm). |
| ADS\_DD\_VERSION\_MAJOR | Sets the user defined major version property of the data dictionary. This property is intended for storing a value associated with the major version of the user's dictionary. The user version property is set, read, and interpreted by the application. It is not currently used internally by the Advantage Database Server. This value can be used by the application developer to determine when the Advantage "database upgrade" functionality needs to be used. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The "database upgrade" functionality will be available for application developers to create and execute the code necessary to upgrade the files and/or definitions in the version "1.0" database to the version "1.1" database. The default value for this property, if it has never been set, is 0. If pvProperty is NULL, the user version property value will be removed. |
| ADS\_DD\_VERSION\_MINOR | Sets the user defined minor version property of the data dictionary. This property is intended for storing a value associated with the minor version of the user's dictionary. The user version property is set, read, and interpreted by the application. It is not currently used internally by the Advantage Database Server. This value can be used by the application developer to determine when the Advantage "database upgrade" functionality needs to be used. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The "database upgrade" functionality will be available for application developers to create and execute the code necessary to upgrade the files and/or definitions in the version "1.0" database to the version "1.1" database. The default value for this property, if it has never been set, is 0. If pvProperty is NULL, the user version property value will be removed. |
| ADS\_DD\_FTS\_DELIMITERS | Changes the default Full Text Search (FTS) delimiter characters for the data dictionary. When new FTS indexes are created with the default delimiters, these will be used as the defaults for the new index. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_FTS\_NOISE | Changes the default Full Text Search (FTS) noise words for the data dictionary. When new FTS indexes are created with the default noise words, these will be used as the defaults for the new index. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_FTS\_DROP\_CHARS | Changes the default Full Text Search (FTS) drop characters for the data dictionary. When new FTS indexes are created with the default drop characters, these will be used as the defaults for the new index. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_FTS\_CONDITIONAL\_CHARS | Changes the default Full Text Search (FTS) conditional drop characters for the data dictionary. When new FTS indexes are created with the default conditional drop characters, these will be used as the defaults for the new index. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_LOGINS\_DISABLED | This property enables/disables logins to the database. Logins can be disabled in order to perform database maintenance in which you do not want new users connecting to the database. See [Disabling Database Logins](master_disabling_database_logins.htm) for more details. Only an administrative user can set this property. |
| ADS\_DD\_LOGINS\_DISABLED\_ERRSTR | This property can be used to specify a custom error string to return when database logins are attempted and the database is currently not accepting new connections (see ADS\_DD\_LOGINS\_DISABLED property above). Only an administrative user can set this property. |
| ADS\_DD\_ENCRYPT\_INDEXES | This property determines whether indexes on dictionary bound ADT tables should be encrypted. This property is a Boolean value. It is defaulted to False when the data dictionary is created. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. When this property is set to True, all encrypted tables must be re-indexed for the property to take effect. If this property is set to False, indexes on encrypted tables will remain encrypted until the table is re-indexed. When setting this property to True, the database property ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD must be set. |
| ADS\_DD\_ENCRYPT\_COMMUNICATION | This property determines whether all communication between the Advantage Database Server and the Advantage-enabled client applications is encrypted. This property is a Boolean value. It is defaulted to False when the data dictionary is created. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. |

Example

This example creates a data dictionary then sets an administrative password.

procedure SetDatabaseProperty;

var

oAdsDictionary : TAdsDictionary;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_LOCAL];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\*

\* The CreateDictionary call leaves an ADSSYS connection open. We will set

\* the password with this connection.

\*}

 

oAdsDictionary.SetDatabaseProperty( ADS\_DD\_ADMIN\_PASSWORD,

pChar( 'foobar' ),

7 );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[GetDatabaseProperty](ade_getdatabaseproperty.htm)

[CreateDictionary](ade_createdictionary.htm)