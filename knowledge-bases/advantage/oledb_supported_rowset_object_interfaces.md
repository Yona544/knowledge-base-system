Supported Rowset Object Interfaces




Advantage Database Server 12  

Supported Rowset Object Interfaces

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Supported Rowset Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Supported Rowset Object Interfaces Advantage OLE DB Provider (for ADO) oledb\_Supported\_rowset\_object\_interfaces Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Rowsets > Supported Rowset Object Interfaces / Dear Support Staff, |  |
| Supported Rowset Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Rowset object is supported with the Advantage OLE DB Provider. Below is the list of supported interfaces in the Rowset object. Generally, for each interface listed, all the methods will be supported.

Rowset Object

|  |  |  |  |
| --- | --- | --- | --- |
| IAccessor | IConvertType | IRowsetIdentity | IRowsetScroll |
| IChapteredRowset | IRowset | IRowsetIndex | IRowsetUpdate |
| IColumnsInfo | IRowsetChange | IRowsetInfo | IRowsetView |
| IColumnsRowset | IRowsetCurrentIndex | IRowsetLocate | ISupportErrorInfo |
| IConnectionPointContainer | IRowsetExactScroll | IRowsetRefresh |  |

 

Implementation Details by Method

The Advantage OLE DB Provider supports IAccessor interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| AddRefAccessor | Adds a reference count to an existing accessor. |
| CreateAccessor | Creates an accessor from a set of bindings. Optimized and ByRef accessors are not supported by the Advantage OLE DB Provider. |
| GetBindings | Returns the bindings in an accessor. |
| ReleaseAccessor | Releases an accessor. |

The Advantage OLE DB Provider supports IColumnsInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetColumnInfo | Returns the column metadata needed by most consumers. |
| MapColumnIDs | Returns an array of ordinals of the columns in a rowset that are identified by the specified column IDs. |

The Advantage OLE DB Provider supports IConvertType interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| CanConvert | Gives information about the availability of type conversions on a command or on a rowset. |

The Advantage OLE DB Provider supports IRowset interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| AddRefRows | Adds a reference count to an existing row handle. |
| GetData | Retrieves data from the rowset's copy of the row. |
| GetNextRows | Fetches rows sequentially, remembering the previous position. |
| ReleaseRows | Releases rows. |
| RestartPosition | Repositions the next fetch position to its initial position; that is, its position when the rowset was first created. |

The Advantage OLE DB Provider supports IRowsetInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetProperties | Returns the current setting of all properties supported by the rowset. |
| GetReferencedRowset | Returns an interface pointer to the rowset to which a bookmark applies. |
| GetSpecification | Returns an interface pointer on the object (command or session) that created the rowset. |

The Advantage OLE DB Provider supports IRowsetChange interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| DeleteRows | Deletes rows. |
| InsertRow | Creates and initializes a new row. |
| SetData | Sets data in one or more columns in a row. |

The Advantage OLE DB Provider supports IRowsetCurrentIndex interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetIndex | Gets the current index on the rowset. |
| SetIndex | Sets the current index on the rowset. |

The Advantage OLE DB Provider supports IRowsetIdentity interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| IsSameRow | Compares two row handles to see whether they refer to the same row instance. |

The Advantage OLE DB Provider supports IRowsetIndex interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetIndexInfo | Returns information about the index rowset capabilities. |
| Seek | Allows direct positioning at a key value within the current range. |
| SetRange | Restricts the set of row entries visible through calls to IRowset::GetNextRows and IRowsetIndex::Seek. |

The Advantage OLE DB Provider supports IRowsetLocate interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| Compare | Compares two bookmarks. |
| GetRowsAt | Fetches rows, starting with the row specified by an offset from a bookmark. |
| GetRowsByBookmark | Fetches the rows that match the specified bookmarks. |
| Hash | Returns hash values for the specified bookmarks. |

The Advantage OLE DB Provider supports IRowsetRefresh interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetLastVisibleData | Gets the most recent data from either the visible data cache or the data store. With a row update pending, this call is identical to calling IRowsetUpdate::GetOriginalData with the Advantage OLE DB Provider. |
| RefreshVisibleData | Retrieves the data values from the data store that are visible to the transaction for the specified rows. |

The Advantage OLE DB Provider supports IRowsetScroll interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetAppoximatePosition | Gets the approximate position of a row corresponding to a specified bookmark. |
| GetRowsAtRatio | Fetches rows starting from a fractional position in the rowset. |

The Advantage OLE DB Provider supports IRowsetUpdate interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetOriginalData | Gets the data most recently fetched from or transmitted to the data store; does not get values based on pending changes. With a row update pending, this call is identical to calling IRowsetRefresh::GetLastVisibleData with the Advantage OLE DB Provider. |
| GetPendingRows | Returns a list of rows with pending changes. With the Advantage OLE DB Provider, one row at most can have a change for it pending. |
| GetRowStatus | Returns the status of rows. |
| Undo | Undoes any changes made to a row since it was last fetched or since Update was called for it. |
| Update | Transmits any changes made to a row since it was last fetched or since Update was called for it. |

The Advantage OLE DB Provider supports ISupportErrorInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| InterfaceSupportsErrorInfo | Indicates whether a specific OLE DB interface can return OLE DB error objects. |

The Advantage OLE DB Provider supports IRowsetView interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| CreateView | Creates a view object on this rowset. View objects can be used to set filters on rowsets. |
| GetView | Returns E\_NOTIMPL. |

The Advantage OLE DB Provider supports IChapteredRowset interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| AddRefChapter | Adds a reference count to an existing chapter. |
| ReleaseChapter | Releases a chapter (decrements the reference count). |

The Advantage OLE DB Provider supports the IColumnsRowset interface on rowsets opened through IOpenRowset; it is not supported for rowsets opened through the ICommand interface. The IColumnsRowset interface supports the following member functions.

|  |  |
| --- | --- |
| Member Function | Description |
| GetAvailableColumns | Returns a list of optional metadata columns that can be supplied in a column metadata rowset. |
| GetColumnsRowset | Returns a rowset containing metadata about each column in the current rowset. This rowset is known as the column metadata rowset and is read-only. |