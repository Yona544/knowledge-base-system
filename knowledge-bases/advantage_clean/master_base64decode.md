---
title: Master Base64Decode
slug: master_base64decode
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_base64decode.htm
source: Advantage CHM
tags:
  - master
checksum: c8b3d4423c2547b0378f5d7ef5ec28daf75dae60
---

# Master Base64Decode

BASE64DECODE

BASE64DECODE()

Advantage Concepts

| BASE64DECODE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a Base64 encoded value to the original value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

BASE64DECODE(<cBase64>) à bValue

Parameters

<cBase64>   The Base64 value to decode

Return Values

BASE64DECODE() returns a a binary value with the bytes representing the original encoded value.

Remarks

BASE64DECODE converts a string representation of a Base64 value into the original value and returns it as binary data. If the original value is a string, then the result value can be cast to the appropriate type (e.g., SQL\_VARCHAR or SQL\_WVARCHAR).

See Also

[Miscellaneous Functions](master_miscellaneous_functions.md)

[BASE64ENCODE](master_base64encode.md)
