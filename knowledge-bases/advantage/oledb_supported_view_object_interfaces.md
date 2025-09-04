Supported View Object Interfaces




Advantage Database Server 12  

Supported View Object Interfaces

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Supported View Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Supported View Object Interfaces Advantage OLE DB Provider (for ADO) oledb\_Supported\_view\_object\_interfaces Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Views (OLE DB) > Supported View Object Interfaces / Dear Support Staff, |  |
| Supported View Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The View object is supported with the Advantage OLE DB Provider. Below is the list of supported interfaces and methods in the View object. Please note that not all methods are implemented. Only the methods that are required for creating and setting filters are supported.

View Object

|  |  |  |  |
| --- | --- | --- | --- |
| IViewChapter | IViewFilter | ISupportErrorInfo |  |

Implementation Details By Method

The Advantage OLE DB Provider supports IViewChapter interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetSpecification | Returns the rowset from which the view was created. |
| OpenViewChapter | Returns a chapter that can be passed to rowset methods that accept HCHAPTER handles. A chapter is an opaque object that contains the necessary filter information to be used by the rowset methods. |

The Advantage OLE DB Provider supports IViewFilter interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetFilter | Returns E\_NOTIMPL. |
| GetFilterBindings | Returns E\_NOTIMPL. |
| SetFilter | Specifies a filter condition for a view. Note that the accessor handle must be created on the rowset from which the view was created. View objects in the Advantage OLE DB Provider do not support the IAccessor interface. Note that the Advantage OLE DB Provider does not support filtering on memo, raw, or BLOB fields. If the accessor references fields of these types, this method returns DB\_E\_CANTFILTER. |

The Advantage OLE DB Provider supports ISupportErrorInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| InterfaceSupportsErrorInfo | Indicates whether a specific OLE DB interface can return OLE DB error objects. |