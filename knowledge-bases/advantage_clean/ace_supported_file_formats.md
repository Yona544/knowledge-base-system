---
title: Ace Supported File Formats
slug: ace_supported_file_formats
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_supported_file_formats.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fa53e374651fd8bb237b7fb5000179e6b7267882
---

# Ace Supported File Formats

Supported File Formats

Supported File Formats

Advantage Client Engine

| Supported File Formats  Advantage Client Engine |  |  |  |  |

Xbase File Formats

The following table shows the DBF file formats and the default extensions for each format.

| Database | Tables | Index Files | Memo Files |
| CA-Clipper 5.01 | DBF | NTX | DBT |
| CA-Clipper 5.2 | DBF | NTX, compact IDX, CDX (structural and non-structural) | DBT, FPT |
| CA-Clipper 5.3 | DBF | NTX, CDX (structural and non-structural) | DBT, FPT |
| Microsoft FoxPro | DBF | compact IDX, CDX (structural and non-structural) | FPT |

Advantage Proprietary File Format

The following table shows the Advantage proprietary file formats and the default extensions for each format.

| Database | Tables | Index Files | Memo Files |
| Advantage | ADT | ADI (auto-open and non-auto-open) | ADM |

Advantage Proprietary Files Versus Xbase Files

Advantage provides a proprietary file format (ADT, ADI, and ADM) that allows for advanced functionality that goes beyond that of the standard Xbase format (DBF, CDX/IDX/NTX, and FPT/DBT). For backwards compatibility and for the ability to share data with non-Advantage applications such as FoxPro, the standard Xbase file format is still supported by Advantage. Some limitations, differences, and functionality changes between Advantage proprietary files and Xbase files are explained below.

Beginning with version 9.0, Advantage added further support for Visual FoxPro tables. These VFP tables are treated as a separate type (ADS\_VFP) for backwards compatibility reasons. In general, the ADS\_VFP table type is a superset of the ADS\_CDX table type. If you need to maintain compability with older applications, then you should continue using the ADS\_CDX type to avoid using features that the older applications would not support. To use some of the newer features supported by Visual FoxPro tables such as NULL field values, long field names, DateTime fields, Money fields, VarChar fields, Auto-Increment fields, etc., then you need to use the ADS\_VFP table type.

Field Names

Field names in Advantage proprietary ADT tables are limited to 128 characters and may contain any character value except 0 (NULL), ";" (a semi-colon), or "," (a comma). Field names in a DBF table are limited to just 10 characters and may contain only the letters a-z and A-Z, digits 0-9, and the underscore "\_" character. However, if you are using the Visual FoxPro (VFP) table type and the table is in a data dictionary, then field names can be up to 128 characters. Note, though, that the physical DBF only stores a 10 byte field name, so any third party utilities that access the table without Advantage would see only the short field name.

Field Types

Advantage proprietary ADT tables have support for some field types that are not available in a DBF table including Short Integer (ADS\_SHORTINT), Time (ADS\_TIME), Raw (ADS\_RAW), RowVersion (ADS\_ROWVERSION), and ModTime (ADS\_MODTIME). See [AdsCreateTable](ace_adscreatetable.md) for a full discussion of the ADT table types.

Index Tag Names

Advantage proprietary ADI index file tag names are limited to 128 characters and may contain any character value except 0 (NULL), ";" (a semi-colon), or "," (a comma). Xbase index file (i.e., CDX index file) tag names are limited to 10 characters and may only contain the letters a-z and A-Z, digits 0-9, and the underscore "\_" character.

Index and Filter Expression Operators

When using an Advantage proprietary ADT table, a concatenation operator named ";" can be used in index and filter expressions. This operator will take fields of any data type and concatenate them with the best possible efficiency. For example, if two fields exist that are named DATE\_FIELD and CHAR\_FIELD, an index can be built with the expression "DATE\_FIELD; CHAR\_FIELD". The equivalent index expression for a DBF table would be "DTOS( DATE\_FIELD ) + CHAR\_FIELD", which concatenates the characters that are the result of the DTOS function call, and the data stored in the character field. See [Expression Engine Operators](master_expression_engine_operators.md) for more information on the concatenation operator.

It is also possible to use the binary concatenation operator with Visual FoxPro (VFP) tables when creating indexes, however, these indexes will not be compatible with Visual FoxPro when accessing the tables directly (and not through Advantage).

Unique indexes (a.k.a. primary indexes)

The "unique" property of indexes is very different between Advantage proprietary indexes and standard Xbase indexes.

An Xbase index order created with the "unique" property will only include records that are referenced by unique values. If two records result in the identical key value, then only one of the records will be referenced by the index. The second is simply never added, and no error is reported. If the record (of the two with identical key values) referenced by the unique index is modified such that the key value changes, that index key will be removed from the index, but the other record with the identical key value will NOT be added to the unique index. Therefore, no key will be referencing the unique record in the index. This is the traditional Xbase behavior of the "unique" property in Xbase indexes.

