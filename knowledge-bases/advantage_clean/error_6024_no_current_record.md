---
title: Error 6024 No Current Record
slug: error_6024_no_current_record
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6024_no_current_record.htm
source: Advantage CHM
tags:
  - error
checksum: a0b1606892a2d0dabc7e935ff2e6a8b9150cda33
---

# Error 6024 No Current Record

6024 No current record

6024 No current record

Advantage Error Guide

| 6024 No current record  Advantage Error Guide |  |  |  |  |

Problem: AX\_KeyAdd() or AX\_KeyDrop() was called and the record pointer was not positioned on a record. For example, you would not be positioned on a record if you were at EOF due to a failed seek operation.

Solution: Perform a GO TOP, GO BOTTOM, SEEK or some other operation to position yourself in the file to a valid record.
