---
title: Error 7055 Field Size Mismatch
slug: error_7055_field_size_mismatch
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7055_field_size_mismatch.htm
source: Advantage CHM
tags:
  - error
checksum: bf7cad62b0c8ebc0f82fed6e3e901e84d7a82fb7
---

# Error 7055 Field Size Mismatch

7055 Field size mismatch

7055 Field size mismatch

Advantage Error Guide

| 7055 Field size mismatch  Advantage Error Guide |  |  |  |  |

Problem: A Copy To or Append From operation was attempted where the source table and the destination table contained numeric fields with the same name, but of different width or number of decimals.

Solution: Do not use source and destination tables that contain numeric fields with the same name but different width or decimals before attempting the Copy To or Append From operations.
