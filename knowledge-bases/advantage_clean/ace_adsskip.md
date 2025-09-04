---
title: Ace Adsskip
slug: ace_adsskip
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsskip.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 6eca15cf331705f5bdcb28f708a9e0063b720d2d
---

# Ace Adsskip

AdsSkip

AdsSkip

Advantage Client Engine

| AdsSkip  Advantage Client Engine |  |  |  |  |

Skips the given number of records

Syntax

| UNSIGNED32 | AdsSkip (ADSHANDLE hObj, SIGNED32 lRecs); |

Parameters

| hObj (I) | Handle of table, cursor, or index order. |
| lRecs (I) | Number of records to skip (can be negative). |

Remarks

Skips the given number of records (backward if lRecs is negative). If the handle is that of a table or cursor, then the movement is based on physical record ordering. If it is the handle of an index order, the movement uses that index order. Scopes and filters are respected. A positive number means the skip will occur toward the bottom of the table in natural order if a table or cursor handle is passed, and in logical index order if an index order handle is passed. A negative number means the skip will approach the top of the table in logical or natural order. AdsSkip obeys all current filters. When passing an index handle, top and bottom scopes are observed.

Skipping one record may skip over many physical records because the Advantage server will filter records that do not meet current filter conditions.

Skipping forward beyond the last visible record results in the record number being set to the number of records in the table +1, and the EOF flag is set to True. Skipping negative past the first logical record sets BOF to True and sets the current record number to zero.

Skipping zero records will flush pending changes to disk but will not move in the table or index.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

Example

[Click Here](ace_examples.md#adsskipexample)

See Also

[AdsGetRecordCount](ace_adsgetrecordcount.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)

[AdsGotoBottom](ace_adsgotobottom.md)

[AdsGotoRecord](ace_adsgotorecord.md)

[AdsGotoTop](ace_adsgototop.md)

[AdsAtBOF](ace_adsatbof.md)

[AdsAtEOF](ace_adsateof.md)
