---
title: Master Rowid
slug: master_rowid
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_rowid.htm
source: Advantage CHM
tags:
  - master
checksum: dce0827f6e89dc956c541ca312eb676fbefedef4
---

# Master Rowid

ROWID

ROWID

Advantage SQL Engine

| ROWID  Advantage SQL Engine |  |  |  |  |

Advantage supports the ROWID pseudocolumn in SQL statements. ROWID identifies the physical address of each row/record in a table. This pseudocolumn is not evident when listing the structure of a table by executing a SELECT \* FROM . . . statement. However, each row's address can be retrieved with an SQL query using the reserved keyword ROWID as a column name, for example:

 

SELECT ROWID, ename FROM emp

 

You cannot set the value of the pseudocolumn ROWID in INSERT or UPDATE statements.

You can reference rowids in the pseudocolumn ROWID like other table columns (used in SELECT lists and WHERE clauses), but rowids are not stored in the database, nor are they database data. If you create a table with a column named ROWID, you will not be able to reference the psudocolumn ROWID.

The ROWID pseudocolumn is a fixed-length character column with column size of 18. ROWID uses a base 64 encoding of the database ID (connection path), table ID, and the record number for each row selected. The encoding characters are A-Z, a-z, 0-9, +, and /. For example, the following query:

SELECT ROWID, ename FROM emp WHERE deptno = 20;

 

might return the following row information:

 

ROWID ENAME

------------------ ----------

DBDBDBTABTABBrXAAA BORTINS

DBDBDBTABTABBrXAAE RUGGLES

DBDBDBTABTABBrXAAG CHEN

DBDBDBTABTABBrXAAN BLUMBERG

 

The first six characters of the ROWID represent the database ID. It is based on the connection path. The next six characters of the ROWID represent the table ID. If the table is a database table), that is, a table that belongs to an [Advantage Data Dictionary](master_advantage_data_dictionary.md), the table ID represents the object ID of the table in the data dictionary. If the table does not belong to an Advantage Data Dictionary, the table ID is constructed using the name of the table file. The last six characters represent the record number of the row in the table.

End users and application developers can use rowids for several important functions:

- Rowids are the fastest means of accessing particular rows.

- Rowids can be used to see how a table is organized.

- Rowids are unique identifiers for rows in a given table.

See Also

[ROWNUM](master_rownum.md)
