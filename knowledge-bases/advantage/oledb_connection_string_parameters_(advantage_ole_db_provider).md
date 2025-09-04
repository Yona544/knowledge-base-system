Connection String Parameters (Advantage OLE DB Provider)




Advantage Database Server 12  

Connection String Parameters

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connection String Parameters  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Connection String Parameters Advantage OLE DB Provider (for ADO) oledb\_Connection\_string\_parameters\_(advantage\_ole\_db\_provider) Advantage OLE DB Provider (for ADO) > Using the Advantage OLE DB Provider with ADO > Connection String Parameters (Advantage OLE DB Provider) / Dear Support Staff, |  |
| Connection String Parameters  Advantage OLE DB Provider (for ADO) |  |  |  |  |

To connect to this provider, set the Provider argument of the ConnectionString property to either:

 

Advantage OLE DB Provider

or

Advantage.OLEDB.1

 

Reading the Provider property will return the string:

 

Advantage.OLEDB.1

Typical Connection String

A typical connection string for a [free connection](javascript:hhpopuplink.TextPopup(popid_1940894724X,FontFace,-1,-1,-1,-1)) for the Advantage OLE DB Provider may look something like:

 

"Provider=Advantage OLE DB Provider; Data Source=x:\data"

 

A typical connection string for a [database connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)) for the Advantage OLE DB Provider may look something like:

 

"Provider=Advantage OLE DB Provider; Data Source=x:\data\MyDatabase.add; User ID=EmersonB; Password=joshua;"

 

Consisting of these keywords:

|  |  |
| --- | --- |
| Keyword | Description |
| Provider | Specifies the Advantage OLE DB Provider. |
| Data Source | The fully qualified path to the computer where the data files exist and the default location of the data files. This fully qualified path must contain a drive letter or use UNC. The Data Source must be specified before a successful connection to an Advantage server can occur. If a [Free Connection](javascript:hhpopuplink.TextPopup(popid_1940894724X,FontFace,-1,-1,-1,-1)) is desired, the Data Source must specify a directory location. For a [Database Connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)), the path and data dictionary file can be specified in the Data Source property (e.g., Data Source=\\myserver\myvolume\mypat\mydd.add). Or the Data Source can contain just the path, and the Initial Catalog property can contain the data dictionary name (e.g., Data Source=\\myserver\myvolume\mypath; Initial Catalog=mydd.add). |
| Initial Catalog | The name of the data dictionary to use when creating a [Database Connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)) to an Advantage server. It is not necessary to specify the initial catalog. The full path to the Advantage Data Dictionary can also be specified in the Data Source property if desired. |
| User ID | Indicates the user name to use when making a [Database Connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)) to an Advantage server. Note that if this property is supplied, Advantage assumes that a Database Connection is being attempted. If a [Free Connection](javascript:hhpopuplink.TextPopup(popid_1940894724X,FontFace,-1,-1,-1,-1)) is desired, do not supply this property. |
| Password | Indicates the password to use in conjunction with the User ID when making a [Database Connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)) to an Advantage server. |

Provider-Specific Connection Parameters

The Advantage OLE DB Provider supports several provider-specific connection parameters in addition to those defined by ADO. As with all other connection parameters, they can be set via the Connection object's Properties collection or as part of the connection string. Note that all of the valid values listed below, such as ADS\_REMOTE\_SERVER and ADS\_LOCAL\_SERVER, must be specified as the literal values as written. These values are not constants that represent some integer value. Available provider-specific connection parameters are:

