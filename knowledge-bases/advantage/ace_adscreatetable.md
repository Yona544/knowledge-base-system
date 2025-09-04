AdsCreateTable




Advantage Database Server 12  

AdsCreateTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCreateTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCreateTable Advantage Client Engine ace\_Adscreatetable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCreateTable  Advantage Client Engine |  |  |  |  |

Creates a new table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCreateTable (ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED8 \*pucAlias,  UNSIGNED16 usTableType,  UNSIGNED16 usCharType,  UNSIGNED16 usLockType,  UNSIGNED16 usCheckRights,  UNSIGNED16 usMemoSize,  UNSIGNED8 \*pucFields,  ADSHANDLE \*phTable); |

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCreateTable71 (ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED8 \*pucDBObjName,  UNSIGNED16 usTableType,  UNSIGNED16 usCharType,  UNSIGNED16 usLockType,  UNSIGNED16 usCheckRights,  UNSIGNED16 usMemoSize,  UNSIGNED8 \*pucFields,  UNSIGNED32 ulOptions,  ADSHANDLE \*phTable); |

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCreateTable90 (ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED8 \*pucDBObjName,  UNSIGNED16 usTableType,  UNSIGNED16 usCharType,  UNSIGNED16 usLockType,  UNSIGNED16 usCheckRights,  UNSIGNED16 usMemoSize,  UNSIGNED8 \*pucFields,  UNSIGNED32 ulOptions,  UNSIGNED8 \*pucCollation,  ADSHANDLE \*phTable); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Optional connection handle used to open the table. If this is 0, then an appropriate connection will be chosen if available, otherwise a new connection will be opened. |
| pucName (I) | Name of the table to create. If this does not contain a path then the default path, ([AdsSetDefault](ace_adssetdefault.htm) ) or the first search path ([AdsSetSearchPath](ace_adssetsearchpath.htm)) will be used. If no path is given and there is no default or search path, then the current working directory of the application will be used. |
| pucAlias (I) | Alias of the table. If NULL, the alias will be the base name of the table. The Alias is limited to 10 bytes. |
| pucDBObjName (I) | The object name to store in the data dictionary if the table is to be added to a data dictionary. This parameter may be NULL. When this parameter is NULL or an empty string, the base name of the table will be stored in the data dictionary. When a table is part of a data dictionary, the object name of the table is used to reference the table. This parameter is useful in the rare case where a table must be created using the same physical table name as an existing table in the data dictionary. See the ulOptions parameter for additional information. |
| usTableType (I) | Type of table. Options are ADS\_ADT, ADS\_VFP, ADS\_NTX, and ADS\_CDX. |
| usCharType (I) | Type of character data in the table. Valid values include ADS\_ANSI, ADS\_OEM, or one of the [dynamic collations](master_collation_support.htm) such as GENERAL\_VFP\_CI\_AS\_1252. This indicates the type of character data to be stored in the table and the collation to use when sorting the data. For compatibility with DOS-based CA-Clipper applications, ADS\_OEM should be specified when opening DBF tables. |
| usLockType (I) | Type of locking to use. Options are ADS\_PROPRIETARY\_LOCKING, ADS\_COMPATIBLE\_LOCKING. If the application is to be used with non-Advantage applications, then ADS\_COMPATIBLE\_LOCKING should be used. If the table will be used only by Advantage applications, then ADS\_PROPRIETARY\_LOCKING should be used. See your Advantage server guide for more information about locking methods. When usTableType is ADS\_ADT, this parameter is ignored. |
| usCheckRights (I) | Indicates if the client is to use rights checking for the table creation. Options are ADS\_CHECKRIGHTS and ADS\_IGNORERIGHTS. Note that beginning with version 10.0, the client ignores this setting by default.  To re-enable this setting, use [AdsSetRightsChecking](ace_adssetrightschecking.htm). When creating a data dictionary-bound table, this parameter is ignored. For data dictionary tables, user access rights are defined in the database (see [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm) for more information).    If rights checking has been enabled with AdsSetRightsChecking and ADS\_CHECKRIGHTS is given, then the Advantage Client Engine will perform an existence check on the given path and will not send the open request to the server if the directory is not visible to the client workstation. If ADS\_IGNORERIGHTS is used, then the client will not perform the existence check. |
| usMemoSize (I) | Size of memo blocks in memo file if memo fields are used. The value of ADS\_DEFAULT (or zero) indicates the default value should be used, which is 256 if usTableType is ADS\_ADT, and 64 if usTableType is ADS\_CDX or ADS\_VFP. This parameter has no effect when using ADS\_NTX, which always uses 512. For ADS\_ADT, valid values are in the range 8-1024. For ADS\_CDX and ADS\_VFP, values are in the range 1-1024. If the value is in the range 1-32, then that value is multiplied by 512 to get the actual block size. |
| pucFields (I) | Field descriptions of the form: "fieldname,type,length,decimals; ". For example: "EMPID,Numeric,5,0;DEPT,Char,20" |
| ulOptions (I) | A bit field for defining the options for the created table. The options that do not conflict with each other can be ORed together. Allowed values are:  ADS\_DEFAULT: No options bit is set. When this value is used as the option and the connection is a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)), the newly created table may be either a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)) or a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)) depending on the capability of the connected user. If the connected user is ADSSYS, the newly create table is a database table. If the connected user is not the ADSSYS user, the newly created table is a free table.  ADS\_DICTIONARY\_BOUND\_TABLE: The newly created table should be part of the data dictionary. The connection handle must be a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)) and the user must have been granted the CREATE TABLE permission in the database. An AE\_PERMISSION\_DENIED error will be returned if the user does not have the permission to create a table in the database. This bit cannot be OR'ed with the ADS\_FREE\_TABLE or the ADS\_TEMP\_TABLE bits.  ADS\_FREE\_TABLE: The newly created table should not be part of the data dictionary. This bit cannot be OR'ed with the ADS\_DICTIONARY\_BOUND\_TABLE bit. This option is required for an ADSSYS user to create a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)).  ADS\_TEMP\_TABLE: The newly created table is a temporary table that is only available on the current connection. This bit cannot be OR'ed with the ADS\_DICTIONARY\_BOUND\_TABLE bit. See [Temporary Tables](master_temporary_tables.htm) for more information. When this option is used, the pucName will be the name of the temporary table and it will have no relation to the names of the physical files created by Advantage. Advantage will choose the appropriate location to store the physical files and will delete the files when the connection is closed. An alternative to using this option is to simply prefix the table name with a hash (#) character.  ADS\_CACHE\_READS: Enables read caching on the table. Ignored by dictionary bound tables. See [Table Data Caching](master_table_data_caching.htm) for details.    ADS\_CACHE\_WRITES: Enables read and write caching on the table. Ignored by dictionary bound tables. See [Table Data Caching](master_table_data_caching.htm) for details. |
| pucCollation (I) | An optional collation language used when creating the new, restructured table. The collation may be specified for ANSI/OEM characters, Unicode characters or both. Unicode collation name must be pre-pended with a single colon character. If both ANSI/OEM collation and Unicode collation are to be specified, the Unicode collation must be specified after the ANSI/OEM collation. For example: Duden\_DE\_ADS\_CS\_AS\_1252:de\_DE. This parameter is optional. If it is not specified, the collation specified by the usCharType will be used. For ADS\_CDX and ADS\_NTX tables, the ANSI/OEM collation must not be specified. See [dynamic collation support](master_collation_support.htm). |
| phTable (O) | Returns the handle of the new table if the create is successful. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_FIELDDEF | One of the field definitions for the table is invalid. |
| AE\_PERMISSION\_DENIED | The connected user does not have the permission to create a table in the database. See ADS\_DICTIONARY\_BOUND\_TABLE in the ulOptions parameter above. |

