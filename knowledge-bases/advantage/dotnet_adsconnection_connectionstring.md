AdsConnection.ConnectionString




Advantage Database Server 12  

AdsConnection.ConnectionString

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.ConnectionString  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.ConnectionString Advantage .NET Data Provider dotnet\_Adsconnection\_connectionstring Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.ConnectionString / Dear Support Staff, |  |
| AdsConnection.ConnectionString  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the connection string that contains all of the property value pairs for connecting to an Advantage Database.

public string ConnectionString {get; set;}

Remarks

This property can be used to retrieve or set the connection string for an AdsConnection object. The connection string consists of property=value pairs delimited by semicolons. Before the connection can be opened, the connection string must be provided either through the [AdsConnection Constructor( string )](dotnet_adsconnection_constructor_string_.htm) constructor or by setting this property after constructing the object.

The "Data Source" property value must be supplied in the connection string in order for the connection to be successfully opened. The remaining properties have default values that will be used if they are not supplied in the connection string.

Values may be delimited by single or double quotes, (for example, name='value' or name="value"). Either single or double quotes may be used within a connection string by using the other delimiter, for example, name="value's" or name= 'value"s',but not name= 'value's' or name= ""value"". All blank characters, except those placed within a value or within quotes, are ignored. Keyword value pairs must be separated by a semicolon (;). If a semicolon is part of a value, it also must be delimited by quotes. No escape sequences are supported. Names are not case sensitive. If a given name occurs more than once in the connection string, the value associated with the last occurence is used.

The following table lists the valid names for values within the ConnectionString.

