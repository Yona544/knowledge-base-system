---
title: Error 2104 Invalid Cursor Name
slug: error_2104_invalid_cursor_name
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2104_invalid_cursor_name.htm
source: Advantage CHM
tags:
  - error
checksum: 214867ef54f5e9cd22263afc7cb7b05b634c7dde
---

# Error 2104 Invalid Cursor Name

2104 Invalid cursor name

2104 Invalid cursor name

Advantage Error Guide

| 2104 Invalid cursor name  Advantage Error Guide |  |  |  |  |

Problem: An invalid cursor name is specified.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
