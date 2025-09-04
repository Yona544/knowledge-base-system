---
title: Ade Dateformat Tadsconnection
slug: ade_dateformat_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_dateformat_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f48d87595809f091d3d17b5bc41033912db88bde
---

# Ade Dateformat Tadsconnection

DateFormat

TAdsConnection.DateFormat

Advantage TDataSet Descendant

| TAdsConnection.DateFormat  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the date format for this Connection. The date format must contain two or more occurrences of the letters D, M, and Y respectively (e.g., "MM-DD-YYYY"). If specified, the DateFormat will mask the DateFormat specified by the AdsSettings component, if present.  By default, the DateFormat is blank, allowing the setting in the AdsSettings component to be used.

Syntax

property DateFormat: String;

Description

The DateFormat setting affects this individual connection.  The Connection-level DateFormat provides a means of specifying the Date Format without the use of an AdsSettings component, and can provide finer control of the setting.

This setting affects how the Advantage Database Server interprets all date strings for tables and queries opened on this connection. It also defines how all dates are passed back to the calling application. DateFormat can also be used to specify separators in the date format. For example, "DD/MM/YYYY" and "DD-MM-YYYY" are both valid date formats.

The DateFormat setting may be changed to a valid date format regardless of whether the component has an active connection.  Clearing the DateFormat (or setting it to an empty string) may only be done when IsConnected is false.
