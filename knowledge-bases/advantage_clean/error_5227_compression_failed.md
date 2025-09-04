---
title: Error 5227 Compression Failed
slug: error_5227_compression_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5227_compression_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 2f829cadb4c2e81d3c092ed78b8b9ab9d8027000
---

# Error 5227 Compression Failed

5227 Compression Failed

5227 Compression Failed

Advantage Error Guide

| 5227 Compression Failed  Advantage Error Guide |  |  |  |  |

Problem: Error was encountered when compression or decompressing data.

Solution: The likely cause for this problem is attempting to updated a compressible blob field in chunks. Unlike regular blob field, compressed blob field can only be updated in whole. Other cause for this error is corrupted memo file.
