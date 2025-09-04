---
title: Ace Adsgettablecollation
slug: ace_adsgettablecollation
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettablecollation.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a671f056b617aff4220cbc81bcb4d4bdba74ff89
---

# Ace Adsgettablecollation

AdsGetTableCollation

AdsGetTableCollation

Advantage Client Engine

| AdsGetTableCollation  Advantage Client Engine |  |  |  |  |

Gets the collation language that the table was opened or created with.

Syntax

| UNSIGNED32 | AdsGetTableCollation ( ADSHANDLE hConnect,                        UNSIGNED8 \*pucCollation,                        UNSIGNED16 \*pusLen ); |

Parameters

| hTbl (I) | Handle of table or cursor. |
| pucCollation (O) | Return the collation language in this buffer. See [dynamic collation support](master_collation_support.md). |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetTableCollation gets the collation language that the table was opened or created with. If no collation language was specified when the table was opened or created, AdsGetTableCollation returns an empty string.

Example

ulRetCode = AdsOpenTable90( 0, "D:\\data\\customers.dbf", "customers", ADS\_VFP,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_IGNORERIGHTS, ADS\_DEFAULT, "GERMAN\_VFP\_CI\_AS\_1252", &hTable );

usLen = sizeof( aucCollation );

ulRetCode = AdsGetTableCollation( hTable, aucCollation, &usLen );

See Also

[AdsGetIndexCollation](ace_adsgetindexcollation.md)

[AdsSetCollation](ace_adssetcollation.md)

[AdsGetCollation](ace_adsgetcollation.md)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.md)
