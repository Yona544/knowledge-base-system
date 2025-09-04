---
title: Ade Cachedupdates
slug: ade_cachedupdates
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_cachedupdates.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 5223f0f52f8969f39b4fd31fc8b49657d9ae5817
---

# Ade Cachedupdates

CachedUpdates

CachedUpdates

Advantage TDataSet Descendant

| CachedUpdates  Advantage TDataSet Descendant |  |  |  |  |

Cached updates enable you to retrieve data from a database, cache and edit it locally, and then apply the cached updates to the database as a unit. When cached updates are enabled, updates to a dataset (such as posting changes or deleting records) are stored in an internal cache instead of being written directly to the datasets underlying table. When changes are complete, your application calls a method that writes the cached changes to the database and clears the cache.

Below are the properties, methods, and events related to CachedUpdates that are NOT supported by the Advantage TDataSet Descendant.

| CachedUpdates | property |
| UpdateObject | property |
| UpdatesPending | property |
| UpdateRecordTypes | property |
| UpdateStatus | method |
| OnUpdateError | event |
| OnUpdateRecord | event |
| ApplyUpdates | method |
| CancelUpdates | method |
| CommitUpdates | method |
| FetchAll | method |
| RevertRecord | method |

In general, cached updates have two unique purposes. First, they provide a way for a pseudo transaction to take place by not applying the updates immediately to the database. This provides an "undo" functionality that would discard changes because they were cached local to the workstation. Second, they typically improve performance by controlling network traffic and timing the transactions to occur during noncritical times.

The Advantage Database Server provides transaction processing capability. With transaction processing, you can rollback or commit any changes that occurred inside a transaction. This will be similar to the ability provided with cached updates, yet more robust because the changed records will be locked during the transaction until a commit or rollback takes place. Another advantage is that it is a true transaction because the server is handling the commit. If anything happens during a commit, the entire transaction is rolled back. This is not the case when the cache is flushed with the cached update. If something happens during the update of the cached changes, the results will be indeterminate. Some may have been updated, and others not. For more information on the functionality of Advantage transactions see [Transaction Processing System](master_transaction_processing_system.md).

The Advantage Database Server, by nature, performs updates very quickly. Although Advantage does not support Cached Updates, network traffic is dramatically reduced when using the Advantage Database Server due to its client/server processing. Thus, the need to use Cached Updates to improve performance is eliminated when using the Advantage Database Server.

Transaction processing is available with the Advantage Database Server, but not the Advantage Local Server. Using the Advantage Local Server would require a developer to create a caching scheme to accomplish the functionality of a cached update.

An example is available on the Advantage Developer Zone (http://devzone.advantagedatabase.com), which shows how to implement CachedUpdates and how to update static cursors. The download file is called updatestatic.exe and can be found in the Delphi Tools download area.
