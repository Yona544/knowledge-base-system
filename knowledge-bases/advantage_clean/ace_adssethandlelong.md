---
title: Ace Adssethandlelong
slug: ace_adssethandlelong
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssethandlelong.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c05d5140f4ca941056aabd0cdb9ce406472f4de3
---

# Ace Adssethandlelong

AdsSetHandleLong

AdsSetHandleLong

Advantage Client Engine

| AdsSetHandleLong  Advantage Client Engine |  |  |  |  |

Sets a long value for the given handle.

Syntax

| UNSIGNED32 | AdsSetHandleLong (ADSHANDLE hObj,  UNSIGNED32 ulValue); |

Parameters

| hObj (I) | Handle of a connection, table, cursor, or an index order. |
| ulValue (I) | The value to be set for the given handle. |

Remarks

Sets a long value that will be associated with the given handle and available to the user for the life of the handle. The value stored is at the users discretion. The Advantage Client Engine does not use the value for any operation, but simply stores it. If the value is a memory reference (e.g., a pointer to an application-specific structure), then the application is responsible for freeing the memory.

Example

[Click Here](ace_examples.md#adssethandlelongexample)

See Also

[AdsGetHandleLong](ace_adsgethandlelong.md)
