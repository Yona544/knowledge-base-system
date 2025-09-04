---
title: Error 2108 Invalid Column Id
slug: error_2108_invalid_column_id
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2108_invalid_column_id.htm
source: Advantage CHM
tags:
  - error
checksum: c0fa953498765e0e5f1227033f730d681a6e3cb9
---

# Error 2108 Invalid Column Id

2108 Invalid column id

2108 Invalid column id

Advantage Error Guide

| 2108 Invalid column id  Advantage Error Guide |  |  |  |  |

Problem: An invalid column id is used.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
