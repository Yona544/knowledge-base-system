---
title: Error 2107 Invalid Cursor State
slug: error_2107_invalid_cursor_state
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2107_invalid_cursor_state.htm
source: Advantage CHM
tags:
  - error
checksum: 9154dc59344b338ff1fbd8e8e00ddc513684ed23
---

# Error 2107 Invalid Cursor State

2107 Invalid Cursor State

2107 Invalid Cursor State

Advantage Error Guide

| 2107 Invalid Cursor State  Advantage Error Guide |  |  |  |  |

Problem: The SQL statement handle is not in a correct state to complete the requested operation.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
