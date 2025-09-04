---
title: Ace Adsgetnumopentables
slug: ace_adsgetnumopentables
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetnumopentables.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0faca87eca2436a52a5bf3ce20b082111df3680b
---

# Ace Adsgetnumopentables

AdsGetNumOpenTables

AdsGetNumOpenTables

Advantage Client Engine

| AdsGetNumOpenTables  Advantage Client Engine |  |  |  |  |

Retrieves the total number of open tables and cursors in this application

Syntax

| UNSIGNED32 | AdsGetNumOpenTables (UNSIGNED16 \*pusNum); |

Parameters

| pusNum (O) | Returns number of open tables and cursors. |

Remarks

AdsGetNumOpenTables will return the total number of open tables and cursors in the application.

Example

[Click Here](ace_examples.md#adsgetnumopentablesexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetAllTables](ace_adsgetalltables.md)
