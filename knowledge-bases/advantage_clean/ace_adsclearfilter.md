---
title: Ace Adsclearfilter
slug: ace_adsclearfilter
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclearfilter.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5bdf1b3ee567b469373fea5aaf0bf4915c9ddd47
---

# Ace Adsclearfilter

AdsClearFilter

AdsClearFilter

Advantage Client Engine

| AdsClearFilter  Advantage Client Engine |  |  |  |  |

Clears the current filter expression in a given table

Syntax

| UNSIGNED32 | AdsClearFilter (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table or cursor. If there is a filter on the given table, remove it. If there is no filter, no action takes place. |

Special Return Codes

| AE\_NO\_FILTER | No filter can be cleared or retrieved because no filter was set. |

Remarks

AdsClearFilter will remove the current filter from the specified table, allowing records that previously had not passed the filter to become visible again.

Example

[Click Here](ace_examples.md#adsclearfilterexample)

See Also

[AdsGetFilter](ace_adsgetfilter.md)

[AdsSetFilter](ace_adssetfilter.md)
