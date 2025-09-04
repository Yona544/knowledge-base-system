---
title: Error 7144 Collation Repository Not Found
slug: error_7144_collation_repository_not_found
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7144_collation_repository_not_found.htm
source: Advantage CHM
tags:
  - error
checksum: 620fe24c06309f673e497732539e85bc761f935c
---

# Error 7144 Collation Repository Not Found

7144 Collation Repository Not Found

7144 Collation Repository Not Found

Advantage Error Guide

| 7144 Collation Repository Not Found  Advantage Error Guide |  |  |  |  |

Problem: Advantage was not able to find the collation repository that stores the [dynamic collations](master_collation_support.md).

Solution: The collation repository is an ADT table named adscollate.adt with an associated memo file named adscollate.adm. It should reside in the same directory as the Advantage Database Server binary image (e.g., ads.exe, libadsd.so, etc.). When using Advantage Local Server, adscollate.adt must be found in the path (normally it would be in the same directory as the adslocal.cfg file).
