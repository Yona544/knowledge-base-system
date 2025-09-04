Sessions Overview




Advantage Database Server 12  

Sessions Overview

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Sessions Overview  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Sessions Overview Advantage OLE DB Provider (for ADO) oledb\_Sessions\_overview Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Sessions > Sessions Overview / Dear Support Staff, |  |
| Sessions Overview  Advantage OLE DB Provider (for ADO) |  |  |  |  |

An Advantage OLE DB Provider session represents a single connection to an Advantage server, which can be the Advantage Database Server, the Advantage Database Server via the Advantage Internet Server, or the Advantage Local Server.

OLE DB requires that sessions delimit transaction space for a data source. All command objects created from a specific session object participate in the local transaction of the session object.

Each session object created on the data source establishes its own connection to the Advantage server specified in the data source. The Advantage server connection is dropped when the application releases all references to objects created that session.

This example shows the Advantage OLE DB Provider Advantage Database Server connection usage.

int main()

{

// Interfaces used in the example.

IDBInitialize \*pIDBInitialize = NULL;

IDBCreateSession \*pIDBCreateSession = NULL;

IDBCreateCommand \*pICreateCmd1 = NULL;

IDBCreateCommand \*pICreateCmd2 = NULL;

 

// Initialize COM.

if ( FAILED( CoInitialize( NULL ) ) )

{

// Display error from CoInitialize.

return ( -1 );

}

 

// Get the memory allocator for this task.

if ( FAILED( CoGetMalloc( MEMCTX\_TASK, &g\_pIMalloc ) ) )

{

// Display error from CoGetMalloc.

goto EXIT;

}

 

// Create an instance of the data source object.

if ( FAILED( CoCreateInstance( CLSID\_Advantage.OLEDB, NULL,

CLSCTX\_INPROC\_SERVER,

ID\_IDBInitialize,

(void\*\*) &pIDBInitialize ) ) )

{

// Display error from CoCreateInstance.

goto EXIT;

}

 

// The InitFromPersistedDS function

// performs IDBInitialize->Initialize(), establishing

// the first application connection to the Advantage Database Server.

if ( FAILED( InitFromPersistedDS( pIDBInitialize, L"MyDataSource",

NULL, NULL ) ) )

{

goto EXIT;

}

 

// The IDBCreateSession interface is implemented on the data source

// object. Maintaining the reference received maintains the

// connection of the data source to the Advantage Database Server.

if ( FAILED( pIDBInitialize->QueryInterface( IID\_IDBCreateSession,

(void\*\*) &pIDBCreateSession ) ) )

{

// Display error from pIDBInitialize.

goto EXIT;

}

 

// Releasing this has no effect on the Advantage Database Server

// connection of the data source object because of the reference

// maintained by pIDBCreateSession.

pIDBInitialize->Release();

pIDBInitialize = NULL;

 

// The session created will establish a connection to the Advantage

// Database Server.

if ( FAILED( pIDBCreateSession->CreateSession( NULL,

IID\_IDBCreateCommand,

(IUnknown\*\*) &pICreateCmd1 ) ) )

{

// Display error from pIDBCreateSession.

goto EXIT;

}

 

// A new connection to the Advantage Database Server is established

// to support the next session object created. On successful

// completion, the application has two active connections on the

// Advantage Database Server.

if ( FAILED( pIDBCreateSession->CreateSession( NULL,

IID\_IDBCreateCommand,

(IUnknown\*\*) &pICreateCmd2 ) ) )

{

// Display error from pIDBCreateSession.

goto EXIT;

}

 

EXIT:

// Even on error, this does not terminate an Advantage Database

// Server connection because pICreateCmd1 has the connection of

// the data source object.

if ( pICreateCmd1 != NULL )

pICreateCmd1->Release();

 

// Releasing the reference on pICreateCmd2 terminates the SQL

// Server connection supporting the session object. The application

// now has only a single active connection on the Advantage Database

// Server.

if ( pICreateCmd2 != NULL )

pICreateCmd2->Release();

 

// On release of the last reference on a data source interface, the

// connection of the data source object to the Advantage Database

// Server is broken.

// The example application now has no Advantage Database Server

// connections active.

if ( pIDBCreateSession != NULL )

pIDBCreateSession->Release();

 

// Called only if an error occurred while attempting to get a

// reference on the IDBCreateSession interface of the data source.

// If so, the call to IDBInitialize::Uninitialize terminates the

// connection of the data source object to the Advantage Database

// Server.

if ( pIDBInitialize != NULL )

{

if ( FAILED( pIDBInitialize->Uninitialize() ) )

{

// Uninitialize is not required, but it fails if an

// interface has not been released. Use it for

// debugging.

}

pIDBInitialize->Release();

}

 

if ( g\_pIMalloc != NULL )

g\_pIMalloc->Release();

 

CoUninitialize();

 

return ( 0 );

}

Connecting Advantage OLE DB Provider session objects to a computer running Advantage Database Server can generate significant overhead for applications that continually create and release session objects. Managing the Advantage OLE DB Provider session objects efficiently can minimize the overhead. The Advantage OLE DB Provider applications can keep the Advantage Database Server connection of a session object active by maintaining a reference on at least one interface of the object.

For example, maintaining a pool of command creation object references keeps active connections for those session objects in the pool. As session objects are required, the pool maintenance code passes a valid IDBCreateCommand interface pointer to the application method requiring the session. When the application method no longer requires the session, the method returns the interface pointer back to the pool maintenance code rather than releasing the application's reference to the command creation object.

Note In the above example, the IDBCreateCommand interface is used because the ICommand interface implements the GetDBSession method, the only method in command or rowset scope that allows an object to determine the session on which it was created. Therefore, a command object, and only a command object, allows an application to retrieve a data source object pointer from which additional sessions can be created.