An Advantage proprietary ADI index order created with the "unique" property enforces all records in the table to be referenced via a unique key. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be generated and the index order will not be created. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the update must be canceled or the table and index must be closed.

The Visual FoxPro (VFP) table type supports the ability to create candidate indexes (ADS\_CANDIDATE). These indexes behave the same as ADI unique indexes. If an update causes a non-unique key to be created, an error is returned.

See [AdsCreateIndex](ace_adscreateindex.md) for more information.

Deleted Records

If a delete record operation is performed on a record in a DBF table, the record is not physically removed from the table. Nor is the record logically removed from the table. The record is instead "marked for deletion". Optionally, records marked for deletion can still be visible to the application. Records marked for deletion can also be "un-deleted", or "recalled" as it is referred to in Xbase terminology. Thus, the deletion status of a record is nothing more than a filter. If an application is written to allow records marked for deletion to be visible (which is the default), then the record deletion status is irrelevant. If an application is written to ignore records that are marked for deletion, then those records marked for deletion have effectively been filtered from visibility. If the Pack operation is performed on a table, then and only then will records marked for deletion be physically removed from the table.

If a delete record operation is performed on a record in an ADT table, the record is not physically removed from the table. The record is, however, logically removed from the table. Deleted records in an ADT table are not visible to the application. Deleted records cannot be "un-deleted" or "recalled". The space used by records deleted from the table are marked for record re-use. That is, a subsequent append or insert operation will use space marked for re-use before using new space at the end of the table for a new record. Thus, the size of an ADT table will not increase after an append or insert operation if there is space marked for re-use in the table. If the Pack operation is performed on a table, space marked as available for record re-use will be physically removed from the table. Because deleted records are reused with ADT tables, they are automatically unlocked by the server when they are flushed. This is done even if the record is explicitly locked by the user (see [AdsLockRecord](ace_adslockrecord.md)).

Record Size

The ADT file format uses less memory to store Date, Memo, and Numeric fields. However, ADT tables do have more overhead per record and within the header information. Overall, ADT tables should require less disk space than DBF tables.

Maximum File Size

For information on maximum record, table, index file, and memo file sizes, see [Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.md)

Encryption

Encryption in ADT tables is more strict and contains many more safeguards than encryption in DBF tables. Each ADT table can be encrypted with just a single password. If an ADT table contains one or more records that have been encrypted with that single password, and an application opens that table but does not have the correct password, those encrypted records will be treated as read-only to the application (and will not be readable since they are encrypted). If an entire ADT table has been encrypted, an application will be unable to update, append, or insert records into that table unless it has the correct password that was used to encrypt the records in that table.

In order to use [AES encryption](master_encryption.md), you must use either the ADT or VFP format. AES encryption requires that additional information be stored with each record. The NTX and CDX table types do not have the capability of storing the additional record information.

Performance

The Advantage proprietary file format is optimized for use with Advantage. With ADT tables, information is stored within each record that is used to decrease the number of Advantage Database Server requests necessary to read and write memo data. Transaction processing with ADT tables is more efficient for the same reason. ADI index files contain keys that can be compared more efficiently especially for non-English collation sequences. Records in an ADT table are generally smaller than records in a DBF table, so less data needs to be transferred between the client and the server.

Record counts and key counts can be computed more efficiently with ADT tables than with DBF tables when using deleted record filtering (see [AdsShowDeleted](ace_adsshowdeleted.md)). The deleted record count is maintained in ADT tables, and no ADI index keys exist that reference deleted records, therefore it is not necessary to perform a physical deleted record count with ADT tables as is necessary with DBF tables.

Memo Block Size

The memo files for ADM (Advantage proprietary), DBT (CA-Clipper compatible) and FPT (FoxPro compatible) memo files are segmented into blocks. The DBT file is always segmented into memo blocks of 512 bytes. The ADM and FPT file memo block sizes are configurable at creation time. ADM files can have memo block sizes from 8 bytes to 32768 bytes. The default ADM memo block size is 256 bytes. FPT files can have memo block sizes of 33 bytes or greater. The default FPT memo block size is 64 bytes. Note that FPT files can be created with memo block sizes of 1-32, but the actual size of the block is that number times 512 bytes. See [AdsCreateTable](ace_adscreatetable.md) for more information on specifying the memo block size.

NULL field values

The ADT file format supports a NULL field value for every non-auto-updating field type. The Visual FoxPro (ADS\_VFP) file format also supports NULL values on fields. Note that when creating a VFP table, the NULL option must be provided specifically for each field that needs to be able to contain NULLs. The ADS\_CDX and ADS\_NTX DBF table types do not support true NULL values.

Advantage API Functional Differences

Some Advantage Client Engine API functions behave differently based upon the file format used. For more information, see the documentation for each function. The APIs are:

[AdsDeleteRecord](ace_adsdeleterecord.md)

[AdsRecallRecord](ace_adsrecallrecord.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsShowDeleted](ace_adsshowdeleted.md)

[AdsCreateIndex](ace_adscreateindex.md)
