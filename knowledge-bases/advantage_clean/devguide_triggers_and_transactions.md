---
title: Devguide Triggers And Transactions
slug: devguide_triggers_and_transactions
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_triggers_and_transactions.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 53e88221926005b6b6477a664b6abbde25564139
---

# Devguide Triggers And Transactions

Triggers and Transactions

     Triggers and Transactions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Triggers and Transactions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As you learned earlier, triggers are commonly used to apply changes to one or more tables within your database. This is especially true with INSTEAD OF triggers, which take responsibility for applying the requested change.

When you register your trigger with a data dictionary, you are given the option to perform all changes within the trigger in an all-or-none fashion within a transaction. When you do this, and your trigger returns an error code, all changes performed within the trigger prior to the error are rolled back.

This implicit transaction is distinct from any transaction that might be active on the connection through which the trigger is firing. Specifically, if a trigger is fired through a connection that is in a transaction, and the trigger returns an error, all changes made by the trigger are restored, but the transaction remains in force. It will be up to the client application to either commit or roll back the transaction, depending on the needs of the application.

It is also important to note that you cannot start a transaction on the connection passed to the trigger from within your trigger's code. Likewise, you cannot commit or roll back any transaction currently active on this connection, nor can you create transaction savepoints within a trigger.

You incur a performance penalty when you use this implicit transaction. Consequently, if data integrity is not as important as performance, you can disable implicit transactions using the "Use implicit transactions to maintain data integrity" option on the Triggers dialog box in the Advantage Data Architect.

ALS (Advantage Local Server) does not support transactions, nor does it support implicit transactions within triggers. As a result, if a trigger executed by ALS makes changes to more than one table, and an error occurs in the trigger, the changes already made to one or more tables within the trigger will remain.
