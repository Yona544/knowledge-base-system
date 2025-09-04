---
title: Error 7215 Rowid Invalidated D
slug: error_7215_rowid_invalidated_d
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7215_rowid_invalidated_d.htm
source: Advantage CHM
tags:
  - error
checksum: 3701e0e4055b9dfd2be4a46a768fcd967bad04db
---

# Error 7215 Rowid Invalidated D

7215 ROWID Invalidated During Pack

7215 ROWID Invalidated During Pack

Advantage Error Guide

| 7215 ROWID Invalidated During Pack  Advantage Error Guide |  |  |  |  |

Problem: A query used a ROWID value for a table that has been packed online.

Solution: ROWID values for packed tables may be invalid and shouldn't be used.  ROWID values should be recalculated after a table has been packed online.
