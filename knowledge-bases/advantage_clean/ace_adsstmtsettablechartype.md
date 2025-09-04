---
title: Ace Adsstmtsettablechartype
slug: ace_adsstmtsettablechartype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtsettablechartype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8b6bd27002edcc9ffa95fde4e7720551ae04a931
---

# Ace Adsstmtsettablechartype

AdsStmtSetTableCharType

AdsStmtSetTableCharType

Advantage Client Engine

| AdsStmtSetTableCharType  Advantage Client Engine |  |  |  |  |

Sets the type of character data used in rowsets

Syntax

| UNSIGNED32 | AdsStmtSetTableCharType( ADSHANDLE hStatement,  UNSIGNED16 usCharType ) |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |
| usCharType (I) | Type of character data used in returned rowsets. Options are ADS\_ANSI and ADS\_OEM, or one of the [dynamic collations](master_collation_support.md) such as GENERAL\_VFP\_CI\_AS\_1252. This indicates the type of character data to be used in the rowset. For compatibility with DOS-based CA-Clipper applications, ADS\_OEM should be specified. |

Remarks

The default value for newly created statement handles is ADS\_ANSI.

If the statement handle was created on a database connection), this setting is ignored when accessing the database tables). The usCharType is obeyed on the free tables.

If the statement handle was created on a free connection), the usCharType setting is always obeyed.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.md) before calling this API.

Example

[Click Here](ace_more_examples.md#adsstmtsettablechartypeexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.md)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.md)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.md)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.md)

[AdsStmtSetTableType](ace_adsstmtsettabletype.md)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.md)
