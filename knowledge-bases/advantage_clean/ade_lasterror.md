---
title: Ade Lasterror
slug: ade_lasterror
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_lasterror.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 356e9dfd7aed88fc75f962477366a575c5770b11
---

# Ade Lasterror

LastError

TAdsSettings.LastError

Advantage TDataSet Descendant

| TAdsSettings.LastError  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.md)

Holds the last error that was encountered with the Advantage Database Server.

Syntax

property LastError: LongInt;

Description

The error code in this property will be the same as the one returned by the last Advantage Database Server reported error. If no error occurred on the last Advantage Database Server call, 0 (zero) is returned.
