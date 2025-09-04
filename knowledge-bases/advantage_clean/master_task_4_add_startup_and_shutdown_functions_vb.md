---
title: Master Task 4 Add Startup And Shutdown Functions Vb
slug: master_task_4_add_startup_and_shutdown_functions_vb
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_4_add_startup_and_shutdown_functions_vb.htm
source: Advantage CHM
tags:
  - master
checksum: 5f2d0abbb0ebf58a54a8032c81fa218030cb8c9e
---

# Master Task 4 Add Startup And Shutdown Functions Vb

Task 4: Add Startup and Shutdown Functions

Task 4: Add Startup and Shutdown Functions

Advantage Concepts

| Task 4: Add Startup and Shutdown Functions  Advantage Concepts |  |  |  |  |

We need to take some time to discuss session management. It would be nice if your AEP did not have to create connections, tables, and queries every time it was called. To help facilitate this sort of functionality, AEP containers can implement two special procedures; Startup and Shutdown. The Startup function will be called by Advantage, on a per-connection basis, the first time a procedure inside of the AEP container is called. The Shutdown function will be called, on a per-connection basis, as each connection that has used the AEP container is closed. This means the Startup function is called once for each Advantage connection that begins using procedures inside of the AEP container, and the Shutdown function is also called once for each Advantage connection that has used procedures inside of the AEP container.

It is important when developing AEPs to keep in mind that they will be run by a multi-threaded server (Advantage). The Advantage Database Server does not necessarily use the same thread every time it executes requests for the client, so thread variables are not a suitable solution for providing client-specific storage in an AEP. All AEP functions are passed a unique identifier, the ulConnectionID parameter. This parameter can be used by the developer to uniquely identify a client connection. Resources allocated on behalf of the client (connections, open tables, etc) can be tied to this unique connection id, and retrieved at a later time.

Keeping this in mind, take some time to familiarize yourself with the Startup and Shutdown functions that were generated for you in the AEP template.

The Startup and Shutdown functions that were automatically generated in the template will be sufficient for this tutorial. Continue on to the next task.

Note When accessing DBF tables in the stored procedure, it may be necessary to modify the connection string in the template code. Some statement level settings are specified via the connection string. The settings that you may need to specify explicitly are LockMode and CharType. These settings are not inherited from the connection and they are not stored in the data dictionary. If you do not provide them in the connection string, the defaults (proprietary locking and ANSI) will be used. When using ADTs, it should not be necessary to specify any additional settings.
