Indexes




Advantage Database Server 12  

Indexes

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Indexes  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Indexes Advantage OLE DB Provider (for ADO) oledb\_Indexes Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Rowsets > Indexes / Dear Support Staff, |  |
| Indexes  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider supports integrated indexes in the IOpenRowset, IRowsetIndex, and IRowsetCurrentIndex interfaces.

Note SetRange is not currently exposed in ADO.

Index Properties

The Advantage OLE DB Provider implements the following properties in the DBPROPSET\_INDEX property set. All of these properties are in the Index property group.

|  |  |
| --- | --- |
| Property ID | Description |
| DBPROP\_INDEX\_AUTOUPDATE | Type: VT\_BOOL  Typical R/W: Read-only  Description: Auto Update  Specifies whether the index is maintained automatically when changes are made to the corresponding base table. For the Advantage OLE DB Provider, the value is always VARIANT\_TRUE, which indicates that the index is automatically maintained. |
| DBPROP\_INDEX\_CLUSTERED | Type: VT\_BOOL  Typical R/W: Read-only  Description: Clustered  Specifies whether an index is clustered. For the Advantage OLE DB Provider, the value is always VARIANT\_FALSE, which indicates that the leaf nodes of the index contain bookmarks relating to the base table rows whose key values match the key values of the index entry. |
| DBPROP\_INDEX\_FILLFACTOR | Type: VT\_BSTR  Typical R/W: Read-only  Description: Fill Factor  For a B+- tree index, this property represents the storage use of page nodes during the creation of the index. The value is an integer, from 1 to 100, that represents the percentage of use of an index node. This value is always 100 in the Advantage OLE DB Provider. |
| DBPROP\_INDEX\_NULLCOLLATION | Type: VT\_I4  Typical R/W: Read-only  Description: NULL Collation  Specifies how null values are collated in the index. For the Advantage OLE DB Provider, the value is always DBPROPVAL\_NC\_LOW, which indicates that null values are collated at the low end of the list. |
| DBPROP\_INDEX\_NULLS | Type: VT\_I4  Typical R/W: Read-only  Description: NULL Keys  Specifies whether null keys are allowed. For the Advantage OLE DB Provider, the value is always DBPROPVAL\_IN\_ALLOWNULL, which indicates that the index allows entries where the key columns are NULL. |
| DBPROP\_INDEX\_PRIMARYKEY | Type: VT\_BOOL  Typical R/W: Read-only  Description: Primary Key  Specifies whether the index represents the primary key on the table. For the Advantage OLE DB Provider, this value is always VARIANT\_FALSE because primary keys are not directly supported. |
| DBPROP\_INDEX\_SORTBOOKMARKS | Type: VT\_BOOL  Typical R/W: Read-only  Description: Sort Bookmarks  Specifies how the index treats repeated keys. For the Advantage OLE DB Provider, the value is always VARIANT\_TRUE, which indicates that the index sorts repeated keys by bookmark. |
| DBPROP\_INDEX\_TEMPINDEX | Type: VT\_BOOL  Typical R/W: Read-only  Description: Temporary Index  Specifies whether the index is temporary. If the index is a temporary index, the value is VARIANT\_TRUE. If the index is permanent, the value is VARIANT\_FALSE. |
| DBPROP\_INDEX\_TYPE | Type: VT\_I4  Typical R/W: Read-only  Description: Index Type  Specifies the type of the index. For the Advantage OLE DB Provider, the value is always DBPROPVAL\_IT\_BTREE, which indicates that the index is a B+ tree. |
| DBPROP\_INDEX\_UNIQUE | Type: VT\_BOOL  Typical R/W: Read-only  Description: Unique  Specifies whether index keys must be unique. If the keys in the index are unique, this value is VARIANT\_TRUE. If the keys in the index are not unique, this value is VARIANT\_FALSE. |