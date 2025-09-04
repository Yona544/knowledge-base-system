---
title: Ace Adsfindconnection25
slug: ace_adsfindconnection25
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsfindconnection25.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 1ee5ee6c9a707fd9085f2dbf10a323c31605ff1a
---

# Ace Adsfindconnection25

AdsFindConnection25

AdsFindConnection25

Advantage Client Engine

| AdsFindConnection25  Advantage Client Engine |  |  |  |  |

Finds a connection handle associated with the full path name.

Syntax

| UNSIGNED32 | AdsFindConnection25 (UNSIGNED8 \*pucFullPath,  ADSHANDLE \*phConnect); |

Parameters

| pucFullPath (I) | Full path name. |
| phConnect (O) | Return the connection handle if connection found. |

Remarks

AdsFindConnection25 is similar to [AdsFindConnection](ace_adsfindconnection.md). It will find the connection handle related to a server. The connection handle will be returned only if the path supplied is identical to a path used when creating a previous Advantage server connection. The connection handle can be used in calls to [AdsOpenTable](ace_adsopentable.md) , [AdsCreateTable](ace_adscreatetable.md) , and the transaction functions such as [AdsBeginTransaction](ace_adsbegintransaction.md).

Example

[Click Here](ace_examples.md#adsfindconnection25_example)

See Also

[AdsConnect](ace_adsconnect.md)

[AdsDisconnect](ace_adsdisconnect.md)

[AdsFindConnection](ace_adsfindconnection.md)

[AdsOpenTable](ace_adsopentable.md)
