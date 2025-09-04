---
title: Ace Adsgetindexcollation
slug: ace_adsgetindexcollation
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexcollation.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b9bb23417256a8977989c0962471a927063dd97f
---

# Ace Adsgetindexcollation

AdsGetIndexCollation

AdsGetIndexCollation

Advantage Client Engine

| AdsGetIndexCollation  Advantage Client Engine |  |  |  |  |

Gets the collation language that the index was created or opened with.

Syntax

| UNSIGNED32 | AdsGetIndexCollation ( ADSHANDLE hIndex,  UNSIGNED8 \*pucCollation,  UNSIGNED16 \*pusLen ); |

Parameters

| hIndex (I) | Handle of an index order. |
| pucCollation (O) | Return the collation language in this buffer. See [dynamic collation support](master_collation_support.md). |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetIndexCollation returns the collation language the index was created or opened with. When an index is opened or created, it inherits the collation language used by the table it belongs to.

Example

usLen = sizeof( aucCollation );

ulRetCode = AdsGetIndexCollation( hIndex, aucCollation, &usLen );

See Also

[AdsGetTableCollation](ace_adsgettablecollation.md)

[AdsSetCollation](ace_adssetcollation.md)

[AdsGetCollation](ace_adsgetcollation.md)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.md)
