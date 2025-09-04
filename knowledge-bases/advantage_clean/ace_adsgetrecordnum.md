---
title: Ace Adsgetrecordnum
slug: ace_adsgetrecordnum
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetrecordnum.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: dfd4272c14ab86c9a61d6dcb391b9720c79aea19
---

# Ace Adsgetrecordnum

AdsGetRecordNum

AdsGetRecordNum

Advantage Client Engine

| AdsGetRecordNum  Advantage Client Engine |  |  |  |  |

Retrieves the current record number

Syntax

| UNSIGNED32 | AdsGetRecordNum (ADSHANDLE hTable,  UNSIGNED16 usFilterOption,  UNSIGNED32 \*pulRec); |

Parameters

| hTable (I) | Handle of table or cursor. |
| usFilterOption (I) | Indicates if filters are to be respected (if they are set). Options are ADS\_RESPECTFILTERS and ADS\_IGNOREFILTERS. |
| pulRec (O) | Returns the current record number. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

Each physical record in a table has a record number. The first physical record is number 1. All records, even deleted ones (in DBF tables), have record numbers. The only way to change record numbers in a table is to perform an [AdsPackTable](ace_adspacktable.md).

If ADS\_IGNOREFILTERS is set, this function returns the current physical record. When ADS\_RESPECTFILTERS is indicated, the function performs a GotoTop on the table and counts until it reaches the current record.

See [AdsGetKeyNum](ace_adsgetkeynum.md) to retrieve logical record numbers based on index orders.

Note When used with ADS\_RESPECTFILTERS, this function may skip through every record in a table, and could be extremely slow. It is not recommended to use this function with ADS\_RESPECTFILTERS except on very small tables.

Example

[Click Here](ace_examples.md#adsgetrecordnumexample)

See Also

[AdsGotoRecord](ace_adsgotorecord.md)

[AdsGetRecordCount](ace_adsgetrecordcount.md)

[AdsGetKeyNum](ace_adsgetkeynum.md)
