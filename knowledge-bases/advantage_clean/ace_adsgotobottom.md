---
title: Ace Adsgotobottom
slug: ace_adsgotobottom
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgotobottom.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 974ac7176034852d9bebc74101648f496fb1ee8b
---

# Ace Adsgotobottom

AdsGotoBottom

AdsGotoBottom

Advantage Client Engine

| AdsGotoBottom  Advantage Client Engine |  |  |  |  |

Positions the given table to the last record

Syntax

| UNSIGNED32 | AdsGotoBottom (ADSHANDLE hObj); |

Parameters

| hObj (I) | Handle of table, cursor, or index order. If hObj is the handle of a table, then it is positioned to the last physical record. If it is an index order handle, it is positioned to the last record of the index order. Filters and scopes are respected. |

Remarks

If the handle passed to AdsGotoBottom is a table handle or cursor, the table (or cursor) is positioned at the last record in natural order, obeying the current filter. If an index order handle is passed, the table is positioned at the last logical record in the order that passes both filters or scopes that are set.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

Example

[Click Here](ace_examples.md#adsgotobottomexample)

See Also

[AdsGotoTop](ace_adsgototop.md)

[AdsGotoRecord](ace_adsgotorecord.md)

[AdsGetRecordCount](ace_adsgetrecordcount.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)

[AdsSkip](ace_adsskip.md)
