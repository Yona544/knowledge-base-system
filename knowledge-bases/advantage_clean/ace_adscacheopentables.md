---
title: Ace Adscacheopentables
slug: ace_adscacheopentables
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscacheopentables.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f6bdee0ce3b21abe9d0148c831dffc015a77b88c
---

# Ace Adscacheopentables

AdsCacheOpenTables

AdsCacheOpenTables

Advantage Client Engine

| AdsCacheOpenTables  Advantage Client Engine |  |  |  |  |

Provides caching of open tables

Syntax

| UNSIGNED32 | AdsCacheOpenTables (UNSIGNED16 usOpen); |

Parameters

| usOpen (I) | Number of tables to cache. |

Remarks

AdsCacheOpenTables allows table closes to be cached in order for subsequent opens to occur faster. A call to [AdsCloseTable](ace_adsclosetable.md) with the table cache greater than zero results in the table appearing closed to an application, but still open on the Advantage server. A subsequent [AdsOpenTable](ace_adsopentable.md) call will return very quickly because the server already has the table open. However, if the access rights for an [AdsOpenTable](ace_adsopentable.md) on a cached table are different than those with which it was originally opened, the Advantage Client Engine will close the table and reopen it with the changed access rights.

Call this function if an application performs multiple opens and closes on the same table. If an application opens tables and leaves them open, AdsCacheOpenTables provides no additional value.

AdsCacheOpenTables is a global setting that affects the behavior of the entire application. The default number of open tables that are cached is 0.

Example

[Click Here](ace_examples.md#adscacheopentablesexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCloseTable](ace_adsclosetable.md)

[AdsCloseCachedTables](ace_adsclosecachedtables.md)
