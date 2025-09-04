---
title: Ace Adsclosesqlstatement
slug: ace_adsclosesqlstatement
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclosesqlstatement.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a0278ebd84a03830130eaaa2beaf99f1307b8a09
---

# Ace Adsclosesqlstatement

AdsCloseSQLStatement

AdsCloseSQLStatement

Advantage Client Engine

| AdsCloseSQLStatement  Advantage Client Engine |  |  |  |  |

Releases memory associated with a statement handle

Syntax

| UNSIGNED32 | AdsCloseSQLStatement ( ADSHANDLE hStatement ) |

Parameters

| hStatement (I) | Handle of statement to free. |

Remarks

All statement resources are released. If tables were opened during generation of the rowset, they will be closed.

If a cursor associated with this statement exists it is freed as well.

To close a cursor without releasing the statement handle, use [AdsCloseTable](ace_adsclosetable.md) on the cursor handle.

Note The [AdsCacheOpenCursors](ace_adscacheopencursors.md) setting must be set to zero in conjunction with the AdsCloseSQLStatement in order for the cursor and underlying table to be truly closed. Use these functions only when necessary or else possible performance loss may occur. To close all cached tables without modifying AdsCacheOpenCursors, see the [AdsCloseCachedTables](ace_adsclosecachedtables.md) API.

Example

[Click Here](ace_more_examples.md#adsclosesqlstatementexample)

See Also

[AdsCreateSQLStatement](ace_adscreatesqlstatement.md)

[AdsCacheOpenCursors](ace_adscacheopencursors.md)

[AdsCloseCachedTables](ace_adsclosecachedtables.md)
