Advantage Proprietary Locking




Advantage Database Server 12  

Advantage Proprietary Locking

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Proprietary Locking  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage Proprietary Locking Advantage Concepts master\_Advantage\_proprietary\_locking Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Advantage Proprietary Locking  Advantage Concepts |  |  |  |  |

The Advantage Database Server uses an intelligent lock management system with its proprietary locking mode that eliminates lock retries and requires no network traffic. The Advantage Database Server uses an internal queuing algorithm that allows application locks to occur without making network operating system lock API calls. All locking information is maintained internally in the lock queues.

Advantage Proprietary locking mode also allows for read-through index locking and immediate index write locking. When an index is being read, there is no danger of that reader changing the structure of that index. Thus, Advantage allows read-through index locking for index "read" locks. All users who desire to read the same index can get concurrent "read" locks on that index and read from the index all at the same time. As you can imagine, this increases multi-user index "read" performance immensely. When an index is being updated, it is possible that the structure of the index may change. Thus, when a user obtains a "write" lock on an index, no other users can obtain a "read" or "write" lock on the index. The Advantage queuing process allows users to "line up" for access to that index. As soon as the user is done updating the index and releases the "write" lock on the index, the next user in the queue will immediately obtain an index lock and can proceed with the index read or write operation. No lock retries are ever required. "Write" lock requests are simply queued, and the locks are immediately granted as soon as the prior user has released the lock. This "write" lock queuing and elimination of lock retries increases multi-user database application performance.

Advantage Proprietary locking is only available with the Advantage Database Server. Advantage Proprietary locking is not available with the Advantage Local Server.

When Advantage Proprietary Locking is used, files are opened in an exclusive mode. Since the files cannot be opened by non-Advantage users, the Advantage Database Server can assume the environment is Advantage-only and internally maintains specific locking information. Non-Advantage applications can not open the files. Likewise, the Advantage Database Server cannot open files that were opened by some other application.

In older versions of Advantage, proprietary locking did not open files using an exclusive mode, instead it used a "deny write" open mode. While this would allow non-Advantage applications access to the data files, it could also lead to index corruption. Non-Advantage applications could still lock bytes in the files causing Advantage read and write operations to fail. For this reason the default proprietary open mode was changed. If, however, you require other non-Advantage enabled applications (such as backup software or reporting software) to open files in a shared, read-only mode, a server option is available to revert to older behavior. For details, see the [Non-Exclusive Proprietary Locking](master_non_exclusive_proprietary_locking.htm) configuration option.

When Advantage Proprietary Locking is used on Advantage ADT files, index "write" locking can be performed per tag. Therefore, multiple applications can be updating different tags in the same ADI file at the same time. This per tag "write" locking is not available with Xbase index files.