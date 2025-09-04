---
title: Master Newidstring
slug: master_newidstring_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_newidstring_.htm
source: Advantage CHM
tags:
  - master
checksum: 0cb70aa68e90a2f9977f37c26f8fcbdf6736becc
---

# Master Newidstring

NEWIDSTRING()

NEWID()

NEWIDSTRING()

Advantage Concepts

| NEWID()  NEWIDSTRING()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) functions that returns a GUID as either binary or string value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

NEWID () -> GUID

NEWIDSTRING ( <format> ) -> cGUIDString

Parameters

| <format> | A string specifying the format for the returned GUID. |
| M or MIME | A GUID encoded as a 24-byte string using MIME base64 encoding with the format of xxxxxxxxxxxxxxxxxxxxxxxx. Base64 encoded strings are case sensitive and should not be stored in case insensitive string fields. |
| F or File | A GUID encoded as a 22-byte string using File and URL Safe base64 encoding with the format of xxxxxxxxxxxxxxxxxxxxxx. Base64 encoded strings are case sensitive and should not be stored in case insensitive string fields. |
| N or Numbers | A GUID encoded as a 32-byte hexadecimal string value with a format of xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx. |
| D or Delimited | A GUID encoded as a 32-byte hexadecimal string with a format of xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. |
| B or Bracketed | A GUID encoded as a 32-byte hexadecimal string with a format of [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx]. |
| P or Parenthesis | A GUID encoded as a 32-byte hexadecimal string with a format of (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx). |
| C or Curlybraces | A GUID encoded as a 32-byte hexadecimal string with a format of {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}. |

Return Value

NEWID returns GUID in native format. NEWIDSTRING returns a string formatted GUID.

Remarks

NEWID returns a Globally Unique Identifier in 16-byte native format that may be specified as the default field value for a GUID field.

NEWIDSTRING() returns a Globally Unique Identifier (GUID) formatted as string.

GUIDs are spatially and temporally unique values.

Note When used in a navigational context (e.g., when setting a record filter), the format must be specified as a string (in quotes).  When used in SQL context, the format type is specified without quotes.

Examples

Navigational:

NEWID()

NEWIDSTRING( "NUMBERS" )

SQL:

SELECT NEWID() FROM system.iota;

 SELECT NEWIDSTRING(N) FROM system.iota;
