---
title: Master Offline Targets Replication
slug: master_offline_targets_replication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_offline_targets_replication.htm
source: Advantage CHM
tags:
  - master
checksum: 72a661f62ba40c2b5fe448bc5547aa11806106b5
---

# Master Offline Targets Replication

Offline Targets

Offline Targets

Advantage Concepts

| Offline Targets  Advantage Concepts |  |  |  |  |

After a replication update is put into the replication queue, a thread will asynchronously attempt to send the update to the target. If the target is not available (e.g., Advantage Database Server is not running at the target, or no network is available to the target, etc.), then replication updates are stored in the replication queue until they can be processed.

Each update at the source will result in an attempt to process the replication queue and send the updates to the target. In addition, Advantage monitors the replication queues on a periodic basis. Advantage modifies the frequency with which it checks the replication queues. The interval between checks can vary between two minutes and one hour. If there are no updates to process, it gradually increases the interval.

If a replication queue has pending updates in it and Advantage Database Server is shut down at the source and then restarted, the pending updates will not be processed until someone connects to the data dictionary that has the pending updates. Advantage Database Server currently does not maintain any security information on the server that allows it to open an Advantage Data Dictionary. It must rely on a successful connection in order to gather the necessary authentication information to process replication queues.

To use Advantage to immediately begin processing the replication queue, call the system procedure [sp\_ProcessReplicationQueues](master_sp_processreplicationqueues.md). This can also be done with Advantage Data Architect. Right-click on the SUBSCRIPTIONS object of a data dictionary in the Connection Repository and choose the Process Replication Queues option.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.md)
