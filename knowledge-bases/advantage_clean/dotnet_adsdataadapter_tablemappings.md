---
title: Dotnet Adsdataadapter Tablemappings
slug: dotnet_adsdataadapter_tablemappings
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_tablemappings.htm
source: Advantage CHM
tags:
  - dotnet
checksum: a3d2b1403194a43b67af3e4865d595f8f6cd25ef
---

# Dotnet Adsdataadapter Tablemappings

AdsDataAdapter.TableMappings

AdsDataAdapter.TableMappings

Advantage .NET Data Provider

| AdsDataAdapter.TableMappings  Advantage .NET Data Provider |  |  |  |  |

Gets a collection that provides the master mapping between a source table and a DataTable.

public DataTableMappingCollection TableMappings {get;}

Remarks

When reconciling changes, the DataAdapter uses the DataTableMappingCollection collection to associate the column names used by the data source with the column names used by the DataSet.
