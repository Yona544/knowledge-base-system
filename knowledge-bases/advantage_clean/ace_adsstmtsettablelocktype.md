---
title: Ace Adsstmtsettablelocktype
slug: ace_adsstmtsettablelocktype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtsettablelocktype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3590f60f0a1a247dcb8a4ab81d64274d896e77c1
---

# Ace Adsstmtsettablelocktype

AdsStmtSetTableLockType

AdsStmtSetTableLockType

Advantage Client Engine

| AdsStmtSetTableLockType  Advantage Client Engine |  |  |  |  |

Sets the locking type used by the statement handle

Syntax

| UNSIGNED32 | AdsStmtSetTableLockType( ADSHANDLE hStatement,  UNSIGNED16 usLockType ) |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |
| usLockType (I) | Type of locking to use. Options are ADS\_PROPRIETARY\_LOCKING and ADS\_COMPATIBLE\_LOCKING. If the application is to be used with non-Advantage applications, then ADS\_COMPATIBLE\_LOCKING should be used. If the table will be used only by Advantage applications, then ADS\_PROPRIETARY\_LOCKING should be used. See [Advantage Locking Modes](master_advantage_locking_modes.md) for more information. When ADS\_COMPATIBLE\_LOCKING is chosen, Advantage uses the appropriate style based on the table type. |

Remarks

The default value for newly created statement handles is ADS\_PROPRIETARY\_LOCKING.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.md) before calling this API.

Example

[Click Here](ace_more_examples.md#adsstmtsettablelocktypeexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.md)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.md)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.md)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.md)

[AdsStmtSetTableType](ace_adsstmtsettabletype.md)
