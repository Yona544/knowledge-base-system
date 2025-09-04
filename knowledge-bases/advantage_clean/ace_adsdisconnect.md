---
title: Ace Adsdisconnect
slug: ace_adsdisconnect
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdisconnect.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a8ca38875859506e0b95eafc692b1f5ffd57cd52
---

# Ace Adsdisconnect

AdsDisconnect

AdsDisconnect

Advantage Client Engine

| AdsDisconnect  Advantage Client Engine |  |  |  |  |

Disconnects the connection associated with the given connection handle

Syntax

| UNSIGNED32 | AdsDisconnect (ADSHANDLE hConnect); |

Parameters

| hConnect (I) | Handle of server to disconnect. |

Remarks

AdsDisconnect is used to disconnect a connection from the specified server. If tables are currently opened, all data is flushed, locks are released, and open tables are closed before the disconnect occurs.

If zero is passed as the connection handle, all connections on the server associated with the user will be disconnected.

If AdsDisconnect is called on a connection with a transaction active, the transaction will be rolled back.

Example

[Click Here](ace_examples.md#adsdisconnectexample)

See Also

[AdsConnect](ace_adsconnect.md)

[AdsOpenTable](ace_adsopentable.md)
