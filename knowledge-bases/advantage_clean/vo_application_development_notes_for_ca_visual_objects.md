---
title: Vo Application Development Notes For Ca Visual Objects
slug: vo_application_development_notes_for_ca_visual_objects
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_application_development_notes_for_ca_visual_objects.htm
source: Advantage CHM
tags:
  - vo
checksum: a47b10e741ee5b10f192709b017f160e7017ff40
---

# Vo Application Development Notes For Ca Visual Objects

Application Development Notes (for CA-Visual Objects)

Application Development Notes

Advantage Visual Objects and Vulcan.NET RDD

| Application Development Notes  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Wherever possible, the Advantage RDDs behave the same as the equivalent RDDs that ship with Visual Objects and Vulcan.NET. The following is a list of all known incompatibilities, unsupported functionality and general development notes:

Known Incompatibilities

- The indexes opened in a work area or data server must reside on the same server as the database file. They can be in different directories or volumes, but must be on the same server.

- SET PATH will not be obeyed with Advantage "ignore rights" security. If no path is specified with a file name to be created or opened, the SetDefault directory is used. If no default directory has been set, then the first path in the SetPath is used if specified. If neither was ever set, then the current working directory is assumed.

- DBSetFilter() and SetSelectiveRelation() require the second parameter which is the expression represented as a string. This string is passed to the Advantage server so that it can be processed on the file server instead of at the client.

- Index files must have the proper extension: ntx, cdx, or .adi.

- RecNo returns zero when the current work area is at EOF (end of file). The Advantage Client Engine (ACE) considers a table at EOF to have an unset record pointer and, therefore, returns zero as the current record number. This is only the case when the EOF flag is True.

- The default Vulcan.NET RDDs read BINARY fields as MEMO fields.  As a result, the data is converted from OEM to ANSI as necessary, as well as converted to Unicode strings.  The Advantage Vulcan.NET RDDs instead treat BINARY (as well as IMAGE) fields as binary data and no conversion is done.  The result of this is that binary data returned from the Vulcan.NET RDD is stored in a String object whereas with the Advantage RDD it is stored in a byte array object.

- Seek() can only accept a maximum of 256 characters in string keys.  If you must seek with larger keys, you can get the ACE table handle with AX\_GetAceTableHandle() and use the AdsSeek ACE API.

Unsupported Functionality

- The "Sort" command and "DBSort()" function are not supported by the Advantage RDD.

- OrderSkipUnique(), OrdSkipUnique(), RDDInfo( \_SET\_AUTOOPEN, .F. ), RDDInfo( \_SET\_AUTOORDER, 1 ), RDDInfo( \_SET\_AUTOSHARE ), and RDDInfo( \_SET\_MEMOEXT ) are not supported.

- The Visual Objects BLOBImport() and BLOBExport() functions are not directly supported. The equivalent Advantage functions, AX\_File2BLOB() and AX\_BLOB2File(), are supported. Visual Objects BLOBs are not compatible with Advantage BLOBs, however. Advantage implemented BLOB support before Visual Objects added BLOB support via the BLOBImport() and BLOBExport() functions. Visual Objects chose to not obey the existing Advantage BLOB storage format, and instead implemented their own format.

- The OrderInfo( DBOI\_KEYTYPE ) is not supported by the Advantage RDD.

- The RDDInfo( \_SET\_AUTOOPEN ) is not supported by the Advantage RDD. The Advantage RDD will automatically open the production index.

- Xbase style expressions cannot reference memo fields. Filtering on memo fields is only supported through the use of an SQL WHERE clause.

- Memo file information returned via the DBFileSpec object is not available with the Advantage RDDs.

- The DBFileSpec:Move() function does not move memo files associated with tables.

- Parent/child relations are not allowed on child work areas which do not have a controlling index.

- The cbEval code block passed to the DBServer:SetOrderCondition method will not be evaluated for every record the server processes. Instead, it will be evaluated about every two seconds while the index order is created. See [AX\_PercentIndexed()](vo_ax_percentindexed.md) for more information. Furthermore, the cbWhileCondition argument is not respected. If a while condition must be specified, call the AdsCreateIndex ACE API directly.

- The Advantage Vulcan.NET RDD does not support the APPEND FROM command or DBApp function.

- The DBFileSpec class will usually not work with ADS paths that use server-side aliases.  This is because DBFileSpec attempts to open the table directly which will fail if the path is invalid (which is normal for a path with a server-side alias).

Development Notes

- The DBServer Editor will fail with an error box stating "Failed to open data file" when selecting DBF files that are not on a server where the Advantage Database Server is not installed. The Advantage Local Server is turned off by default. To use it, see [Using the Advantage Local Server](vo_using_the_advantage_local_server.md).

- To use any Advantage advanced functions, the application must include the library DBFAXS in the Properties window.

