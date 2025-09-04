---
title: Error 7187 Uncommitted Transac
slug: error_7187_uncommitted_transac
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7187_uncommitted_transac.htm
source: Advantage CHM
tags:
  - error
checksum: 89b08d334bb4499acfc770339ca99902d5bc306a
---

# Error 7187 Uncommitted Transac

Uncommitted Transaction

7187 Uncommitted Transaction

Advantage Error Guide

| 7187 Uncommitted Transaction  Advantage Error Guide |  |  |  |  |

Problem: A subprogam, i.e. stored procedure, user defined function or trigger, started a transaction without committing it.

Solution: This is a warning that a nested transaction should be committed in the same subprogram that initiated it. Advantage will automatically commit unbalanced transaction that started in a subprogram. It is a good programming practice to explicitly commit nested transactions. See [Nesting Transactions](master_nesting_transactions.md) for additional information.
