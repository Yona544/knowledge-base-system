Preparing Commands




Advantage Database Server 12  

Preparing Commands

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Preparing Commands  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Preparing Commands Advantage OLE DB Provider (for ADO) oledb\_Preparing\_commands Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Commands > Preparing Commands / Dear Support Staff, |  |
| Preparing Commands  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider supports command preparation for optimized multiple execution of a single command; however, command preparation generates overhead, and a consumer does not need to prepare a command to execute it more than once. In general, a command should be prepared if it will be executed more than three times.

In the Advantage Database Server, when a command is executed directly (without preparing it first), an execution plan is created and cached. If the SQL statement is executed again, Advantage Database Server has an efficient algorithm to match the new statement with the existing execution plan in the cache and reuses the execution plan for that statement.

For prepared commands, Advantage Database Server provides native support for preparing and executing command statements. When you prepare a statement, Advantage Database Server creates an execution plan, caches it, and returns a handle to this execution plan to the provider. The provider then uses this handle to execute the statement repeatedly. Because the handle directly identifies the execution plan for an SQL statement instead of matching the statement to the execution plan in the cache (as is the case for direct execution), it is more efficient to prepare a statement than directly execute it, if you know it will be executed more than a few times.