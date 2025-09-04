---
title: Ace Adsskipunique
slug: ace_adsskipunique
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsskipunique.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4ac6beeeb77025d403768d3c24434074be581134
---

# Ace Adsskipunique

AdsSkipUnique

AdsSkipUnique

Advantage Client Engine

| AdsSkipUnique  Advantage Client Engine |  |  |  |  |

Skips through an index only stopping on unique keys.

Syntax

| UNSIGNED32 | AdsSKipUnique ( ADSHANDLE hIndex,                 SIGNED32 lRecs ); |

Parameters

| hIndex (I) | Handle of index order. |
| lRecs (I) | Number of records to skip (can be negative). |

Remarks

Skips the given number of records (backward if lRecs is negative) only stopping on unqiue keys in the index. Scopes and filters are respected. A positive number means the skip will occur in logical index order to next unique key value. A negative number means the skip will approach the top of the table in logical order. AdsSkipUnique obeys all current filters and top and bottom scopes are observed.

Skipping one record may skip over many physical records because the Advantage server will filter records that do not meet current filter conditions.

Skipping forward beyond the last visible record results in the record number being set to the number of records in the table +1, and the EOF flag is set to True. Skipping negative past the first logical record sets BOF to True and sets the current record number to zero.

Skipping zero records will flush pending changes to disk but will not move in the index.

Example

ulRetCode = AdsSkipUnique( hIndex2, 1 );

See Also

[AdsSkip](ace_adsskip.md)

[AdsGetRecordCount](ace_adsgetrecordcount.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)

[AdsGotoBottom](ace_adsgotobottom.md)

[AdsGotoRecord](ace_adsgotorecord.md)

[AdsGotoTop](ace_adsgototop.md)

[AdsAtBOF](ace_adsatbof.md)

[AdsAtEOF](ace_adsateof.md)
