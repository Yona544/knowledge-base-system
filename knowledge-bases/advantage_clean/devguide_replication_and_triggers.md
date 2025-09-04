---
title: Devguide Replication And Triggers
slug: devguide_replication_and_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_replication_and_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 38dd83ef17496bea7c64bb415179bdf71fc8fd8f
---

# Devguide Replication And Triggers

Replication and Triggers

     Replication and Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Replication and Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As you learned in Chapter 8, so long as they have not been disabled, triggers are guaranteed to execute in response to their associated event, such as a record being inserted, updated, or deleted. There is a major exception to this behavior when it comes to replication. Specifically, when a record is inserted, updated, or deleted in a target database through replication, any related triggers on that target table do not execute.

At first this might seem puzzling, but if you consider the role played by triggers, it is easy to see why this behavior is correct. Consider what triggers are designed to do. A BEFORE trigger is designed to validate an operation, preventing the operation from occurring if it is unacceptable to the trigger code.

An INSTEAD OF trigger is designed to conditionally modify data involved in the operation, and an AFTER trigger is designed to react to something that has already happened.

So why do these triggers not execute when a table is updated through replication? The answer is that these operations should be performed by the source data dictionary. Once these records have been validated, conditionally modified, or reacted to, there is nothing else left for the target data dictionary to do.

There is one exception to this behavior. There is a special type of trigger designed specifically for replication. This trigger, ON CONFLICT, executes when there is a mismatch between the source and target record being deleted or updated. (ON CONFLICT does not apply to inserted records.)

Consider first what happens when there is no ON CONFLICT trigger. When the source data dictionary locates the target data dictionary record based on the configured row identifiers, the source record replaces the target record unconditionally. For example, if the row identifiers use the primary key, the target record, when located, is overwritten, regardless of what data was contained in its non-key fields.

When an ON CONFLICT trigger is present on the target table, Advantage takes additional steps. First, it calculates the CRC (cyclic redundancy check) for the destination record, including BLOB (binary large object) and memo fields (excluding only rowversion and modtime fields). It then compares this value to the CRC it calculated for the source record (the source record CRC is always calculated, even if an ON CONFLICT trigger is absent). If the CRC values from source and target do not match, the source and target records are not identical and the ON CONFLICT trigger is executed.

The purpose of the ON CONFLICT trigger is to permit you to programmatically resolve differences between source and target records.

From within the ON CONFLICT trigger you have access to three in-memory tables: \_ \_old, \_ \_new, and \_ \_error (names are preceded by two consecutive underscore characters). The \_ \_new table contains a copy of the source table record and the \_ \_old table contains the current values of the target table record.

By examining these in-memory tables, your ON CONFLICT can take one of several actions. Your trigger can overwrite the target table record, it can discard the source table record, it can write some but not all of the source record fields to the target table record (a merge), it can write the conflicting record to a table for manual evaluation, or it can generate an error. If any data needs to be written to the target table record, it is your ON CONFLICT trigger's responsibility to perform the write, based on the \_ \_new and \_ \_old table values. If your ON CONFLICT trigger needs to generate an error, it must write an error code and error message to the \_ \_error table.

   
NOTE: An ON CONFLICT trigger is similar to an INSTEAD OF trigger, in that the ON CONFLICT trigger must write to the corresponding target table record if the replication is to be successful.
