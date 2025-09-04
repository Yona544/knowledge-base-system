---
title: Ace Adsstmtreadallcolumns
slug: ace_adsstmtreadallcolumns
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtreadallcolumns.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 27c67a29ba1ba5e0907d12469e3109c94056ebac
---

# Ace Adsstmtreadallcolumns

AdsStmtReadAllColumns

AdsStmtReadAllColumns

Advantage Client Engine

| AdsStmtReadAllColumns  Advantage Client Engine |  |  |  |  |

Enables or disables reading of all columns in live cursors resulting from SQL SELECT statements.

Syntax

UNSIGNED32 AdsStmtReadAllColumns( ADSHANDLE hStatement,

UNSIGNED16 usReadColumns );

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |
| usReadColumns (I) | Select field read setting. Valid options are ADS\_READ\_ALL\_COLUMNS and ADS\_READ\_SELECT\_COLUMNS. |

Remarks

The default value for newly created statement handles is ADS\_READ\_SELECT\_COLUMNS.

When a live cursor is generated from an SQL SELECT statement, the default behavior (ADS\_READ\_SELECT\_COLUMNS) is for the server to return only the data for columns specified in the SELECT statement to the client. This can be very beneficial especially on low bandwidth networks. If the value ADS\_READ\_ALL\_COLUMNS is specified, subsequent cursors generated from SELECT statements will have all data for all columns returned to the client.

When records in the table are locked (presumably for an edit operation), the entire record is sent from the server to the client so that the update operation can maintain the consistency of all indexes.

This setting only applies to live cursors produced by the Advantage Database Server (client/server). This setting does not apply to Advantage Local Server; there is no efficiency gain because the processing is all performed at the client. Also note that static cursors generated from SELECT statements have only the selected column data in the table by definition, so this setting does not apply to static cursors.
