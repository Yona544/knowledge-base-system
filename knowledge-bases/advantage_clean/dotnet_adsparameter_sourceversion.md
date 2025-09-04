---
title: Dotnet Adsparameter Sourceversion
slug: dotnet_adsparameter_sourceversion
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_sourceversion.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 644edccce7569ae9cd8cb83bd321866f8f287ac3
---

# Dotnet Adsparameter Sourceversion

AdsParameter.SourceVersion

AdsParameter.SourceVersion

Advantage .NET Data Provider

| AdsParameter.SourceVersion  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the DataRowVersion to use when loading Value.

public DataRowVersion SourceVersion {get; set;}

Remarks

The SourceVersion property is used by the [AdsDataAdapter.UpdateCommand](dotnet_adsdataadapter_updatecommand.md) during the Update to determine whether the original or current value is used for a parameter value. This allows primary keys to be updated. This property is ignored by the [AdsDataAdapter.InsertCommand](dotnet_adsdataadapter_insertcommand.md) and [AdsDataAdapter.DeleteCommand](dotnet_adsdataadapter_deletecommand.md). The default value is DataRowVersion.Current.
