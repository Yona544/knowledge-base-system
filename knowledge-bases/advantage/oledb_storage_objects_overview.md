Storage Objects Overview




Advantage Database Server 12  

Storage Objects Overview

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Storage Objects Overview  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Storage Objects Overview Advantage OLE DB Provider (for ADO) oledb\_Storage\_objects\_overview Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > BLOBs and Storage Objects > Storage Objects Overview / Dear Support Staff, |  |
| Storage Objects Overview  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB provider exposes the ISequentialStream interface to support consumer access to the Advantage data types ADS\_BINARY, ADS\_IMAGE, and ADS\_MEMO. It provides the capability to read those data types as binary large objects (BLOBs) and to handle the data in manageable pieces. For example, an application that uses ADO can read and write to these fields using the ADO GetChunk and AppendChunk methods.

The implementation of ISequentialStream in the Advantage OLE DB Provider has the following limitations:

|  |  |
| --- | --- |
| · | Advantage OLE DB does not support transactioning on ISequentialStream. STGM\_TRANSACTED is ignored if it is specified. |

|  |  |
| --- | --- |
| · | BLOB writes can be done two ways through storage objects. BLOB data can be written using the ISequentialStream::Write method, or a consumer can give a pointer to its own consumer-implemented storage object to the OLE DB provider through IRowsetUpdate::SetData. When using the former method, the Advantage OLE DB actually writes the BLOB data when the consumer releases the storage object. With the latter method, the Advantage OLE DB provider writes the data as soon as it receives the consumer's interface pointer via the IRowsetUpdate::SetData call. |

|  |  |
| --- | --- |
| · | When using a consumer-implemented storage object to write a BLOB object, it is most efficient if the consumer makes the data length known to the provider by binding the length indicator in the DBBINDING structure used for accessor creation. If the length is not provided, then the Advantage OLE DB Provider must read the entire BLOB into its own memory to determine the length before writing it because Advantage requires the length of ADS\_BINARY and ADS\_IMAGE fields to be specified before any data can be written. Alternatively, if the consumer-implemented storage object supports the IStream or ILockBytes interfaces, the Advantage OLE DB Provider can retrieve the length directly from those interfaces. |

|  |  |
| --- | --- |
| · | A consumer-implemented storage object must support at least one of the interfaces IStream, ILockBytes, or ISequentialStream. |

|  |  |
| --- | --- |
| · | When reading BLOB data through the Advantage OLE DB Provider ISequentialStream::Read method, only the specific data requested for a given Read request is transferred from the server. |