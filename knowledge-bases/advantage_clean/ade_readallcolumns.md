---
title: Ade Readallcolumns
slug: ade_readallcolumns
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_readallcolumns.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9bfd4b1f119ab12fa9aae94c5f741ec136cbc55b
---

# Ade Readallcolumns

ReadAllColumns

TAdsQuery.ReadAllColumns

Advantage TDataSet Descendant

| TAdsQuery.ReadAllColumns  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Enables or disables reading of all columns in live cursors resulting from SQL SELECT statements.

Syntax

property ReadAllColumns: Boolean;

Description

This setting controls whether the Advantage Database Server sends data for all columns or for selected columns in a live cursor to the client. ReadAllColumns is False by default. When a live cursor is generated from an SQL SELECT statement, the default behavior is for the server to return only the data for columns specified in the SELECT statement to the client. This can be very beneficial especially on low bandwidth networks. If ReadAllColumns is set to True, subsequent cursors generated from SELECT statements will have all data for all columns returned to the client.

When records in the table are locked (presumably for an edit operation), the entire record is sent from the server to the client so that the update operation can maintain the consistency of all indexes.

This setting only applies to live cursors produced by the Advantage Database Server (client/server). This setting does not apply to Advantage Local Server; there is no efficiency gain because the processing is all performed at the client. Also note that static cursors generated from SELECT statements have only the selected column data in the table by definition, so this setting does not apply to static cursors.
