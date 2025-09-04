---
title: Master Performance Factors Relative To Non Client Server
slug: master_performance_factors_relative_to_non_client_server
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_performance_factors_relative_to_non_client_server.htm
source: Advantage CHM
tags:
  - master
checksum: b9c06295f16d4972029af277f5c81bbdba08ab6f
---

# Master Performance Factors Relative To Non Client Server

Performance Factors Relative to Non-Client/Server

Performance Factors Relative to Non-Client/Server

Advantage Database Server

| Performance Factors Relative to Non-Client/Server  Advantage Database Server |  |  |  |  |

The following are keys to performance when comparing Advantage to non-client/server solutions.

Multiple Users Usually Required

Multiple users are often required to see performance gains with Advantage Database Server versus non-client/server solutions. When a single user has a table(s) open with a non-client/server database engine, and they are the only user on the network with that table(s) open, they will cache vast amounts of database data on the client after that has been read from server. Since they are the only user on the network with that table(s) open, they know the information they have cached is up to date and, therefore, never read it again from the server. When they do updates, these updates are also often cached on the client as there is no need to send it to the server since there are no other users who need to see that updated data. Due to this vast amount of caching, the amount of data passed across the network will be nearly eliminated. This causes non-client/server database drivers to have very good performance in a single-user environment.

Advantage Database Server was designed from the ground up to be a multi-user client/server database engine. It does little caching of the data on the client, as it expects other users on the system will need access to that data. Plus, Advantage Database Server ensures database stability by verifying all updates are written to the database. Non-client/server drivers often suffer from frequent corruption due to the vast amount of updated data cached on the client that sometimes never makes it to the server if the application, workstation, or network fails.

There are exceptions where Advantage Database Server will almost always be faster than non-client/server drivers, even when only a single user is accessing the database. These exceptions include database-intensive operations such as SQL UPDATE statements, complex SQL queries, index creation, copying all records from one table to another, etc. The use of the Advantage Database Server processing may be slower in certain situations with single users, but will greatly increase multi-user performance.

Open Tables for Shared Use

Open tables for "shared" use. First, if tables are opened for "exclusive" use, multi-user access that was discussed above is eliminated, and non-client/server database drivers will be able to use client data caching to its advantage. Even when files are opened for shared use, especially when the file server is running a Windows operating system, much of the caching discussed above will occur. Thus, make sure and open tables for shared use and have multiple users accessing the database to see Advantage Database Server in the environment in which it was designed. There are cases where exclusive use of tables is required, and then it makes sense to do so. These include operations such as index creation, copy to, append from, pack, and zap (also referred to as empty table). If tables are opened for "exclusive" use, Advantage Database Server may not increase read and write performance versus non-client/server drivers.

The More Indexes/Tags Open, the Better

The more indexes/tags that are open, the better Advantage performance will be relative to non-Advantage drivers. In most multi-user systems, there is a lot of contention for index access. Every index access, whether it be for a read, skip, seek, write, etc., requires an internal index lock to be obtained. The initial attempts to lock the index files will often fail because another user already has the index locked. Non-client/server drivers try and retry the index locks from the client, which leads to increased network traffic and very slow performance. Advantage performs index locking on the server using an intelligent read-through locking queuing system, which greatly increases performance. If applications generally use very few or no indexes/tags, then the Advantage Database Server may not greatly increase read and write performance versus non-client/server drivers.

Note The above does not recommend that you create and open more indexes/tags to improve performance. In fact, applications with few indexes/tags usually perform better than similar applications with more indexes/tags. The point is, that if your existing application already uses many indexes/tags, Advantage should significantly improve performance compared to non-client/server drivers.

The Larger the Tables, the Better

The larger the tables and index files, the better Advantage will perform in comparison to non-client/server drivers. If tables and index files are small, non-client/server drivers do not have much data to read and write to and from the server. The most significant way Advantage increases performance is by reducing network traffic. If the non-client/server driver does not generate much network traffic because data files are small, the benefit of using Advantage is eliminated. If tables are generally small, that is, they have fewer than 10,000 records, Advantage may not greatly increase read and write performance versus non-client/server drivers.

Note The above does not recommended that you increase the size of your tables and indexes to improve performance. In fact, applications with smaller tables and indexes usually perform better than similar applications with larger tables and indexes. The point is, that if your existing application already uses large tables and indexes, Advantage should significantly improve performance compared to non-client/server drivers.

Read the Data in Performance Tests

If writing a performance test that does skip and seek operations, be sure to read the data to which you are skipping or seeking. Non-client/server drivers do not necessarily automatically read over the corresponding table record after a skip or a seek. The Advantage Database Server "bundles" the record with the skip or seek result back to the client. 99% of the time, applications read the data to which they are skipping or seeking. So make sure your performance test does, too.

Speed of the Network

The network infrastructure itself plays a key role in database application performance. Non-client/server database applications transport all data from the server to the workstation and vice versa. Even with the Advantage Database Server client/server architecture, which significantly reduces network traffic, database applications generate more traffic than other types of applications. Thus, the speed of your network and the number of bridges and routers between the workstation and the server, play a role in performance. In general, the slower the communications between the workstation and server, the faster Advantage applications will perform relative to non-client/server applications. This is simply the result of client/server processing reducing the amount of data transferred across the network. Applications using the Advantage Database Server in a WAN environment will produce very impressive performance improvements.
