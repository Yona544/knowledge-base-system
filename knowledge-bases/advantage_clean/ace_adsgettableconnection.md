---
title: Ace Adsgettableconnection
slug: ace_adsgettableconnection
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettableconnection.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: bd65f05bc3b7aefb49c8520639332e74ea42528f
---

# Ace Adsgettableconnection

AdsGetTableConnection

AdsGetTableConnection

Advantage Client Engine

| AdsGetTableConnection  Advantage Client Engine |  |  |  |  |

Returns the connection handle associated with a table handle.

Syntax

| UNSIGNED32 | AdsGetTableConnection (ADSHANDLE hTbl,  ADSHANDLE \*phConnect); |

Parameters

| hTbl (I) | Handle of table or cursor |
| phConnect (O) | Returned connection handle |

Remarks

AdsGetTableConnection returns the connection handle associated with a given table handle. This function can be used to extract a table handle from a table opened by calling [AdsOpenTable](ace_adsopentable.md) with a zero for the connection handle. Every table handle has an associated connection handle, no matter how the table handle was generated.

Example

None.

See Also

[AdsConnect](ace_adsconnect.md)

[AdsGetConnectionType](ace_adsgetconnectiontype.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)

[AdsOpenTable](ace_adsopentable.md)
