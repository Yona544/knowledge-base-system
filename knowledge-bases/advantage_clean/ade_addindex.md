---
title: Ade Addindex
slug: ade_addindex
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_addindex.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 15199e4ce0508e09d5564f2bb574b126e7014bd4
---

# Ade Addindex

AddIndex

TAdsDataSet.AddIndex

Advantage TDataSet Descendant

| TAdsDataSet.AddIndex  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md)

Creates a new index for the table.

Syntax

type TIndexOptions = set of (ixPrimary, ixUnique, ixDescending, ixCaseInsensitive, ixExpression);

 

procedure AddIndex (const Name, Fields: string; Options: TIndexOptions);

Description

Call AddIndex to create a new index for the table associated with a dataset. The index created with this procedure is added to the table underlying the dataset. Name is the name of the new index. Fields is a semicolon-delimited list of the fields to include in the index or an index expression. For example, Upper(field1)+Lower(field2). Options is a potentially restricted set of one or more of the following values:

| Value | Meaning |
| ixPrimary | Creates a unique index and specifies this index as the table's primary key. Only respected on ADT tables created in a data dictionary. |
| ixUnique | Creates a unique index. |
| ixDescending | Sorts in descending alphanumeric order. |
| ixCaseInsensitive | Sorts records case-insensitively. |
| ixExpression | Does nothing (compatibility only). Expressions can be used without this parameter. |

Attempting to create an index using options that are not applicable to the table raises an exception.

Note If the TableType is ttAdsCDX or ttAdsVFP, then the created index order will be included in the structural index file. A structural index file is an auto-open index file that has the same name as the table but has a CDX extension.

 

If the TableType is ttAdsADT, then the created index order will be included in the auto-open index file. An auto-open index file has the same name as the table but has a ADI extension.

 

If the TableType is ttAdsNTX, then the created index order will be a single index order within a single index file. The file name of the index will be the tag name of the index. If the index tag is greater than 8 characters, it will be truncated to conform to an 8-character file name. The tag within the index will remain the full length.

The UNIQUE property of indexes is very different between DBF (CDX and NTX) and ADT and VFP table types. With CDX and NTX tables, an index order created with the UNIQUE property will only include records that are referenced by unique values. If two records result in the identical key value, then only one of the records will be referenced by the index. The second is simply never added, and no error is reported. This is the traditional Xbase behavior of the UNIQUE property.

With Advantage proprietary (ADT) and Visual FoxPro (VFP) tables, an index order created with the UNIQUE property enforces all records in the table to be referenced via a unique key. Note that use of the ixUnique property actually creates an index with the ADS\_CANDIDATE option with VFP tables. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be logged in the Advantage error log. That error log entry will indicate the record number, the tag name, and the index name associated with the non-unique index value. Up to fifty of these unique key violations will be logged before the index creation will be aborted. If any records are not unique, an error will be returned, and the index will not be usable. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the AdsCancelUpdate or AdsCloseTable API must be called to cancel the update of the record. Note that the AdsLookupKey API may be used to predetermine that a key is unique.

When creating new index files for ADT tables, the [AdsIndexPageSize](ade_adsindexpagesize.md) property will be respected. When adding a new index order to an existing index file, the AdsIndexpageSize property is ignored, and the existing index page size is maintained. See [Index Page Size](master_index_page_size.md) for more information.

Note ixCaseInsensitive is not compatible with ixExpression. Creating an index with the option set [ixCaseInsensitive, ixExpression] is illegal and will raise an exception.

 

Note Indexes created with the ixCaseInsensitive option will correctly disregard case in all operations. However, the IndexDefs.Options property of these indexes will fail to list the ixCaseInsensitive option.

 

Note for Data Dictionary Users If the table was opened by the ADSSYS user, the newly created index is automatically added to the database and it is available to all users accessing the table.

 

5054 errors: If the current user does not have ALTER permissions on the table, and attempts to call the AddIndex method a 5054 error will be returned. Instead, the user can create a temporary index which will not be added to the dictionary. Temporary indexes require the user to specify the index filename that the index will belong to. This is not possible through the AddIndex method. Use the [TAdsDataSet.AddIndexEx](ade_addindexex.md) method instead.
