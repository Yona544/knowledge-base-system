---
title: Error 5195 Ae Subscription Queue Not Empty
slug: error_5195_ae_subscription_queue_not_empty
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5195_ae_subscription_queue_not_empty.htm
source: Advantage CHM
tags:
  - error
checksum: c81ac3b021a4924aaafda98835cb67e1d8bed2e1
---

# Error 5195 Ae Subscription Queue Not Empty

5195 AE\_SUBSCRIPTION\_QUEUE\_NOT\_EMPTY

5195 AE\_SUBSCRIPTION\_QUEUE\_NOT\_EMPTY

Advantage Error Guide

| 5195 AE\_SUBSCRIPTION\_QUEUE\_NOT\_EMPTY  Advantage Error Guide |  |  |  |  |

Problem: An attempt was made to delete or rename a replication subscription definition while the replication queue was not empty.

Solution: The replication queue must be empty in order to delete the subscription object from the data dictionary or to rename the replication queue. You must either wait for replication to complete, or you can physically delete the table from the hard drive if it is not currently open by Advantage. If this is not desirable to wait for replication to complete, you can open the replication queue and empty the table of records (the table name is the subscription name prefixed by two underscores). Note that if you perform either of these actions, the items that were in the queue will not be replicated.

Problem: An attempt was made to delete a table from a publication while the table had entries in a replication queue associated with that publication. This can happen if an attempt is made to remove the table from the dictionary.

Solution: The error text should indicate which replication queue contained entries for the table. You must wait for replication to complete for the pending entries. Verify that the replication target is online and that the subscription is not paused.
