---
title: Ace Adsmgdisconnect
slug: ace_adsmgdisconnect
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsmgdisconnect.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: ce90d2ab49f024f67e6c84a7b6f3a5c6bf8b94b4
---

# Ace Adsmgdisconnect

AdsMgDisconnect

AdsMgDisconnect

Advantage Client Engine

| AdsMgDisconnect  Advantage Client Engine |  |  |  |  |

Disconnects the management API connection from the given server

Syntax

| UNSIGNED32 | AdsMgDisconnect (ADSHANDLE hMgmtConnect); |

Parameters

| hMgmtConnect (I) | Handle of management API connection. |

Remarks

AdsMgDisconnect currently is stubbed to call [AdsDisconnect](ace_adsdisconnect.md). It is recommended you use AdsMgDisconnect to disconnect the management API connection. A future release of the Advantage Client Engine may not support using a standard connection handle in place of a management API connection handle.

In a future release, AdsMgDisconnect may be used to disconnect the management API from the specified server.

Example

[Click Here](ace_advantage_management_api_examples.md#adsmgdisconnect_example)

See Also

[AdsMgConnect](ace_adsmgconnect.md)

[AdsMgDisconnect](ace_adsmgdisconnect.md)

[AdsConnect](ace_adsconnect.md)
