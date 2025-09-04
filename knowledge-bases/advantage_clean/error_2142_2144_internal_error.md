---
title: Error 2142 2144 Internal Error
slug: error_2142_2144_internal_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2142_2144_internal_error.htm
source: Advantage CHM
tags:
  - error
checksum: e1a4a663a5b7b97cb857ab7fcd3b636e9bee7bf5
---

# Error 2142 2144 Internal Error

2142 - 2144 Internal Error

2142 - 2144 Internal Error

Advantage Error Guide

| 2142 - 2144 Internal Error  Advantage Error Guide |  |  |  |  |

Problem: Internal error.

Solution: This error indicates an internal problem in the Advantage SQL Engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
