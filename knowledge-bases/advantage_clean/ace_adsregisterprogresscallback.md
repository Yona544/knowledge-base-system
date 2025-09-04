---
title: Ace Adsregisterprogresscallback
slug: ace_adsregisterprogresscallback
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsregisterprogresscallback.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: aae15e4d2976533240625dae50c2292587fc8e0a
---

# Ace Adsregisterprogresscallback

AdsRegisterProgressCallback

AdsRegisterProgressCallback

Advantage Client Engine

| AdsRegisterProgressCallback  Advantage Client Engine |  |  |  |  |

Provides a callback function that the Advantage Client Engine can call during long index operations.

Note This API still functions as before, but is now obsolete. It is suggested you use [AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.md) as it works better with threads and has more complete functionality.

Syntax

| UNSIGNED32 | AdsRegisterProgressCallback (UNSIGNED32(WINAPI \*lpfnCallback)  (UNSIGNED16 usPercent)); |

Parameters

| \*lpfnCallback (I) | Pointer to a function to be called during index builds. |
| usPercent (I) | The parameter usPercent will contain the percentage of the current operation that is complete. |

Remarks

AdsRegisterProgressCallback directs the Advantage Client Engine to call the given function during index builds or reindexing to give a measure of progress. A non-zero return value from the registered user function will cause the Advantage Client Engine to send an abort signal to the server to stop the current operation.

The Advantage Client Engine will call the registered callback function for the first time approximately two seconds after the server begins the operation it was registered for. The callback function will be called approximately every two seconds thereafter until the operation completes or is cancelled. At either of these points, one final call to the callback function is made with a value of 100 contained in usPercent.

The registered function should not make any Advantage Client Engine calls. If it does, it is possible to get error code 6619 "Communication Layer is busy".

This function will not be called if it goes out of scope. The Advantage Client Engine will verify that it is a valid function pointer before calling it. The Advantage Client Engine uses exception handling when calling the user-supplied function to trap errors that may occur.

Linux Note Linux users should not use the WINAPI declaration in the declaration of their callback function. In Linux your callback function should be of the form: UNSIGNED32 MyCallbackFunction( UNSIGNED16 usPercent ).

Example

[Click Here](ace_examples.md#adsregisterprogresscallbackexample)

See Also

[AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.md)

[AdsClearCallbackFunction](ace_adsclearcallbackfunction.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsReindex](ace_adsreindex.md)
