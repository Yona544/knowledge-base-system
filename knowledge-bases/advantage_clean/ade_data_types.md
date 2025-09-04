---
title: Ade Data Types
slug: ade_data_types
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_data_types.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f38ff78be6a78a5d7f9a9064199f2bb85d28a86f
---

# Ade Data Types

Data Types

Data Types

Advantage TDataSet Descendant

| Data Types  Advantage TDataSet Descendant |  |  |  |  |

This table shows how field types are converted when Paradox tables are imported to the Advantage ADT Table format.

| Paradox Data Type | Advantage Data Type | Comment |
| Alpha | Character |  |
| Number | Double |  |
| Money | Money | This data type applies to Advantage ADT tables only. It does not apply to DBF tables.  Note to Delphi users: Delphi 5 or greater is required to use the Money data type. |
| Short | Integer | The Paradox Short type is unsigned. Since Advantage has no unsigned 2-byte data types, an Integer type is used. |
| Long Integer | Integer |  |
| BCD | Money or Double | If the precision of the BCD field contains four or less decimal digits, the result data type will be Money. Otherwise, it will be double. Note: The Money data type applies to ADT and Visual FoxPro (VFP) tables only. |
| Date | Date |  |
| Time | Time | This data type applies to Advantage ADT tables only. It does not apply to DBF tables. |
| Timestamp | TimeStamp | This data type applies to Advantage ADT and Visual FoxPro (VFP) tables only. |
| Memo | Memo |  |
| Formatted Memo | Memo |  |
| Graphic | Image |  |
| OLE | Binary |  |
| Logical | Logical |  |
| AutoIncrement | AutoIncrement | This data type applies to Advantage ADT and Visual FoxPro (VFP) tables only. |
| Binary | Binary |  |
| Bytes | Raw | This data type applies to Advantage ADT tables only. It does not apply to DBF tables. |
| RowVersion | RowVersion | This data type applies to Advantage ADT tables only. It does not apply to DBF tables. |
| ModTime | ModTime | This data type applies to Advantage ADT tables only. It does not apply to DBF tables. |

Primary Indexes

An index named PRIMARY is created for each of the Paradox tables during the import process. By default, the PRIMARY index is not the default index with an Advantage application. The PRIMARY index can be set as the default index in the [Advantage Data Dictionary](master_advantage_data_dictionary.md) or otherwise, the PRIMARY index name will need to be specified in the application wherever needed.

Index Structures

Advantage places all individual indexes into a single file called a compound index file. Specific indexes within a compound index file are differentiated via "tag" names. Tag names are a way to specify a unique name to set an active index. If the base file name of the compound index file is the same as the base file name of the associated table, the index file is called an auto-open or structural index file and is automatically opened when the table is opened. The maximum number of tags inside a single compound index file is limited to 50.

Index Expression

You can use an index expression and an index condition with Advantage proprietary ADI index files. The Advantage Expression Engine is used to evaluate expression index statements. See [Advantage Expression Engine](master_advantage_expression_engine.md) for more information.
