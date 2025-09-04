---
title: Ade Sessionname
slug: ade_sessionname
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_sessionname.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2e5d38c8aed5ff17c9e5b35666e8d2ee25bda781
---

# Ade Sessionname

SessionName

SessionName

Advantage TDataSet Descendant

| SessionName  Advantage TDataSet Descendant |  |  |  |  |

The Advantage TDataSet Descendant does not support the concept of a session, nor does it need one. With a BDE dataset, the applications database connections, drivers, cursors, queries, and so on, are maintained within the context of one or more BDE sessions. This provides the ability to cross the multi-threaded boundaries with a BDE dataset. In Advantage, no "session" is necessary in order for all connections, tables, and index handles to be available across all threads.
