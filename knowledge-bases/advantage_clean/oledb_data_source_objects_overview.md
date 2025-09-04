---
title: Oledb Data Source Objects Overview
slug: oledb_data_source_objects_overview
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_data_source_objects_overview.htm
source: Advantage CHM
tags:
  - oledb
checksum: 8d8dcab5321d025a37701ee807d2c384c684c1d2
---

# Oledb Data Source Objects Overview

Data Source Objects Overview

Data Source Objects Overview

Advantage OLE DB Provider (for ADO)

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
