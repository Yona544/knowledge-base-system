---
title: Master Database Stability
slug: master_database_stability
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_database_stability.htm
source: Advantage CHM
tags:
  - master
checksum: 3536807f91b22593e435fb0d5e5169b0063b993b
---

# Master Database Stability

Database Stability

Database Stability

Advantage Concepts

| Database Stability  Advantage Concepts |  |  |  |  |

During traditional non-client/server interaction between a workstation and server, tables and index files are susceptible to corruption. Workstations can be interrupted or fail because of a reboot, power failure, or memory problem. It takes several calls between the workstation and the server to complete an update operation. If during this process the application, workstation, or network fails, the operation is partially executed, leaving the database in an unknown state. Index file stability and possibly table stability are compromised. The following diagram shows the interaction between client and server in a non-client/server environment during an update to a single record in a table that causes two related indexes to be updated. Note that if the application, workstation, or network fails at any time between the first index write and the write of the table record, the database will be left in an unstable and corrupt state.

Note Due to space considerations, the example in the diagram below has been overly simplified. In fact, many more read and write operations than are shown must occur between the workstation and file server before each index update can be completed. In actuality, there is even a larger window for possible database corruption in non-client/server environments than shown.

Advantage provides database stability ensuring that every database operation is executed completely or is not executed at all. Entire database update operations are executed on the server. Therefore, if the application, workstation, or network fails, the database operation will either successfully be transmitted to the Advantage Database Server or not transmitted at all. The status of the application, workstation, and network cannot affect the data in your database. By transmitting entire table and index file update operations in one command from the client to the server, Advantage eliminates corruption errors introduced by application, workstation, or network failure. If you have a file server failure, database corruption can still be eliminated if you are using the [Transaction Processing System (TPS)](master_transaction_processing_system.md).

The following diagram shows the interaction between client and server with Advantage client/server processing during the same update shown above to a single record in a table which causes two related indexes to be updated. Note that there is no unstable state with Advantage as no database updates will occur until all required update information has been received by the Advantage Database Server. Once all update information has been received, those updates will occur on the server by the Advantage Database Server requiring no network traffic and no workstation involvement.
