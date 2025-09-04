---
title: Ace Adsstmtsettablereadonly
slug: ace_adsstmtsettablereadonly
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtsettablereadonly.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: df8ad41a7dd03ac25567f9943846a968fd590bce
---

# Ace Adsstmtsettablereadonly

AdsStmtSetTableReadOnly

AdsStmtSetTableReadOnly

Advantage Client Engine

| AdsStmtSetTableReadOnly  Advantage Client Engine |  |  |  |  |

Modifies the read-only flag associated with the statement handle

Syntax

| UNSIGNED32 | AdsStmtSetTableReadOnly( ADSHANDLE hStatement,  UNSIGNED16 usReadOnly ) |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |
| usReadOnly (I) | Mode to open the file. Options are ADS\_CURSOR\_READONLY and ADS\_CURSOR\_READWRITE. If ADS\_CURSOR\_READONLY is used then any future cursors resulting from an [AdsExecuteSQL](ace_adsexecutesql.md) statement will be read-only. If the value of ADS\_CURSOR\_READWRITE is used, then the resulting cursor may be used to update the rowset if a key-set cursor is possible. |

Remarks

The default value for newly created statement handles is ADS\_CURSOR\_READWRITE.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.md) before calling this API.

Example

[Click Here](ace_more_examples.md#adsstmtsettablereadonlyexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.md)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.md)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.md)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.md)

[AdsStmtSetTableType](ace_adsstmtsettabletype.md)
