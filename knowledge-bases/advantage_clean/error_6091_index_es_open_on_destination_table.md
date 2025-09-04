---
title: Error 6091 Index Es Open On Destination Table
slug: error_6091_index_es_open_on_destination_table
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6091_index_es_open_on_destination_table.htm
source: Advantage CHM
tags:
  - error
checksum: 2bf6f072c06cbf45d95f3c528d6ff618cd783030
---

# Error 6091 Index Es Open On Destination Table

6091 Index(es) open on destination table

6091 Index(es) open on destination table

Advantage Error Guide

| 6091 Index(es) open on destination table  Advantage Error Guide |  |  |  |  |

Problem: A Copy To or Append From operation was attempted on the server, but index(es) are open on the destination table, so the operation was performed on the client.

Solution: Close all open indexes on the destination table before attempting the Copy To or Append From operation on the server. Then re-open the indexes when the operation is completed and re-build the indexes.
