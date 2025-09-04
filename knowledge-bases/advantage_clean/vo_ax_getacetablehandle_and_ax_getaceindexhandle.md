---
title: Vo Ax Getacetablehandle And Ax Getaceindexhandle
slug: vo_ax_getacetablehandle_and_ax_getaceindexhandle
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_getacetablehandle_and_ax_getaceindexhandle.htm
source: Advantage CHM
tags:
  - vo
checksum: 8824b42f1d7ece09b06a5eb550516b47b036c88f
---

# Vo Ax Getacetablehandle And Ax Getaceindexhandle

AX\_GetAceTableHandle and AX\_GetAceIndexHandle

AX\_GetAceTableHandle and AX\_GetAceIndexHandle

Advantage AXSQL RDDs

| AX\_GetAceTableHandle and AX\_GetAceIndexHandle  Advantage AXSQL RDDs |  |  |  |  |

With the AXSQL RDDs the AX\_GetAceTableHandle and AX\_GetAceIndexHandle utility functions still work. The AX\_GetAceTableHandle function will return the cursor handle of the result set. In most ways a cursor handle is just like a normal ACE table handle.

The AX\_GetAceIndexHandle function will return the index handle of the cursor if one is available. Typically an index handle will only be available with the AXSQL RDDs if the query had an ORDER BY specified. An index handle would also be available if an index order was created on a result set after it was instantiated.
