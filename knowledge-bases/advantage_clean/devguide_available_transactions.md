---
title: Devguide Available Transactions
slug: devguide_available_transactions
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_available_transactions.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: bf9582f86c6701501de9c382fdf827bad8ac8b9b
---

# Devguide Available Transactions

Available Transactions

     Available Transactions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Available Transactions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A transaction is an operation that treats two or more changes to a database as a discrete unit of work, saving those changes in an all-or-none fashion. If all of the operations involved in the transaction can be completed, the transaction itself is committed. However, if even one operation cannot be successfully completed, all operations within the transaction are canceled, ensuring that your data remains consistent.

Transactions require centralized control of data access, and file-server-based systems cannot provide that. ADS provides that centralized control: it is aware of the various operations being performed by each connected client. By comparison, each ALS client is autonomous and cannot see what the other clients are doing to the database (this is true of all file-server-based databases). As a result, ALS cannot assure that all operations of a transaction can be completed successfully.

One very important feature of a transaction comes into play if the database server, the client workstation, or the network across which they communicate, fails before the transaction is committed. In those cases, the edits of the transaction are rolled back automatically by the Advantage Database Server once the problem is detected, or the server is restarted (if the server crashed).

Though ALS does not support transactions, you can write your applications that use ALS as if it did. Specifically, when using ALS, your code can include calls to begin, commit, and roll back transactions. These statements will be ignored. However, if you then migrate that application to use ADS, no changes are necessary in your code, and the transactions will be respected.
