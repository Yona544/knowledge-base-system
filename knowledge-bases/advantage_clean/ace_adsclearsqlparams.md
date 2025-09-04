---
title: Ace Adsclearsqlparams
slug: ace_adsclearsqlparams
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclearsqlparams.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 862e03a76e7f7ca30e90cb7d22f6c21854424ef2
---

# Ace Adsclearsqlparams

AdsClearSQLParams

AdsClearSQLParams

Advantage Client Engine

| AdsClearSQLParams  Advantage Client Engine |  |  |  |  |

Clears out parameters on this statement previously set using the AdsSet\* APIs

Syntax

| UNSIGNED32 | AdsClearSQLParams( ADSHANDLE hStatement ) |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |

Remarks

Use AdsClearSQLParams to clear all values assigned to parameters and free their associated memory. If this function is not called, then parameter values will remain until the statement handle is closed. If the SQL statement text is changed via the [AdsPrepareSQL](ace_adspreparesql.md) function, then the old parameter values are assigned to the new statements parameters from left to right.

This method should be used to prevent the accidental use of old parameters with new statements and to free allocated resources. See [AdsPrepareSQL](ace_adspreparesql.md) for more details.

Example

[Click Here](ace_more_examples.md#adsclearsqlparamsexample)

See Also

[AdsPrepareSQL](ace_adspreparesql.md)
