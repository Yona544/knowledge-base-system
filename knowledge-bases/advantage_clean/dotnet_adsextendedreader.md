---
title: Dotnet Adsextendedreader
slug: dotnet_adsextendedreader
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 0719d20ac3beea99da30300a8ea271b1c4fe56ed
---

# Dotnet Adsextendedreader

AdsExtendedReader

AdsExtendedReader

| AdsExtendedReader |  |  |  |  |

Advantage .NET Data Provider

Full name: Advantage.Data.Provider.AdsExtendedReader

Implements: System.Data.IDataReader

[Properties](dotnet_adsextendedreader_properties.md)

[Methods](dotnet_adsextendedreader_methods_1.md)

[Enumerations](dotnet_adsextendedreader_enumerations.md)

[Events](dotnet_adsextendedreader_events.md)

An AdsExtendedReader object represents a result set obtained from Advantage Database Server or Advantage Local Server via an SQL statement or a directly opened table. AdsExtendedReader is derived from AdsDataReader and offers an extended feature set that includes advanced table navigation, indexed searches, scopes, filters, locks and direct data manipulation.

To create an AdsExtendedReader, you must call the AdsCommand.ExecuteExtendedReader method, rather than directly using a constructor.