|  |  |  |
| --- | --- | --- |
| Name | Default | Description |
| CharType | ANSI | Specifies the character type (collation) to use when opening tables and executing SQL statements. For table types CDX, VFP, and NTX, the CharType value can be ANSI or OEM in order to use the ANSI or OEM collation that is stamped in Advantage Databse Server or specified in the adslocal.cfg file. The OEM option is not used for ADT tables (ANSI will be used if OEM is specified for ADT tables). When using ADT and VFP table types, the value can also be the name of one of the [dynamically loaded collations](master_collation_support.htm). |
| UnicodeCollation |  | Specifies the [Unicode collation](master_unicode_support.htm) to use for Unicode field data. |
| CommType |  | Specifies the communication protocol used to connect to the Advantage Database Server. Valid values are UDP\_IP, IPX, TCP\_IP, and TLS. If UDP\_IP is specified, the client will only use UDP/IP to communicate with the Advantage Database Server. If IPX is specified, the client will only use IPX to communicate with the Advantage Database Server. If TCP\_IP is specified, the client will only use TCP/IP to communicate with the Advantage Database Server. If TLS is chosen, the ODBC client will use [Transport Layer Security](master_communications_encryption.htm) to communicate with the server. When using TLS, it is also necessary to provide the TLSCertificate and TLSCommonName keys. |
| Compression |  | Specifies the option for [communications compression](master_communications_compression.htm) Valid values are INTERNET, ALWAYS, and NEVER. If INTERNET is specified, then all data communications for AIS connections will be compressed unless compression is specifically turned off at the server. If ALWAYS is specified, then all data communications between the client and server will be compressed unless compression is specifically turned off at the server. If NEVER is specified, then compression will not be used for communications between the client and server. If this property is not specified, then the COMPRESSION setting in the ADS.INI file will be used if available. This property is ignored for LOCAL connections. |
| Data Source |  | The fully qualified path to the computer where the data files exist and the default location of the data files. This fully qualified path must contain a drive letter or use UNC. The Data Source must be specified before a successful connection to an Advantage server can occur. If a [free connection](javascript:hhpopuplink.TextPopup(popid_272466414,FontFace,-1,-1,-1,-1)) is desired, the Data Source must specify a directory location. For a [database connection](javascript:hhpopuplink.TextPopup(popid_1862942045X,FontFace,-1,-1,-1,-1)), the path and data dictionary file can be specified in the Data Source property (e.g., Data Source=\\myserver\myvolume\mypat\mydd.add). Or the Data Source can contain just the path, and the Initial Catalog property can contain the data dictionary name (e.g., Data Source=\\myserver\myvolume\mypath; Initial Catalog=mydd.add). |
| DbfsUseNulls | FALSE | Specifies whether DBF tables are to return NULL for column data that is ordinarily considered as "empty" in Xbase terminology. Valid values are TRUE or FALSE. This setting is applicable to the CDX and NTX TableType options. If set to TRUE, "empty" column values in DBF tables will be returned as NULL. If set to FALSE, most "empty" column values in DBF (CDX/NTX) tables will be returned as actual valid data. The exception to this is the date field type. The .NET framework does not allow a DateTime value to contain a "zero" date. Therefore, empty DBF date fields will be returned as DBNull.Value. This property does not apply to Visual FoxPro (VFP) tables, which have true NULL support. |
| EncryptionPassword |  | Specifies the encryption password to use with all tables on [free connections](javascript:hhpopuplink.TextPopup(popid_272466414,FontFace,-1,-1,-1,-1)) that are opened directly (CommandType.TableDirect). The encryption password can be from 1 to 20 characters. If the password contains special characters such as semicolons or spaces, it should be enclosed in either single or double quotes.  For [Database Connections](javascript:hhpopuplink.TextPopup(popid_1862942045X,FontFace,-1,-1,-1,-1)) (see Data Source), this property is not used. Database Connections should use the User ID and Password properties.  Note This parameter only affects direct table opens (CommandType.TableDirect). To use encrypted tables with SQL, use a Database Connection. |
| Enlist | TRUE | Specifies whether the connection will be enlisted in the thread's current transaction context. See [Transaction Support in the Advantage .NET Data Provider](dotnet_transaction_support_in_the_advantage_net_data_provider.htm) for more information. This property is only applicable if you are using the .NET Framework version 2.0 or later. |
| IncrementUserCount | FALSE | Specifies whether to increment the user count on the Advantage Database Server for each new connection to the Advantage Database Server. Valid values are TRUE and FALSE. With a value of FALSE, if the same PC connects to the Advantage Database Server more than one time the connections are counted as a single user and only the connection count is incremented. With a value of TRUE, each connection counts as a new user on the Advantage Database Server. This property allows an Advantage middleware type of application to increment the Advantage Database Server user count for each remote client workstation indirectly accessing the Advantage Database Server. This provides an easy way for Advantage middleware applications to abide by the Advantage Database Server license agreement as related to remote client workstations taking up a "user" toward the maximum number of licensed users. |
| Initial Catalog |  | The name of the data dictionary to use when creating a [database connection](javascript:hhpopuplink.TextPopup(popid_1862942045X,FontFace,-1,-1,-1,-1)) to an Advantage server. It is not necessary to specify the initial catalog. The full path to the Advantage Data Dictionary can also be specified in the Data Source property if desired. |
| LockMode | PROPRIETARY | Specifies the locking mode to use with DBF tables. Valid values include PROPRIETARY and COMPATIBLE. This setting is applicable to the CDX and NTX TableType options. If set to PROPRIETARY, Advantages high-performance internal locking mode is used. If set to COMPATIBLE, DBF tables can be shared in a writable mode with non-Advantage database applications. |
| Password |  | Indicates the password to use in conjunction with the User ID when making a [Database Connection](javascript:hhpopuplink.TextPopup(popid_1862942045X,FontFace,-1,-1,-1,-1)) to an Advantage server. |
| ReadOnly | FALSE | Specifies whether tables are opened read-only or read-write. Valid values are TRUE (to open tables read-only) or FALSE (to open tables read-write). |
| SecurityMode | CHECKRIGHTS | Specifies the security mode to use. Valid values include CHECKRIGHTS and IGNORERIGHTS.  Note This property is ignored when obtaining a database connection. User Access Control security is implemented into the data dictionary. |
| ServerType | REMOTE | AIS | Specifies the Advantage server types to which connections should be attempted. Valid values include REMOTE, LOCAL, and AIS.  These values can be logically ORed together with the vertical bar character "|" in order to choose multiple server types. If multiple types are specified and multiple server types are available, the order of precedence is REMOTE first, AIS second, and LOCAL last.  The ServerType setting can also be specified as an integer value from 1 to 7. The value 1 represents LOCAL, 2 represents REMOTE, and 4 represents AIS. These can be summed together for the desired combination. For example, a ServerType value of 3 is equivalent to setting the server type to "LOCAL | REMOTE". |
| Shared | TRUE | Specifies whether tables are opened shared or exclusive. Valid values are TRUE or FALSE. This option only applies type CommandType.TableDirect. |
| ShowDeleted | FALSE | Specifies whether deleted records in DBF tables are visible. Valid values are TRUE or FALSE. This setting is applicable to the CDX and NTX TableType options. If set to TRUE, deleted records in the DBF table will be visible. |
| StoredProcedureConnection | FALSE | Specifies if this connection lives within a stored procedure executed on the behalf of remote clients. Valid values are TRUE and FALSE. If this property is set to TRUE, the application will not increment the server user count for the stored procedure. If it is FALSE, then the stored procedure will increment the server user count, which will prevent other users from connecting when the user count reaches the maximum. Connections to Advantage Local Server are not affected by this property. |
| TableType | ADT | Specifies the desired table type. Valid values for opening tables on [free connections](javascript:hhpopuplink.TextPopup(popid_272466414,FontFace,-1,-1,-1,-1)) include ADT, VFP, and CDX. Valid values for creating tables include ADT, CDX, VFP, and NTX.  Note: When opening tables (directly or via SQL statements) on a [database connection](javascript:hhpopuplink.TextPopup(popid_1862942045X,FontFace,-1,-1,-1,-1)), this property is ignored, as the table type is stored in the data dictionary for [database tables](javascript:hhpopuplink.TextPopup(popid_182218373,FontFace,-1,-1,-1,-1)). When creating tables (on either a [database connection](javascript:hhpopuplink.TextPopup(popid_1862942045X,FontFace,-1,-1,-1,-1)) or a [free connection](javascript:hhpopuplink.TextPopup(popid_272466414,FontFace,-1,-1,-1,-1))), this property is obeyed to know which table type to create.  Note To get support for creating and opening NTX index files, create a database (defined in a data dictionary) and add the tables and the associated NTX index files to that database. Then use those tables on that [database connection](javascript:hhpopuplink.TextPopup(popid_1862942045X,FontFace,-1,-1,-1,-1)). The NTX index files will then get automatically opened when the corresponding DBF table is opened. You can use the Advantage Data Architect to create a database and data dictionary. |
| TrimTrailingSpaces | FALSE | Specifies whether trailing white space is removed from string fields when the data is retrieved. Valid values are TRUE or FALSE. If TRUE is specified, then fields of type String will have trailing white spaced trimmed on retrieval. If FALSE is specified, then trailing white space is maintained on the values when they are retrieved. This means that a fixed length String field with a width of 10, for example, will always return 10 characters when the value is retrieved; it is padded with as many spaces as necessary. |
| User ID |  | Indicates the user name to use when making a Database Connection to an Advantage server. Note that if this property is supplied, Advantage assumes that a Database Connection is being attempted. If a Free Connection is desired, do not supply this property. |
| TLSCertificate |  | Specifies the path and file name of the the public certificate for [Transport Layer Security (TLS) communications](master_communications_encryption.htm). |
| TLSCommonName |  | Specifies the expected "common name" from the server when using Transport Layer Security (TLS) communications. If this is not given or does not match the common name sent back from the server, the connection is terminated. |
| TLSCiphers |  | Specifies the allowed combination of Transport Layer Security (TLS) cipher suites. Multiple entries can be delimited by colons. Valid values are AES128-SHA, AES256-SHA, and RC4-MD5. For example, to specify both AES ciphers, use a value of "AES128-SHA:AES256-SHA".  See [TLS\_CIPHERS](master_tls_ciphers.htm) and [Communication Encryption](master_communications_encryption.htm) for more information. |
| DDPassword |  | Specifies the AES password for the dictionary if using [strong encryption](master_encryption.htm). When connecting to Advantage Database Server, it is more secure to use the [SE\_PASSWORDS](master_se_passwords.htm) configuration option to specify this value. Note that if an application does provide this option, the server will validate the password each time a connection is made. This is a relatively expensive operation due to the large number of iterations the hash function is executed. |
| EncryptionType | RC4 | Specifies the encryption type to use when [encrypting tables](master_encryption.htm). A newly encrypted table will be encrypted with this encryption type. A newly created data dictionary on this connection will use the specified encryption. When opening an existing table or data dictionary that is encrypted, this connection string option is ignored and the appropriate encryption type is used. To change the encryption type associated with an existing dictionary refer to [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm). It is important to note that any table created when an AES encryption type is used (even if the table is not encrypted) will not be compatible with versions of Advantage prior to v10.1. |
| FIPS | FALSE | Specifies whether or not the client should run in [FIPS](master_fips.htm) mode. This setting must be the same as the server to which the connection is made. All connections must use the same value in an application. It is not allowed to mix FIPS mode connections and non-FIPS mode connections. |
| ConnectionHandle |  | Provides the AdsConnection object with an already connected connection handle.  The value must be a valid connection handle in string form.  If the value is in a hexadecimal format it must be preceded with "0x" otherwise it must be an integer number.  This value is primarily for use with triggers or AEPs that are given a connection handle. |

