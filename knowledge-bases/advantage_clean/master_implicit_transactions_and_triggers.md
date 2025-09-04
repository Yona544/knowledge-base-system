---
title: Master Implicit Transactions And Triggers
slug: master_implicit_transactions_and_triggers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_implicit_transactions_and_triggers.htm
source: Advantage CHM
tags:
  - master
checksum: ca19f17ea88f80939259c7c1162ab585e15e3836
---

# Master Implicit Transactions And Triggers

Implicit Transactions and Triggers

Implicit Transactions and Triggers

Advantage Concepts

| Implicit Transactions and Triggers  Advantage Concepts |  |  |  |  |

When using the Advantage Database Server (as opposed to the Advantage Local Server) all operations performed inside of a trigger are done so inside of an implicit transaction. If any trigger (or nested trigger) operation fails, all operations will be rolled back, and the database will be returned to the state it was in before the trigger(s) fired. If a transaction is already active before the first trigger is fired, a savepoint will be set, and on error, all operations will be rolled back to the savepoint.

When using the Advantage Local Server, if a trigger fails for any reason, the database is left as is. This means any operations the trigger may have already performed will be persistent.

Because triggers use transactions automatically, it is illegal to begin a transaction inside of a trigger. Committing or rolling back a transaction from inside a trigger will result in unexpected behavior, and should be avoided.

In certain situations, you may find that data integrity is not as important as performance. For this reason, there is a trigger option to disable implicit transactions. This option can be used to increase the performance of simple triggers that do not need the additional integrity that implicit transactions provide. Note that currently the "no transactions" trigger option is implemented on a per-event basis, so if you specify this flag for a trigger, all triggers with that event type (insert, update, or delete) will respect the "no transactions" flag.
