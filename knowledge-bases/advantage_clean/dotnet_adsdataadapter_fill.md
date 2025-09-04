---
title: Dotnet Adsdataadapter Fill
slug: dotnet_adsdataadapter_fill
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_fill.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 882a0281716e11f9475581142bdf896c0218b20d
---

# Dotnet Adsdataadapter Fill

AdsDataAdapter.Fill

AdsDataAdapter.Fill

Advantage .NET Data Provider

| AdsDataAdapter.Fill  Advantage .NET Data Provider |  |  |  |  |

Adds or refreshes rows in a specified range in the DataSet to match those in the data source.

The following overloaded versions are supported:

public override int Fill( DataSet dataSet );

 

public int Fill( DataTable dataTable );

 

public int Fill( DataSet dataSet, string srcTable );

 

public int Fill( DataSet dataSet, int startRecord,

int maxRecords, string srcTable );

Remarks

The Fill method retrieves rows from the data source using the SELECT statement specified by an associated SelectCommand property. The connection object associated with the SELECT statement must be valid, but it does not need to be open. If the connection is closed before Fill is called, it is opened to retrieve data, then closed. If the connection is open before Fill is called, it remains open.

The Fill operation then adds the rows to the specified destination DataTable object in the DataSet, creating the DataTable object if it does not already exist. When creating a DataTable object, the Fill operation normally creates only column name metadata. However, if the [AdsDataAdapter.MissingSchemaAction](dotnet_adsdataadapter_missingschemaaction.md) property is set to AddWithKey, appropriate primary keys and constraints are also created.

If the AdsDataAdapter object encounters duplicate columns while populating a DataTable, it will generate names for the subsequent columns, using the pattern "columnname1", "columnname2", "columnname3", and so on. If the incoming data contains unnamed columns, they are placed in the DataSet according to the pattern "Column1", "Column2", and so on.

You can use the Fill method multiple times on the same DataTable. If a primary key exists, incoming rows are merged with matching rows that already exist. If no primary key exists, incoming rows are appended to the DataTable.

Note Advantage does not currently support multiple result sets, therefore the SelectCommand must be a single statement.

Example

AdsConnection conn = new AdsConnection( "data source=c:\\data" );

conn.Open();

AdsDataAdapter da = new AdsDataAdapter( "select \* from customer", conn );

 

DataSet data = new DataSet();

 

da.Fill( data, "thetable" );
