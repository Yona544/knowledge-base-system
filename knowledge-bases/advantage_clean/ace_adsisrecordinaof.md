---
title: Ace Adsisrecordinaof
slug: ace_adsisrecordinaof
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisrecordinaof.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: aa2f1320e8c84c6a4bd8db52ad213e607f839fe7
---

# Ace Adsisrecordinaof

AdsIsRecordInAOF

AdsIsRecordInAOF

Advantage Client Engine

| AdsIsRecordInAOF  Advantage Client Engine |  |  |  |  |

Determine if a specific record is in an Advantage Optimized Filter (AOF).

Syntax

| UNSIGNED32 | AdsIsRecordInAOF (ADSHANDLE hTable,  UNSIGNED32 ulRecordNumber,  UNSIGNED16 \*pbIsInAOF ); |

Parameters

| hTable (I) | Handle of table or cursor with existing AOF. |
| ulRecordNumber (I) | Record number to check. If this is 0, then the current record number is checked. |
| \*pbIsInAOF (O) | Return True if the specified record number is in the AOF, False if not. |

Remarks

AdsIsRecordInAOF can be used to determine if an Advantage Optimized Filter (AOF) on the server contains a specific record. If the call is made while using [Advantage Local Server](master_advantage_local_server.md), the value returned by this API does not guarantee that the actual record value matches the AOF's view of that record. This is because another client could have updated the record and those changes would not be reflected in other clients' AOFs. Also, if an AOF is not fully optimized, it is possible for a record to be included in the AOF initially but not to pass the filter. Records that fit this description are dynamically removed from the filter as the records are read. A call to AdsIsRecordInAOF can indicate that a given record is in the AOF, but it is possible for that record to be filtered out when it is read. Therefore, this API is best used with fully optimized AOFs or with AOFs that have been created with the ADS\_RESOLVE\_IMMEDIATE option (see [AdsSetAOF](ace_adssetaof.md) ).

Example

[Click Here](ace_aof_and_encryption_examples.md#adsisrecordinaof_example)

See Also

[AdsSetAOF](ace_adssetaof.md)

[AdsGetAOFOptLevel](ace_adsgetaofoptlevel.md)

[AdsCustomizeAOF](ace_adscustomizeaof.md)
