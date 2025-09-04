---
title: Ace Adssetindexdirection
slug: ace_adssetindexdirection
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetindexdirection.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: cb1080f393c40da0dd13bd1325429556b6329adf
---

# Ace Adssetindexdirection

AdsSetIndexDirection

AdsSetIndexDirection

Advantage Client Engine

| AdsSetIndexDirection  Advantage Client Engine |  |  |  |  |

Reverses the DESCEND flag on an index.

Syntax

| UNSIGNED32 | AdsSetIndexDirection( ADSHANDLE hIndex,  UNSIGNED16 usReverseDirection ); |

Parameters

| hIndex (I) | Handle of index order. |
| usReverseDirection (I) | If FALSE (0) the original state of the DESCEND flag is restored. If TRUE (1) the DESCEND flag is flipped for the index. |

Remarks

The DESCEND flag of the index is flipped when usReverseDirection is TRUE. The index is then traversed in the opposite direction. Any scopes on the index must be reset because the top and bottom key have been reversed.

This option is not supported for ADS\_NTX indexes.

Example

ulRetCode = AdsSetIndexDirection( hIndex2, 1 );

See Also

[AdsSkip](ace_adsskip.md)

[AdsGetRecordCount](ace_adsgetrecordcount.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)

[AdsGotoBottom](ace_adsgotobottom.md)

[AdsGotoRecord](ace_adsgotorecord.md)

[AdsGotoTop](ace_adsgototop.md)

[AdsAtBOF](ace_adsatbof.md)

AdsAtEOF