- An "AXS Client Incompatible with AXS Server" error may occur when opening a database file. This is due to running a previous version of an Advantage server with the new version of Advantage RDD. Verify the Advantage server version is the same or newer than the Advantage RDD version.

- SetAnsi() and SetCollation() usage.

In order for the Advantage RDD to work properly, the SetAnsi value must be False. The Advantage RDD takes care of all conversion and always returns the data in the native Windows format-ANSI. If you incorrectly set SetAnsi() to True in your Advantage application, Visual Objects will incorrectly assume the data from the Advantage RDD is not ANSI and will also perform conversion, which will corrupt your data. The Advantage Visual Objects RDD will use the SetCollation() value to determine if ANSI conversion is necessary as explained below.

If the data is stored in the DBF as OEM data (to be shared with a Clipper application for example), it must also be collated using the Clipper collation sequence (which is ASCII for the English language). Therefore, add the line SetCollation( #Clipper ) to the beginning of the application (before any data files are opened). Since the data is stored as OEM characters, the data will be translated automatically by the RDD to ANSI for use with Visual Objects (because all Windows applications require data to be represented in the ANSI character set).

If the data is stored as ANSI characters, the RDD will need to collate the data using ANSI collation sequences. The data cannot be shared with DOS applications such as Clipper Therefore, add the line SetCollation( #Windows ) to your application before any data files are opened (this is the default). The RDD will read and write ANSI characters and no conversion will take place.

- If VO applications are going to share DBFs with Advantage applications using the .cdx driver, the non-Advantage applications must use the command RDDInfo( \_SET\_FOXLOCK, .T. ) so that VO uses the same locking scheme as FoxPro and Advantage.

- The SetSelectiveRelation method in the CAVO DBServer does not provide accurate relations. This problem has been fixed in Visual Objects version 2.0b-1. For earlier versions, the file, ADSDBSER.AEF, containing the AdsDBServer is provided to fix this problem. All data servers that will use the SetSelectiveRelation method must inherit from AdsDBServer instead of DBServer.

It is possible to make the AdsDBServer become the default parent class for future projects. To accomplish this, you will need to edit your system registry. Find the key ParentClass, located in HKEY\_CURRENT\_USER | Software | ComputerAssociates | Visual Objects 2.0 | DBServerEditor. Change the key value from "DBSERVER" to ADSDBSERVER". This change will cause all future DBServerEditor created classes to use the AdsDBServer as the parent by default.

- The Advantage [Expression Engine](master_advantage_expression_engine.md) supports a number of Expression Engine functions. Advantage does not support any other expressions or local variables other than those listed in this documentation. User Defined Functions (UDFs) are also not supported.

- Filters, by default, will be optimized. Advantage Optimized Filters (AOFs) are much faster than traditional record filters. The optimization can be turned off with the Visual Objects "Set Optimize" command, so that the older style traditional record filters will be used. See [Advantage Optimized Filters](master_advantage_optimized_filters.md) for more information.

- SET FILTER TO may not work with Advantage since the filter string is capitalized before it is sent to the Advantage RDD. For example, SET FILTER TO lastname = "Smith" will result in setting a filter on "SMITH" not "Smith". To use lower case filters use DBSetFilter() or use the DBServer object. For example, DBSetFilter({|| "lastname='Smith'"}, "lastname='Smith'" ) or dbs:setfilter({|| "lastname='Smith'"}, "lastname='Smith'" ).

- To receive a Visual Objects style array of record locks on a table use DBServer:RLockList. The DBServer:INFO( DBI\_GETLOCKARRAY ) method returns a C-type array of 4-byte integers, which is the same type that the Visual Objects RDDs return. For ease of use in accessing the array, it is recommended that the DBServer:RLockList access be used.

- The DBServer:SetFilter method has a maximum length for the string expression of about 250 characters. This is a limitation of VO, not the Advantage VO drivers. One alternative method is to use the AdsSetAOF or AdsSetFilter ACE APIs, which the maximum character expression length is 65,534 characters.

- A date format set via SetDateFormat() may not always be recognized by the Advantage RDD. In order to be certain the RDD uses the date format set by SetDateFormat(), the ACE API AdsSetDateFormat() should be called as well as SetDateFormat(). However, in most cases this is not necessary. By default, Advantage uses "MM/DD/YYYY" as the date format. The default date format of VO depends on the nation driver it is using.

- Tables with extended data types cannot be created with the native VO DBCreate function or CREATE command. Instead, use the ACE API AdsCreateTable or AdsCreateTable71.

- The popular Wildseek() function that allows searching on any field in a table is not compatible with Advantage.  This function requires access to the file handle of the table which with Advantage is held by the server, not the client.  Instead, Advantage users can use the [CONTAINS()](master_contains.md) function and [Full Text Search (FTS) indexes](master_full_text_search.md) to quickly search character fields in a similar manner.
