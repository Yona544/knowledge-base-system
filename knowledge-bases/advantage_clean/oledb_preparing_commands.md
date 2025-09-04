---
title: Oledb Preparing Commands
slug: oledb_preparing_commands
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_preparing_commands.htm
source: Advantage CHM
tags:
  - oledb
checksum: decfb5990a950194b640f9e30c4877a15ebc82ae
---

# Oledb Preparing Commands

Preparing Commands

Preparing Commands

Advantage OLE DB Provider (for ADO)

| Preparing Commands  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider supports command preparation for optimized multiple execution of a single command; however, command preparation generates overhead, and a consumer does not need to prepare a command to execute it more than once. In general, a command should be prepared if it will be executed more than three times.

In the Advantage Database Server, when a command is executed directly (without preparing it first), an execution plan is created and cached. If the SQL statement is executed again, Advantage Database Server has an efficient algorithm to match the new statement with the existing execution plan in the cache and reuses the execution plan for that statement.

For prepared commands, Advantage Database Server provides native support for preparing and executing command statements. When you prepare a statement, Advantage Database Server creates an execution plan, caches it, and returns a handle to this execution plan to the provider. The provider then uses this handle to execute the statement repeatedly. Because the handle directly identifies the execution plan for an SQL statement instead of matching the statement to the execution plan in the cache (as is the case for direct execution), it is more efficient to prepare a statement than directly execute it, if you know it will be executed more than a few times.
