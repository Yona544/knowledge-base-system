Referential Integrity and Replication




Advantage Database Server 12  

Referential Integrity and Replication

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Referential Integrity and Replication  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Referential Integrity and Replication Advantage Concepts master\_Referential\_integrity\_and\_replication Advantage Concepts > Advantage Functionality > Replication > Referential Integrity and Replication / Dear Support Staff, |  |
| Referential Integrity and Replication  Advantage Concepts |  |  |  |  |

When replication is performed, referential integrity rules are enforced to maintain primary and foreign key relationships. However, cascade operations are not performed at the target; they are only performed at the source. If an RI cascade rule exists, all tables involved in the cascade operation should be replicated.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.htm)