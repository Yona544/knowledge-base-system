---
title: Error 2119 Internal Error
slug: error_2119_internal_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2119_internal_error.htm
source: Advantage CHM
tags:
  - error
checksum: 48c3fa0788711c540eb1938240c80c5810b3c594
---

# Error 2119 Internal Error

2119 Internal error

2119 Internal error

Advantage Error Guide

| 2119 Internal error  Advantage Error Guide |  |  |  |  |

Problem: The Advantage SQL engine encountered an internal error.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
