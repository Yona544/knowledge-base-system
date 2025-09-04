---
title: Dotnet Adsdataadapter Constructor Adscommand
slug: dotnet_adsdataadapter_constructor_adscommand_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_constructor_adscommand_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 99420c76f3dc4d120dcd01ca6d26bdc983831132
---

# Dotnet Adsdataadapter Constructor Adscommand

AdsDataAdapter Constructor( AdsCommand )

AdsDataAdapter Constructor( AdsCommand )

Advantage .NET Data Provider

| AdsDataAdapter Constructor( AdsCommand )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsDataAdapter object with a given command object.

public AdsDataAdapter( AdsCommand command );

Remarks

The provided [AdsCommand](dotnet_adscommand.md) object is stored as the [SelectCommand](dotnet_adsdataadapter_selectcommand.md) property. The command is not cloned; the AdsDataAdapter simply keeps a reference to the command object.
