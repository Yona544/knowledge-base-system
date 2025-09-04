---
title: Error 7146 Collation Name Not Unique
slug: error_7146_collation_name_not_unique
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7146_collation_name_not_unique.htm
source: Advantage CHM
tags:
  - error
checksum: 85b9a8634d55e514bae6b017a2463cb15c2eb18f
---

# Error 7146 Collation Name Not Unique

7146 Collation Name Not Unique

7146 Collation Name Not Unique

Advantage Error Guide

| 7146 Collation Name Not Unique  Advantage Error Guide |  |  |  |  |

Problem: When loading a [dynamic collation](master_collation_support.md), multiple entries in the repository were found that match the name.

Solution: The error log (ads\_err.adt or ads\_err.dbf) entry for this error will show the name that was found to be non-unique. It may be necessary to replace the adscollate.adt and adscollate.adm files with valid copies.
