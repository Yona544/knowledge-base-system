---
title: Oledb Data Source Properties
slug: oledb_data_source_properties
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_data_source_properties.htm
source: Advantage CHM
tags:
  - oledb
checksum: d7f956f9b35a311ee412e6b9ab99af721ae1d059
---

# Oledb Data Source Properties

Data Source Properties

Data Source Properties

Advantage OLE DB Provider (for ADO)

| Data Source Properties  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider implements the following property in the DBPROPSET\_DATASOURCE property set. All DBPROPSET\_DATASOURCE properties are in the Data Source property group.

| Property ID | Description |
| DBPROP\_CURRENTCATALOG | Type: VT\_BSTR  Typical R/W: Read-only  Description: Current Catalog (current database)  Specifies the name of the current catalog. The consumer can use the CATALOGS schema rowset to enumerate catalogs. For the Advantage OLE DB Provider, a catalog is equivalent to a database. This property will contain the name of the database (data dictionary) that was opened once a Database Connection) to an Advantage server has been made. This property will contain an empty string if a Free Connection) to an Advantage server has been made. The Advantage OLE DB provider does not allow the catalog (data dictionary name) to be changed after the connection has been made to the server. |
