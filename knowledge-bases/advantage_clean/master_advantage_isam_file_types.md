---
title: Master Advantage Isam File Types
slug: master_advantage_isam_file_types
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_isam_file_types.htm
source: Advantage CHM
tags:
  - master
checksum: 127bf3c8b18c2f198fca43293ccc0dcbc9c3eeb4
---

# Master Advantage Isam File Types

Advantage ISAM File Types

Advantage ISAM File Types

Advantage Concepts

| Advantage ISAM File Types  Advantage Concepts |  |  |  |  |

The Advantage Database Server handles three individual file types: tables, index files, and memo files.

Tables

Tables are the "main" file type containing the rows (records) and columns (fields) of data. The records of data in the table are a fixed length and do not exist in any sorted order. The data stored in columns in tables are fixed in length. Each record in the table is assigned a unique record number.

Index Files

Index files contain one or more index orders that allow table data to be viewed in a sorted order based on one or more columns in a single table, or an expression involving one or more columns in a single table. Index orders do not physically re-order the records in the table. Instead they provide for a very fast and efficient method of viewing your table data or searching for a particular item of table data. For example, to view the table data in rows sorted in "last name" order, the application would have to create an index order on the "last name" column and make it the "active" index order. As many as 15 index files can be open at one time per table, and certain types of index files can contain many individual index "orders". Once an index file is created, that index file must be opened every time the table is opened in order for updates to the table to be reflected in the index order(s) in the index file. If a table is open and is updated, but an associated index file is not open, that index file is logically corrupt and must be re-built (re-indexed) for it to contain valid and current information. ADI and CDX index files can be created as auto-open index files, and, therefore, will be automatically opened when the table is opened and cannot be closed until the table is closed.

Although multiple index files can be opened per table, only one index order can be "active" for the table. The active index identifies in what sorted order the table will be viewed. If no index files are open, or if index files are open but no index order has been made the "active" index order, the table will be viewed in "natural" order, which is simply record number order. If the table is updated, index orders in all open index files will be updated whether they are the active index order or not. Updates to index orders automatically occur when a record in the table is updated, inserted, or deleted. No special code is necessary in the application to update an index order, other than making sure the index file is open when the table is open.

Index "keys" are the individually sorted elements in an index order that reference a record in a table. Basically, what a record is to a table, a key is to an index. For example, if an index order exists on the "last name" field, and if record 100 in the table has the value "Smith" in the last name field, then the index order would have a "Smith" key that references record 100.

Memo Files

Advantage supports variable length memo, binary, and image data types. The data for memo, binary, and image fields are not stored in the table file, but are stored in a separate file called a memo file. Memo files allow the table to remain relatively small even if data for the memo, binary, and image fields is very large. The table does contain a short, fixed length field for each memo, binary, and image field, but it is nothing more than a "pointer" to the data in the memo file. Memo fields contain character data while binary and image fields contain BLOB data. If the table contains no memo, binary, or image fields, no associated memo file will exist.
