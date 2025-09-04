---
title: Devguide Automatic Transactions
slug: devguide_automatic_transactions
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_automatic_transactions.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: befa45ece54145e875fdd3333fab250326f954a7
---

# Devguide Automatic Transactions

Automatic Transactions

     Automatic Transactions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Automatic Transactions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You can use SET TRAN or SET TRANSACTION to automatically start a transaction whenever an INSERT, UPDATE, or DELETE statement is executed. You follow SET TRAN with one of three autocommit settings: AUTOCOMMIT\_ON (automatically begins a transaction and then commits the completed transaction), AUTOCOMMIT\_OFF (automatically begins transaction, but you must then commit or roll back the transaction in code), and EXPLICT (returns SET TRAN to default state in which you must explicitly begin and commit transactions). For example:

SET TRAN AUTOCOMMIT\_ON;  
TRY  
  INSERT INTO #TEMP VALUES('Sue Alan', NULL, 1000, True);  
  COMMIT;  
CATCH ADS\_SCRIPT\_EXCEPTION  
  ROLLBACK;  
END;  
SET TRAN EXPLICIT;

In the preceding code, AUTOCOMMIT is set to on, after which a record is inserted in a transaction and the transaction is committed. The last line, SET TRAN EXPLICIT, returns Advantage to its default mode, where you begin, commit, and roll back transactions manually.

As mentioned at the beginning of this section, most developers prefer explicit transactions, where all aspects of the transaction are managed by the client code.

There are a couple of final points to note about transactions. First, ADS permits only one transaction per connection. In other words, once you begin a transaction you must commit it or roll it back before you can initiate another transaction.

Second, it is important to keep in mind that transactions should be kept brief. Never wait for user input after beginning a transaction. If you need user input, get it before you initiate the transaction so that your code can start the transaction, apply changes, and commit or roll back as quickly as possible.

The need to keep transactions short is a performance issue. During a transaction, ADS holds record locks on all records that are modified during the transaction, until it is committed or rolled back. If you permit lengthy transactions, these locks can create bottlenecks and degrade the performance of your applications.

 

In the next chapter you will learn how to access metadata, as well as perform maintenance tasks on your data dictionary using SQL.
