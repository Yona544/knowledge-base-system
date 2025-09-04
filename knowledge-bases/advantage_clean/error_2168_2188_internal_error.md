---
title: Error 2168 2188 Internal Error
slug: error_2168_2188_internal_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2168_2188_internal_error.htm
source: Advantage CHM
tags:
  - error
checksum: dfac0c23c1b6be9c4d0b576ad48fed11f5536fd5
---

# Error 2168 2188 Internal Error

2168 - 2188 Internal Error

2168 - 2188 Internal Error

Advantage Error Guide

| 2168 - 2188 Internal Error  Advantage Error Guide |  |  |  |  |

Problem: Internal error.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
