---
title: Error 7086 Cannot Open Table Directly
slug: error_7086_cannot_open_table_directly
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7086_cannot_open_table_directly.htm
source: Advantage CHM
tags:
  - error
checksum: c9c178c14c552606b3e9c9798489b4dada130201
---

# Error 7086 Cannot Open Table Directly

7086 Cannot open table directly

7086 Cannot open table directly

Advantage Error Guide

| 7086 Cannot open table directly  Advantage Error Guide |  |  |  |  |

Problem: The database table cannot be opened directly for navigational access because the database administrator has set up the table to be accessed through SQL only.

Solution: Use SQL "SELECT ... " statement to access the table. If navigational access is required, the database administrator must change the table permission level to allow such access.
