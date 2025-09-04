---
title: Ace Adsconnect101
slug: ace_adsconnect101
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsconnect101.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 2add959dea8c7270f935e709dc37ce1d0457c185
---

# Ace Adsconnect101

AdsConnect101

AdsConnect101

Advantage Client Engine

| AdsConnect101  Advantage Client Engine |  |  |  |  |

Connects to the given server or to a database in an Advantage Data Dictionary using a connection string.

Syntax

UNSIGNED32 AdsConnect101( UNSIGNED8 \*pucConnectString,

ADSHANDLE \*phConnectOptions,

ADSHANDLE \*phConnect );

Parameters

| pucConnectString (I) | Connection string.  Cannot be NULL or an empty string.  See below for supported options. |
| phConnectOptions (O) | The handle of an in-memory table that contains the provided connection string options.  Optional, can be NULL. |
| phConnect (O) | The handle of the connection is returned if it the connection is made successfully. |

Special Return Codes

| AE\_NO\_DRIVE\_CONNECTION | An Advantage server could not be located for the indicated path. |
| AE\_INVALID\_PASSWORD | Either the user is unknown in the database or an incorrect password is entered for the user. |
| 7077 | The Advantage Database Server cannot open the specified data dictionary. |
| 7078 | Authentication error. |
| 7085 | Invalid UNC server name. The server name used in the connection path could not be resolved. If using local server verify the name exists in the ads.ini file and that the application is using the correct ads.ini file. If using remote server you should not get this error. Contact your Advantage Technical Services representative. |

Remarks

AdsConnect101 connects to the Advantage Database Server on the given server. The pucConnectString parameter must contain at least the Data Source option which can be a full file path to an Advantage Data Dictionary file, a drive letter, or any valid path (standard name resolution will be performed). Only those server types that are specified by the ServerType option in the connection string will be considered when attempting to connect. If the ServerType option is not provided, this call obeys the default server types that may have been set by calling [AdsSetServerType](ace_adssetservertype.md). The function returns a connection handle if it succeeds. The connection handle can be used in subsequent calls to [AdsOpenTable101](ace_adsopentable101.md), [AdsCreateTable](ace_adscreatetable.md), and transaction processing functions.

If the Data Source option specifies a path to an Advantage Data Dictionary file, the returned connection handle is a database connection) handle. A database connection handle can be used in all functions where a connection handle is required. In addition, a database connection provides access to additional functionality provided by the Advantage Data Dictionary. Specifically, a database connection handle is required to open ADT tables that are part of the database defined in the data dictionary. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

If the Data Source option does not specify a path to an Advantage Data Dictionary file, the returned connection handle is a free connection) handle.

The User ID and Password options are optional. They are used by the Advantage Server to authenticate the user when attempting to obtain a database connection. If the User ID option is provided, the Data Source must specify a path to an Advantage Data Dictionary file. However, the user name and password are not required when making a database connection. The database specified by the Data Source option can be set up to allow anonymous user connections (see [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md) for information). In such a case, using no user name and no password is a valid combination to obtain a database connection. If the database specified by the Data Source is set up to require users to log in, a valid combination of user name and password must be supplied to obtain a database connection.

Connection string values may be delimited by single or double quotes, (for example, name='value' or name="value"). Either single or double quotes may be used within  the connection string by using the other delimiter, for example, name="value's" or name= 'value"s',but not name= 'value's' or name= ""value"". All blank characters, except those placed within a value or within quotes, are ignored. Keyword value pairs must be separated by a semicolon (;). If a semicolon is part of a value, it also must be delimited by quotes. No escape sequences are supported. Names are not case sensitive. If a given name occurs more than once in the connection string, the value associated with the last occurrence is used.

The following table lists the supported option and values for the ConnectString parameter.

