---
title: Ace Adsclearsqlabortfunc
slug: ace_adsclearsqlabortfunc
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclearsqlabortfunc.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3dfa167f3441f628e489ad52179a1e22fe7ae04a
---

# Ace Adsclearsqlabortfunc

AdsClearSQLAbortFunc

AdsClearSQLAbortFunc

Advantage Client Engine

| AdsClearSQLAbortFunc  Advantage Client Engine |  |  |  |  |

Clears the SQL abort callback function registered using AdsRegisterSQLAbortFunc.

Note This API still functions as before, but is now obsolete. It is suggested that you use [AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.md) and [AdsClearCallbackFunction](ace_adsclearcallbackfunction.md) instead, as they work better with threads and have more complete functionality.

Syntax

UNSIGNED32 AdsClearSQLAbortFunc();

Parameters

None.

Remarks

AdsClearSQLAbortFunc will cause the Advantage Client Engine to stop calling the registered callback function. The SQL abort callback function is used to abort an SQL query.

See Also

[AdsRegisterSQLAbortFunc](ace_adsregistersqlabortfunc.md)
