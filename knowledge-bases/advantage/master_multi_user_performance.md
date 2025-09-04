Multi-User Performance




Advantage Database Server 12  

Multi-User Performance

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Multi-User Performance  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Multi-User Performance Advantage Concepts master\_Multi\_user\_performance Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Multi-User Performance  Advantage Concepts |  |  |  |  |

In a multi-user, networked environment, traffic to and from the network is nearly always the bottleneck that leads to poor multi-user performance. Thus, the key to improving performance is to reduce the amount of data transferred across the network.

Optimized Data Access

In non-client/server environments, all application and data processing takes place on the individual client workstations. The file server, where the data files are located, serves only as an unintelligent, shared hard disk. The server CPU also remains largely unused. When the database needs to be updated, all necessary table and index data is read from the server, across the network, to the client workstation. Actual updates occur on the client workstation. The new data is then sent back across the network where it is written to the file server. When a piece of information needs to be found in the database, a search of the database is required. Index data must be read from the server, across the network, to the client workstation where the search of the data takes place. Index data must be continually read over to the client until the desired data is found or until it is determined the data does not exist in the database. As a result, non-client/server database applications typically suffer from poor performance. As more users are added to the system, the larger the database becomes, the amount of data transferred across the network increases even more, and performance deteriorates even further.

With the Advantage Database Server, network database application performance is increased dramatically. Advantage uses the client/server architecture to off-load all index traffic associated with index look-ups and index maintenance. The Advantage Database Server allows a central point of control for all database operations. No index data is ever transferred across the network to the client workstation. All database opens, reads, and writes are performed on the server by the Advantage Database Server where the data exists. Since no index data and no unnecessary table data is ever sent to the client workstation, network traffic is drastically reduced and performance increases. An additional benefit of Advantage client/server technology is that the Advantage Database Server performs all data processing on the file server, therefore the CPU on the file server is fully utilized. Advantage database applications have both the workstation CPU and the file server CPU working for them.

Intelligent Lock Management

Another critical, but often overlooked, factor contributing to increased performance with Advantage client/server technology is data locking that occurs behind the scenes by the database system. Before index data can be read or updated, an implicit lock is obtained on that index. As an application developer, you have no control over when or how these implicit locks are obtained. The database system that the application is using obtains these locks for you.

In non-client/server environments, all internal locking requests are issued from the individual client workstations. In multi-user systems, there is much contention for index access. The initial attempts to lock the index files will often fail because another user already has the index locked. Non-client/server database systems try and retry the locks from the client, which takes more time and leads to poor performance for that application. In addition, these lock retries generate increased network traffic that will slow performance for all users on the network. Non-client/server application index locking generally leads to slow performance for that individual application as well as compounding performance problems for other applications on the network.

With Advantage client/server technology, the internal index locks occur on the server. The Advantage Database Server uses an intelligent lock management system with its proprietary locking mode that eliminates lock retries and requires no network traffic. The Advantage Database Server uses an internal queuing algorithm that allows for read-through index locking and immediate index write locking. In non-client/server systems, there is no differentiation between index "read" locks and index "write" locks. There is only one kind of lock that can be obtained whether reading or updating an index, and thus all index access is sequentialized. With the Advantage Database Server, index "read" locks exist as well as index "write" locks. When an index is being read, there is no danger of that reader changing the structure of that index. Thus, Advantage allows read-through index locking for index "read" locks. This means all users who desire to read the same index can get concurrent "read" locks on that index and read from the index all at the same time. As you can imagine, this increases multi-user index "read" performance immensely.

When an index is being updated, it is possible that the structure of the index may change. Therefore, when a user obtains a "write" lock on an index, no other users can obtain a "read" or "write" lock on the index. The Advantage queuing process allows for users to "line up" for access to that index. As soon as the update operation completes and the "write" lock on the index is released, the next user in the queue will immediately obtain his index lock and can proceed with the index read or write operation. No lock retries are ever required. "Write" lock requests are simply queued, and the locks are immediately granted as soon as the prior user has released the lock. This "write" lock queuing and the elimination of lock retries significantly increases multi-user database application performance.