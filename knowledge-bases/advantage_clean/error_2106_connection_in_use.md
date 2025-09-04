---
title: Error 2106 Connection In Use
slug: error_2106_connection_in_use
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2106_connection_in_use.htm
source: Advantage CHM
tags:
  - error
checksum: 729f834240aba53786fcf5365c1d766620bfb939
---

# Error 2106 Connection In Use

2106 Connection in use

2106 Connection in use

Advantage Error Guide

| 2106 Connection in use  Advantage Error Guide |  |  |  |  |

Problem: The connection is already in use.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
