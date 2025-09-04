---
title: Error 2110 Driver Not Capable
slug: error_2110_driver_not_capable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2110_driver_not_capable.htm
source: Advantage CHM
tags:
  - error
checksum: 18d14d18da0bff58a5a5044e1a947096d66e7c8b
---

# Error 2110 Driver Not Capable

2110 Driver not capable

2110 Driver not capable

Advantage Error Guide

| 2110 Driver not capable  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine cannot complete the request.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
