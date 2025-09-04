Limitations of Selecting the Advantage Local Server




Advantage Database Server 12  

Limitations of Selecting the Advantage Local Server

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Limitations of Selecting the Advantage Local Server  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Limitations of Selecting the Advantage Local Server Advantage Concepts master\_Limitations\_of\_selecting\_the\_advantage\_local\_server Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Limitations of Selecting the Advantage Local Server  Advantage Concepts |  |  |  |  |

Decreased Multi-User Performance

In Advantage Local Server environments, all application and data processing takes place on the individual client workstations. The file server, where the data files are located, serves only as an unintelligent, shared hard disk. The server CPU also remains largely unused. When the database needs to be updated, all necessary table and index data is read from the server, across the network, to the client workstation. Actual updates occur on the client workstation. The new data is then sent back across the network where it is written to the file server. When a piece of information needs to be found in the database, a search of the database is required. Index data must be read from the server, across the network, to the client workstation where the search of the data takes place. Index data must be continually read over to the client until the desired data is found or until it is determined that the data does not exist in the database. As a result, multi-user Advantage Local Server database applications may suffer from poor performance. As more users are added to the system, the larger the database becomes, the amount of data transferred across the network increases even more, and performance deteriorates even further. Refer to Advantage Database Server for explanations on why the Advantage Database Server improved multi-user performance.

No Database Security Options

When an Advantage Local Server application needs to open or create a file on the file server, the network operating system will verify that the user has sufficient network access rights to that directory and/or file before allowing that user to open or create the file. If the user has no network access rights to the directory and/or file, the network operating system will not allow the application to open or create the file. If the user has limited network access rights to the directory and/or file, such as read-only access, the network operating system will only allow the application to open a file for read-only use.

Restricting a user's network access rights to the directory and/or files as just described often does not provide enough database security. If a user has been given the necessary read, write, create, and/or delete rights necessary to read, write, create, and/or delete data via your database application, then that user can also read, write, create, and/or delete data without using your application. Users can maliciously or accidentally corrupt the database by writing to the database with uncontrolled database editors. Files in the database could also be purposely or accidentally deleted entirely. What mission critical database applications often need is an additional level of security that only allows users to access the database via your database application. That way the database application has full control over what users are reading, writing, creating, and/or deleting data in the database. Advantage Local Server applications have no way to enforce this additional security; the Advantage Database Server does. Refer to Advantage Database Server for explanations on how the Advantage Database Server implements additional database security features.

No Guaranteed Database Stability

During Advantage Local Server interaction between a workstation and server, tables and index files are susceptible to corruption. Workstations can be interrupted or fail because of a reboot, power failure, or memory problem. It takes several calls between the workstation and the server to complete an update operation. If during this process the application, workstation, or network fails, the operation is partially executed, leaving the database in an unknown state. Index file stability and possibly table stability are compromised. The following diagram shows the interaction between client and server in a non-client/server environment during an update to a single record in a table that causes two related indexes to be updated. Note that if the application, workstation, or network fails at any time between the first index write and the write of the table record, the database will be left in an unstable and corrupt state.

Note Due to space considerations, the example in the diagram below has been overly simplified. In fact, many more read and write operations than are shown must occur between the workstation and file server before each index update can be completed. In actuality, there is even a larger window for possible database corruption in Advantage Local Server environments than shown.

Refer to Advantage Database Server for explanations on why the Advantage Database Server guarantees database stability.

No Transaction Processing

A Transaction Processing System (TPS) allow an application to perform multiple insert, update, and delete operations to any number of tables with complete confidence that either all of the insert, update, and delete operations will be successful or that none of the operations will occur. In other words, a TPS processes multiple insertions, updates, and deletions as though they were a single operation.

In networked environments, tables and their associated index files are susceptible to corruption if a workstation crashes or a network failure occurs while the tables and index files are being updated. Building an audit trail to monitor these failures is difficult. Developing a method to recover from incomplete updates is even more difficult. Transaction Processing Systems eliminate these problems and protect database integrity by automatically undoing any updates that were performed in the event of workstation or network failure. This leaves a database exactly as it was before a transaction began.

Transaction Processing is not supported in the Advantage Local Server. Use of Advantage Transaction Processing functionality may appear to complete successfully when using Advantage Local Server, but in fact, use of Transaction Processing features will be ignored by Advantage Local Server applications.

See [Transaction Processing System (TPS)](master_transaction_processing_system.htm) for a full explanation of the Transaction Processing System available in the Advantage Database Server.