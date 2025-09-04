---
title: Ace Adsgetlasterror
slug: ace_adsgetlasterror
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetlasterror.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 795cfffc9a9a326091989714fb71b65fcfabdd3e
---

# Ace Adsgetlasterror

AdsGetLastError

AdsGetLastError

Advantage Client Engine

| AdsGetLastError  Advantage Client Engine |  |  |  |  |

Retrieves the result of the last Advantage Client Engine function call

Syntax

| UNSIGNED32 | AdsGetLastError (UNSIGNED32 \*pulErrCode,  UNSIGNED8 \*pucBuf,  UNSIGNED16 \*pusBufLen); |

Parameters

| pulErrCode (O) | Returns the error code of the last error. |
| pucBuf (O) | Returns the error string corresponding to pulErrCode. It will be similar to the string return by AdsGetErrorString but may have information specific to the error instance, such as table names. |
| pusBufLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

The error code returned by this function will be the same as the one returned by the last Advantage Client Engine function call. The first action of each Advantage Client Engine function is to clear the previous error if there is one. Thus, a call to AdsGetLastError is valid only for the most recent function call as opposed to the most recently occurring error. If no error occured on the last Advantage Client Engine function call, AE\_SUCCESS is returned in pulErrCode.

Example

[Click Here](ace_examples.md#adsgetlasterrorexample)

See Also

[AdsGetErrorString](ace_adsgeterrorstring.md)

[AdsShowError](ace_adsshowerror.md)
