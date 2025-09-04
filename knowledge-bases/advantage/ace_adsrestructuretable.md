AdsRestructureTable




Advantage Database Server 12  

AdsRestructureTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRestructureTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRestructureTable Advantage Client Engine ace\_Adsrestructuretable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRestructureTable  Advantage Client Engine |  |  |  |  |

Adds, removes, or changes field definitions for a table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRestructureTable( ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED8 \*pucPassword,  UNSIGNED16 usTableType,  UNSIGNED16 usCharType,  UNSIGNED16 usLockType,  UNSIGNED16 usCheckRights,  UNSIGNED8 \*pucAddFields,  UNSIGNED8 \*pucDeleteFields,  UNSIGNED8 \*pucChangeFields ); |

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRestructureTable90( ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED8 \*pucPassword,  UNSIGNED16 usTableType,  UNSIGNED16 usCharType,  UNSIGNED16 usLockType,  UNSIGNED16 usCheckRights,  UNSIGNED8 \*pucAddFields,  UNSIGNED8 \*pucDeleteFields,  UNSIGNED8 \*pucChangeFields,  UNSIGNED8 \*pucCollation ); |

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRestructureTable120( ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED8 \*pucPassword,  UNSIGNED16 usTableType,  UNSIGNED16 usCharType,  UNSIGNED16 usLockType,  UNSIGNED16 usCheckRights,  UNSIGNED8 \*pucAddFields,  UNSIGNED8 \*pucDeleteFields,  UNSIGNED8 \*pucChangeFields,  UNSIGNED8 \*pucCollation,  UNSIGNED32 ulMemoBlockSize,  UNSIGNED32 ulOptions ); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | An optional connection handle used to open the table. If this is 0, then any available connection of the appropriate type will be used, or a new connection will be created if one is not available. To restructure a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)), this parameter must be a [free connection](javascript:hhpopuplink.TextPopup(popid_7577555X,FontFace,-1,-1,-1,-1)) handle or 0. To restructure a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)), this parameter must be a database connection handle to the Advantage Data Dictionary the table is bound to. For a data dictionary-bound table, the connected user must have the ALTER permission to restructure the table. |
| pucName (I) | Name of table to open. To open a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)), this parameter must specify the name of the table in the data dictionary. The Advantage Database Server will use the information from the data dictionary to resolve the file path of database table. To open a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)), this parameter may specify the file path of the table. If this parameter does not specify a path, then the default path (see [AdsSetDefault](ace_adssetdefault.htm) ) or the search path (see [AdsSetSearchPath](ace_adssetsearchpath.htm) ) will be used. If no path is given and there is no default or search path, then the current working directory of the application will be used. The Advantage Client Engine resolves all table path names to UNC (Universal Naming Convention). Therefore, it is slightly faster to pass UNC names (e.g., \\server\volume\data\file.dbf) to the Advantage Client Engine rather than relative paths or paths with drive letters. |
| pucPassword (I) | Encryption password if the table to be restructured is encrypted. If the table is an encrypted [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)) and the encryption password for the table is not supplied, the function will fail with error 5096 (AE\_ENCRYPTION\_NOT\_ENABLED). This parameter is ignored when restructuring a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). This parameter is also ignored when restructuring a free table that is not encrypted. |
| usTableType (I) | Type of table. Options are ADS\_DEFAULT, ADS\_ADT, ADS\_VFP, ADS\_NTX and ADS\_CDX. If the specified table type is ADS\_DEFAULT, the function will attempt to open a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). In such case, the hConnect parameter must be a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)) handle and the Advantage Server will use the information stored in the data dictionary to resolve the table type. If the specified table type is ADS\_ADT, ADS\_VFP, ADS\_NTX, or ADS\_CDX, the function will attempt to open a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)). |
| usCharType (I) | Type of character data in the table. Valid values include ADS\_ANSI, ADS\_OEM, or one of the [dynamic collations](master_collation_support.htm) such as GENERAL\_VFP\_CI\_AS\_1252. This indicates the type of character data to be stored in the table and the collation to use when sorting the data. For compatibility with DOS-based CA-Clipper applications, ADS\_OEM should be specified when opening DBF tables. When opening a database table, (i.e., the usTableType is ADS\_DEFAULT), this parameter is ignored. The Advantage server will use the information stored in the data dictionary to resolve the character data type. |
| usLockType (I) | Type of locking to use. Options are ADS\_PROPRIETARY\_LOCKING and ADS\_COMPATIBLE\_LOCKING. When opening a database table, (i.e., the usTableType is ADS\_DEFAULT) this parameter is ignored and ADS\_PROPRIETARY\_LOCKING is the default. If the application is to be used with non-Advantage applications, then ADS\_COMPATIBLE\_LOCKING should be used. If the table will be used only by Advantage applications, then ADS\_PROPRIETARY\_LOCKING should be used. See your Advantage server guide for more information about locking methods. When ADS\_COMPATIBLE\_LOCKING is chosen, Advantage uses the appropriate style based on the table type. When usTableType is ADS\_ADT, this parameter is ignored and ADS\_PROPRIETARY\_LOCKING is always used. |
| usCheckRights (I) | Indicates if the client is to use rights checking for the table creation. Options are ADS\_CHECKRIGHTS and ADS\_IGNORERIGHTS. Note that beginning with version 10.0, the client ignores this setting by default.  To re-enable this setting, use [AdsSetRightsChecking](ace_adssetrightschecking.htm). When creating a data dictionary-bound table, this parameter is ignored. For data dictionary tables, user access rights are defined in the database (see [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm) for more information).    If rights checking has been enabled with AdsSetRightsChecking and ADS\_CHECKRIGHTS is given, then the Advantage Client Engine will perform an existence check on the given path and will not send the open request to the server if the directory is not visible to the client workstation. If ADS\_IGNORERIGHTS is used, then the client will not perform the existence check. |
| pucAddFields (I) | Field descriptions of the form: "fieldname,type,length,decimals,(order);". For example: "EMPID,Numeric,5,0;DEPT,Char,20,(3)" |
| pucDeleteFields (I) | Field descriptions of the form: "fieldname;". For example: "EMPID;LASTNAME" |
| pucChangeFields (I) | Field descriptions of the form: "oldfieldname,newfieldname,type,length,decimals,(order);". For example: "EMPID,Employee ID,Numeric,5,0,(3);DEPT,Char,20" |
| pucCollation (l) | An optional collation language used when opening the table to be restructured. This option is only valid with ADS\_ADT and ADS\_VFP tables. For ADS\_CDX and ADS\_NTX tables this option must be NULL or empty. See [dynamic collation support](master_collation_support.htm). |
| ulMemoBlockSize (I) | New memo block size to use for the memo file. If the value 0 (ADS\_DEFAULT) is specified, the memo block size will be unchanged. |
| ulOptions (I) | Reserved for future use. Must be 0. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_RESTRUCTURE\_FAILED | The table restructure failed. Call [AdsGetLastError](ace_adsgetlasterror.htm) for details. |

