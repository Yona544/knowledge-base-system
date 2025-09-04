---
title: Ace Adsstmtconstrainupdates
slug: ace_adsstmtconstrainupdates
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtconstrainupdates.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8dbf92f1d523bdbdf21dcdcd86c1a63a874b9e38
---

# Ace Adsstmtconstrainupdates

AdsStmtConstrainUpdates

AdsStmtConstrainUpdates

Advantage Client Engine

| AdsStmtConstrainUpdates  Advantage Client Engine |  |  |  |  |

Sets constraint behavior for the statement handle

Syntax

| UNSIGNED32 | AdsStmtConstrainUpdates ( ADSHANDLE hStatement,  UNSIGNED16 usConstrain ) |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |
| usConstrain (I) | Constraint value to set. Options are ADS\_CONSTRAIN and ADS\_NO\_CONSTRAIN. |

Remarks

The default value for newly created statement handles is ADS\_NO\_CONSTRAIN.

If AdsStmtConstrainUpdates is called with a value of ADS\_CONSTRAIN the behavior of future cursors on this statement will change. Any row that is modified with the AdsSet functions (see [AdsCreateSQLStatement](ace_adscreatesqlstatement.md)) will undergo a WHERE clause verification on the server. If the row does not meet the WHERE clause that created the cursor, then the update will fail and an error will be returned. If the new row does meet the select criteria, then the update will occur normally.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.md) before calling this API.

Example

[Click Here](ace_more_examples.md#adsstmtconstrainupdatesexample)

See Also

None.
