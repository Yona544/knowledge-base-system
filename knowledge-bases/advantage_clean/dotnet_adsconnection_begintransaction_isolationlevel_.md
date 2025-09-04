---
title: Dotnet Adsconnection Begintransaction Isolationlevel
slug: dotnet_adsconnection_begintransaction_isolationlevel_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_begintransaction_isolationlevel_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 0e7c2538e583d783a5c1b6953c0996d4ce394632
---

# Dotnet Adsconnection Begintransaction Isolationlevel

AdsConnection.BeginTransaction( IsolationLevel )

AdsConnection.BeginTransaction( IsolationLevel )

Advantage .NET Data Provider

| AdsConnection.BeginTransaction( IsolationLevel )  Advantage .NET Data Provider |  |  |  |  |

Begins a database transaction with the specified isolation level.

public AdsTransaction BeginTransaction( IsolationLevel iso );

Remarks

This returns an [AdsTransaction](dotnet_adstransaction.md) object representing the new transaction. Currently, the isolation level must be IsolationLevel.ReadCommitted. Advantage currently does not support other isolation levels. This method will throw a NotSupportedException if a different isolation level is specified.

Distributed transactions are not supported. If any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is started. Note that Advantage Local Server does not support transactions. If the ServerType property ([AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md)) is LOCAL, no transaction will actually be started, although an AdsTransaction object will still be returned. Transactions can be nested by calling BeginTransaction inside of an existing transaction.

Example

see [AdsConnection.BeginTransaction()](dotnet_adsconnection_begintransaction_.md)

See Also

[AdsConnection.BeginTransaction](dotnet_adsconnection_begintransaction_.md)

[AdsTransaction](dotnet_adstransaction.md)
