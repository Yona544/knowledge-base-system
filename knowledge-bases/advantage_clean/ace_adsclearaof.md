---
title: Ace Adsclearaof
slug: ace_adsclearaof
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclearaof.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7f8a75a7f18109c96a3bb1afac6863b5076aa697
---

# Ace Adsclearaof

AdsClearAOF

AdsClearAOF

Advantage Client Engine

| AdsClearAOF  Advantage Client Engine |  |  |  |  |

Deactivates the AOF and releases all resources associated with it

Syntax

| UNSIGNED32 | AdsClearAOF ( ADSHANDLE hTable ); |

Parameters

| hTable (I) | Handle of a table or cursor with an AOF to clear. |

Special Return Codes

| AE\_NO\_FILTER | No filter can be cleared or retrieved because no filter was set. |

Remarks

The AdsClearAOF function deactivates the AOF and releases all resources associated with it on both the client and the server. Also note that when a table is closed, any AOF associated with it is automatically cleared as well.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example

[Click Here](ace_aof_and_encryption_examples.md#adsclearaof_example)

See Also

[AdsSetAOF](ace_adssetaof.md)
