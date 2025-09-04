---
title: Master Trigger Options
slug: master_trigger_options
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_trigger_options.htm
source: Advantage CHM
tags:
  - master
checksum: 954dd3600e9c35b989b7d9119592d35b90e8ba29
---

# Master Trigger Options

Trigger Options

Trigger Options

Advantage Concepts

| Trigger Options  Advantage Concepts |  |  |  |  |

When creating a trigger, you can specify trigger options that modify trigger behavior. The following options are supported (see the SQL documentation for CREATE TRIGGER or the Advantage Data Architect help file for specific examples of where/how to configure these options):

NO VALUES

This option can be used if your trigger code will not be making use of the \_\_new or \_\_old table. The \_\_new and \_\_old tables will not be built by the server when a trigger fires, which can increase performance.

NO MEMOS/BLOBS

This option can be used if your trigger code will not be making use of memo or blob fields in the \_\_new and \_\_old tables. The \_\_new and \_\_old tables will be built by the server, but will not contain memo or blob data. This option can be used to increase performance on tables that have large memo or blob fields.

Note If a table has multiple triggers, and at least one of those triggers requires memo/BLOB data in the values tables, all triggers for the table in question will get the memo/BLOB data in their values tables.

PRIORITY

When creating a trigger, you can specify a firing priority. If more than one trigger exists for a given table, this priority will be used when determining the order in which the triggers will be fired. Consider a table that has two AFTER UPDATE triggers, one with a priority of 1, and another with a priority of 2. The trigger with a priority of 1 will fire first, followed by the trigger with a priority value of 2.

NO TRANSACTION

In certain situations, you may find that data integrity is not as important as performance. For this reason, there is a trigger option to disable implicit transactions. This option can be used to increase the performance of simple triggers that do not need the additional integrity that [implicit transactions](master_implicit_transactions_and_triggers.md) provide. Note that currently the "no transactions" trigger option is implemented on a per-event basis, so if you specify this flag for a trigger, all triggers with that event type (INSERT, UPDATE, or DELETE) will respect the "no transactions" flag.
