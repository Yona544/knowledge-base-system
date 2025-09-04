---
title: Master Replication Scenarios
slug: master_replication_scenarios
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_replication_scenarios.htm
source: Advantage CHM
tags:
  - master
checksum: 67dc597277d5787f9287b39c4a1183e7b4bc40e2
---

# Master Replication Scenarios

Replication Scenarios

Replication Scenarios

Advantage Concepts

| Replication Scenarios  Advantage Concepts |  |  |  |  |

This section describes some typical scenarios in which replication might be used.

One-Way Replication

This is the simplest type of replication. The replication information (publication and subscription) is defined at a source database, and table modifications are replicated to a target database.

Two-Way Replication

Two-way replication is needed if you will be making independent changes at two databases that need to be kept equivalent. In this case, you need to define a publication and subscription in both databases. Both are source databases that will replicate to the other database. For this situation, you should not turn on forwarding in the subscription.

Note If modifications are made at the same time to the equivalent record in both databases, then it is possible for a replication failure to occur. It depends on the identification columns that you are using and whether or not you have CONFLICT triggers defined. If there are no CONFLICT triggers and the identification column(s) is the primary key, it is likely no replication failure will occur (assuming you are not modifying the primary key). In this case, the most recent update will win. If you have a CONFLICT trigger, the trigger will fire because the source and target records will not match. If you are using all columns as the set of identification columns for replication, the replication update will probably fail to locate the target record.

N-Way Replication

N-Way replication can be used if multiple databases are to be replicating to each other. The best way to use this is to treat it as a slightly more complex form of two-way replication. At each database (data dictionary), define a subscription to replicate the publication to each of the other databases. For this situation, you should not turn on forwarding in the subscription.

An alternative form of this might be to have a central database (hub) replicate to each of the other databases (spokes) and have each "spoke" database replicate only to the central "hub" database. In this case, you should turn on forwarding in each of the subscriptions at the hub if you want to replicate changes from each spoke database to each of the other spoke databases.

If the spoke databases contain subsets of the data, filters can be used at the central hub database to control which updates go to which spoke databases. And in this situation, it is unlikely that forwarding would be enabled at the central hub database.

See Also

[Replication Overview](master_replication_overview.md)
