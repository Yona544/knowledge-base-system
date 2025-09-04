---
title: Master Ttoc
slug: master_ttoc
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ttoc.htm
source: Advantage CHM
tags:
  - master
checksum: 1c83528a33a4aeaf930c20fa82faab62a8e0d3a2
---

# Master Ttoc

TTOC()

TTOC()

Advantage Concepts

| TTOC()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a timestamp value into a character string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

TTOC(<tTimeStamp>, <nFormat>) à cTimestamp

Parameters

<tTimestamp>  The timestamp value to format.

<nFormat> The format to be used for the timestamp value, [ 1 | 2 | 3 ] are the only formats currently supported.

Return Values

TTOC() returns a character string representation of a timestamp value. The function returns NULL if the parameter is a null date in an ADT table.

- Format 1 returns a character string of yyyymmddhhmmss.

- Format 2 returns only the time portion as hhmmss.

- Format 3 returns an XML DateTime format of yyyy-mm-ddThh:mm:ss.

Remarks

These functions are used to format a timestamp into a value suitable for concatenation with a character string.

See Also

[STOTS()](master_stots.md)