The following table lists the valid names for connection pooling values within the ConnectionString. See [Advantage .NET Data Provider and Connection Pooling](dotnet_advantage_net_data_provider_and_connection_pooling.htm).

|  |  |  |
| --- | --- | --- |
| Name | Default | Description |
| Pooling | TRUE | Specifies whether or not [connection pooling](dotnet_advantage_net_data_provider_and_connection_pooling.htm) is used. Valid values are TRUE or FALSE. If the value is TRUE, new connections are taken from the appropriate pool. This can reduce the time and overhead of establishing subsequent connections when the same database is repeatedly accessed. |
| Min Pool Size | 0 | Specifies the minimum number of connections to keep in an individual connection pool. |
| Max Pool Size | 100 | Specifies the maximum number of connections allowed in an individual connection pool. |
| Connection Lifetime | 0 | Specifies the time (in seconds) in which a connection is allowed to be returned to the pool. At connection close, if the time has not been exceeded the connection will be returned to the pool for future use, otherwise if the time has been exceeded the connection will be closed and not returned to the pool.  A value of zero(0) will cause the connection to never time-out and always be returned to the pool for future use. The timeout period is measured from when the connection was originally created. The time is not reset when it is returned to the pool. |

Example

AdsConnection conn = new AdsConnection();

conn.ConnectionString = "data source=c:\\data\\demodictionary.add; " +

"user id = adsuser; password = 'my;pass' " +

"ServerType=REMOTE; TrimTrailingSpaces = true";

conn.Open();

See Also

[AdsConnection Constructor( string )](dotnet_adsconnection_constructor_string_.htm)