---
title: Error 7057 Record Update Failed
slug: error_7057_record_update_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7057_record_update_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 98ee03a5fd79a158de643639a8daa54c811a301c
---

# Error 7057 Record Update Failed

7057 Record update failed

7057 Record update failed

Advantage Error Guide

| 7057 Record update failed  Advantage Error Guide |  |  |  |  |

Problem: The key value produced from this record was not unique, and the index for the current table has the UNIQUE property.

Solution: Replace the key value field(s) with a unique value(s). If this is not possible, cancel the operation. When using the Advantage Client Engine API directly, call AdsCancelUpdate. When using the Advantage TDataSet Descendant, use the TTable.Cancel method.
