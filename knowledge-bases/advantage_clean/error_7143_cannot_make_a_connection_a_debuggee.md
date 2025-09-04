---
title: Error 7143 Cannot Make A Connection A Debuggee
slug: error_7143_cannot_make_a_connection_a_debuggee
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7143_cannot_make_a_connection_a_debuggee.htm
source: Advantage CHM
tags:
  - error
checksum: 4127461bb8ab8bfa14f8738d75d434ad8e6c9dcb
---

# Error 7143 Cannot Make A Connection A Debuggee

7143 Cannot make a connection a debuggee

7143 Cannot make a connection a debuggee

Advantage Error Guide

| 7143 Cannot make a connection a debuggee  Advantage Error Guide |  |  |  |  |

Problem: When using the SQL DEBUG command, a connection cannot be made a debuggee connection because it is processing a client request.

Solution: A connection can only be made a debuggee when it is in an idle state. Wait till the client is idle to retry the command or repeat the command until successful.
