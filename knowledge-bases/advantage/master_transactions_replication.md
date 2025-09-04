Transactions and Replication




Advantage Database Server 12  

Transactions and Replication

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Transactions and Replication  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Transactions and Replication Advantage Concepts master\_Transactions\_replication Advantage Concepts > Advantage Functionality > Replication > Transactions and Replication / Dear Support Staff, |  |
| Transactions and Replication  Advantage Concepts |  |  |  |  |

Transaction updates are processed only when the commit at the source happens (in other words, a transaction that is rolled back does not result in communication to the target database).

Replication respects transaction boundaries. When record updates are made outside of a transaction, the update information is immediately stored in the replication queue and will be processed shortly thereafter. Updates that are made inside transactions, however, are not placed in the replication queue until the commit is issued. When the updates of that transaction are replicated, they are performed inside a transaction at the target.

Once all updates in a transaction have been transmitted to the target, the transaction is committed at the target and the replication entries are removed from the queue. If any one update fails, or if the commit fails, the transaction is rolled back and the entries are not removed from the replication queue.

Note If an update of one record executes successfully but fails to update the record, then the behavior depends on the [Ignore Replication Failures](master_replication_options.htm#ignore_replication_failures) option. If it is set to ignore the failure, the error information will be logged and the remainder of the updates in the transaction will be processed. If the setting is set not to ignore the failure, the transaction will be rolled back at the target and the entries will not be removed from the replication queue.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.htm)