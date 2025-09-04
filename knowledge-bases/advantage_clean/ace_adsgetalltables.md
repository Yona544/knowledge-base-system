---
title: Ace Adsgetalltables
slug: ace_adsgetalltables
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetalltables.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b8d19579793651cd09b24ca2810a0a52f2ec9d6a
---

# Ace Adsgetalltables

AdsGetAllTables

AdsGetAllTables

Advantage Client Engine

| AdsGetAllTables  Advantage Client Engine |  |  |  |  |

Returns an array of handles of all open tables and cursors

Syntax

| UNSIGNED32 | AdsGetAllTables (ADSHANDLE ahTable[],  UNSIGNED16 \*pusArrayLen); |

Parameters

| ahTable[] (O) | Returns table and cursor handles in the given array. |
| pusArrayLen (I/O) | Number of entries (not bytes) in the array on input, number of returned entries on output. |

Remarks

AdsGetAllTables will return the handles for all open tables and cursors. The handle array must be supplied with each element having room for a handle (not byte). If there are more handles than the array can hold, the array will be filled with the handles that fit, an error will be returned, and the number of open tables and cursors will be returned in the pusArrayLen parameter.

Example

[Click Here](ace_examples.md#adsgetalltablesexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetNumOpenTables](ace_adsgetnumopentables.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)
