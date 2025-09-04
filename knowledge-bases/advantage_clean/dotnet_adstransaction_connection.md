---
title: Dotnet Adstransaction Connection
slug: dotnet_adstransaction_connection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adstransaction_connection.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 7d010a9ef92ddbf0d7bcfefb795c1f498db0ae2d
---

# Dotnet Adstransaction Connection

AdsTransaction.Connection

AdsTransaction.Connection

Advantage .NET Data Provider

| AdsTransaction.Connection  Advantage .NET Data Provider |  |  |  |  |

Retrieves the AdsConnection associated with the transaction.

public AdsConnection Connection {get;}

Remarks

The Advantage .NET Data Provider stores a reference to the AdsConnection object that began the transaction in the AdsTransaction object. This property can be used by an application to retrieve that connection. This may be useful for applications that have multiple connections active at a time.

See Also

[AdsConnection](dotnet_adsconnection.md)
