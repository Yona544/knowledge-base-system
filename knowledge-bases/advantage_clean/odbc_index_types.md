---
title: Odbc Index Types
slug: odbc_index_types
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_index_types.htm
source: Advantage CHM
tags:
  - odbc
checksum: 98a9a3ad12b713a6a73cc5bcb847d6707589294d
---

# Odbc Index Types

Index Types

Index Types

Advantage ODBC Driver

| Index Types  Advantage ODBC Driver |  |  |  |  |

Index files must reside in the same directory as their corresponding database files in order for the Advantage ODBC Driver to properly access and maintain the indexes. Advantage index files are defined with different names from the Xbase database files. Because of this flexibility, index files must be associated with their corresponding database files. Depending on the [Table Type](odbc_table_type.md) selected in your Advantage Data Source, index file management may vary.

Advantage uses the index files to optimize queries, enabling the query engine to process query requests more rapidly. The indexes selected for each table are maintained as updates and inserts are executed on the database files. If indexes are not opened with the tables, they will become logically corrupted if the database files are modified.

The Advantage SQL engine can use ADI, CDX, and NTX indexes to aid in optimizing SELECT statements. While the ADI and CDX index types can be used to optimize complex queries, the NTX index type has very limited usefulness in optimizing SQL queries. It is only used to optimize a query containing a simple WHERE clause or ORDER BY clause. When creating indexes, the Driver can create one of three index types, depending on the selected Default Index type in the Data Source. The following chart describes the type of indexes created and what limitations must be noted.

| Index Type | Xbase UNIQUE | DESC | Auto-Open Indexes |
| FoxPro CDX | Yes | Yes | Yes |
| Visual FoxPro CDX | Yes, however candidate indexes can be used. | Yes | Yes |
| Advantage ADI | No | Yes | Yes |
| CA-Clipper NTX | Yes | Yes | No |

 

Note The Advantage ODBC driver supports auto-open indexes only with free connection). To use NTX indexes, and other non-auto-open indexes, you must use a database connection). Create a database (defined in an [Advantage Data Dictionary](master_advantage_data_dictionary.md)) and add the tables and the associated NTX index files to that database. Then use those tables on that database connection). The NTX index files will then get automatically opened when the corresponding DBF table is opened. You can use the Advantage Data Architect to create a database and data dictionary.

 

Note Advantage ADI indexes support Unique indexes in a different way than Xbase Unique. Advantage Unique indexes require inserted keys to be unique. Visual FoxPro (VFP) tables have similar true unique enforcement via candidate indexes.

See Also

[FoxPro Behavior](odbc_foxpro_behavior.md)

[Advantage Behavior](odbc_advantage_behavior.md)

[Compatability](odbc_compatability.md)
