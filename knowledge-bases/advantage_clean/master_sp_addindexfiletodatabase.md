---
title: Master Sp Addindexfiletodatabase
slug: master_sp_addindexfiletodatabase
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_addindexfiletodatabase.htm
source: Advantage CHM
tags:
  - master
checksum: 600d606b9c716f640a675a2a8600ca8bdd40df01
---

# Master Sp Addindexfiletodatabase

sp\_AddIndexFileToDatabase

sp\_AddIndexFileToDatabase

Advantage SQL Engine

| sp\_AddIndexFileToDatabase  Advantage SQL Engine |  |  |  |  |

Associates an index file with a database table in the data dictionary.

Syntax

sp\_AddIndexFileToDatabase(

TableName,CHARACTER,200,

IndexFilePath,CHARACTER,515,

Comment,memo )

Parameters

| TableName (I) | Name of the table to associate the index file. |
| IndexFilePath (I) | File path of the index file as a relative path from the data dictionary file or fully qualified UNC path. If the path given is not a fully qualified path, the index file is assumed to be in the same directory as the table. Once the index file is successfully added in the data dictionary and associated with the table, the base filename of the index file including the extension can be used to identify the index file in the data dictionary. |
| Comment (I) | Optional description of the index file to store in the data dictionary. This parameter can be NULL. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The table specified by TableName cannot be located in the data dictionary. |
| AE\_INDEX\_ALREADY\_OPEN | The index files is already associated with the specified table. |

Remarks

sp\_AddIndexFileToDatabase associates the specified index file with a database table. After calling this function, all index orders in the specified index file will be automatically available for the table when the table is opened.

Note sp\_AddIndexFileToDatabase requires an exclusive open of the table. An error will be returned if the table cannot be opened exclusively.

Example

After making a connection to the database, add a DBF table into the data dictionary and associate three NTX index files with it (two using the sp\_AddTableToDatabase system procedure and one using the sp\_AddIndexFileToDatabase system procedure).

EXECUTE PROCEDURE sp\_AddTableToDatabase(

Customer Information,

\\server\share\mydata\customer.dbf,

1,

2,

Lastname.ntx;Cust\_id.ntx,

NULL );

 

EXECUTE PROCEDURE sp\_AddIndexFileToDatabase(

Customer Information,

InvoiceDate.ntx,

NULL );

See Also

[sp\_AddTableToDatabase](master_sp_addtabletodatabase.md)
