---
title: Error 7157 Maximum Number Of Active
slug: error_7157_maximum_number_of_active_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7157_maximum_number_of_active_.htm
source: Advantage CHM
tags:
  - error
checksum: 554fc4243fb41b6344bfef08821078eadc680cdf
---

# Error 7157 Maximum Number Of Active

7157 Maximum number of active Unicode collators for a connection have been exceeded.

7157 Maximum number of active Unicode collators for a connection have been exceeded

Advantage Error Guide

| 7157 Maximum number of active Unicode collators for a connection have been exceeded  Advantage Error Guide |  |  |  |  |

Each connection in Advantage server is allowed to use 128 distinct Unicode collation locales. For example, if two index files with en\_US collation locale and three index files with de\_DE collation locale are opened on a connection, then the connection is using two distinct Unicode collation locale. The opened Unicode collators are cached on the connection until the connection is closed. If the connection already has 128 Unicode collators active, then it will not be able to use index files built with Unicode locale that is not the same as one of the already opened collators.
