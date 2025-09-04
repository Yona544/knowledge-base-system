---
title: Error 7088 The User Could Not Be Disconnected At This Time
slug: error_7088_the_user_could_not_be_disconnected_at_this_time
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7088_the_user_could_not_be_disconnected_at_this_time.htm
source: Advantage CHM
tags:
  - error
checksum: fb9a80c627626463fe499d3f3f18751f629b8204
---

# Error 7088 The User Could Not Be Disconnected At This Time

7088 The user could not be disconnected at this time

7088 The user could not be disconnected at this time

Advantage Error Guide

| 7088 The user could not be disconnected at this time  Advantage Error Guide |  |  |  |  |

Problem: When attempting to disconnect a user from the server by performing a "kill user" management operation, a 7088 error occurs.

Solution: The "kill user" management operation failed because the server is processing a request from the user that cannot be stopped at this time. Retry the "kill user" operation at some later time when the user's current operation has completed.
