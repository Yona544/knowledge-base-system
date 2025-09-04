---
title: Ace Adsfindconnection
slug: ace_adsfindconnection
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsfindconnection.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4fd21a137604ea6a3d9ff61dc980cd43e7e27108
---

# Ace Adsfindconnection

AdsFindConnection

AdsFindConnection

Advantage Client Engine

| AdsFindConnection  Advantage Client Engine |  |  |  |  |

Finds a connection handle associated with the server name

Syntax

| UNSIGNED32 | AdsFindConnection (UNSIGNED8 \*pucServerName,  ADSHANDLE \*phConnect); |

Parameters

| pucServerName (I) | Server name. |
| phConnect (O) | Return the connection handle if connection found. |

Remarks

AdsFindConnection will find the connection handle related to a server. The connection handle can be used in calls to [AdsOpenTable](ace_adsopentable.md) , [AdsCreateTable](ace_adscreatetable.md) , and the transaction functions such as [AdsBeginTransaction](ace_adsbegintransaction.md).

Example

[Click Here](ace_examples.md#adsfindconnection_example)

See Also

[AdsConnect](ace_adsconnect.md)

[AdsDisconnect](ace_adsdisconnect.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsFindConnection25](ace_adsfindconnection25.md)
