---
title: Ade Management Capabilities Overview
slug: ade_management_capabilities_overview
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_management_capabilities_overview.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 33b9227c9627600c7bbb98bd6b00e76f7c425e32
---

# Ade Management Capabilities Overview

Management Capabilities Overview

Management Capabilities Overview

Advantage TDataSet Descendant

| Management Capabilities Overview  Advantage TDataSet Descendant |  |  |  |  |

The Advantage Database Server can supply management information directly to Advantage TDataSet Descendant applications via the Advantage Management API and Advantage Management System Procedures. The following Advantage Database Server information can be obtained via the Advantage Management API and System Procedures:

- Database activity information

- Installation information

- Information about connected users

- Information about tables and index files that are open

- Configuration parameters

- Communication statistics

- Transaction information

- Worker thread activity information

- Owner of a file or record lock

- List of locks on a given table

- Advantage server type

In addition to the ability to retrieve the above information, Advantage applications have the ability to disconnect a user from the Advantage Database Server.

The Advantage Management APIs are not available as extended methods in the Advantage TDataSet Descendant . They are available by calling the Advantage Client Engine API directly. For information on how to call the Advantage Client Engine API directly, see [When to Make Direct Calls to the Advantage Client Engine](ade_when_to_make_direct_calls_to_the_advantage_client_engine.md).

An alternative to the Advantage Management API is to use the [Advantage Management System Procedures](master_using_sql_to_access_management_information.md). They are a set of "canned" system procedures that can be executed as SQL statements. The information is returned as a result set. For example, as an alternative to AdsMgGetLockOwner, it is possible to execute the system procedure sp\_mgGetLockOwner(). In some situations, it is much simpler to execute the system procedure as opposed to calling the API. The drawback, though, is that it is quite a bit more expensive to call the equivalent stored procedure than to call one of the APIs. Most of the APIs result in a single call to the server. The equivalent system procedure involves the parse of an SQL statement and the creation of a temporary cursor. If you will be retrieving some piece of management information (e.g., the list of open tables) repeatedly over a short period of time, it is probably best to use the API for efficiency reasons.

See Also

[Advantage Management System Procedures](master_using_sql_to_access_management_information.md)
