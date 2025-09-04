---
title: Ace Adsgetindexcondition
slug: ace_adsgetindexcondition
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexcondition.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 80b29925f6a1e0a5062b774e0b94bdf12e92f077
---

# Ace Adsgetindexcondition

AdsGetIndexCondition

AdsGetIndexCondition

Advantage Client Engine

| AdsGetIndexCondition  Advantage Client Engine |  |  |  |  |

Retrieves the conditional index expression of this index order if one exists.

Syntax

| UNSIGNED32 | AdsGetIndexCondition (ADSHANDLE hIndex,  UNSIGNED8 \*pucExpr,  UNSIGNED16 \*pusLen); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pucExpr (O) | Return the expression in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

A conditional expression is a logical expression that filters the records placed in an index order. Only records that pass the conditional expression are in the index order. If records that do not pass the conditional expression are modified such that they pass the condition, a key is added to the index for that record. If an updated record no longer passes the condition, any associated key is removed from the index.

If no index condition exists, AdsGetIndexCondition will return an empty string.

Example

[Click Here](ace_examples.md#adsgetindexconditionexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)
