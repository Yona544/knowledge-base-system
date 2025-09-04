---
title: Oledb Supported View Object Interfaces
slug: oledb_supported_view_object_interfaces
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_supported_view_object_interfaces.htm
source: Advantage CHM
tags:
  - oledb
checksum: 2c59635cb079fc9ae7a29e4dc4f044d108b7cfaa
---

# Oledb Supported View Object Interfaces

Supported View Object Interfaces

Supported View Object Interfaces

Advantage OLE DB Provider (for ADO)

| Supported View Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The View object is supported with the Advantage OLE DB Provider. Below is the list of supported interfaces and methods in the View object. Please note that not all methods are implemented. Only the methods that are required for creating and setting filters are supported.

View Object

| IViewChapter | IViewFilter | ISupportErrorInfo |  |

Implementation Details By Method

The Advantage OLE DB Provider supports IViewChapter interface member functions as described in the following table.

| Member Function | Description |
| GetSpecification | Returns the rowset from which the view was created. |
| OpenViewChapter | Returns a chapter that can be passed to rowset methods that accept HCHAPTER handles. A chapter is an opaque object that contains the necessary filter information to be used by the rowset methods. |

The Advantage OLE DB Provider supports IViewFilter interface member functions as described in the following table.

| Member Function | Description |
| GetFilter | Returns E\_NOTIMPL. |
| GetFilterBindings | Returns E\_NOTIMPL. |
| SetFilter | Specifies a filter condition for a view. Note that the accessor handle must be created on the rowset from which the view was created. View objects in the Advantage OLE DB Provider do not support the IAccessor interface. Note that the Advantage OLE DB Provider does not support filtering on memo, raw, or BLOB fields. If the accessor references fields of these types, this method returns DB\_E\_CANTFILTER. |

The Advantage OLE DB Provider supports ISupportErrorInfo interface member functions as described in the following table.

| Member Function | Description |
| InterfaceSupportsErrorInfo | Indicates whether a specific OLE DB interface can return OLE DB error objects. |
