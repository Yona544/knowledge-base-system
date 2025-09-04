---
title: Devguide Overview Of Index Files
slug: devguide_overview_of_index_files
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_overview_of_index_files.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ba9f822ebe779383b87cee1f0d1908c26480c6c3
---

# Devguide Overview Of Index Files

Overview of Index Files

 

     Overview of Index Files

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Overview of Index Files  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

An index file is one that contains one or more index orders, also referred to as tags. An index file that contains only one index order is called a single-order index, but these are rare. Because you often need to access a table in a number of different ways, most developers include many index orders in a given index file. An index file that has two or more index orders is referred to as a multiple-order index file, or compound index file. A given index file can contain up to 50 index orders.

Not all index files are alike. Index files that have the same name as their associated table are known as structural indexes. The primary advantage of structural index files is that they are auto-open index files. Specifically, if you open a table, Advantage automatically opens that tables structural index. Likewise, when you close the table, the structural index is closed for you.

A given table can have up to 15 index files. However, only the structural index file is an auto-open index file. Any additional index files associated with a given table must be explicitly opened and closed through code (or the appropriate utility in the Advantage Data Architect). If you make any changes to a table without opening all of its indexes, those indexes that were left closed would likely be logically corrupt, in which case they would need to be rebuilt.

   
NOTE: When a table is associated with a data dictionary, and the table is being opened using the data dictionary, all of the table's indexes are opened automatically.  
 

Index orders consist of zero or more keys. A key has two parts, an index key expression and a reference to a record in a table. The index key expression is used to sort and search the keys in the index. Most index key expressions consist of data from one or more fields in a table. For example, an index key expression may consist of the data from the customer ID field of a customer table. The associated index could then be used to order customers by their customer ID, as well as to search for records based on customer ID. But index key expressions can also be more involved, and may include two or more field values, constants, functions, and a variety of operators, including concatenation, arithmetic, and Boolean.

Every record in an Advantage table has a unique record number, and each key points to a single record using this record number. Some types of index orders, such as expression indexes, have one key in the index order for each record in the associated table. Other index orders, such as conditional index orders and custom index orders, may have far fewer keys than records in the associated table. As a result, these index orders refer only to some of a tables records. Finally, an FTS index may have many keys for each record, with one key for each indexed word in each record.
