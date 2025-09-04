Forwarding and Loop Detection




Advantage Database Server 12  

Forwarding and Loop Detection

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Forwarding and Loop Detection  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Forwarding and Loop Detection Advantage Concepts master\_Forwarding\_and\_loop\_detection\_replication Advantage Concepts > Advantage Functionality > Replication > Forwarding and Loop Detection / Dear Support Staff, |  |
| Forwarding and Loop Detection  Advantage Concepts |  |  |  |  |

When defining a subscription, you can choose to forward replication updates. The forwarding option controls whether or not a subscription at the target will distribute replication updates to its own target. In other words, suppose database A has a subscription to replicate to database B and that B replicates to database C:

A à B à C

An update that originates in database A will be sent on to C only if B has forwarding turned on.

In most situations, it is not necessary to turn on forwarding. For example, in a simple scenario where you want updates from A to be replicated to B and updates from B to be replicated to A, you should not turn on forwarding. Forwarding in that situation would create a replication loop, causing extra network communication and would result in replication errors being logged.

The following scenario defines a situation where a replication loop is possible:

A à B à C à A

In this case, A replicates to B, B replicates to C, and C replicates to A. If forwarding is turned on in all three databases, it would result in a replication loop. Advantage will detect the loop once an update reaches its source. The information for each replication update includes unique identifiers of all the databases that it "travels through". Once Advantage detects a loop, it ignores the update.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.htm)