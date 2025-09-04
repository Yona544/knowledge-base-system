---
title: Oledb Creating A Rowset With Iopenrowset
slug: oledb_creating_a_rowset_with_iopenrowset
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_creating_a_rowset_with_iopenrowset.htm
source: Advantage CHM
tags:
  - oledb
checksum: 6248e42be939874d9a99190968287f5474af4d9b
---

# Oledb Creating A Rowset With Iopenrowset

Creating a Rowset with IOpenRowset

Creating a Rowset with IOpenRowset

Advantage OLE DB Provider (for ADO)

| Creating a Rowset with IOpenRowset  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider supports the IOpenRowset::OpenRowset method with the following restrictions:

- •   A base table must be specified in a DBID structure that the pTableID parameter points to.

- •   The DBID eKind member must indicate DBKIND\_NAME.

- •   The DBID uName member must specify name of an existing base table as a Unicode character string.

- •   The pIndexID parameter of OpenRowset should be NULL if you wish to view the table in natural record number order.

- •   An index order name should be specified in a DBID structure that the pIndexID parameter points to if you wish to view the table in a sorted order.

- •   The DBID eKind member must indicate DBKIND\_NAME.

- •   The DBID uName member must specify name of an existing index order as a Unicode character string.

The result set of IOpenRowset::OpenRowset contains a single rowset.
