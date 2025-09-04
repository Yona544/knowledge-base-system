---
title: Ace Connection Handles
slug: ace_connection_handles
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_connection_handles.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 87ba32215e58f94a28db1b9b474b67635b7a9a0f
---

# Ace Connection Handles

Connection Handles

Connection Handles

Advantage Client Engine

| Connection Handles  Advantage Client Engine |  |  |  |  |

The idea of controllable connections to Advantage servers has not been available before. This capability exposes new functionality for Advantage. A connection handle is a reference to a single communication link with the Advantage server. These Advantage connections can be controlled explicitly, but it is also possible to let the Advantage Client Engine control connections. To allow the Advantage Client Engine to control server connections, specify a zero for the connection parameter on calls to [AdsOpenTable](ace_adsopentable.md), [AdsCreateTable](ace_adscreatetable.md) and the transaction functions ([AdsBeginTransaction](ace_adsbegintransaction.md), [AdsCommitTransaction](ace_adscommittransaction.md), [AdsRollbackTransaction](ace_adsrollbacktransaction.md), and [AdsInTransaction](ace_adsintransaction.md)).

To control Advantage server connections explicitly, use the functions [AdsConnect](ace_adsconnect.md), [AdsDisconnect](ace_adsdisconnect.md), and [AdsFindConnection](ace_adsfindconnection.md). The availability of these functions allows an application to obtain multiple connections to the same Advantage server. Because Advantage Server transactions are performed by connection, it is now possible for an application to control multiple independent transactions at one time.

Note Although multiple transactions are now possible from one client on an Advantage Server, record visibility through the separate table handles on the separate connections is exactly as if the transactions were taking place from different client machines. Therefore, if a record in one transaction is updated, the other transaction will not see the change until it is committed.

[AdsApplicationExit](ace_adsapplicationexit.md) will close all implicit and all explicit connections. In addition, [AdsDisconnect](ace_adsdisconnect.md) can be used to close connections explicitly.
