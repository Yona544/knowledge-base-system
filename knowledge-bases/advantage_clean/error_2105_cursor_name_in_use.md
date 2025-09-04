---
title: Error 2105 Cursor Name In Use
slug: error_2105_cursor_name_in_use
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2105_cursor_name_in_use.htm
source: Advantage CHM
tags:
  - error
checksum: d89a61906f68ea911ea3c8de62d8d236b97494bf
---

# Error 2105 Cursor Name In Use

2105 Cursor name in use

2105 Cursor name in use

Advantage Error Guide

| 2105 Cursor name in use  Advantage Error Guide |  |  |  |  |

Problem: Specified cursor name is already in use.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
