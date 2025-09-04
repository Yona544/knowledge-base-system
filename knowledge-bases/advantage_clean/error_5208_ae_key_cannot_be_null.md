---
title: Error 5208 Ae Key Cannot Be Null
slug: error_5208_ae_key_cannot_be_null
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5208_ae_key_cannot_be_null.htm
source: Advantage CHM
tags:
  - error
checksum: 504ee58b83be8750da809cd38b829e8a9d850e53
---

# Error 5208 Ae Key Cannot Be Null

5208 AE\_KEY\_CANNOT\_BE\_NULL

5208 AE\_KEY\_CANNOT\_BE\_NULL

Advantage Error Guide

| 5208 AE\_KEY\_CANNOT\_BE\_NULL  Advantage Error Guide |  |  |  |  |

Problem: A field value was modified such that it resulted in a NULL key value, but the index does not allow NULL values. This can happen with candidate indexes created on Visual FoxPro tables.

Solution: Change the data so that it does not result in a NULL key value or cancel the update.
