---
title: Master Hex2Char
slug: master_hex2char
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_hex2char.htm
source: Advantage CHM
tags:
  - master
checksum: d0ee7532a200aa8eff81062dec5441b026b62c0c
---

# Master Hex2Char

HEX2CHAR

HEX2CHAR()

Advantage Concepts

| HEX2CHAR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a binary value to a character string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

HEX2CHAR(<bBinary>) à cHexadecimal

Parameters

<bBinary>       The binary value to convert.

Return Values

HEX2CHAR() returns a binary value. If <cHexadecimal> is not a valid hexadecimal string, an error will be returned.

Remarks

HEX2CHAR() returns a character string representation of a binary value. Each byte of the binary value is represented as two hexadecimal characters.  Hexadecimal characters are the digits 0-9 and the uppercase letters A-F.

HEX2CHAR() is the inverse CHAR2HEX() of which converts a character string to a binary value.

The binary input can come from a field with a raw data type. Note variable length fields like binary fields are not supported by the Advantage Expression Engine.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[Functions to Convert Hexadecimal Values](master_functions_to_convert_hexadecim.md)

[String Functions](master_string_functions.md)

[CHAR2HEX()](master_char2hex.md)
