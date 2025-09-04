---
title: Error 7142 The Maximum Number Of Debuggees Was Exceeded
slug: error_7142_the_maximum_number_of_debuggees_was_exceeded
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7142_the_maximum_number_of_debuggees_was_exceeded.htm
source: Advantage CHM
tags:
  - error
checksum: 10aa8eb605f8edebbbe49235942d1bf182ea4de8
---

# Error 7142 The Maximum Number Of Debuggees Was Exceeded

7142 The maximum number of debuggees was exceeded

7142 The maximum number of debuggees was exceeded

Advantage Error Guide

| 7142 The maximum number of debuggees was exceeded  Advantage Error Guide |  |  |  |  |

Problem: When using the SQL DEBUG command, a connection cannot be made a debuggee because the server has reached the limit of number of concurrent debuggee connections.

Solution: When debugging an SQL script on the Advantage Database server, the maximum number of concurrent debuggees is the number of configured worker threads minus one. Increase the number of configured worker threads and restart the server to debug additional connections.
