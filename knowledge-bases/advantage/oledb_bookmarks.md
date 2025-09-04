Bookmarks




Advantage Database Server 12  

Bookmarks

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bookmarks  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Bookmarks Advantage OLE DB Provider (for ADO) oledb\_Bookmarks Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Rowsets > Bookmarks / Dear Support Staff, |  |
| Bookmarks  Advantage OLE DB Provider (for ADO) |  |  |  |  |

Bookmarks allow consumers to return quickly to a row. The Advantage OLE DB Provider supports bookmarks for all non-schema rowsets. With bookmarks, consumers can access rows randomly based on the bookmark value. The bookmark column is column 0 in the rowset. The consumer sets the dwFlag field value of the binding structure to DBCOLUMNSINFO\_ISBOOKMARK to indicate that the column is used as bookmark. The IRowsetLocate::GetRowsAt method is then used to fetch rows, starting with the row specified as an offset from a bookmark.