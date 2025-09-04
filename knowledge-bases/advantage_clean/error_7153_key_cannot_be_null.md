---
title: Error 7153 Key Cannot Be Null
slug: error_7153_key_cannot_be_null
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7153_key_cannot_be_null.htm
source: Advantage CHM
tags:
  - error
checksum: 49280e4e29ad2d28154453b3f8043c9e057c4413
---

# Error 7153 Key Cannot Be Null

7153 Key Cannot Be Null

7153 Key Cannot Be Null

Advantage Error Guide

| 7153 Key Cannot Be Null  Advantage Error Guide |  |  |  |  |

Problem: A field value was modified such that it resulted in a NULL key value, but the index does not allow NULL values. This can happen with candidate indexes created on Visual FoxPro tables.

Solution: Change the data so that it does not result in a NULL key value or cancel the update.
