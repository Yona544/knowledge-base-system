---
title: Ace Adsclosealltables
slug: ace_adsclosealltables
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclosealltables.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 004f0e13e64d8cc31d8e3eaddef7d0eb3852bdc7
---

# Ace Adsclosealltables

AdsCloseAllTables

AdsCloseAllTables

Advantage Client Engine

| AdsCloseAllTables  Advantage Client Engine |  |  |  |  |

Closes all open tables in the application

Syntax

| UNSIGNED32 | AdsCloseAllTables (void); |

Parameters

None.

Remarks

AdsCloseAllTables will close ALL tables opened for the application. Any associated index or memo files will also be closed. The Advantage Client Engine will NOT disconnect from the server when all tables are closed, and settings specified by [AdsCacheOpenTables](ace_adscacheopentables.md) will be obeyed. Changes in the tables are flushed, and implicit locks are released.

Note Closing tables is illegal in a transaction. AdsCloseAllTables will return the error code AE\_ILLEGAL\_COMMAND\_DURING\_TRANS if any tables are in transactions, and those tables will not be closed. All tables that are not in transactions will be closed.

Example

[Click Here](ace_examples.md#adsclosealltablesexample)

See Also

[AdsCloseTable](ace_adsclosetable.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsCloseCachedTables](ace_adsclosecachedtables.md)
