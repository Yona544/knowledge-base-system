---
title: Ace Adsgetdateformat60
slug: ace_adsgetdateformat60
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetdateformat60.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7b39b08d026cb5398e7e81cbce47b2b266c8e71b
---

# Ace Adsgetdateformat60

AdsGetDateFormat60

AdsGetDateFormat60

Advantage Client Engine

| AdsGetDateFormat60  Advantage Client Engine |  |  |  |  |

Retrieves the current date format for a given connection.

Syntax

| UNSIGNED32 | AdsGetDateFormat60( ADSHANDLE hConn,  UNSIGNED8 \*pucFormat,  UNSIGNED16 \*pusLen ); |

Parameters

| hConn (I) | Connection to retrieve the date format from. If this is 0, it is the same as calling AdsGetDateFormat. |
| pucFormat (O) | Contains the returned date format string. |
| pusLen (I/O) | Length of the buffer on input, amount of data stored on output. |

Remarks

AdsGetDateFormat60 returns the current date format for the given connection.

See Also

[AdsGetDateFormat](ace_adsgetdateformat.md)

[AdsSetDateFormat60](ace_adssetdateformat60.md)
