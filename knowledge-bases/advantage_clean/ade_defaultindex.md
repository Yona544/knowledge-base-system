---
title: Ade Defaultindex
slug: ade_defaultindex
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_defaultindex.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9490e954eec00eb575268593a53861ef0253bf62
---

# Ade Defaultindex

DefaultIndex

DefaultIndex

Advantage TDataSet Descendant

| DefaultIndex  Advantage TDataSet Descendant |  |  |  |  |

The data dictionary can store a default index for each table. The default index does not have to be the primary key, it can be any existing index. When new table objects are created (in Delphi, OLE DB, etc.) they will automatically be configured to use the default index from the data dictionary. If the default index is changed in the dictionary at a later time, all tables will automatically begin using the new default index.

For optimized performance, the default index is initially not set to reduce unneccessary index page reads.
