---
title: Error 2160 2165 Internal Error
slug: error_2160_2165_internal_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2160_2165_internal_error.htm
source: Advantage CHM
tags:
  - error
checksum: 182874b96e330c722cf71de4833f0da70985d9a6
---

# Error 2160 2165 Internal Error

2160 - 2165 Internal Error

2160 - 2165 Internal Error

Advantage Error Guide

| 2160 - 2165 Internal Error  Advantage Error Guide |  |  |  |  |

Problem: Internal error.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
