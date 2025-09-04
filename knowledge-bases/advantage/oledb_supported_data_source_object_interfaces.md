Supported Data Source Object Interfaces




Advantage Database Server 12  

Supported Data Source Object Interfaces

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Supported Data Source Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Supported Data Source Object Interfaces Advantage OLE DB Provider (for ADO) oledb\_Supported\_data\_source\_object\_interfaces Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Data Source Objects > Supported Data Source Object Interfaces / Dear Support Staff, |  |
| Supported Data Source Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Data Source object is supported with the Advantage OLE DB Provider. Below is the list of supported interfaces in the Data Source object. Generally, for each interface listed, all the methods will be supported.

Data Source Object

|  |  |
| --- | --- |
| IDBCreateSession | IPersist |
| IDBInitialize | ISupportErrorInfo |
| IDBProperties | IDBInfo |

Implementation Details by Method

The Advantage OLE DB Provider supports IDBCreateSession interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| CreateSession | Creates a new session from the data source object and returns the requested interface on the newly created session. |

The Advantage OLE DB Provider supports IDBInitialize interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| Initialize | Initializes a data source object. |
| Uninitialize | Returns the data source object to an uninitialized state. |

The Advantage OLE DB Provider supports IDBProperties interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetProperties | Returns the values of properties in the Data Source, Data Source Information, and Initialization property groups that are currently set on the data source object. |
| GetPropertyInfo | Returns information about all properties supported by the provider. |
| SetProperties | Sets properties in the Data Source and Initialization property groups. |

The Advantage OLE DB Provider supports IPersist interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetClassID | Supplies the CLSID of an object that can be stored persistently in the system. |

The Advantage OLE DB Provider supports ISupportErrorInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| InterfaceSupportsErrorInfo | Indicates whether a specific OLE DB interface can return OLE DB error objects. |

The Advantage OLE DB Provider supports IDBInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetKeyWords | Returns a list of provider-specific keywords. |
| GetLiteralInfo | Returns information about literals used in text commands. |