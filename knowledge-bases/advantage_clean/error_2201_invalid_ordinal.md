---
title: Error 2201 Invalid Ordinal
slug: error_2201_invalid_ordinal
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2201_invalid_ordinal.htm
source: Advantage CHM
tags:
  - error
checksum: 13fa0668f1e36de738060f406ed2da741b2b98c1
---

# Error 2201 Invalid Ordinal

2201 Invalid Ordinal

2201 Invalid Ordinal

Advantage Error Guide

| 2201 Invalid Ordinal  Advantage Error Guide |  |  |  |  |

The SQL statement used an ordinal in the GROUP BY or ORDER BY clause but the ordinal specified does not correspond to the number of values in the SELECT clause. For example: SELECT lastname FROM Employees ORDER BY 2 -- The ordinal 2 is not valid because there is only one value in the SELECT clause.
