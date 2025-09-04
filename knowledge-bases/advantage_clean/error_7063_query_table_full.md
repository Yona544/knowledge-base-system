---
title: Error 7063 Query Table Full
slug: error_7063_query_table_full
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7063_query_table_full.htm
source: Advantage CHM
tags:
  - error
checksum: 25c0f45b844957b1fc20d7aac832a95c0a6aec24
---

# Error 7063 Query Table Full

7063 Query table full

7063 Query table full

Advantage Error Guide

| 7063 Query table full  Advantage Error Guide |  |  |  |  |

Problem: The maximum number of configured query elements is already in use.

Solution: The maximum number of configured query elements is the same as the configured work areas. There are two possible solutions: 1) Restart/reload the Advantage server with a larger value for number of work areas; 2) Make sure that query handles are freed after they are no longer used.
