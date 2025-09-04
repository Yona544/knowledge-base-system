---
title: Ace Adssetcollation
slug: ace_adssetcollation
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetcollation.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e09d0a1582757ffb84f5f03d268f4210a0375cb3
---

# Ace Adssetcollation

AdsSetCollation

AdsSetCollation

Advantage Client Engine

| AdsSetCollation  Advantage Client Engine |  |  |  |  |

Sets the collation language on a connection.

Syntax

| UNSIGNED32 | AdsSetCollation( ADSHANDLE hConnect,  UNSIGNED8 \*pucCollation ); |

Parameters

| hConnect (I) | A connection handle. |
| pucCollation (I) | The collation language to be set. See [dynamic collation support](master_collation_support.md). |

Remarks

AdsSetCollation sets the collation language for a specific connection handle. The collation language of a connection is used when ACE APIs which take a collation language (AdsOpenTable90, AdsCreateTable90, AdsDDAddTable90, and AdsRestructureTable90) are called without a collation language. It is also used with SQL statement handles which have not had a collation language set on them using AdsStmtSetTableCollation.

Note Collation languages passed to ACE APIs are only valid with ADS\_ADT or ADS\_VFP tables. The AdsSetCollation API will not affect ADS\_NTX and ADS\_CDX tables.

Example

ulRetCode = AdsSetCollation( hConnect, "GERMAN\_VFP\_CI\_AS\_1252" );

See Also

[AdsGetCollation](ace_adsgetcollation.md)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.md)

[AdsGetTableCollation](ace_adsgettablecollation.md)

[AdsGetIndexCollation](ace_adsgetindexcollation.md)

[Dynamic Collation Support](master_collation_support.md).
