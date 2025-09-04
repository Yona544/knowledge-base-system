---
title: Ade Adscopytablecontents
slug: ade_adscopytablecontents
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscopytablecontents.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 513ea9cfaa01f55edaa5856d7aebce102ff05f9a
---

# Ade Adscopytablecontents

AdsCopyTableContents

TAdsTable/TAdsQuery.AdsCopyTableContents

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsCopyTableContents  Advantage TDataSet Descendant |  |  |  |  |

Appends the contents of one dataset to another existing dataset.

Syntax

procedure AdsCopyTableContents( poDestination : TAdsDataSet );

Parameter

| poDestination | Pointer to the dataset instance you want to copy to. |

Description

AdsCopyTableContents only copies fields to the destination dataset that have matching names in the source dataset. A dataset cannot be copied onto itself.

The records copied to the new table depend on the filter options selected under AdsTableOptions.AdsFilterOptions and AdsTableOptions.AdsScopeOptions. The following table determines how the different combinations of these options will behave:

| Options Set | Respects Filters | Respects Scopes |
| RESPECT\_WHEN\_COUNTING  RESPECT\_SCOPES\_WHEN\_COUNTING | X | X |
| RESPECT\_WHEN\_COUNTING  IGNORE\_SCOPES\_WHEN\_COUNTING | X | X |
| IGNORE\_WHEN\_COUNTING  RESPECT\_SCOPES\_WHEN\_COUNTING |  | X |
| IGNORE\_WHEN\_COUNTING  IGNORE\_SCOPES\_WHEN\_COUNTING |  |  |

If performing an AdsCopyTableContents operation on an ADT table, and that ADT table contains an AutoIncrement field, the AutoIncrement values in records copied to the destination table will not necessarily be preserved. That is, the new records copied to the destination table are not guaranteed to have the same values in the AutoIncrement column as those records in the source table. Since the AdsCopyTableContents operation copies records to an existing table, it is possible that AutoIncrement values in the existing records in the destination table are identical to those in the source table. Since AutoIncrement values must be unique, the AutoIncrement values in the source table may not be preserved when they are copied to the destination table.

The copy will be done on the server if the following conditions are met:

- Both tables are on the same server and both tables are of the same type (e.g., both are opened with ADS\_CDX)

- Neither table is opened exclusively

- hObj is not a cursor

- If hObj is an index, it isnt opened exclusively

- The destination table does not have a file lock

If the server fails to copy the data and the client succeeds, the error that caused the copy to scale back from the server to the client is available by calling [AdsGetLastError](ade_adsgetlasterror.md). The error codes that will be returned by AdsGetLastError if the copy is scaled back to the client will be one of the following:

| AE\_FILE\_NOT\_ON\_SERVER | The destination file was on another server. |
| AE\_INFO\_COPY\_MADE\_BY\_CLIENT | This error is returned in all other cases and contains specific information in the returned error buffer. |

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note This function is illegal in a transaction.

Example

AdsTable1.TableName := 'Employee';

AdsTable1.Active := TRUE;

AdsTable1.AdsTableOptions.AdsFilterOptions := RESPECT\_WHEN\_COUNTING;

AdsTable1.Filter := 'Date Of Hire > CTOD( "1/13/90" )';

AdsTable1.Filtered := TRUE;

 

AdsTable2.Active := TRUE;

AdsTable1.AdsCopyTableContents( AdsTable2 );

See Also

[AdsCopyTable](ade_adscopytable.md)

[AdsCopyTableStructure](ade_adscopytablestructure.md)

[AdsConvertTable](ade_adsconverttable.md)
