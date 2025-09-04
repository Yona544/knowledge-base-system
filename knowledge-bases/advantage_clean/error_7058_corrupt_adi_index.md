---
title: Error 7058 Corrupt Adi Index
slug: error_7058_corrupt_adi_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7058_corrupt_adi_index.htm
source: Advantage CHM
tags:
  - error
checksum: 941b9394a1f169a00878740f1a00b41ff5468cad
---

# Error 7058 Corrupt Adi Index

7058 Corrupt ADI index

7058 Corrupt ADI index

Advantage Error Guide

| 7058 Corrupt ADI index  Advantage Error Guide |  |  |  |  |

Problem: The current ADI index file contains corrupt or invalid data. It is possible that the index file was created with a version of Advantage Database Server greater than the version you are currently using. For example, if Advantage Database Server 7.0 or greater is used to build a full text search (FTS) index, it is not possible to open that index file with prior versions of Advantage.

Solution: Rebuild the index.
