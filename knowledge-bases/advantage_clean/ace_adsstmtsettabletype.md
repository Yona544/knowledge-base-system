---
title: Ace Adsstmtsettabletype
slug: ace_adsstmtsettabletype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtsettabletype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8e3361e50edf023d2b8452cb4d75690adb3eeb32
---

# Ace Adsstmtsettabletype

AdsStmtSetTableType

AdsStmtSetTableType

Advantage Client Engine

| AdsStmtSetTableType  Advantage Client Engine |  |  |  |  |

Sets the table type used by the statement handle

Syntax

| UNSIGNED32 | AdsStmtSetTableType( ADSHANDLE hStatement,  UNSIGNED16 usTableType ) |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |
| usTableType (I) | Type of table. Options are ADS\_CDX, ADS\_VFP, and ADS\_ADT. ADS\_NTX is a valid option on a statement handle created on a database connection). |

Remarks

The default value for newly created statement handles is ADS\_ADT.

If the statement handle was created on a database connection, the usTableType will affect the table created using the CREATE TABLE statement. It also determines the table type of free table(s)) that are used in the query.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.md) before calling this API.

Example

[Click Here](ace_more_examples.md#adsstmtsettabletypeexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.md)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.md)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.md)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.md)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.md)
