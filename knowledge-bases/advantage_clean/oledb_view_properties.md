---
title: Oledb View Properties
slug: oledb_view_properties
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_view_properties.htm
source: Advantage CHM
tags:
  - oledb
checksum: cd3c3156e0209e4ee6bd9ed0fad75f8f1d48f2c3
---

# Oledb View Properties

View Properties

View Properties

Advantage OLE DB Provider (for ADO)

| View Properties  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider implements the following properties in the DBPROPSET\_VIEW property set.

| Property ID | Description |
| DBPROP\_FILTERCOMPAREOPS | Type: VT\_I4  Typical R/W: Read-only  Default: DBPROPVAL\_CO\_EQUALITY | DBPROPVAL\_CO\_STRING | DBPROPVAL\_CO\_CONTAINS | DBPROPVAL\_CO\_BEGINSWITH  Description: This specifies the filter operations that are supported by the Advantage OLE DB Provider. The provider supports LT, LE, EQ, GE, GT, NE, BEGINSWITH, NOTBEGINSWITH, CONTAINS, and NOTCONTAINS. |
| DBPROP\_IViewChapter | Type: VT\_BOOL  Typical R/W: Read-only  Default: VARIANT\_TRUE  Description: Indicates that the Advantage OLE DB Provider supports the IViewChapter interface on view objects. |
| DBPROP\_IViewFilter | Type: VT\_BOOL  Typical R/W: Read-only  Default: VARIANT\_TRUE  Description: Indicates that the Advantage OLE DB Provider supports the IViewFilter interface on view objects. |
| DBPROP\_ISupportErrorInfo | Type: VT\_BOOLTypical  R/W: Read-only  Default: VARIANT\_TRUE  Description: Indicates that the Advantage OLE DB Provider supports the ISupportErrorInfo interface on view objects. |
| DBPROP\_MAXORSINFILTER | Type: VT\_I4  Typical R/W: Read-only  Default: 0  Description: Indicates the maximum number of disjoint conditions that can be supported in a view filter. This property returns a value of 0 because the Advantage OLE DB Provider does not limit the number of conditions that can be joined with OR operators. |
