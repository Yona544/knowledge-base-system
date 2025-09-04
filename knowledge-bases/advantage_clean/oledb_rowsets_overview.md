---
title: Oledb Rowsets Overview
slug: oledb_rowsets_overview
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_rowsets_overview.htm
source: Advantage CHM
tags:
  - oledb
checksum: 51558d14bdce1b7183f19e8fabddfe18fbe61478
---

# Oledb Rowsets Overview

Rowsets Overview

Rowsets Overview

Advantage OLE DB Provider (for ADO)

| Rowsets Overview  Advantage OLE DB Provider (for ADO) |  |  |  |  |

A rowset is a set of rows that contains columns of data. Rowsets are central objects that enable all OLE DB data providers to expose result set data in tabular form.

After a consumer creates a session by using the IDBCreateSession::CreateSession method, the consumer can use either the IOpenRowset or IDBCreateCommand interface on the session to create a rowset. The Advantage OLE DB Provider supports both of these interfaces, and following are descriptions of both methods:

- •   Create a rowset by calling the IOpenRowset::OpenRowset method.

This is equivalent to creating a rowset over a single table. This method opens and returns a rowset that includes all the rows from a single base table. One of the arguments to OpenRowset is a table ID that identifies the table from which to create the rowset. Another argument to OpenRowset is an index ID that identifies the index order you want to make active on the specified table.

- •   Create a command object by calling the IDBCreateCommand::CreateCommand method.

The command object executes commands that the provider supports. In the Advantage OLE DB Provider, the consumer can specify any SQL statement (such as a SELECT statement). Following are the steps for creating a rowset by using a command object:

| 1. | 1. The consumer calls the IDBCreateCommand::CreateCommand method on the session to get a command object requesting the ICommandText interface on the command object. This ICommandText interface sets and retrieves the actual command text. The consumer fills in the text command by calling the ICommandText::SetCommandText method. |

| 2. | 2. The user calls the ICommand::Execute method on the command. The rowset object built when the command executes contains the result set from the command. |

The consumer can use the ICommandProperties interface to get or set the properties for the rowset returned by the command executed by the ICommand::Execute interfaces. The most commonly requested properties are the interfaces the rowset must support. In addition to interfaces, the consumer can request properties that modify the behavior of the rowset or interface.

Consumers release rowsets with the IRowset::Release method. Releasing a rowset releases any row handles held by the consumer on that rowset. Releasing a rowset does not release the accessors. If you have obtained an IAccessor interface, it still needs to be released.
