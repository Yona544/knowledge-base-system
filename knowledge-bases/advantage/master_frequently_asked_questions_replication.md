Frequently Asked Questions




Advantage Database Server 12  

Replication: Frequently Asked Questions

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Replication: Frequently Asked Questions  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Replication: Frequently Asked Questions Advantage Concepts master\_Frequently\_asked\_questions\_replication Advantage Concepts > Advantage Functionality > Replication > Frequently Asked Questions / Dear Support Staff, |  |
| Replication: Frequently Asked Questions  Advantage Concepts |  |  |  |  |

Why isnt my data being replicated?

|  |  |
| --- | --- |
| · | Check the error log (ads\_err.adt). Replication occurs behind the scenes from the perspective of client applications. Replication failures will not affect a client application. Therefore, it is necessary to check the error log for replication failures. The error class for replication is 7600. Look at the specific error number and at the More\_Info field for more detailed information about failures. Beginning with v10.10.0.6, some of the same information that is in the error log is also written directly to the replication queue itself. See [Advantage Error Log and Replication](master_advantage_error_log_and_replication.htm) for more information. |

|  |  |
| --- | --- |
| · | Make sure that Advantage Database Server was able to load the Advantage Client Engine. Search the error log for error codes 8044 and 8045. Advantage will log an 8044 error if it is not able to dynamically load the Advantage Client Engine library and an 8045 error if it failed to find all required entry point functions. |

|  |  |
| --- | --- |
| · | Verify that Advantage Database Server is running at the target. Once it is running, it can take up to an hour before the source will attempt to connect again unless another update is made at the source. |

|  |  |
| --- | --- |
| · | Open the replication queue (it is an Advantage table with the name of the subscription prefixed by two underscores). If there are records in the replication queue, record updates are being queued for replication. Refresh the table to see if any records are being removed. If so, the queue is currently being processed. If not, something is preventing the updates from being distributed to the target. If the replication queue is empty and no replication updates have occurred, replication is not being attempted. Check the following bullets. |

|  |  |
| --- | --- |
| · | Check the publication information. Make sure the table is included in the publication used by the subscription. If there is a filter on the table, verify that it is correct. |

|  |  |
| --- | --- |
| · | Check the subscription information. Make sure the target database path and login credentials are correct. If they are not, it will result in 7600 errors being logged to the error log. |

|  |  |
| --- | --- |
| · | Verify that the subscription is enabled. |

|  |  |
| --- | --- |
| · | Verify that Advantage Database Server is licensed for replication. Replication requires a separate validation code to enable it. Contact your Advantage sales representative for more information. It is possible to define publications and subscriptions, but no replication will occur without a valid replication validation code. |

|  |  |
| --- | --- |
| · | Verify that you are using Advantage Database Server. Replication is not supported with Advantage Local Server. |

|  |  |
| --- | --- |
| · | If the top record in the replication queue cannot be replicated, then you need to manually delete it or set the "Ignore Replication Failures" option in the subscription. If you are deleting the entry and it is a transaction update (TxnID is non-empty), you will need to delete all entries for that transaction. |

|  |  |
| --- | --- |
| · | Was the table open (and never closed) when the subscription was created? A table is only marked for replication when it is first opened. |

How can I identify the target record of a failed update?

If a replication update fails, locate the entry in the error log (ads\_err.adt). Replication errors have error class 7600. The More\_Info field will contain the SQL statement of the failed update. It will also contain the subscription name, table name, and the EntryID (primary key) of the replication queue entry that failed. It also logs the physical record number of the source table. If you are using v10.10.0.6 or later, this same information may be in the replication queue itself. See [Advantage Error Log and Replication](master_advantage_error_log_and_replication.htm) for more information.

Note There is no guarantee that the record numbers match in the source and target.

Finally, if you have the subscription option enabled to log data with replication failures, the searchable field information will be logged with the failed SQL statement. This should help identify the record.

How is replication different from the online backup functionality?

While there are some conceptual similarities between replication and backup functionality, they are implemented with very different solutions in mind. The backup functionality is intended for making backups of your data for subsequent restore operations. Replication is used to keep two or more live databases logically consistent with each other.

|  |  |
| --- | --- |
| · | Replication sends updates to another usable live database. Backup sends the data to a backup location that is not intended to be accessed directly by an Advantage application. |

