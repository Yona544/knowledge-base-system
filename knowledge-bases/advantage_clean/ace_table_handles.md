---
title: Ace Table Handles
slug: ace_table_handles
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_table_handles.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: dadd4e06ac88577fa326250ceac5bdf8c0373fe0
---

# Ace Table Handles

Table Handles

Table Handles

Advantage Client Engine

| Table Handles  Advantage Client Engine |  |  |  |  |

Each table that is opened through the Advantage Client Engine via [AdsOpenTable](ace_adsopentable.md) or [AdsCreateTable](ace_adscreatetable.md) has an associated handle. This table handle is returned in the parameter list in each of these calls and must be passed to other API calls that operate on tables (e.g., [AdsSetString](ace_adssetstring.md)).

Table handles are generally equivalent to the work area concept. They are always associated with a connection handle, but with a zero sent to the Advantage Client Engine as a connection handle on the open or create, you need not store or worry about that connection handle. The most significant change with this implementation is that it requires the user to maintain these table handles to be able to pass them as parameters to the Advantage Client Engine API.

A table handle requires a work area resource on the server. The table handle encapsulates the core of Advantage Client Engine functionality, therefore, all data manipulation, table information, and natural order movement is based on the table handle. Index handles are also associated with a parent table handle. Table handles are invalid after calling [AdsCloseTable](ace_adsclosetable.md) or [AdsDisconnect](ace_adsdisconnect.md) for the connection on which the table is opened, or [AdsApplicationExit](ace_adsapplicationexit.md).