| Name | Description |
| ApplicationID | Specifies the application ID to be sent to the server. If not provided, the default behavior is to use the application executable name. Using this property is an alternative to using [sp\_SetApplicationID](master_sp_setapplicationid.md). |
| CharType | Specifies the character type (collation) to use when opening tables and executing SQL statements. For table types CDX, VFP, and NTX, the CharType value can be ANSI or OEM in order to use the ANSI or OEM collation that is stamped in Advantage Databse Server or specified in the adslocal.cfg file. The OEM option is not used for ADT tables (ANSI will be used if OEM is specified for ADT tables). When using ADT and VFP table types, the value can also be the name of one of the [dynamically loaded collations](master_collation_support.md). |
| CheckFreeTableAccess | Valid values are TRUE and FALSE. This options specifies whether access to free table "ace") is allowed on a database connection). The default is FALSE which means that a user properly connected to the data dictionary may create, open, or delete free tables. Because Advantage currently have no mechanism for controlling access to free tables, this may present a security risk when the application allows execution of user supplied SQL statements. Setting this option to TRUE will cause Advantage to deny access to free table on database connection. |
| Collation | An optional collation language used when opening tables. The collation may be specified for ANSI/OEM characters, Unicode characters or both. Unicode collation name must be pre-pended with a single colon character. If both ANSI/OEM collation and Unicode collation are to be specified, the Unicode collation must be specified after the ANSI/OEM collation. For example: Duden\_DE\_ADS\_CS\_AS\_1252:de\_DE. This option is not required. If it is not specified, the collation specified by the CharType option will be used. For ADS\_CDX and ADS\_NTX tables, the ANSI/OEM collation must not be specified.  See [dynamic collation support](master_collation_support.md). |
| CommType | Specifies the communication protocol used to connect to the Advantage Database Server. Valid values are UDP\_IP, IPX, TCP\_IP, and TLS. If UDP\_IP is specified, the client will only use UDP/IP to communicate with the Advantage Database Server. If IPX is specified, the client will only use IPX to communicate with the Advantage Database Server. If TCP\_IP is specified, the client will only use TCP/IP to communicate with the Advantage Database Server. Specifying TLS causes [Transport Layer Security](master_communications_encryption.md) to be used. When TLS is used, the TLSCertificate and TLSCommonName options must also be provided. |
| Compression | Specifies the option for [communications compression](master_communications_compression.md) Valid values are INTERNET, ALWAYS, and NEVER. If INTERNET is specified, then all data communications for AIS connections will be compressed unless compression is specifically turned off at the server. If ALWAYS is specified, then all data communications between the client and server will be compressed unless compression is specifically turned off at the server. If NEVER is specified, then compression will not be used for communications between the client and server. If this option is not specified, then the COMPRESSION setting in the ADS.INI file will be used if available. This option is ignored for LOCAL connections. |
| Connect Timeout | Specifies the maximum amount of time in seconds to wait for a connection from the connection caching pool.  Valid values are any integer number 0 or greater.  By default this value is 15. |
| Connection Lifetime | Specifies the maximum amount of time in seconds a cached connection will be kept open.  A connection over it's life time will be freed the next time it is returned to the cache pool.  Valid values are any integer number 0 or greater.  By default this value is 0 and will live indefinitely. |
| Data Source | The fully qualified path to the computer where the data files exist and the default location of the data files. This fully qualified path must contain a drive letter or use UNC. The Data Source must be specified before a successful connection to an Advantage server can occur. If a free connection is desired, the Data Source must specify a directory location. For a database connection, the path and data dictionary file must be specified  (e.g., Data Source=\\myserver\myvolume\mypat\mydd.add). |
| DateFormat | Specifies the date format for dates represented as character strings for the connection.  For example "DD/MM/YYYY" or "YYYY-MM-DD".  See [AdsSetDateFormat60](ace_adssetdateformat60.md) for more information. |
| DDPassword | Specifies the AES password for the dictionary if using [strong encryption](master_encryption.md). When connecting to Advantage Database Server, it is more secure to use the [SE\_PASSWORDS](master_se_passwords.md) configuration option to specify this value. Note that if an application does provide this option, the server will validate the password each time a connection is made. This is a relatively expensive operation due to the large number of iterations the hash function is executed. |
| Decimals | Specifies the resulting number of decimal places in a division, modulus, or exponentiation operation in an index or filter expression evaluated in the expression engine.  See [AdsSetDecimals](ace_adssetdecimals.md) for more information. |
| Description | Specifies the description for a newly created data dictionary.  This option only applies to [AdsDDCreate101](ace_adsddcreate101.md) and is ignored by AdsConnect101. |
| EncryptDictionary | Valid values are TRUE and FALSE.  With [AdsDDCreate101](ace_adsddcreate101.md), a value of TRUE will cause the data dictionary data file to be encrypted.  This option is ignored by AdsConnect101. |
| EncryptionPassword | Specifies the encryption passwords to use with tables on free connections) that are opened with [AdsOpenTable101](ace_adsopentable101.md) or with SQL statements created on the connection.  If only one password is specified it will be used with all free tables.  For example, EncryptionPassword=password;  If different passwords are needed for different tables, a comma delimited list of tablename=password should be used.  For example, EncryptionPassword=table1=password1,table2=password2;  If a password contains special characters such as semicolons or spaces, it should be enclosed in either single or double quotes.  For example, EncryptionPassword=table1="pass;word",table2='pass"word';  For Database Connections) (see Data Source), the password(s) given here will only affect encrypted free tables that are not part of the data dictionary. |
| EncryptionType | Specifies the encryption type to use when [encrypting tables](master_encryption.md).  A newly encrypted table will be encrypted with this encryption type.  A newly created data dictionary on this connection will use the specified encryption. When opening an existing table or data dictionary that is encrypted, this connection string option is ignored and the appropriate encryption type is used. Valid values are AES128, AES256, and RC4 (the default encryption type). To change the encryption type associated with an existing dictionary refer to [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md). It is important to note that any table created when an AES encryption type is used (even if the table is not encrypted) will not be compatible with versions of Advantage prior to v10.1. |
| Epoch | Specifies the default epoch to determine how dates without century digits are interpreted.  See [AdsSetEpoch](ace_adssetepoch.md) for more information. |
| Exact | Specifies how string comparisons are performed with certain relational operators.  Valid values are TRUE and FALSE.  See [AdsSetExact22](ace_adssetexact22.md) for more information. |
| FIPS | Specifies whether or not the client should run in [FIPS mode](master_fips.md). This setting must be the same as the server to which the connection is made. All connections must use the same value in an application. It is not allowed to mix FIPS mode connections and non-FIPS mode connections. Valid values are 0, 1. |
| IncrementUserCount | Specifies whether to increment the user count on the Advantage Database Server for each new connection to the Advantage Database Server. Valid values are TRUE and FALSE. With a value of FALSE, if the same PC connects to the Advantage Database Server more than one time the connections are counted as a single user and only the connection count is incremented. With a value of TRUE, each connection counts as a new user on the Advantage Database Server. This option allows an Advantage middleware type of application to increment the Advantage Database Server user count for each remote client workstation indirectly accessing the Advantage Database Server. This provides an easy way for Advantage middleware applications to abide by the Advantage Database Server license agreement as related to remote client workstations taking up a "user" toward the maximum number of licensed users. |
| LockMode | Specifies the locking mode to use with the [AdsOpenTable101](ace_adsopentable101.md) API when opening DBF tables. Valid values include PROPRIETARY and COMPATIBLE. This setting is applicable to the CDX, VFP and NTX TableType options. If set to PROPRIETARY, Advantages high-performance internal locking mode is used. If set to COMPATIBLE, DBF tables can be shared in a writable mode with non-Advantage database applications. |
| Max Pool Size | Configures the maximum number of connections to cache.  Valid values are any integer number greater than 0.  The default number of cached connections is controlled by the MAX\_CONNECTIONS property in the [ADS.INI](master_ads_ini_file_support.md) file. |
| Password | Indicates the password to use in conjunction with the User ID when making a Database Connection) to an Advantage server.  If the password contains special characters like semicolons or spaces, use single or double quotes around it.  When specified in a call to [AdsDDCreate101](ace_adsddcreate101.md), this will become the ADSSYS administrative user password for the new data dictionary. |
| Pooling | Indicates if connection pooling should be used with this connection.  Valid values are TRUE or FALSE with FALSE being the default option. |
| ReadOnly | Specifies whether tables opened with [AdsOpenTable101](ace_adsopentable101.md) are opened read-only or read-write. Valid values are TRUE (to open tables read-only) or FALSE (to open tables read-write). |
| SecurityMode | Specifies the security mode to use when opening tables with [AdsOpenTable101](ace_adsopentable101.md). Valid values include CHECKRIGHTS and IGNORERIGHTS.  Note This option is ignored when obtaining a database connection. User Access Control security is implemented into the data dictionary. |
| ServerType | Specifies the Advantage server types to which connections should be attempted. Valid values include REMOTE, LOCAL, and INTERNET.  These values can be logically ORed together with the vertical bar character "|" in order to choose multiple server types. If multiple types are specified and multiple server types are available, the order of precedence is REMOTE first, AIS second, and LOCAL last.  The ServerType setting can also be specified as an integer value from 1 to 7. The value 1 represents LOCAL, 2 represents REMOTE, and 4 represents AIS. These can be summed together for the desired combination. For example, a ServerType value of 3 is equivalent to setting the server type to "LOCAL | REMOTE". |
| Shared | Specifies whether tables opened with [AdsOpenTable101](ace_adsopentable101.md) are opened shared or exclusive. Valid values are TRUE or FALSE. |
| ShowDeleted | Specifies whether deleted records in DBF tables are visible. Valid values are TRUE or FALSE. This setting is applicable to the CDX, VFP and NTX TableType options. If set to TRUE, deleted records in the DBF table will be visible. |
| SQLTimeout | Specifies the timeout (in seconds) for any SQL statements created on the connection.  The default is zero (no timeout).  See [AdsSetSQLTimeout](ace_adssetsqltimeout.md) for more information. |
| StoredProcedureConnection | Specifies if this connection lives within a stored procedure executed on the behalf of remote clients. Valid values are TRUE and FALSE. If this option is set to TRUE, the application will not increment the server user count for the stored procedure. If it is FALSE, then the stored procedure will increment the server user count, which will prevent other users from connecting when the user count reaches the maximum. Connections to Advantage Local Server are not affected by this option. |
| TableType | Specifies the desired table type when opening tables with [AdsOpenTable101](ace_adsopentable101.md) and free connections). Valid values are ADT, VFP, CDX, and NTX.  For database connections), this option will cause [AdsOpenTable101](ace_adsopentable101.md) to attempt to open tables as free tables) of the specified type.  To open data dictionary bound tables) leave this option out or specify "default". |
| TLSCertificate | Specifies the path and file name of the the public certificate for [Transport Layer Security (TLS) communications](master_communications_encryption.md). |
| TLSCiphers | Specifies the allowed combination of Transport Layer Security (TLS) cipher suites. Multiple entries can be delimited by commas or colons. Valid values are AES128-SHA, AES256-SHA, and RC4-MD5. For example, to specify both AES ciphers, use a value of "AES128-SHA:AES256-SHA".  See [TLS\_CIPHERS](master_tls_ciphers.md) and [Communication Encryption](master_communications_encryption.md) for more information. |
| TLSCommonName | Specifies the expected "common name" from the server when using Transport Layer Security (TLS) [communications](master_communications_encryption.md). If this is not given or does not match the common name sent back from the server, the connection is terminated. |
| TrimTrailingSpaces | Specifies whether trailing white space is removed from string fields when the data is retrieved. Valid values are TRUE or FALSE. If TRUE is specified, then fields of type String will have trailing white spaced trimmed on retrieval. If FALSE is specified, then trailing white space is maintained on the values when they are retrieved. This means that a fixed length String field with a width of 10, for example, will always return 10 characters when the value is retrieved; it is padded with as many spaces as necessary. |
| Unused Timeout | Specifies the number of seconds an unused cached connection will remain in the pool before being freed.  Valid values are integer numbers greater than 0. A value of zero indicates that it will stay in the pool indefinitely. |
| User ID | Indicates the user name to use when making a Database Connection to an Advantage server. Note that if this option is supplied, Advantage assumes that a Database Connection is being attempted. If a free connection) is desired, do not supply this option. |

