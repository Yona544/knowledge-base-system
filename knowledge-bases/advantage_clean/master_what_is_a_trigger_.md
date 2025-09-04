---
title: Master What Is A Trigger
slug: master_what_is_a_trigger_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_what_is_a_trigger_.htm
source: Advantage CHM
tags:
  - master
checksum: ef0301d503d0f7fa3a4a915ad4399c6cf15a4783
---

# Master What Is A Trigger

What is a Trigger?

What is a Trigger?

Advantage Concepts

| What is a Trigger?  Advantage Concepts |  |  |  |  |

A trigger is a piece of code (similar to a stored procedure) that is executed on the server. Triggers differ from stored procedures because triggers are not called by the client, but instead are executed automatically in response to an insert, update, or delete operation.

Triggers are supported for both SQL and navigational update operations. Throughout this documentation the update operations will be specified using uppercase notation (for example, INSERT), but this does not imply an SQL-only limitation.

When a trigger is "fired" it contains some state information, which can be used inside the body of the trigger. Two in-memory tables are available inside a trigger; a [\_\_new table and an \_\_old table](master_trigger___old___new_and___error_tables.md). The \_\_new table contains new field values that were, or are about to be, inserted into the table. The \_\_old table contains old field values for the record in question. An [\_\_error](master_trigger___old___new_and___error_tables.md) table is also available that can be written to in order to indicate that an error occurred.

Triggers can provide a very powerful means to maintain business rules inside of a database.

Triggers can be defined for any supported table type, and are not limited to the proprietary ADT format.

Both the Advantage Database Server and the Advantage Local Server support triggers. [Implicit Transactions](master_implicit_transactions_and_triggers.md) are the only trigger functionality that differ depending on server type.

Trigger support is a server-side feature. Any Advantage client version 6.0 or greater capable of opening a dictionary-bound table can utilize triggers. This can be beneficial if you want to add trigger support to your application, but dont want to upgrade your client applications. Only the database server needs to be upgraded (to Advantage version 7.0 or greater) in order to start using triggers.

Triggers can also be defined at the database level to fire in response to certain events.  These database triggers can be used for auditing purposes for to provide additional checks on the operations for which they are supported. Database triggers are passed an \_\_info in-memory table containing data pertinent to the operation. Like table-based triggers, the \_\_error table is also available for indicating that an error occurred if necessary.
