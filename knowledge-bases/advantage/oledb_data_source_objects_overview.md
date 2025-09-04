Data Source Objects Overview




Advantage Database Server 12  

Data Source Objects Overview

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Source Objects Overview  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Data Source Objects Overview Advantage OLE DB Provider (for ADO) oledb\_Data\_source\_objects\_overview Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Data Source Objects > Data Source Objects Overview / Dear Support Staff, |  |
| Data Source Objects Overview  Advantage OLE DB Provider (for ADO) |  |  |  |  |

OLE DB uses the term data source for the set of OLE DB interfaces used to establish a link to a data store, such as the Advantage Database Server. Creating an instance of the data source object of the provider is the first task of an OLE DB consumer.

Every OLE DB provider declares a class identifier for itself. The class identifier for the Advantage OLE DB Provider is the C/C++ GUID CLSID\_Advantage.OLEDB. With the class identifier, the consumer uses the OLE CoCreateInstance function to manufacture an instance of the data source object.

The Advantage OLE DB Provider is an in-process server. Instances of the Advantage OLE DB Provider objects are created using the CLSCTX\_INPROC\_SERVER macro to indicate the executable context.

The Advantage OLE DB Provider data source object exposes the OLE DB initialization interfaces that allow the consumer to connect to existing Advantage databases.

The following example uses the class identifier macro to create an Advantage OLE DB Provider data source object and get a reference to its IDBInitialize interface:

 

IDBInitialize \*pIDBInitialize;

HRESULT hr;

 

hr = CoCreateInstance( CLSID\_Advantage.OLEDB, NULL,

CLSCTX\_INPROC\_SERVER, IID\_IDBInitialize,

(void\*\*) &pIDBInitialize );

if ( SUCCEEDED( hr ) )

{

// Do necessary processing with the interface.

pIDBInitialize->Uninitialize();

pIDBInitialize->Release();

}

else

{

// Display error from CoCreateInstance.

}

With successful creation of an instance of an Advantage OLE DB Provider data source object, the consumer application can continue on by initializing the data source object and creating sessions. OLE DB sessions present the interfaces that allow data access and manipulation.