---
title: Master Sp Processreplicationqueues
slug: master_sp_processreplicationqueues
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_processreplicationqueues.htm
source: Advantage CHM
tags:
  - master
checksum: 4119444f4b2a84fc988ab1d4788964ea2b57f6d1
---

# Master Sp Processreplicationqueues

sp\_ProcessReplicationQueues

sp\_ProcessReplicationQueues

Advantage SQL Engine

| sp\_ProcessReplicationQueues  Advantage SQL Engine |  |  |  |  |

Causes Advantage to immediately process pending updates in the replication queue.

Syntax

sp\_ProcessReplicationQueues( ProcessOption, Integer )

Parameters

| ProcessOption (I) | This parameter specifies whether to process queues in the current connection or to process all known queues. If the value 1 is given, then only the replication queues in the current data dictionary are processed. If the value 2 is given, then all replication queues in all known dictionaries will be examined. |

Remarks

sp\_ProcessReplicationQueues provides the capability to cause replication processing to occur immediately. This is useful if there are pending updates that have not been processed because the target database was not available at the time the source update was made. If target databases are available when updates are made at the source database, the updates will generally be processed without delay. If the target is offline or some other error prevents replication from occurring, Advantage will periodically attempt to process the replication queues. If you do not want to wait for that to occur, you can execute this stored procedure to make Advantage to immediately attempt the processing.

This functionality is also available from Advantage Data Architect. If you right-click on the SUBSCRIPTIONS object of a data dictionary in the Connection Repository, you can choose the Process Replication Queues option to force processing of the queues.

For more information, see [Offline Targets](master_offline_targets_replication.md).

Example

EXECUTE PROCEDURE sp\_ProcessReplicationQueues( 1 )

See Also

[Sp\_CreateSubscription](master_sp_createsubscription.md)