|  |  |
| --- | --- |
| Parameter | Description |
| TableType | Specifies the desired table type. Valid values include ADS\_ADT, ADS\_CDX, ADS\_VFP, and ADS\_NTX. The default is ADS\_ADT.  Note When opening tables (directly or via SQL statements) on a [database connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)), this property is ignored, as the table type is stored in the data dictionary for [database tables](javascript:hhpopuplink.TextPopup(popid_1429223343,FontFace,-1,-1,-1,-1)). When creating tables (on either a [database connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)) or a [free connection](javascript:hhpopuplink.TextPopup(popid_1940894724X,FontFace,-1,-1,-1,-1))), this property is obeyed to know which table type to create.  Note To get support for creating and opening DBF/DBT/NTX files directly or via SQL statements, create a database (defined in a data dictionary) and add the tables and the associated NTX index files to that database. Then use those tables on that [database connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)). The NTX index files will then get automatically opened when the corresponding DBF table is opened. You can use the Advantage Data Architect to create a database and data dictionary. It is possible to access tables with the ADS\_NTX table type on [free connections](javascript:hhpopuplink.TextPopup(popid_1940894724X,FontFace,-1,-1,-1,-1)), however Advantage will not open any of the associated index files. Thus, any updates made to tables opened with the ADS\_NTX table type on free connections would logically corrupt the NTX indexes. |
| ServerType | Specifies the Advantage server types to which connections should be attempted. Valid values include ADS\_REMOTE\_SERVER, ADS\_LOCAL\_SERVER, and ADS\_AIS\_SERVER. These values can be logically ORed together with the vertical bar character "|" in order to choose multiple server types. The default is ADS\_REMOTE\_SERVER. If multiple types are specified and multiple server types are available, the order of precedence is ADS\_REMOTE\_SERVER first, ADS\_AIS\_SERVER second, and ADS\_LOCAL\_SERVER last. |
| SecurityMode | Specifies the security mode to use. Valid values include ADS\_CHECKRIGHTS and ADS\_IGNORERIGHTS. The default is ADS\_CHECKRIGHTS. Note: this property is ignored when obtaining a [database connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)). User Access Control security is implemented into the data dictionary.  Beginning with version 10.0, the client no longer performs rights checking by default. See [Check Rights](master_check_rights.htm). |
| EncryptionPassword | Specifies the encryption password to use with all tables on [Free Connections](javascript:hhpopuplink.TextPopup(popid_1940894724X,FontFace,-1,-1,-1,-1)) that are opened directly (adCmdTableDirect). The encryption password will consist of the first twenty characters specified after the equals sign following the EncryptionPassword key word. If using less than a twenty-letter password, a semi-colon should be included directly after the password so the Advantage OLE DB Provider knows when the password ends. For [Database Connections](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)) (see Data Source), this property is not used. [Database Connections](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)) should use the User ID and Password properties. Note: This parameter only affects direct table opens (adCmdTableDirect). To use encrypted tables with SQL, use a Database Connection. |
| LockMode | Specifies the locking mode to use with DBF tables. Valid values include ADS\_PROPRIETARY\_LOCKING and ADS\_COMPATIBLE\_LOCKING. This setting is applicable to the ADS\_CDX, ADS\_VFP, and ADS\_NTX TableType options. If set to ADS\_PROPRIETARY\_LOCKING, Advantages high-performance internal locking mode is used. If set to ADS\_COMPATIBLE\_LOCKING, DBF tables can be shared in a writable mode with non-Advantage database applications. The default is ADS\_PROPRIETARY\_LOCKING. |
| ShowDeleted | Specifies whether deleted records in DBF tables are visible. Valid values are TRUE or FALSE. This setting is applicable to the ADS\_CDX, ADS\_VFP, and ADS\_NTX TableType options. If set to TRUE, deleted records in the DBF table will be visible. The default is FALSE. |
| DbfsUseNulls | Specifies whether DBF tables are to return NULL for column data that is ordinarily considered as "empty" in Xbase terminology. Valid values are TRUE or FALSE. This setting is applicable to the ADS\_CDX, ADS\_VFP, and ADS\_NTX TableType options. If set to TRUE, "empty" column values in DBF tables will be returned as NULL. If set to FALSE, "empty" column values in DBF tables will be returned as actual valid data. The default is FALSE. |
| CharType | Specifies whether the data in DBF tables is ANSI or OEM. Valid values include ADS\_ANSI and ADS\_OEM. This setting is applicable to the ADS\_CDX, ADS\_VFP, and ADS\_NTX TableType options. The default is ADS\_ANSI. When using ADS\_ADT and ADS\_VFP tables, the value can also be one of the [dynamically loaded collations](master_collation_support.htm). |
| TrimTrailingSpaces | Specifies whether trailing white space is removed from string fields when the data is retrieved. Valid values are TRUE or FALSE. If TRUE is specified, then fields of type DBTYPE\_STR will have trailing white spaced trimmed on retrieval. Note that the Advantage data types ADS\_STRING and ADS\_MEMO are both mapped to DBTYPE\_STR. If FALSE is specified, then trailing white space is maintained on the values when they are retrieved. This means that a fixed length field (ADS\_STRING) with a width of 10, for example, will always return 10 characters when the value is retrieved; it is padded with as many spaces as necessary. It may be desirable to specify TRUE to trim trailing blanks if, for example, an application is using the ADO Find method. If trailing blanks are not trimmed, then search values given to the Find method would have to be padded to the full field length in order for the search to succeed. The default is FALSE |
| FilterOptions | Specifies whether to respect the filtering applied to the rowset when determining record count and logical positioning information. Valid values are IGNORE\_WHEN\_COUNTING and RESPECT\_WHEN\_COUNTING. When using RESPECT\_WHEN\_COUNTING, the record count and scroll bar positioning will be accurate but with a potential speed tradeoff. In some cases, the provider may have to skip through all records in the rowset to determine the count and position. It is not recommended to use the RESPECT\_WHEN\_COUNTING option except on very small rowsets. When a rowset is to be opened and displayed in a data bound grid, the grid requests record count information from the provider to position the scroll bar. Because it can request this information several times for any movement in the grid, it is usually best if the IGNORE\_WHEN\_COUNTING option is used in order for the grid to be more responsive. If you use the ADO RecordSet property .RecordCount and need a completely accurate count, then use the RESPECT\_WHEN\_COUNTING option. All record count requests are sent to the same OLE DB interface, so it is not possible for it to know implicitly how accurate the count should be for a given call. The default is IGNORE\_WHEN\_COUNTING. |
| IncrementUsercount | Specifies whether to increment the user count on the Advantage Database Server for each new connection to the Advantage Database Server. Valid values are TRUE and FALSE. With a value of FALSE, if the same PC connects to the Advantage Database Server more than one time the connections are counted as a single user and only the connection count is incremented. With a value of TRUE, each connection counts as a new user on the Advantage Database Server. This property allows an Advantage middleware type of application to increment the Advantage Database Server user count for each remote client workstation indirectly accessing the Advantage Database Server. This provides an easy way for Advantage middleware applications to abide by the Advantage Database Server license agreement as related to remote client workstations taking up a "user" toward the maximum number of licensed users. The default is FALSE. |
| StoredProcedureConnection | Specifies if this connection lives within a stored procedure executed on the behalf of remote clients. Valid values are TRUE and FALSE. If this property is set to TRUE, the application will not increment the server user count for the stored procedure. If it is FALSE, then the stored procedure will increment the server user count, which will prevent other users from connecting when the user count reaches the maximum. The default is FALSE. Connections to Advantage Local Server are not affected by this property. |
| Compression | Specifies the option for [communications compression](master_communications_compression.htm) Valid values are INTERNET, ALWAYS, and NEVER. If INTERNET is specified, then all data communications for ADS\_AIS\_SERVER connections will be compressed unless compression is specifically turned off at the server. If ALWAYS is specified, then all data communications between the client and server will be compressed unless compression is specifically turned off at the server. If NEVER is specified, then compression will not be used for communications between the client and server. If this property is not specified, then the COMPRESSION setting in the ADS.INI file will be used if available. This property is ignored for ADS\_LOCAL\_SERVER connections. |
| CommType | Specifies the communication protocol used to connect to the Advantage Database Server. Valid values are UDP\_IP, IPX, TCP\_IP, and TLS. If UDP\_IP is specified, the client will only use UDP/IP to communicate with the Advantage Database Server. If IPX is specified, the client will only use IPX to communicate with the Advantage Database Server. If TCP\_IP is specified, the client will only use TCP/IP to communicate with the Advantage Database Server. If TLS is chosen, the ODBC client will use [Transport Layer Security](master_communications_encryption.htm) to communicate with the server. When using TLS, it is also necessary to provide the TLSCertificate and TLSCommonName keys. |
| TLSCertificate | Specifies the path and file name of the the public certificate for [Transport Layer Security (TLS) communications](master_communications_encryption.htm). |
| TLSCommonName | Specifies the expected "common name" from the server when using Transport Layer Security (TLS) communications. If this is not given or does not match the common name sent back from the server, the connection is terminated. |
| TLSCiphers | Specifies the allowed combination of Transport Layer Security (TLS) cipher suites. Multiple entries can be delimited by colons. Valid values are AES128-SHA, AES256-SHA, and RC4-MD5. For example, to specify both AES ciphers, use a value of "AES128-SHA:AES256-SHA".  See [TLS\_CIPHERS](master_tls_ciphers.htm) and [Communication Encryption](master_communications_encryption.htm) for more information. |
| DDPassword | Specifies the AES password for the dictionary if using [strong encryption](master_encryption.htm). When connecting to Advantage Database Server, it is more secure to use the [SE\_PASSWORDS](master_se_passwords.htm) configuration option to specify this value. Note that if an application does provide this option, the server will validate the password each time a connection is made. This is a relatively expensive operation due to the large number of iterations the hash function is executed. |
| EncryptionType | Specifies the encryption type to use when [encrypting tables](master_encryption.htm). A newly encrypted table will be encrypted with this encryption type. A newly created data dictionary on this connection will use the specified encryption. When opening an existing table or data dictionary that is encrypted, this connection string option is ignored and the appropriate encryption type is used. To change the encryption type associated with an existing dictionary refer to [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm). It is important to note that any table created when an AES encryption type is used (even if the table is not encrypted) will not be compatible with versions of Advantage prior to v10.1. |
| FIPS | Specifies whether or not the client should run in [FIPS](master_fips.htm) mode. This setting must be the same as the server to which the connection is made. All connections must use the same value in an application. It is not allowed to mix FIPS mode connections and non-FIPS mode connections. |

For example, to specify that the provider is to use Advantage Local Server and FoxPro-compatible tables for a [free connection](javascript:hhpopuplink.TextPopup(popid_1940894724X,FontFace,-1,-1,-1,-1)), you could use the ADO connection string specified below. Note the provider name can be specified by either its friendly name, Advantage OLE DB Provider, or by its official registry name, Advantage.OLEDB.1:

"Provider=Advantage OLE DB Provider; Data Source=z:\data\tables; ServerType=ADS\_LOCAL\_SERVER; TableType=ADS\_CDX;"