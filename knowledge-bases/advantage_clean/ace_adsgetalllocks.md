---
title: Ace Adsgetalllocks
slug: ace_adsgetalllocks
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetalllocks.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e6d4b1aa2479811b8e05f96fbd92fe4a45433cc9
---

# Ace Adsgetalllocks

AdsGetAllLocks

AdsGetAllLocks

Advantage Client Engine

| AdsGetAllLocks  Advantage Client Engine |  |  |  |  |

Returns an array of records locked by the current user for the given table

Syntax

| UNSIGNED32 | AdsGetAllLocks (ADSHANDLE hTable,  UNSIGNED32 aulLocks[],  UNSIGNED16 \*pusArrayLen); |

Parameters

| hTable (I) | Handle of table or cursor. |
| aulLocks[] (O) | Return record locks in the given array. |
| pusArrayLen (I/O) | Number of entries (not bytes) in the array on input, number of returned entries on output. |

Remarks

After a successful call to AdsGetAllLocks, aulLocks will contain the record numbers of all records that are locked for the given hTable. It does not include record locks by other applications or from separate table handles to the same table in the same application. The locks returned will include both implicit and explicit locks. If the aulLocks parameter will not hold all current locks, the function will return as many locks as the array can hold, return the number of available locks in pusArrayLen, and return the error code AE\_INSUFFICIENT\_BUFFER.

Example

[Click Here](ace_examples.md#adsgetalllocksexample)

See Also

[AdsGetNumLocks](ace_adsgetnumlocks.md)

[AdsIsRecordLocked](ace_adsisrecordlocked.md)

[AdsLockRecord](ace_adslockrecord.md)