Remarks

CAUTION AdsRestructureTable significantly modifies existing tables and may result in data loss. Prior to using this function, the table to be modified should be backed up. If the table is part of a data dictionary, then the entire database should be backed up. The original table file, memo file, and index files will be renamed by the Advantage Client Engine and left in the same directory. Multiple calls to this function will cause the previously renamed files to be overwritten.

AdsRestructureTable provides the capability to add, delete, or change field definitions within a table. The table may be a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)) or a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). If the table is associated with a database, then the current user must have ALTER permissions for the specified table.

This function will open the table exclusively, so the table may not be opened elsewhere. If the table is part of a database, then all tables interlinked with referential integrity rules will also be opened exclusively. AdsRestructureTable will fail if:

|  |  |
| --- | --- |
| · | A field to be deleted is used in any index. |

|  |  |
| --- | --- |
| · | A field to be deleted is used in the record level constraint. |

|  |  |
| --- | --- |
| · | A field change includes altering the width or type of the field that is part of any index used as a primary or foreign key in a referential integrity constraint. |

|  |  |
| --- | --- |
| · | Any indexes exist for the table that were built using the ADS\_CUSTOM value in the options parameter. |

|  |  |
| --- | --- |
| · | The table is part of a dictionary and the current user does not have ALTER permissions for the specified table. |

|  |  |
| --- | --- |
| · | The table cannot be opened exclusively. |

If any of these limitations exist, you may delete the offending indexes or constraint and try again.

The parameters named pucAddFields, pucDeleteFields, and pucChangeFields are comprised of semicolon delimited lists of fields to be manipulated. The pucAddFields is identical to the field definitions passed into AdsCreateTable with one optional, additional parameter. If desired, the field definition can be appended with a comma followed with an integer within parentheses (ex ,(3)). That integer will indicate the position of the field within the table.

For example, "lastname, char, 20, (2); employee id, autoinc, (3)" will add two fields into the second and third positions within sequence of fields in the table.

The pucDeleteFields parameter is simply a list of existing fields to be deleted. An example to delete two fields is "customer;date".

The last parameter, pucChangeFields, is the same as a field definition that is passed to AdsCreateTable except that it is preceded with the original field name. The second field name is the renamed field name. Regardless of what is being changed in the field (the name, size, or type). All values are required. An example that changes the field name "lastname" to the new name "last name" is: "lastname, last name, char, 20". If desired, the field definition can be appended with a comma followed with an integer within parentheses (ex ,(3)). That integer will indicate the position of the field within the table. For example, "Lastname, Lastname, char, 20, (5)" will move the field "Lastname" to the fifth position in the field list.

Note This function is illegal in a transaction.

For information on data types supported, see the following:

[ADT Field Types and Specifications](master_adt_field_types_and_specifications.htm)

[DBF Field Types and Specifications](master_dbf_field_types_and_specifications.htm)

Note When restructuring a table and changing an integer field to an auto increment (autoinc) field type, Advantage does not verify the uniqueness of the existing integer values. It preserves the existing values and sets the next auto increment value (for the next appended record) to be the maximum existing integer value plus one. You can test the uniqueness of integer field values prior to changing the structure of the table by building a unique index on the field.

Example

ulRetCode = AdsRestructureTable90( hDD, "demotable", NULL, ADS\_DEFAULT, ADS\_ANSI,

ADS\_PROPRIETARY\_LOCKING, ADS\_IGNORERIGHTS, "NewCharField,ch,30,(3);NewIntField,integer,(4);", "Date; Time", "doublefield,NewNameForDouble,double,10,2; Tax,Tax,double,10,2,(20) ", "GERMAN\_VFP\_CI\_AS\_1252" );

 

ulRetCode = AdsRestructureTable( hDD, "demotable", NULL,

ADS\_DEFAULT, ADS\_ANSI, ADS\_PROPRIETARY\_LOCKING,

ADS\_IGNORERIGHTS,

"NewCharField,ch,30,(3);NewIntField,integer,(4);",

"Date; Time",

"doublefield,NewNameForDouble,double,10,2; Tax,Tax,double,10,2,(20) " );