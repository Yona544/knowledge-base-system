---
title: Ace Adsgethandlelong
slug: ace_adsgethandlelong
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgethandlelong.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 1ec765dd781ccd8e4d8de0381e4d001d22ba8cf7
---

# Ace Adsgethandlelong

AdsGetHandleLong

AdsGetHandleLong

Advantage Client Engine

| AdsGetHandleLong  Advantage Client Engine |  |  |  |  |

Returns the long value for this handle set with a call to [AdsSetHandleLong](ace_adssethandlelong.md).

Syntax

| UNSIGNED32 | AdsGetHandleLong (ADSHANDLE hObj,  UNSIGNED32 \*pulValue); |

Parameters

| hObj (I) | Handle of a connection, table, cursor, or an index order. |
| pulValue (O) | Returns the value that has been set for this handle. |

Remarks

Returns the value set for this handle in a previous call to AdsSetHandleLong. This function allows one value to be stored for this handle. The value stored is at the users discretion. The Advantage Client Engine does not use the value for any operation, but simply stores it. The value is readable as long as the handle is valid.

If a value for this handle has not been set, the function returns AE\_INVALID\_HANDLE.

Example

[Click Here](ace_examples.md#adsgethandlelongexample)

See Also

[AdsSetHandleLong](ace_adssethandlelong.md)
