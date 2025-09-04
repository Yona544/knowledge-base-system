---
title: Ade Handle Tadsstoredproc
slug: ade_handle_tadsstoredproc
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_handle_tadsstoredproc.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c0aba582ddaff26993ffcff7cda1df128890182d
---

# Ade Handle Tadsstoredproc

Handle

TAdsStoredProc.Handle

Advantage TDataSet Descendant

| TAdsStoredProc.Handle  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.md)

Advantage Client Engine (ACE) handle to the cursor (if one exists) returned from procedure execution.

Syntax

property Handle: ADSHANDLE;

Description

Handle contains the Advantage Client Engine handle to the cursor returned from procedure execution. If the handle value is <= 0 it is not a valid handle, and should not be used. This will occur if the procedure does not return any parameters, if the procedure does not return a result set, or if the procedure is not currently active. Use the Handle property if it is necessary to directly call Advantage Client Engine API's.
