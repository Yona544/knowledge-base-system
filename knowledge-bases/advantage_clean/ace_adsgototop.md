---
title: Ace Adsgototop
slug: ace_adsgototop
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgototop.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: cbb44c1b32ab6312820c53ff15e9f65d1478f528
---

# Ace Adsgototop

AdsGotoTop

AdsGotoTop

Advantage Client Engine

| AdsGotoTop  Advantage Client Engine |  |  |  |  |

Positions the given table to the first record

Syntax

| UNSIGNED32 | AdsGotoTop (ADSHANDLE hObj); |

Parameters

| hObj (I) | Handle of table, cursor, or index order. |

Remarks

If the handle given as hObj is the handle of a table or cursor, the table (or cursor) is positioned at the top of its natural order. The record on which it positions is the first record starting from record 1 (one) that satisfies current filter conditions. If the handle passed is an index order handle, the table is positioned at the top of the current logical order, obeying both current filters and scopes.

Example

[Click Here](ace_examples.md#adsgototopexample)

See Also

[AdsGotoBottom](ace_adsgotobottom.md)

[AdsGotoRecord](ace_adsgotorecord.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)

[AdsGetRecordCount](ace_adsgetrecordcount.md)

[AdsSkip](ace_adsskip.md)
