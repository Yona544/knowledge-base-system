---
title: Ace Adsgetsqlstatementhandle
slug: ace_adsgetsqlstatementhandle
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetsqlstatementhandle.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 1fff52338e404e3d5a1a7e7f3f256bcba3cab542
---

# Ace Adsgetsqlstatementhandle

AdsGetSQLStatementHandle

AdsGetSQLStatementHandle

Advantage Client Engine

| AdsGetSQLStatementHandle  Advantage Client Engine |  |  |  |  |

Returns the statement handle associated with the cursor handle passed in.

Syntax

UNSIGNED32 AdsGetSQLStatementHandle( ADSHANDLE hCursor,

ADSHANDLE \*phStmt );

Parameters

| hCursor (I) | Cursor handle to retrieve the statement handle from. |
| phStmt (O) | Handle of the statement that ownes hCursor. |

Remarks

Use AdsGetSQLStatementHandle to get the statement handle a cursor was executed on.

See Also

[AdsGetTableHandle](ace_adsgettablehandle.md)

[AdsGetIndexHandle](ace_adsgetindexhandle.md)
