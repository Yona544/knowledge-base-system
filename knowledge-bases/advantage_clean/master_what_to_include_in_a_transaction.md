---
title: Master What To Include In A Transaction
slug: master_what_to_include_in_a_transaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_what_to_include_in_a_transaction.htm
source: Advantage CHM
tags:
  - master
checksum: d0463e21a2cb77848fc515a8894b46e5646ce0d3
---

# Master What To Include In A Transaction

What to Include in a Transaction

What to Include in a Transaction

Advantage Concepts

| What to Include in a Transaction  Advantage Concepts |  |  |  |  |

A transaction consists of a command to begin the transaction, the steps to complete the transaction (your insert, update, and delete operations), and a command to end the transaction. Transactions should be limited in their complexity. In most applications, the only operations that should be included within transactions are insert, update, and delete operations. All operations that create files, open files, and receive user input should be excluded. In general, transactions should open/create files first, read/input the necessary information, begin the transaction, issue the insert and update operations, and finally, commit the transaction.
