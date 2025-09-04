---
title: Error 7145 Collation Load Failed
slug: error_7145_collation_load_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7145_collation_load_failed.htm
source: Advantage CHM
tags:
  - error
checksum: e56ffc0ea1fedb432c9137ae54ba432e2f87297f
---

# Error 7145 Collation Load Failed

7145 Collation Load Failed

7145 Collation Load Failed

Advantage Error Guide

| 7145 Collation Load Failed  Advantage Error Guide |  |  |  |  |

Problem: Advantage was not able to open and use the collation repository that stores the [dynamic collations](master_collation_support.md).

Solution: An error occurred when trying to read the collation repository, which is an ADT table named adscollate.adt with an associated memo file named adscollate.adm. Check the error log (ads\_err.adt or ads\_err.dbf) for details.
