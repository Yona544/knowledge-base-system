---
title: Ace Adsgetservername
slug: ace_adsgetservername
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetservername.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: ccad0a506b697271edcf0480b2aee2c0ae4ab026
---

# Ace Adsgetservername

AdsGetServerName

AdsGetServerName

Advantage Client Engine

| AdsGetServerName  Advantage Client Engine |  |  |  |  |

Retrieves the server name associated with a connection

Syntax

| UNSIGNED32 | AdsGetServerName (ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED16 \*pusLen); |

Parameters

| hConnect (I) | Valid connection handle. |
| pucName (O) | Return the server name in this buffer. |
| pusLen (I/O) | Length of buffer on input, length of name on output. |

Remarks

AdsGetServerName returns the name of the server on which the connected Advantage server is loaded. The server name will not include any volume or share information. If accessing data on a local drive and using Advantage Local Server, the drive letter is returned.

Example

[Click Here](ace_examples.md#adsgetservernameexample)

See Also

None.
