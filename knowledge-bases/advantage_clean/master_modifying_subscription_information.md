---
title: Master Modifying Subscription Information
slug: master_modifying_subscription_information
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_modifying_subscription_information.htm
source: Advantage CHM
tags:
  - master
checksum: d25b00c52802b890cb24e2d4b8f66364b3455129
---

# Master Modifying Subscription Information

Modifying Subscription Information

Modifying Subscription Information

Advantage Concepts

| Modifying Subscription Information  Advantage Concepts |  |  |  |  |

When modifying subscription and publication information for replication, the information will normally be refreshed at the server at the same time. However, if the subscription is in use, it is possible that cached information on the server cannot be refreshed. Therefore, for consistent results, it is best not to modify and create subscriptions while tables are actively being edited.

Note If a table is added to a subscription while that table is open, it will not start being replicated until all instances are closed and re-opened.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.md)
