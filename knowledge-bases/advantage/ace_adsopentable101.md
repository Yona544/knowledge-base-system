AdsOpenTable101




Advantage Database Server 12  

AdsOpenTable101

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsOpenTable101  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsOpenTable101 Advantage Client Engine Ace\_Adsopentable101 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsOpenTable101  Advantage Client Engine |  |  |  |  |

Opens an existing table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsOpenTable101( ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  ADSHANDLE \*phTable); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle used to open the table, a valid connection handle must be provided. To open a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)), this parameter must be a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)) handle to the appropriated Advantage Data Dictionary file. |
| pucName (I) | Name of table to open. To open a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)), this parameter must specify the name of the table in the data dictionary. The Advantage Database Server will use the information from the data dictionary to resolve the file path of database table. To open a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)), this parameter may specify the file path of the table or just the table name. If this parameter does not specify a path, then the path  of the connection will be used. The Advantage Client Engine resolves all table path names to UNC (Universal Naming Convention). Therefore, it is slightly faster to pass UNC names (e.g., \\server\volume\data\file.dbf) to the Advantage Client Engine rather than relative paths or paths with drive letters. |
| phTable (O) | The handle to the table is returned if the table is opened successfully. |

Special Return Codes

|  |  |
| --- | --- |
| 7087 | Attempt to open a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)) failed because the database connection does not allow access to free table. |
| 7079, 7080 | The user does not have the proper rights to open the database table. |

Remarks

When opening a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)), if any path information including relative paths such as "..\file.dbf" is included, then the name will be used as given. If no path information is given with pucName, then the path of the connection will be used.

AdsOpenTable101 is used to open an existing table. The connection handle is used to specify which connection to open the table on. This allows flexibility during transactions because transactions are per connection. Using a separate connection will allow a table to remain outside of a transaction if another connection to the same server is in a transaction. See Transaction Processing for more information.

If the table type is ADS\_ADT, then the associated index type is the ADI format, and memos are the ADM format. If the table type is ADS\_NTX, then the associated index type is the NTX format, and memos are DBT format. If the table type is ADS\_CDX or ADS\_VFP, then IDX and CDX index types are used, and memos are the FPT format.

Note LockMode is always set to compatible locking (ADS\_COMPATIBLE\_LOCKING) when used with Advantage Local Server (ADS\_LOCAL\_SERVER) with ADT and DBF tables. LockMode is always set to proprietary locking (ADS\_PROPRIETARY\_LOCKING) when used with the Advantage Database Server (ADS\_REMOTE\_SERVER) with ADT tables. If ADS\_OEM is specified for CharType when using ADT tables, it will be changed to ADS\_ANSI. ADT tables do not support OEM character sets.

If the table to be opened is a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)), (i.e., TableType connection string option is not specified or is default) there may be additional features and limitations on the use of the returned table handle. Properties defined for the table in the data dictionary are automatically available for the database table. See [AdsDDSetTableProperty](ace_adsddsetdatabaseproperty.htm) and [AdsDDSetFieldProperty](ace_adsddsetfieldproperty.htm) for more information. Adding or removing an index with the table will modify the definitions stored in the database.

Example

ulRetCode = AdsConnect101( "Data Source=D:\\data; TableType=ADS\_VFP; CharType=OEM; LockMode=Compatible; Collation=GERMAN\_VFP\_CI\_AS\_125;", &hConnect );

ulRetCode = AdsOpenTable101( hConnect, "customers.dbf", &hTable );

See Also

[sp\_GetCollations](master_sp_getcollations.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsConnect101](ace_adsconnect101.htm)

[AdsCloseTable](ace_adsclosetable.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)

[AdsSetDefault](ace_adssetdefault.htm)

[AdsSetSearchPath](ace_adssetsearchpath.htm)

[AdsCacheOpenTables](ace_adscacheopentables.htm)

[AdsGetTableFilename](ace_adsgettablefilename.htm)

[AdsGetTableType](ace_adsgettabletype.htm)

[AdsGetTableCharType](ace_adsgettablechartype.htm)

[AdsGetTableLockType](ace_adsgettablelocktype.htm)

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm)

[AdsGetTableRights](ace_adsgettablerights.htm)

[AdsGetTableAlias](ace_adsgettablealias.htm)

[AdsSetServerType](ace_adssetservertype.htm)

[AdsDDCreate101](ace_adsddcreate101.htm)

[AdsDDAddTable](ace_adsddaddtable.htm)

[AdsDDSetTableProperty](ace_adsddsettableproperty.htm)

[AdsDDGetTableProperty](ace_adsddgettableproperty.htm)

[AdsDDSetFieldProperty](ace_adsddsetfieldproperty.htm)

[AdsDDGetFieldProperty](ace_adsddgetfieldproperty.htm)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm)