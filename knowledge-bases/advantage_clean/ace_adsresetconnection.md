---
title: Ace Adsresetconnection
slug: ace_adsresetconnection
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsresetconnection.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e28c0cd6d67b6bcc15744aae701637e80da93187
---

# Ace Adsresetconnection

AdsResetConnection

AdsResetConnection

Advantage Client Engine

| AdsResetConnection  Advantage Client Engine |  |  |  |  |

Resets a given connection.

Syntax

| UNSIGNED32 | AdsResetConnection (ADSHANDLE hConnect); |

Parameters

| hConnect (I) | Connection handle to reset. |

Remarks

AdsResetConnection resets a connection, (i.e., it closes all tables, indexes, SQL statements, unloads all stored procedure modules, and rolls back any uncommitted transactions.)
