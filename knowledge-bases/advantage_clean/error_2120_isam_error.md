---
title: Error 2120 Isam Error
slug: error_2120_isam_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2120_isam_error.htm
source: Advantage CHM
tags:
  - error
checksum: c007ae12ac1bf800499417747f4d139da565e125
---

# Error 2120 Isam Error

2120 ISAM error

2120 ISAM error

Advantage Error Guide

| 2120 ISAM error  Advantage Error Guide |  |  |  |  |

Problem: Advantage SQL engine encountered an internal error.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
