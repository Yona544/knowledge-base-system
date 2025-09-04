---
title: Dotnet Direct Table Access In Ado Net
slug: dotnet_direct_table_access_in_ado_net
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_direct_table_access_in_ado_net.htm
source: Advantage CHM
tags:
  - dotnet
checksum: d3cddc7324637c9de4a5835cbe709b1d62476520
---

# Dotnet Direct Table Access In Ado Net

Direct Table Access in ADO.NET

Direct Table Access in ADO.NET

Advantage .NET Data Provider

| Direct Table Access in ADO.NET  Advantage .NET Data Provider |  |  |  |  |

While ADO.NET uses a disconnected data model, it is often very convenient to have direct access to a table. The [AdsExtendedReader](dotnet_adsextendedreader.md) class can be used to perform advanced table navigation, indexed searches, scopes, filters, locks and direct data manipulation.

While this class is a descendant of the AdsDataReader class, its functionality is not limited to reading data. It is basically a class that exposes much of the Advantage ISAM functionality to ADO.NET users, and is part of what makes Advantage unique.

The AdsExtendedReader class provides direct access to tables, elminating the need to read an entire result set into an in-memory dataset on the client. Because it supports ISAM functionality, it can also provide the functionality necessary to migrate legacy code to the ADO.NET framework.