|  |  |
| --- | --- |
| · | Replication requires the target location to be running Advantage Database Server. Backup functionality does not. |

|  |  |
| --- | --- |
| · | Replication operates on an update-by-update basis. If the target database is online, the update is sent to the target immediately after the original update occurs. Backup functionality works on a request basis. Updated records are tracked by the backup functionality and then all processed when requested by a user application or by the backup scheduling utility. |

Why do connections still exist after I have disconnected my application?

Replication uses connection pooling for both internal connections and external connections to the target. The lifetime of the entries in the pool is approximately one minute. If the replication queue is empty, these connections should close automatically after a short time. If there are entries in the replication queue that are being processed, the connections will stay active until the queue is empty.

What happens if I restructure the replication queue?

It will cause replication failures. The replication queue is created with administrator privileges to prevent casual modifications. It may be necessary to remove entries from the replication queue at times, but you should not restructure the table. If the table has been corrupted beyond repair, it is possible to delete the physical replication queue file; Advantage will re-create the replication queue file on its next use.

What will happen if I delete the replication queue from the hard drive?

The replication queue is implemented as an Advantage ADT table. If you delete the physical table and there are unprocessed replication updates in it, those updates will not be replicated. If the table is empty, it will be created again the next time a replication update occurs.

Will replication cause performance degradation?

Some extra processing is required, but there should be very little performance degradation due to replication. When an update for a client application occurs, the update is stored in the replication queue. That is the primary cost of replication that may affect a user application. The bulk of the replication work is performed asynchronously by other threads and, thus, reduces the direct impact on existing applications.

What permissions are needed for replication to work?

No specific permissions are needed at the source database. All updates to replicated tables are replicated regardless of the permissions of the user making the update. The replication user (the username and password that are defined in the subscription) must have INSERT, UPDATE, and DELETE permissions at the target database in order to make the necessary updates (assuming that all of those operations can occur at the source). In addition, the replication user must have SELECT (READ) permissions on the identification columns at the target database in order to be able to locate the record that is to be updated.

Do the source and target tables need to be identical in format?

The names of the fields that are replicated must be the same in both the source and target tables. In addition, the types must be compatible. For example, you cannot replicate an integer field in the source to a text field in the target.

Beginning with version 8.1, however, it is no longer required that the source and target tables have identical structures. The target table can have a subset of the columns that are in the source table. For this to work, you must specify a vertical filter on the source table. You can specify the list of columns to include or exclude from replication. Define the vertical filter using Advantage Data Architect as part of the publication definition. You can also define a vertical filter programmatically with the Advantage Client Engine API AdsDDSetArticleProperty or through the stored procedure sp\_ModifyArticleProperty.

Does replication guarantee that source and target tables are always in sync?

No. Advantage replication simply distributes updates from the source database to the target database(s). If updates made to the target are not replicated to the source, the tables will be out of sync. Advantage replication does not perform any synchronization actions.

When two databases are replicating to one another, can one of them have its own set of triggers to do a task unique to that server?

Yes. Each database can have a unique set of CONFLICT triggers.

How long will it take after bringing up the target server before the replication updates occur?

If there are pending replication updates at the source database, it will periodically attempt to connect to the target server to perform the updates. The time between attempts varies up to one hour but will occur immediately if an update is made to the source.

Note If the source server has pending replication updates and has been shut down, it requires someone to log in to the database before replication will occur.

What happens if the target record is modified prior to a modification of the same record at the source?

It depends on the replication definition. For each table being replicated, you specify how the record is located (identified) at the target. You can choose to use all searchable (non-memo/blob) fields or specify some subset of fields (e.g., primary key). If you are choosing to use all fields to identify a row, then the replication update will fail because it will not be able to find the record. If you are using, for example, the primary key, then the update attempt will be able to find the record (assuming the primary key was not changed). If there is a CONFLICT trigger, then it will fire the trigger, and it is up to the trigger to make the decision about what to do. If there is no CONFLICT trigger, then the update will simply succeed and will overwrite the previous change.

How can I specify which part of my table to replicate?

You can control what data is replicated by defining both horizontal and vertical filters on a table. A horizontal filter is an expression equivalent to a WHERE clause in an SQL statement that defines whether or not a modified or new record will be replicated. A vertical filter defines which columns of the table will be replicated.