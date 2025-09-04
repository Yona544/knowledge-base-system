Encryption




Advantage Database Server 12  

Encryption

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Encryption  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Encryption Advantage Concepts master\_Encryption Advantage Concepts > Advantage Functionality > Encryption / Dear Support Staff, |  |
| Encryption  Advantage Concepts |  |  |  |  |

Advantage provides the capability to encrypt tables and associated data. Data encryption is just one part of the process of creating a secure system. The following are some of the steps that can be taken to secure a database:

|  |  |
| --- | --- |
| · | Restrict physical access: Prevent direct user access by keeping all data on a physically [remote server](master_client_server_technology.htm) and using Advantage Database Server to access the data. |

|  |  |
| --- | --- |
| · | Use access controls: Use a [data dictionary](master_advantage_data_dictionary.htm) with user logins to restrict who can connect to the database. |

|  |  |
| --- | --- |
| · | Permissions: Use [database roles](master_database_base_roles.htm) and assign [user and group permissions](master_advantage_data_dictionary_user_permissions.htm) to fine-tune levels of access that users can have. |

|  |  |
| --- | --- |
| · | Require logins: [Disable free connections](master_disable_free_connections.htm) on the Advantage Database Server to force all connections to authenticate through a data dictionary. |

|  |  |
| --- | --- |
| · | Encrypt communications: Enable the [encryption of communications](master_communications_encryption.htm) between the client and server application with Transport Layer Security (TLS) available beginning in v10.1 or with the existing encryption available with both UDP and TCP/IP communications. |

|  |  |
| --- | --- |
| · | If requirements call for it, enable [FIPS mode](master_fips.htm) to ensure that only encryption algorithms approved for the Federal Information Processing Standard (FIPS) 140-2 are used. |

|  |  |
| --- | --- |
| · | Encrypt data: Enable table encryption at the data dictionary level or in individual free tables. |

The current topic discusses data encryption. It can be used with both free tables and data dictionary tables and with Advantage Local Server and Advantage Database Server. The general scheme is the same for all cases: Advantage uses a password to seed an encryption stream that is used to encrypt the data (plain text) into "unreadable" cipher text using a symmetric encryption algorithm.

Default Encryption

Beginning with v6.0, Advantage has supported data encryption via an industry standard encryption algorithm. A table encryption password is used to initialize the state of the encryption function. The state of the encryption key is updated based on record and page number. This encryption is lightweight and fast and provides a moderate level of security.

Strong Encryption

