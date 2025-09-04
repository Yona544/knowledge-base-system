---
title: Error 7181 Stateful Connection
slug: error_7181_stateful_connection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7181_stateful_connection.htm
source: Advantage CHM
tags:
  - error
checksum: 8ec4de3cdf9a08a1d0a638d5263eaae5089bae4f
---

# Error 7181 Stateful Connection

7181 Maximum Number of Connected (Stateful) Users Exceeded

7181 Maximum Number of Connected (Stateful) Users Exceeded

Advantage Error Guide

| 7181 Maximum Number of Connected (Stateful) Users Exceeded  Advantage Error Guide |  |  |  |  |

Problem: The maximum configured number of connected (stateful) users has been exceeded.

Solution: The Advantage user count can be allocated between stateful connections (e.g., those consumed by a Delphi application) and stateless connections (e.g., those used by the Advantage Web Platform) . The [WEB\_PLATFORM\_USERS](master_web_platform_users_para.md) configuration parameter can be used to specify the [maximum number of web platform users](master_web_platform_users.md). Reducing that value will allow for more concurrent stateful connections.
