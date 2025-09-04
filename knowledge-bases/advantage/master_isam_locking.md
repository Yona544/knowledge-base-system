ISAM Locking




Advantage Database Server 12  

ISAM Locking

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ISAM Locking  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ISAM Locking Advantage Concepts master\_Isam\_locking Advantage Concepts > Advantage ISAM Concepts > ISAM Locking / Dear Support Staff, |  |
| ISAM Locking  Advantage Concepts |  |  |  |  |

Record locking allows a record to be updated in a table that is opened for Shared use in a multi-user environment. Before a record can be updated, it must first be locked. This will prevent any other user from updating that specific record, but that record can still be read by other users. Other users, at the same time, can obtain record locks on other records and update them concurrently with that first user's update of his record. A table lock locks an entire table, which allows the user who holds the table lock to update any record in the table while preventing all other users from being able to update or insert records in the table. Other users can still read the record/table while a record/table lock is in place. Keep in mind that use of table locks may cause multi-user performance degradation as other users wanting to perform updates and inserts will have to wait for the table lock to be released. With the Advantage TDataSet Descendant, record locking can be explicitly specified before updating a record or it can be implicitly done for you. If a record is explicitly locked, it must be explicitly unlocked. The converse is also true. If a record is implicitly locked, it will be implicitly unlocked for you after the record update is completed or a movement operation is performed. With other Advantage clients, such as the Advantage OLE DB Provider, record locking is implicitly done for you when a record is updated, deleted, or inserted. The implicitly locked record will be implicitly unlocked for you after the record update is completed or a movement operation is performed.

When a record is inserted or appended, a lock on that record is implicitly obtained for the user. Therefore, no explicit record locking is ever required when appending or inserting a record into the table.

If a client application should crash, the client computer should crash, or some other abnormal situation occur that causes an Advantage client application to disconnect, the Advantage Database Server will automatically release any locks held by that application once it has sensed that the application has abnormally disconnected. If a transaction was active, that transaction will be rolled back before the locks are released, however. This will keep the database in a known and stable state as well as allowing for optimal multi-user throughput even when a client abnormally disconnects.

Index file locking and memo file locking are always implicitly performed for the user. No special application logic is required to perform index file or memo file locking. Before an index is read, an implicit index "read" lock is obtained. Before an index is updated, an implicit index "write" lock is obtained. Before a memo file is updated, an implicit memo lock is obtained. For information on the intelligent lock management system used by the Advantage Database Server in order to increase application performance, see [Multi-User Performance](master_multi_user_performance.htm).

If a table is opened for Exclusive use, no locking is necessary because no other user can have the table, index files, or memo file open. If a lock operation is issued when the table is opened for Exclusive use, the operation is simply ignored.

Linux users, see [Lock Offset Configuration](master_lock_offset_configuration.htm) for system-specific locking notes.