Note that if none of the Compression options are specified, the COMPRESSION setting in the ADS.INI file will be used if available.

Connection paths to the Advantage Database Server can also include a port number if the Advantage Database Server configuration specifies the port number. The form of the connection string can be either of the following (using forward or backward slashes):

//servername:port/path

//ip\_addr:port/path

In the first format (//servername:port), the client will attempt a DNS lookup for the host to find the IP address and then will use the given port to attempt communication with the Advantage Database Server. In the second format, the client simply uses the given IP address and port to attempt to communicate with the Advantage Database Server. The following are syntactically correct connection paths using port numbers:

//theserver:31237/adsdata/testing

//theserver.mydomain.com:31237/adsdata/testing

//1.2.3.4:31237/adsdata/testing

Example

Making a data dictionary bound connection and opening the "Customer Information" table in the database.

AdsConnect101( "Data Source=n:\\MyData\\myData.ADD; ServerType=Remote;", NULL, &hConn );

AdsOpenTable101( hConn, "Customer Information", &hTable );

See Also

[AdsOpenTable101](ace_adsopentable101.md)

[AdsDisconnect](ace_adsdisconnect.md)

[AdsSetServerType](ace_adssetservertype.md)

[AdsDDCreate101](ace_adsddcreate101.md)

[AdsDDAddTable](ace_adsddaddtable.md)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md)

[AdsDDGetTableProperty](ace_adsddgettableproperty.md)

[AdsDDGetFieldProperty](ace_adsddgetfieldproperty.md)

[AdsIsConnectionAlive](ace_adsisconnectionalive.md)
