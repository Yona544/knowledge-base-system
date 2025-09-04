---
title: Master Referential Integrity And Replication
slug: master_referential_integrity_and_replication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_referential_integrity_and_replication.htm
source: Advantage CHM
tags:
  - master
checksum: 123098e98403a6e553a10936f1ec3b29f99fb323
---

# Master Referential Integrity And Replication

Referential Integrity and Replication

Referential Integrity and Replication

Advantage Concepts

| Referential Integrity and Replication  Advantage Concepts |  |  |  |  |

When replication is performed, referential integrity rules are enforced to maintain primary and foreign key relationships. However, cascade operations are not performed at the target; they are only performed at the source. If an RI cascade rule exists, all tables involved in the cascade operation should be replicated.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.md)