Remarks

AdsCreateTable provides the capability to create new tables in the database. The table is left open for usage after it has been created.

The connection handle is used to specify a connection, if necessary. This allows flexibility during transactions because transactions are per connection. Using a separate connection will allow a table to remain outside of a transaction if another connection to the same server is in a transaction. See Transaction Processing for more information.

If the table type is ADS\_ADT, then the associated index type is the ADI format, and memos are the ADM format. If the table type is ADS\_NTX, then the associated index type is the NTX format, and memos are the DBT format. If the table type is ADS\_CDX or ADS\_VFP, then IDX and CDX index types are used, and memos are the FPT format.

The pucFields parameter defines the structure of the table. The supported types are shown in the field type specifications linked below. The pucFields definition need only contain as much of the type name as is needed for uniqueness. For example, "name, ch, 25" is a valid definition for a character field.

The total record length must be no greater than 65535. Each record in a DBF table uses one byte for the deleted record indicator, so the longest any field can be is 65534. Each record in an ADT table has an additional 5 bytes, so the longest any field can be in an ADT is 65530. Also note that the record buffer is dynamically allocated when a table is opened or created.

For ADT tables, valid field names are 128 characters or less and can contain any character value except 0 (NULL), ";" (a semi-colon), or "," (a comma). For DBF tables, valid field names are 10 characters or less. Valid characters for field names are the letters a-z and A-Z, digits 0-9, and the underscore "\_" character.

For information on the data types supported, see the following:

[DBF Field Types and Specifications](master_dbf_field_types_and_specifications.htm)

[ADT Field Types and Specifications](master_adt_field_types_and_specifications.htm)

Note When creating an auto-increment field, the initial value can be optionally specified in the third parameter of the creation syntax. For example, "field name, AutoIncrement, 67" will cause the first record in the newly created table to have the value 67 in the auto-increment field.

 

Note usLockType is always set to compatible locking (ADS\_COMPATIBLE\_LOCKING) when used with Advantage Local Server (ADS\_LOCAL\_SERVER) with ADT and DBF tables. usLockType is always set to proprietary locking (ADS\_PROPRIETARY\_LOCKING) when used with the Advantage Database Server (ADS\_REMOTE\_SERVER) with ADT tables. usCheckRights is ignored when used with Advantage Local Server (ADS\_LOCAL\_SERVER) with ADT and DBF tables. It is effectively treated as rights checking on (ADS\_CHECKRIGHTS). If ADS\_OEM is specified for the usCharType when using ADT tables, it will be changed to ADS\_ANSI. ADT tables do not support OEM character sets.

Example

ulRetCode = AdsCreateTable90( 0, "D:\\data\\newtable.dbf", NULL, ADS\_VFP,

ADS\_OEM, ADS\_PROPRIETARY\_LOCKING, ADS\_IGNORERIGHTS, ADS\_DEFAULT,

"name,char,100;id,integer;",

ADS\_DEFAULT, "GERMAN\_VFP\_CI\_AS\_1252", &hTable );

See Also

[AdsOpenTable90](ace_adsopentable90.htm)

[AdsConnect](ace_adsconnect.htm)

[AdsCloseTable](ace_adsclosetable.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)

[sp\_GetCollations](master_sp_getcollations.htm)