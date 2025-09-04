---
title: Ace Adsgethandletype
slug: ace_adsgethandletype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgethandletype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 777c4074e81f40dff5ed74f48cdd85108e2f2f17
---

# Ace Adsgethandletype

AdsGetHandleType

AdsGetHandleType

Advantage Client Engine

| AdsGetHandleType  Advantage Client Engine |  |  |  |  |

Returns the type of a given Advantage Client Engine handle.

Syntax

| UNSIGNED32 | AdsGetHandleType (ADSHANDLE hObj,  UNSIGNED16 \*pusType); |

Parameters

| hObj (I) | Handle of an Advantage Client Engine object. |
| pusType ( O ) | Type of the Advantage Client Engine handle. |

Remarks

Possible types returned are ADS\_TABLE for table handles, ADS\_CONNECTION for connection handles, ADS\_INDEX\_ORDER for index order handles, ADS\_FTS\_INDEX\_ORDER for full text search index order handles, ADS\_CURSOR for cursor handles, ADS\_SQL\_STATEMENT for statement handles, ADS\_DATABASE\_CONNECTION for data dictionary connections, and ADS\_SYS\_ADMIN\_CONNECTION for system administrator (adssys) data dictionary connections.

Example

None.

See Also

[AdsFindConnection](ace_adsfindconnection.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)

[AdsGetIndexHandle](ace_adsgetindexhandle.md)

[AdsGetIndexHandleByOrder](ace_adsgetindexhandlebyorder.md)
