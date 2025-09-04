---
title: Ace Adsclearprogresscallback
slug: ace_adsclearprogresscallback
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclearprogresscallback.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5f9044e926aa18bba5c0ca01dea0ead833e4a55b
---

# Ace Adsclearprogresscallback

AdsClearProgressCallback

AdsClearProgressCallback

Advantage Client Engine

| AdsClearProgressCallback  Advantage Client Engine |  |  |  |  |

Clears the progress callback registered using AdsRegisterProgressCallback.

Note This API still functions as before, but is now obsolete. It is suggested you use [AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.md) and [AdsClearCallbackFunction](ace_adsclearcallbackfunction.md) instead, as they work better with threads and have more complete functionality.

Syntax

| UNSIGNED32 | AdsClearProgressCallback (); |

Parameters

None.

Remarks

AdsClearProgressCallback will make the Advantage Client Engine stop calling the registered callback function. The progress callback is used to indicate progress while an Advantage server is building an index.

Example

[Click Here](ace_examples.md#adsclearprogresscallbackexample)

See Also

[AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.md)

[AdsClearCallbackFunction](ace_adsclearcallbackfunction.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsReindex](ace_adsreindex.md)