With the introduction of v10.1, Advantage supports a stronger level of data encryption through improved techniques and through the use of algorithms in libraries from the OpenSSL Project. The new encryption can be used in a manner compliant with the Federal Information Processing Standard (FIPS) 140-2. It is available as an add-on. For information on obtaining the add-on, contact your Advantage sales representative or visit [www.AdvantageDatabase.com.](http://www.AdvantageDatabase.com.%20)

The [strong encryption usage overview](master_se_usage_overview.htm) outlines what an application can do to take advantage of AES encryption.

The new encryption available in v10.1 includes the 128-bit and 256-bit Advanced Encryption Standard algorithms sometimes referred to as AES-128 and AES-256. Some of the improvements include the following:

|  |  |
| --- | --- |
| · | Advantage hashes the encryption password with randomly generated salt values to produce the key data that feeds the encryption algorithms. This password "strengthening" provides, for example, a 256-bit key for AES256 usage regardless of the original password length. |

|  |  |
| --- | --- |
| · | Each individual encrypted item (record, memo, index page, etc.) uses a newly generated 64-bit value to be used as part of the initialization vector for the encryption stream. |

|  |  |
| --- | --- |
| · | If data dictionary files (.add, .am, .ai) are encrypted, a user-provided password is used. The password can be provided as an Advantage configuration parameter, a startup option (via the command line) or through a connection option, which can be useful with Advantage Local Server. |

The use of AES encryption is limited to the ADT and VFP table types due to the necessity of storing additional encryption information in the physical table. The CDX and NTX table types do not have the capability of storing the addition information.

General Notes

Passwords in Advantage can be up to 20 bytes in length. Passwords longer than 20 characters are truncated internally to 20 characters.

It is possible to use encryption with both free tables and with [data dictionary](master_advantage_data_dictionary.htm) bound tables. When using encryption with free tables, your application must provide the password for each table. For example, use the [TAdsTable.AdsEnableEncryption](ade_adsenableencryption.htm) method in a Delphi application, or in a .NET application, it would be specified via the EncryptionPassword [connection string](dotnet_adsconnection_connectionstring.htm) property. When using a data dictionary, the process is simpler. Advantage handles the enabling of encryption on selected tables automatically behind the scenes and access to the data is controlled through the user credentials.

When using the default encryption algorithm, the password that is used for encrypting data dictionary bound tables is stored (in encrypted form) in the dictionary itself. Advantage is able to decrypt that password when a user logs in successfully. With the AES encryption available in v10.1, the dictionary files (.add, .am, and .ai) as well as tables are encrypted using a data dictionary password that can be provided at server startup time or through a [connection string](ace_adsconnect101.htm) option.

Historical note: When using encryption with free tables, you should call the appropriate method to encrypt the table after enabling encryption for the first time by calling the appropriate method such as the ACE API AdsEncryptTable or the Delphi TAdsTable.AdsEncryptTable method. Alternatively, it can be performed in one step by calling the system procedure [sp\_EncryptTable](master_sp_encrypttable.htm). If you simply enable encryption on a free table that has existing data and never call the method to encrypt the table, only records that are updated after the encryption is enabled will be encrypted. Existing records in the table will be encrypted if (and only if) they are updated at some point in the future.

The type of encryption used for newly encrypted tables depends on the encryption type specified at the connection level. In order to use one of the AES encryption algorithms for data encryption, you must specify the encryption type at the connection level. For example, include "EncryptionType=AES256;" in the connection string ([AdsConnect101](ace_adsconnect101.htm)). When a table is encrypted via sp\_EncryptTable(), it will use the connection's current encryption type.

It is important to note that any table created when an AES encryption type is active (even if the table is not encrypted) will have updated version information and will not be compatible versions of Advantage prior to v10.1. Every record and memo/BLOB value will maintain an extra 8 bytes for AES encryption. It is possible to change the encryption type to the older version via [sp\_DecryptTable](master_sp_decrypttable.htm) and [sp\_EncryptTable](master_sp_encrypttable.htm).

Index encryption is supported on data dictionary-bound ADT tables. When using the default encryption, it is necessary to specifically enable index encryption as a data dictionary property. This can be done through Advantage Data Architect in the dictionary properties dialog or by setting the ENCRYPT\_INDEXES property via the [sp\_ModifyDatabase()](master_sp_modifydatabase.htm) procedure. After this property is set, it is necessary to reindex any existing encrypted tables in order for the associated indexes to be encrypted. When using AES encryption, ADT indexes (associated with dictionary-bound ADT tables) are always encrypted. The ENCRYPT\_INDEXES property is ignored with AES encryption.

Using AES encryption with free tables may add significant processing time to an application's processing each time it opens a table. The key generation for the AES encryption algorithm uses the PBKDF2 (Password-Based Key Derivation Function) with 10,000 iterations. Each time an application opens a free table and enables encryption on it, this cost is incurred. The server does not keep the password in memory, therefore it must verify it each time even if another user already has that same table open. This cost is also incurred each time the SQL engine opens a free table. It is much more efficient to use AES encryption with data dictionaries. The key derivation function is run only when a connection string provides the DDPassword or, alternatively, a single time at server startup when it is provided via the [SE\_Passwords](master_se_passwords.htm) configuration parameter.

Client versus Server Encryption

An important difference between the default encryption and newer AES encryption usage exists. Default table encryption in Advantage provided a dual purpose. The very first encryption implementation was for DOS based CA-Clipper applications connected to Advantage. There was no communications encryption available in that environment; the client handled the data encryption so that the table data, when passed over network, would be encrypted.

With the AES data encryption, all encryption is handled by the server. When using Advantage Local Server, this difference makes no real difference because the encryption is handled in the client process regardless of the encryption type (because Advantage Local Server runs in-process). With Advantage Database Server, however, this is a crucial difference:

|  |  |
| --- | --- |
| · | Because the server handles the encryption, the encryption key data need never exist in the client application when using data dictionaries. The only way any encryption key information would exist in the client application is if you choose to supply the data dictionary password as part of the connection string rather than as a server configuration parameter. Even in this scenario, the Advantage client does not keep the password in memory once it has transferred it to the server. With free tables, the application must provide the password and can then delete it from memory. The Advantage client does not keep the free table password in memory once it has transferred it to the server. |

|  |  |
| --- | --- |
| · | The table data will be passed over the network in the clear unless communications encryption is utilized. In general, though, this is a logical separation that provides for much cleaner solutions. |

System Procedures Available for Encryption

The following system stored procedures can be used for encrypting tables and specifying the encryption type to use with existing data dictionaries.

|  |  |
| --- | --- |
| · | [sp\_EncryptTable](master_sp_encrypttable.htm) |

|  |  |
| --- | --- |
| · | [sp\_DecryptTable](master_sp_decrypttable.htm) |

|  |  |
| --- | --- |
| · | [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm) |

|  |  |
| --- | --- |
| · | [sp\_GetTableEncryptionType](master_sp_gettableencryptiontype.htm) |

|  |  |
| --- | --- |
| · | [sp\_GetSecurityInfo](master_sp_getsecurityinfo.htm) |

Encryption Functions Available with the Advantage Client Engine API

The following is a list of the encryption functions available with the Advantage Client Engine API:

|  |  |
| --- | --- |
| · | [AdsDecryptTable](ace_adsdecrypttable.htm) |

|  |  |
| --- | --- |
| · | [AdsDisableEncryption](ace_adsdisableencryption.htm) |

|  |  |
| --- | --- |
| · | [AdsEnableEncryption](ace_adsenableencryption.htm) |

|  |  |
| --- | --- |
| · | [AdsEncryptTable](ace_adsencrypttable.htm) |

|  |  |
| --- | --- |
| · | [AdsIsEncryptionEnabled](ace_adsisencryptionenabled.htm) |

|  |  |
| --- | --- |
| · | [AdsIsTableEncrypted](ace_adsistableencrypted.htm) |

Encryption with the Advantage ODBC Driver

The ODBC driver does not provide a mechanism to specify free table passwords. Use a data dictionary in order to use encrypted tables with the ODBC driver.

Encryption with the Advantage OLE DB Provider

The OLE DB provider does not provide a mechanism to specify free table passwords for tables used in SQL statements. Use a data dictionary in order to use encrypted tables in SQL statements with the OLE DB Provider.

An application can provide a password for free tables that are opened directly (e.g., adCmdTableDirect):

|  |  |
| --- | --- |
| · | The [ADSPROP\_INIT\_ENCRYPTION\_PASSWORD](oledb_provider_specific_initialization_properties.htm) property in the topic Initialization Properties. |

|  |  |
| --- | --- |
| · | The [EncryptionPassword](oledb_connection_string_parameters_(advantage_ole_db_provider).htm) provider-specific Connection parameter in the topic Using the Advantage OLE DB Provider with ADO. |

Encryption with the Advantage CA-Visual Objects RDD

For additional information on encryption with free connections with the Advantage CA-Visual Objects RDD, see [AX\_SetPassword()](vo_ax_setpassword.htm) function found in the DBFAXS library. To access all of the encryption functionality with free connections with the Advantage CA-Visual Objects RDD, import the Advantage Client Engine library from the file ACE.AEF and use the Advantage Client Engine encryption APIs.

Encryption with the Advantage .NET Data Provider

To specify an encryption password for free tables with the .NET data provider, specify the password in the [connection string](dotnet_adsconnection_connectionstring.htm) using the EncryptionType property.

Encryption with the Advantage TDataSet Descendant

Refer to the topic [Encryption with the Advantage TDataSet Descendant](master_encryption_with_the_advantage_tdataset_descendant.htm) for information on using encryption in Delphi applications.