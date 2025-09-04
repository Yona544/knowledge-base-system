ODBC Data Source Keys




Advantage Database Server 12  

ODBC Data Source Keys

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ODBC Data Source Keys  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - ODBC Data Source Keys Advantage ODBC Driver odbc\_Odbc\_data\_source\_keys Advantage ODBC Driver > Installation and Distribution > ODBC Data Source Keys / Dear Support Staff, |  |
| ODBC Data Source Keys  Advantage ODBC Driver |  |  |  |  |

The following ODBC registry is required for the driver to load.

|  |  |
| --- | --- |
| DataDirectory=data path | For [free connections](javascript:hhpopuplink.TextPopup(popid_709342792X,FontFace,-1,-1,-1,-1)), it should be a valid path name to where the data files are located (e.g., x:\data). This path is used to automatically select all tables in the specified directory. For [database connections](javascript:hhpopuplink.TextPopup(popid_727119539X,FontFace,-1,-1,-1,-1)), it should be a valid path name including the Advantage Data Dictionary file name (e.g., x:\database\mydictionary.add). |
| DefaultType=FoxPro | Advantage | Visual FoxPro | Sets the type of database files to use: A setting of FoxPro chooses the ADS\_CDX table type for FoxPro-compatible DBF/CDX/FPT files. Visual FoxPro chooses the ADS\_VFP table type, which is a superset of ADS\_CDX (NULL field support, additional types, etc.). Advantage chooses the ADS\_ADT table type for proprietary ADT/ADI/ADM files. This setting is ignored for [database connections](javascript:hhpopuplink.TextPopup(popid_727119539X,FontFace,-1,-1,-1,-1)). |
| ServerTypes=n | N is a sum of values indicating the types of Advantage Servers to which connections are attempted.  The values for the servers are ADS\_REMOTE\_SERVER = 2,  ADS\_LOCAL\_SERVER = 1, and ADS\_AIS\_SERVER = 4.  For example, to allow the Driver to use the remote or local server, but not the Advantage Internet Server, use:  ServerTypes=3 (1+2). |
| The following ODBC registry keys are optional: | |
| AdvantageLocking=ON | OFF | The default is ON to use the Advantage proprietary locking. |
| CharSet=OEM | ANSI | The default character collation setting is ANSI. If OEM is specified, Language must be indicated as well. |
| Language=OEM | ANSI | named collation | If this setting is provided, it overrides the CharSet setting. It can be used to specify one of the [dynamic collations](master_collation_support.htm) such as GENERAL\_VFP\_CI\_AS\_1252 for Visual FoxPro compatibility. These collations can be used with Advantage ADT tables and Visual FoxPro (VFP) tables. |
| Description=String | This value is not used. It is provided for easier administration. |
| Locking=RECORD | FILE | Indicates whether updates lock the entire file or the individual records that are updated. The default is RECORD. |
| MaxTableCloseCache=n | N is the number of tables to hold in cache when cursors are opened and closed. The default is 25. |
| MemoBlockSize=n | N is the size of the FoxPro or Advantage memo blocks in tables that are created by the ODBC driver. This value is always 512 for CA-Clipper-compatible tables (DBF/DBT). The default value is 64 for FoxPro-compatible DBF tables (DBF/FPT), and the default value is 8 for Advantage proprietary table (ADT/ADM). |
| Rows=TRUE | FALSE | If True, deleted rows are displayed. The default is False. |
| Compression=INTERNET | ALWAYS | NEVER | The default is empty (not set). This setting controls the option for [communications compression](master_communications_compression.htm). If INTERNET is specified, then all data communications for ADS\_AIS\_SERVER connections will be compressed unless compression is specifically turned off at the server. If ALWAYS is specified, then all data communications between the client and server will be compressed unless compression is specifically turned off at the server. If NEVER is specified, then compression will not be used for communications between the client and server. If this entry is not specified or is left empty, then the COMPRESSION setting in the ADS.INI file will be used if available. This entry is ignored for ADS\_LOCAL\_SERVER connections. |
| CommType=UDP\_IP | IPX | TCP\_IP | TLS | If this value is specified, it defines which protocol will be used for communicating with Advantage Database Server. Refer to [Advantage Communication Transport Layer](master_advantage_communication_transport_layer.htm) for information on choosing a protocol. If TLS is chosen, the ODBC client will use [Transport Layer Security](master_communications_encryption.htm) to communicate with the server. When using TLS, it is also necessary to provide the TLSCertificate and TLSCommonName keys. |
| TLSCertificate=path and name of public certificate | Specifies the path and file name of the the public certificate for [Transport Layer Security (TLS) communications](master_communications_encryption.htm). |
| TLSCommonName=domain name | Specifies the expected "common name" from the server when using [Transport Layer Security (TLS) communications](master_communications_encryption.htm). If this is not given or does not match the common name sent back from the server, the connection is terminated. |
| TLSCiphers=AES256-SHA | AES128-SHA | RC4-MD5 | Specifies the allowed combination of Transport Layer Security (TLS) cipher suites. Multiple entries can be delimited by colons. Valid values are AES128-SHA, AES256-SHA, and RC4-MD5. For example, to specify both AES ciphers, use a value of "AES128-SHA:AES256-SHA".  See [TLS\_CIPHERS](master_tls_ciphers.htm) and [Communication Encryption](master_communications_encryption.htm) for more information. |
| DDPassword=dictionary password | Specifies the AES password for the dictionary if using [strong encryption](master_encryption.htm). When connecting to Advantage Database Server, it is more secure to use the [SE\_PASSWORDS](master_se_passwords.htm) configuration option to specify this value. Note that if an application does provide this option, the server will validate the password each time a connection is made. This is a relatively expensive operation due to the large number of iterations the hash function is executed. |
| EncryptionType=AES256 | AES128 | RC4 | Specifies the encryption type to use when [encrypting tables](master_encryption.htm). A newly encrypted table will be encrypted with this encryption type. A newly created data dictionary on this connection will use the specified encryption. When opening an existing table or data dictionary that is encrypted, this connection string option is ignored and the appropriate encryption type is used. To change the encryption type associated with an existing dictionary refer to [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm). It is important to note that any table created when an AES encryption type is used (even if the table is not encrypted) will not be compatible with versions of Advantage prior to v10.1. |
| FIPS=TRUE | FALSE | Specifies whether or not the client should run in [FIPS](master_fips.htm) mode. This setting must be the same as the server to which the connection is made. All connections must use the same value in an application. It is not allowed to mix FIPS mode connections and non-FIPS mode connections. |
| TrimTrailingSpaces=TRUE | FALSE | The default is False. If TRUE is specified, trailing spaces in character fields will be removed prior to returning the values to the application. |
| SQLTimeout=n | N is the number of seconds any SQL statement will be allowed to execute before being cancelled. |
| The following additional entry is not set by the Advantage setup utility ([Data Source Setup Screen](odbc_data_source_setup_screen.htm)), but may be added as needed to data source definitions to produce the desired behavior. See the function SQLWritePrivateProfileString() in ODBC SDK for more information. | |
| RightsChecking=OFF | ON | Beginning with version 10.0, the client no longer performs rights checking by default. See [Check Rights](master_check_rights.htm) for more information. The default value for this setting is OFF. In order for the setting to have any affect, the application must call the Advantage Client Engine API [AdsSetRightsChecking](ace_adssetrightschecking.htm). This setting affects catalog operations such as the ability to retrieve column names from free tables.  It has no affect on data dictionary-bound tables or on SQL statements. If this setting is ON and rights checking is enabled, the client driver will perform a file existence check before requesting the server to open the table. If the client workstation does not have access to the table, the operation will fail. If this setting is OFF, the client will send the open request to the server without performing an existence check. |