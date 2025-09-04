---
title: Dotnet Adsdataadapter Missingmappingaction
slug: dotnet_adsdataadapter_missingmappingaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_missingmappingaction.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 03ffceb69120feda412445a6db659e361487a229
---

# Dotnet Adsdataadapter Missingmappingaction

AdsDataAdapter.MissingMappingAction

AdsDataAdapter.MissingMappingAction

Advantage .NET Data Provider

| AdsDataAdapter.MissingMappingAction  Advantage .NET Data Provider |  |  |  |  |

Indicates or specifies whether unmapped source tables or columns are passed with their source names in order to be filtered or to raise an error.

public MissingMappingAction MissingMappingAction {get; set;}

Remarks

The valid values are shown in the following table. The default is PassThrough. The [AdsDataAdapter.TableMappings](dotnet_adsdataadapter_tablemappings.md) property provides the master mapping between the returned records and the DataSet.

| Member Name | Description |
| Error | A SystemException is generated. |
| Ignore | The column or table not having a mapping is ignored. Returns a null reference (Nothing in Visual Basic). |
| Passthrough | The source column or source table created and added to the DataSet using its original name. |

See Also

[TableMappings](dotnet_adsdataadapter_tablemappings.md)
