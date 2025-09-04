---
title: Dotnet Adsconnection Ddversionmajor
slug: dotnet_adsconnection_ddversionmajor
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_ddversionmajor.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 90c1553796214f41a02f262e67a1e49b647dd6cd
---

# Dotnet Adsconnection Ddversionmajor

AdsConnection.DDVersionMajor

AdsConnection.DDVersionMajor

Advantage .NET Data Provider

| AdsConnection.DDVersionMajor  Advantage .NET Data Provider |  |  |  |  |

Get or set the database major version.

public int DDVersionMajor{ get; set; }

Remarks

Gets or sets the user major version property of the data dictionary. This property is intended for storing a value associated with the major version of the user's dictionary. The user version property is set, read, and interpreted by the application. The Advantage Database Server does not currently use it internally. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The default value for this property, if it has never been set, is 0. If set to NULL, the user version property value will be removed.

See Also

[DDVersionMinor](dotnet_adsconnection_ddversionminor.md)
