---
title: Master Go Top Movement
slug: master_go_top_movement
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_go_top_movement.htm
source: Advantage CHM
tags:
  - master
checksum: 01550284a264ed3b0471c39e817dcfc143cd7a7a
---

# Master Go Top Movement

Go Top (First, MoveFirst)

Go Top (First, MoveFirst)

Advantage Concepts

| Go Top (First, MoveFirst)  Advantage Concepts |  |  |  |  |

Go Top will position to the first record in the table if no index files are open, no index order is active, or no index order was specified in the Go Top operation. If an index order is active or is specified, then Go Top will position to the first logical record in the index order. For example, if the index order is on "name", a Go Top will position to the record containing the first "A" name in the table.
