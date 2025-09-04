---
title: Error 7150 Collation Is Corrupt
slug: error_7150_collation_is_corrupt
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7150_collation_is_corrupt.htm
source: Advantage CHM
tags:
  - error
checksum: facd72f59a7986684cefaea824d16d956ae77ba8
---

# Error 7150 Collation Is Corrupt

7150 Collation Is Corrupt

7150 Collation Is Corrupt

Advantage Error Guide

| 7150 Collation Is Corrupt  Advantage Error Guide |  |  |  |  |

Problem: An attempt to load a [dynamic collation](master_collation_support.md) failed because the information in the collation repository did not contain the expected data.

Solution: When Advantage loads a dynamic collation from the repository (adscollate.adt and adscollate.adm), it verifies that the information is consistent. If it finds a problem with the collation information, it will log this error. To resolve this error, you will need to replace adscollate.adt and adscollate.adm with valid copies of the files.
