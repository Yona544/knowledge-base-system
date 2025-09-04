---
title: Ade Indexcollationmismatch
slug: ade_indexcollationmismatch
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_indexcollationmismatch.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: fbe9cbddcaa8a716d9cf07862da466a9db5b4aa2
---

# Ade Indexcollationmismatch

IndexCollationMismatch

TAdsTable.IndexCollationMismatch

Advantage TDataSet Descendant

| TAdsTable.IndexCollationMismatch  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Defines the action to take when Advantage opens an index file that was created with a collation sequence that differs from the current collation sequence.

Syntax

TIndexCollationMismatchOptions = (icmError, icmIgnore, icmReindex);

 

property TAdsTable.IndexCollationMismatch;

Description

Beginning with version 6.2, Advantage stores a collation sequence identifier in the header of Advantage proprietary index (.ADI) files when it creates a new index file. When opening the index again, it can use that identifier to determine if the current collation sequence matches the one used to create the index. This property controls the action that Advantage takes when it detects a collation mismatch. A collation mismatch effectively causes the index file to be corrupt. For example, Advantage may not be able to find some keys because they may be sorted differently than they would be according to the current collation sequence.

The following values can be used:

| icmError | Causes Advantage to return a 5175 error when it encounters a collation mismatch. This is the default value. |
| icmIgnore | Causes Advantage to ignore the collation mismatch and continue to open the index. This option should only be used if the application plans to rebuild the index file. |
| icmReindex | Causes Advantage to attempt to automatically rebuild the index when it detects that the index was originally built with a different collation sequence. Advantage will be unable to rebuild the index if it has any index orders created with the ADS\_CUSTOM option (see AdsCreateIndex, AdsCreateIndex61). It is also not possible to rebuild the index if another user currently has the index open; this can happen when different clients use Advantage Local Server and each client has a different collation sequence. If Advantage is unable to rebuild the index, it will return error code 5175. It is important to note that if the use of this option does trigger an index rebuild, it can slow down the open of the index or table (when using auto-open indexes). For example, if an application is using Advantage Local Server with large tables across a network, an index rebuild may take a considerable amount of time. If any record locks are held by the application on the table that owns this index when this option triggers a reindex, Advantage will release those locks. |
