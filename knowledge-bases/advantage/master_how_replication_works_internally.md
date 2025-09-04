Replication - Behind the Scenes




Advantage Database Server 12  

Replication - Behind the Scenes

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Replication - Behind the Scenes  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Replication - Behind the Scenes Advantage Concepts master\_How\_replication\_works\_internally Advantage Concepts > Advantage Functionality > Replication > How Replication Works Internally / Dear Support Staff, |  |
| Replication - Behind the Scenes  Advantage Concepts |  |  |  |  |

Conceptually, replication is very simple. When a record in a replicated table is updated, the following operations occur as part of the processing of the regular record update.

|  |  |
| --- | --- |
| 1. | Compute a CRC of the original record data for conflict detection. |

|  |  |
| --- | --- |
| 2. | Evaluate the replication filter (if one exists) against the record. |

|  |  |
| --- | --- |
| 3. | If the record passes the filter or if there is no filter, place the record information in the replication queue along with the necessary original record data if it is needed for locating the target record. |

|  |  |
| --- | --- |
| 4. | Schedule a thread to process the replication queue. |

 

The previous steps are the cost that replication incurs directly on a client applications update. The subsequent processing that occurs to send the update to the target is performed asynchronously by other threads in the server. When a thread processes the replication queue, the following steps occur:

|  |  |
| --- | --- |
| 1. | Read the top entry in the replication queue. |

|  |  |
| --- | --- |
| 2. | Acquire a connection to the target server. |

|  |  |
| --- | --- |
| 3. | Construct a parameterized SQL statement. The statement will be an INSERT, UPDATE, or DELETE, based on the source operation. |

|  |  |
| --- | --- |
| 4. | Execute the SQL statement against the target. |

|  |  |
| --- | --- |
| 5. | If the statement is successful, remove the entry from the replication queue. |

 

Because the replication occurs at the row update level (as opposed to the SQL statement level), it is possible for a single SQL statement at the source to result in more than one SQL statement being issued against the target. For example, the statement "update sometable set somefield = somefield+1" will result one SQL statement being executed against the target for every record in the source.

The replication information is only read when a user connects to the database. The server does not have any mechanism to be able read the data dictionary; it must wait until a valid connection is made so it has the necessary information to be able to read the replication information. The primary ramification of this is that if Advantage Database Server is stopped while it has a non-empty replication queue, it cannot immediately start processing the queue when it is restarted. It will wait until someone connects to that data dictionary before the processing of the replication queue can resume.

See Also

[Connection Pooling Usage](master_connection_pooling_usage_replication.htm)

[Transactions and Replication](master_transactions_replication.htm)

[Referential Integrity and Replication](master_referential_integrity_and_replication.htm)

[Triggers and Replication](master_triggers_and_replication.htm)

[Forwarding and Loop Detection](master_forwarding_and_loop_detection_replication.htm)

[Offline Targets](master_offline_targets_replication.htm)

[Security](master_security.htm)

[Auto-Updating Fields](master_auto_updating_fields_replication.htm)

[Modifying Subscription Information](master_modifying_subscription_information.htm)

[Replication and Deleted Records](master_replication_and_deleted_records.htm)

[Advantage Error Log and Replication](master_advantage_error_log_and_replication.htm)

[Frequently Asked Questions](master_frequently_asked_questions_replication.htm)