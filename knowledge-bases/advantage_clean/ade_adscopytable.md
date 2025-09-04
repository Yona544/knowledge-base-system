---
title: Ade Adscopytable
slug: ade_adscopytable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscopytable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d6be5abde4ddaf4e7f091408d203004fc9f9dfbf
---

# Ade Adscopytable

AdsCopyTable

TAdsTable/TAdsQuery.AdsCopyTable

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsCopyTable  Advantage TDataSet Descendant |  |  |  |  |

Copies a dataset structure and its records to a new table.

Syntax

procedure AdsCopyTable( strFileName : String );

Parameter

| strFileName | Name of the file to copy to, which must include the full path of the destination table. |

Description

The records copied to the new table depend on the filter options selected under AdsTableOptions.AdsFilterOptions and AdsTableOptions.AdsScopeOptions. The following table determines how the different combinations of these options will behave:

Index files will not be copied as they can be created after the copy. The resulting table must be opened by the application after making the copy in order to use it.

If performing an AdsCopyTable operation on an ADT table, and that ADT table contains an AutoIncrement field, the AutoIncrement values will be preserved in the destination table. That is, the new records in the destination table will have the same values in the AutoIncrement column as those records in the source table. The next available AutoIncrement value will also be identical in the source and destination tables.

The copy will be done on the server if the following conditions are met:

- Both tables are on the same server and both tables are of the same type (e.g., both are opened with ADS\_CDX)

- Neither table is opened exclusively

- The destination table does not have a file lock

If the table name provided does not include a path, the current working directory will be used. A "default" search path can be specified using the AdsSetDefault API. It is recommend you always pass a path, however.

If the server fails to copy the data and the client succeeds, AdsCopyTableContents returns AE\_SUCCESS. The error that caused the copy to scale back from the server to the client is available by calling [AdsGetLastError](ade_adsgetlasterror.md). The error codes that will be returned by AdsGetLastError if the copy is scaled back to the client will be one of the following:

| AE\_FILE\_NOT\_ON\_SERVER | The destination file was on another server. |
| AE\_INFO\_COPY\_MADE\_BY\_CLIENT | This error is returned in all other cases and contains specific information in the returned error buffer. |

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note This function is illegal in a transaction.

 

Note Static cursors are always in the ADT format. If you pass this function a static cursor, the resulting file will be in ADT format as well. Live cursors will maintain their file format in the new file. Specifically, when AdsCopyTable is called with static cursors from DBF tables, the resulting table will be an ADT. And when AdsCopyTable is called with live cursors created from DBF tables, the resulting table will be a DBF. To convert to another file format use [AdsConvertTable](ade_adsconverttable.md).

Example

AdsTable1.TableName := x:\data\employee.adt;

AdsTable1.Active := TRUE;

AdsTable1.AdsCopyTable( x:\backup\savefile.adt );

See Also

[AdsCopyTableContents](ade_adscopytablecontents.md)

[AdsCopyTableStructure](ade_adscopytablestructure.md)

[AdsConvertTable](ade_adsconverttable.md)
