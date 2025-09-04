---
title: Ace Adsgetconnectionpath
slug: ace_adsgetconnectionpath
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetconnectionpath.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 41a670403cba87b0df922cde3add4396c4403289
---

# Ace Adsgetconnectionpath

AdsGetConnectionPath

AdsGetConnectionPath

Advantage Client Engine

| AdsGetConnectionPath  Advantage Client Engine |  |  |  |  |

Retrieves the connection path for the given connection.

Syntax

| UNSIGNED32 | AdsGetConnectionPath (ADSHANDLE hConnect,  UNSIGNED8 \*pucConnectionPath,  UNSIGNED16 \*pusLen); |

Parameters

| hConnect (I) | Handle of a connection. |
| pucFldName (O) | Return the connection path. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetConnectionPath is used to retrieve the connection path for the given connection handle. The connection path returned is the connection path given to Advantage when the connection was created.
