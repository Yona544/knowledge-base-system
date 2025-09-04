---
title: Dotnet Adsdataadapter Fillschema
slug: dotnet_adsdataadapter_fillschema
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_fillschema.htm
source: Advantage CHM
tags:
  - dotnet
checksum: fcebf6be7343fc82ce761cf68d8ba8c9c5b2a934
---

# Dotnet Adsdataadapter Fillschema

AdsDataAdapter.FillSchema

AdsDataAdapter.FillSchema

Advantage .NET Data Provider

| AdsDataAdapter.FillSchema  Advantage .NET Data Provider |  |  |  |  |

Adds a DataTable to a DataSet and configures the schema to match that in the data source.

The following overloaded versions are supported:

public override DataTable[] FillSchema( DataSet dataSet, SchemaType schemaType );

 

public DataTable FillSchema( DataTable dataTable, SchemaType schemaType );

 

public DataTable[] FillSchema( DataSet dataSet, SchemaType schemaType, string srcTable );

Remarks

The return value is a reference to a collection of DataTable objects that were added to the DataSet. This method retrieves the schema information from the data source using the [AdsDataAdapter.SelectCommand](dotnet_adsdataadapter_selectcommand.md).

See Also

[GetSchemaTable](dotnet_adsdatareader_getschematable.md)
