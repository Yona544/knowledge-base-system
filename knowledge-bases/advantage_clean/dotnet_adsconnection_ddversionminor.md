---
title: Dotnet Adsconnection Ddversionminor
slug: dotnet_adsconnection_ddversionminor
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_ddversionminor.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 301bb77951c06277c3cc3cac8e80db50f3c413ce
---

# Dotnet Adsconnection Ddversionminor

AdsConnection.DDVersionMinor

AdsConnection.DDVersionMinor

Advantage .NET Data Provider

| AdsConnection.DDVersionMinor  Advantage .NET Data Provider |  |  |  |  |

Get or set the database minor version.

public int DDVersionMinor{ get; set; }

Remarks

Gets or sets the user minor version property of the data dictionary. This property is intended for storing a value associated with the minor version of the user's dictionary. The user version property is set, read, and interpreted by the application. The Advantage Database Server does not currently use it internally. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The default value for this property, if it has never been set, is 0. If set to NULL, the user version property value will be removed.

See Also

[DDVersionMajor](dotnet_adsconnection_ddversionmajor.md)
