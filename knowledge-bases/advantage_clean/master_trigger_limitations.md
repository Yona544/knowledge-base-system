---
title: Master Trigger Limitations
slug: master_trigger_limitations
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_trigger_limitations.htm
source: Advantage CHM
tags:
  - master
checksum: b613a7d6a0d69394abaf5f0bd2a49c27cb5bcb23
---

# Master Trigger Limitations

Trigger Limitations

Trigger Limitations

Advantage Concepts

| Trigger Limitations  Advantage Concepts |  |  |  |  |

Only one INSTEAD OF trigger is allowed for each event type (INSERT, UPDATE, or DELETE) per table.

If a table has a BEFORE trigger, it cannot have an INSTEAD OF trigger. The reverse is also true.

If a table has an INSTEAD OF X trigger, AFTER X triggers defined for that table will not fire (where X is an event type).

The \_\_error table can only have one row. Delete operations are not currently allowed on the \_\_error table.

VarChar fields are not supported in the \_\_old and \_\_new tables.

When using the Advantage Local Server, if a trigger fails for any reason, the database is left as is. This means any operations the trigger may have already performed will be persistent.

Nested and recursive triggers are limited to 64 levels of server re-entrance before an error is returned.
