---
title: Ace Adsstmtsettablecollation
slug: ace_adsstmtsettablecollation
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtsettablecollation.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 1dfb846894cc5b20593d64e2c197c30d8bbb36e7
---

# Ace Adsstmtsettablecollation

AdsStmtSetTableCollation

AdsStmtSetTableCollation

Advantage Client Engine

| AdsStmtSetTableCollation  Advantage Client Engine |  |  |  |  |

Sets the collation language used by the statement handle.

Syntax

| UNSIGNED32 | AdsStmtSetTableCollation ( ADSHANDLE hStatement,  UNSIGNED8 \*pucCollation ); |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |
| pucCollation (I) | The collation language to set on the statement handle. See [dynamic collation support](master_collation_support.md). |

Remarks

AdsStmtSetTableCollation sets the collation language used by a statement handle when creating or opening ADS\_ADT or ADS\_VFP tables. For all other table types, the statement collation language setting has no effect.

Example

ulRetCode = AdsConnect60( "D:\\data", ADS\_REMOTE\_SERVER, NULL, NULL, 0, &hConnect )

ulRetCode = AdsCreateSQLStatement( hConnect, &hStmt );

ulRetCode = AdsStmtSetTableCollation( hStmt, "GERMAN\_VFP\_CI\_AS\_1252" );

See Also

[AdsSetCollation](ace_adssetcollation.md)

[AdsGetCollation](ace_adsgetcollation.md)

[AdsGetTableCollation](ace_adsgettablecollation.md)

[AdsGetIndexCollation](ace_adsgetindexcollation.md)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.md)
