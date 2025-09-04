---
title: Dotnet Adsconnection
slug: dotnet_adsconnection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 672eb76a4e16f96d8a23af0df5158894d546fe21
---

# Dotnet Adsconnection

AdsConnection

AdsConnection

Advantage .NET Data Provider

| AdsConnection  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsConnection

Implements: System.Data.IDbConnection

[Constructors](dotnet_adsconnection_constructors.md)

[Properties](dotnet_adsconnection_properties.md)

[Methods](dotnet_adsconnection_methods.md)

[Events](dotnet_adsconnection_events.md)

The AdsConnection class represents a single connection to Advantage Database Server or Advantage Local Server. It can be used for both free connections) and [data dictionary connections](master_advantage_data_dictionary.md).

Example

The following C# code shows a simple example that creates a new AdsConnection object

AdsConnection conn = new AdsConnection( "data source=c:\\data;" +

"ServerType=remote|local; TableType=ADT" );

conn.Open();
