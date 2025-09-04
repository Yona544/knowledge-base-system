---
title: Master Getting Started With Replication
slug: master_getting_started_with_replication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_getting_started_with_replication.htm
source: Advantage CHM
tags:
  - master
checksum: 97c50cfbc4c1beeb11b00d6c4b0fa3ab1498e189
---

# Master Getting Started With Replication

Getting Started with Replication

Getting Started with Replication

Advantage Concepts

| Getting Started with Replication  Advantage Concepts |  |  |  |  |

To use replication, it is necessary to define the replication rules in the source data dictionary to which your application connects. The replication information needs to be defined only in the source data dictionary. It is not necessary to define any replication information at the target database unless you want to replicate changes to that database back to the source or to another location.

At the source data dictionary, define a [publication](master_replication_overview.md#publication_replication) and a [subscription](master_replication_overview.md#subscription_replication). The simplest way to do this is to use Advantage Data Architect. Open a data dictionary, right-click on PUBLICATIONS in the connection repository and choose Create. A wizard will take you through the steps of creating the publication. You choose how to identify rows at the target (either via primary key or by all searchable columns) and you choose which tables (articles) to include in the publication.

Once you have created a publication, create a subscription. Right-click on SUBSCRIPTIONS in the connection repository and choose Create. Specify the subscription name, the publication to replicate, the target database with username/password, and the path for the replication queue. When specifying the target database, include the full connection path with the target data dictionary name. You can specify it the same as you would any connection path in a client application (e.g., UNC or IP address and port). The username and password are used by Advantage Database Server to connect to the target data dictionary. The specified username should have the necessary privileges to make updates to the replicated tables.

At this point, you should be able to edit one of the source tables that you selected for replication, and the changes will be replicated.

Note A table is marked for replication only when it is first opened, so if a table was open when the subscription was created, it will not be replicated until all instances of the table are closed.

See Also

[Replication Overview](master_replication_overview.md)

[Replication Scenarios](master_replication_scenarios.md)

[Replication Options](master_replication_options.md)

[Frequently Asked Questions](master_frequently_asked_questions_replication.md)
