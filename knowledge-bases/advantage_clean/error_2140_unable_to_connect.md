---
title: Error 2140 Unable To Connect
slug: error_2140_unable_to_connect
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2140_unable_to_connect.htm
source: Advantage CHM
tags:
  - error
checksum: 47c2e31bb388793cd03d55f5ac5d750617c5bcae
---

# Error 2140 Unable To Connect

2140 Unable to connect

2140 Unable to connect

Advantage Error Guide

| 2140 Unable to connect  Advantage Error Guide |  |  |  |  |

Problem: Unable to connect to Advantage Database Server or Advantage Local Server

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.
