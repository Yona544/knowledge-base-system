---
title: Error 2139 Invalid Connection String
slug: error_2139_invalid_connection_string
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2139_invalid_connection_string.htm
source: Advantage CHM
tags:
  - error
checksum: 2cf2138bc9968be64940fece8e9e3947da257b2f
---

# Error 2139 Invalid Connection String

2139 Invalid connection string

2139 Invalid connection string

Advantage Error Guide

| 2139 Invalid connection string  Advantage Error Guide |  |  |  |  |

Problem: An invalid connection string is specified.

Solution: This error indicates an internal problem in the Advantage SQL Engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
