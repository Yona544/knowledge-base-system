Creating a Rowset with IOpenRowset




Advantage Database Server 12  

Creating a Rowset with IOpenRowset

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Rowset with IOpenRowset  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Creating a Rowset with IOpenRowset Advantage OLE DB Provider (for ADO) oledb\_Creating\_a\_rowset\_with\_iopenrowset Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Rowsets > Creating a Rowset with IOpenRowset / Dear Support Staff, |  |
| Creating a Rowset with IOpenRowset  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider supports the IOpenRowset::OpenRowset method with the following restrictions:

|  |  |
| --- | --- |
| · | •   A base table must be specified in a DBID structure that the pTableID parameter points to. |

|  |  |
| --- | --- |
| · | •   The DBID eKind member must indicate DBKIND\_NAME. |

|  |  |
| --- | --- |
| · | •   The DBID uName member must specify name of an existing base table as a Unicode character string. |

|  |  |
| --- | --- |
| · | •   The pIndexID parameter of OpenRowset should be NULL if you wish to view the table in natural record number order. |

|  |  |
| --- | --- |
| · | •   An index order name should be specified in a DBID structure that the pIndexID parameter points to if you wish to view the table in a sorted order. |

|  |  |
| --- | --- |
| · | •   The DBID eKind member must indicate DBKIND\_NAME. |

|  |  |
| --- | --- |
| · | •   The DBID uName member must specify name of an existing index order as a Unicode character string. |

The result set of IOpenRowset::OpenRowset contains a single rowset.