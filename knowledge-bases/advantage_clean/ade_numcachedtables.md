---
title: Ade Numcachedtables
slug: ade_numcachedtables
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_numcachedtables.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4419d4e958fc31a4e2059053e3ce6729a5965f5c
---

# Ade Numcachedtables

NumCachedTables

TAdsSettings.NumCachedTables

Advantage TDataSet Descendant

| TAdsSettings.NumCachedTables  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.md)

Provides caching of open tables.

Syntax

property NumCachedTables: ShortInteger;

Description

Advantage allows table closes to be cached in order for subsequent opens to occur more quickly. Setting NumCachedTables to a value greater than zero results in the table appearing closed to an application, but still open on the Advantage server. A subsequent open call will return very quickly because the server already has the table open. However, if the access rights for a table are different than those it was originally opened with, the Advantage Client Engine will close the table and reopen it with the changed access rights.

Set this property to a value greater than zero if an application performs many opens and closes on the same table. If an application opens tables and leaves them open, this function provides no additional value.

TAdsSettings.NumCachedTables is a global setting that affects the behavior of the entire application. The default number of open tables that are cached is 0.

See Also

[NumCachedCursors](ade_numcachedcursors.md)

[CloseCachedTables](ade_closecachedtables.md)
