---
title: Error 6633 The Advantage Database Server Did Not Respond To A Database Request In A Timely Manner
slug: error_6633_the_advantage_database_server_did_not_respond_to_a_database_request_in_a_timely_manner
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6633_the_advantage_database_server_did_not_respond_to_a_database_request_in_a_timely_manner.htm
source: Advantage CHM
tags:
  - error
checksum: 4931aef05ef0110b86640ea74a22ad42553d427c
---

# Error 6633 The Advantage Database Server Did Not Respond To A Database Request In A Timely Manner

6633 The Advantage Database Server did not respond to a database request in a timely manner

6633 The Advantage Database Server did not respond to a database request in a timely manner

Advantage Error Guide

| 6633 The Advantage Database Server did not respond to a database request in a timely manner  Advantage Error Guide |  |  |  |  |

Problem: This error will occur if the server does not respond to the client while using inter-process communications when the client and server processes are on the same physical workstation.

Solution: Verify that Advantage Database Server is still running. If it is running, then check the [MAX\_TIMEOUTS](master_ads_ini_file_support.md) value in the ads.ini file. If that value is very small and the server is extremely busy, it is possible that the server might not be able to respond in the timeout period. Increase the value (or remove it from the ads.ini file so that the default value will be used).
