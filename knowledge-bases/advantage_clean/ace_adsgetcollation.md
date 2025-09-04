---
title: Ace Adsgetcollation
slug: ace_adsgetcollation
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetcollation.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fe76bf64dc7ff3ee1a53d3f8356e7a4d5e660df9
---

# Ace Adsgetcollation

AdsGetCollation

AdsGetCollation

Advantage Client Engine

| AdsGetCollation  Advantage Client Engine |  |  |  |  |

Gets the collation language setting of a connection.

Syntax

| UNSIGNED32 | AdsGetCollation( ADSHANDLE hConnect,  UNSIGNED8 \*pucCollation,  UNSIGNED16 \*pusLen ); |

Parameters

| hConnect (I) | A connection handle. |
| pucCollation (O) | The collation language of the connection, or an empty string. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetCollation returns the collation language set on a connection. Initially, a connection has no collation set on it and AdsGetCollation will return an empty string. [AdsSetCollation](ace_adssetcollation.md) can be used to set the collation language. See [AdsSetCollation](ace_adssetcollation.md) for a description of when the collation language of a connection is used.

Example

usLen = sizeof( aucCollation );

ulRetCode = AdsGetCollation( hConnect, aucCollation, &usLen );

See Also

[AdsSetCollation](ace_adssetcollation.md)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.md)

[AdsGetTableCollation](ace_adsgettablecollation.md)

[AdsGetIndexCollation](ace_adsgetindexcollation.md)

[Dynamic Collation Support](master_collation_support.md).
