---
title: Master Go Bottom Movement
slug: master_go_bottom_movement
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_go_bottom_movement.htm
source: Advantage CHM
tags:
  - master
checksum: 3c60bdb4bd5d5d121539c8f08bb5040c002986e9
---

# Master Go Bottom Movement

Go Bottom (Last, MoveLast)

Go Bottom (Last, MoveLast)

Advantage Concepts

| Go Bottom (Last, MoveLast)  Advantage Concepts |  |  |  |  |

Go Bottom will position to the last record in the table if no index files are open, no index order is active, or no index order was specified in the Go Bottom operation. If an index order is active or is specified, then Go Bottom will position to the last logical record in the index order. For example, if the index order is on "name", a Go Bottom will position to the record containing the last "Z" in the table. This operation can be quite time consuming if it causes an SQL static cursor to be dynamically populated. See [Populating Static Cursors](master_populating_static_cursors.md) for details.
