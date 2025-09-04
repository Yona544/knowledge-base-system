---
title: Error 5204 Ae Invalid Collation
slug: error_5204_ae_invalid_collation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5204_ae_invalid_collation.htm
source: Advantage CHM
tags:
  - error
checksum: 66bfcabeafd2353f45125790a95b17ee4603574c
---

# Error 5204 Ae Invalid Collation

5204 AE\_INVALID\_COLLATION

5204 AE\_INVALID\_COLLATION

Advantage Error Guide

| 5204 AE\_INVALID\_COLLATION  Advantage Error Guide |  |  |  |  |

Problem: The application attempted to load a [dynamic collation](master_collation_support.md) that has invalid information associated with it.

Solution: This problem may be that the adscollate.adt table has been corrupted. Replace adscollate.adt and adscollate.adm with valid copies of the files.
