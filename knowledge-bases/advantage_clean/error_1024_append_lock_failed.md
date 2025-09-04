---
title: Error 1024 Append Lock Failed
slug: error_1024_append_lock_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_1024_append_lock_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 9a8e0f7dfbfd2f107b33431ec356fc4b73a79ac0
---

# Error 1024 Append Lock Failed

1024 Append Lock Failed

1024 Append Lock Failed

Advantage Error Guide

| 1024 Append Lock Failed  Advantage Error Guide |  |  |  |  |

Problem: A new record could not be appended because a lock could not be obtained for the new record.

Solution: For a shared work area, the append blank operation automatically obtains a record lock for the newly appended record. If the record cannot be locked, the append fails. This generally occurs because another process has obtained a file lock on the table. Change the program to handle the lock contention.
