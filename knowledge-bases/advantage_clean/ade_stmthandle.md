---
title: Ade Stmthandle
slug: ade_stmthandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_stmthandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 7adb31fe408df114ab6f049a2ede9ba67fd0b765
---

# Ade Stmthandle

StmtHandle

TAdsStoredProc.StmtHandle

Advantage TDataSet Descendant

| TAdsStoredProc.StmtHandle  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.md)

Advantage Client Engine (ACE) statement handle for the stored procedure.

Syntax

property StmtHandle: ADSHANDLE;

Description

Retrieve StmtHandle if an application makes a direct call to the Advantage Client Engine, bypassing the methods of TAdsStoredProc. Some API calls require a statement handle as a parameter. Under all other circumstances an application does not need to access this property.
