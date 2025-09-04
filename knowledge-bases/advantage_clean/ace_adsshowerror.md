---
title: Ace Adsshowerror
slug: ace_adsshowerror
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsshowerror.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 12f735f25fdf5f13b4866dae08eda20abb96c0fb
---

# Ace Adsshowerror

AdsShowError

AdsShowError

Advantage Client Engine

| AdsShowError  Advantage Client Engine |  |  |  |  |

Displays a message box for the last error (if there was one)

Syntax

| UNSIGNED32 | AdsShowError (UNSIGNED8 \*pucTitle); |

Parameters

| pucTitle (I) | The title for the message box. Can be NULL. |

Remarks

AdsShowError will display a message box containing the last error message. The message displayed is identical to the error message available from [AdsGetErrorString](ace_adsgeterrorstring.md). This function is useful during development or debugging to view error messages immediately after the error occurred.

Example

[Click Here](ace_examples.md#adsshowerrorexample)

See Also

[AdsGetLastError](ace_adsgetlasterror.md)

[AdsGetErrorString](ace_adsgeterrorstring.md)
