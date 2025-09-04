---
title: Error 7147 Collation Name Not Found
slug: error_7147_collation_name_not_found
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7147_collation_name_not_found.htm
source: Advantage CHM
tags:
  - error
checksum: 638d94f91a07941ac2aef148acfa0ba5dc436a6b
---

# Error 7147 Collation Name Not Found

7147 Collation Name Not Found

7147 Collation Name Not Found

Advantage Error Guide

| 7147 Collation Name Not Found  Advantage Error Guide |  |  |  |  |

Problem: An attempt to load a [dynamic collation](master_collation_support.md) failed because the given collation name was not found.

Solution: Verify that the correct collation name was specified in the application. The error log (ads\_err.adt or ads\_err.dbf) entry for this error will show the name that was being searched for.
