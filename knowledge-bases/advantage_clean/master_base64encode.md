---
title: Master Base64Encode
slug: master_base64encode
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_base64encode.htm
source: Advantage CHM
tags:
  - master
checksum: 0e24f2deeeb3714a6c3e6d54b9e6ffab419dd529
---

# Master Base64Encode

BASE64ENCODE()

BASE64ENCODE()

Advantage Concepts

| BASE64ENCODE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a binary or string value to a Base64 representation.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

BASE64ENCODE(<bBinary> | <cString>) à cBase64

Parameters

<bBinary> | <cString>   The value to convert.

Return Values

BASE64ENCODE() returns a string value.

Remarks

BASE64ENCODE() returns a character string with the Base64 representation of the given value.

See Also

[Miscellaneous Functions](master_miscellaneous_functions.md)

[BASE64DECODE](master_base64decode.md)
