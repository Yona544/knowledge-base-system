Data Source Properties




Advantage Database Server 12  

Data Source Properties

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Source Properties  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Data Source Properties Advantage OLE DB Provider (for ADO) oledb\_Data\_source\_properties Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Data Source Objects > Data Source Properties / Dear Support Staff, |  |
| Data Source Properties  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider implements the following property in the DBPROPSET\_DATASOURCE property set. All DBPROPSET\_DATASOURCE properties are in the Data Source property group.

|  |  |
| --- | --- |
| Property ID | Description |
| DBPROP\_CURRENTCATALOG | Type: VT\_BSTR  Typical R/W: Read-only  Description: Current Catalog (current database)  Specifies the name of the current catalog. The consumer can use the CATALOGS schema rowset to enumerate catalogs. For the Advantage OLE DB Provider, a catalog is equivalent to a database. This property will contain the name of the database (data dictionary) that was opened once a [Database Connection](javascript:hhpopuplink.TextPopup(popid_2045887057,FontFace,-1,-1,-1,-1)) to an Advantage server has been made. This property will contain an empty string if a [Free Connection](javascript:hhpopuplink.TextPopup(popid_1940894724X,FontFace,-1,-1,-1,-1)) to an Advantage server has been made. The Advantage OLE DB provider does not allow the catalog (data dictionary name) to be changed after the connection has been made to the server. |