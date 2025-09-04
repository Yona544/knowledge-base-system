---
title: Master Populating Static Cursors
slug: master_populating_static_cursors
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_populating_static_cursors.htm
source: Advantage CHM
tags:
  - master
checksum: 25a8acff3459938a3ec04b37e97826ece12dc507
---

# Master Populating Static Cursors

Populating Static Cursors

Populating Static Cursors

Advantage SQL Engine

| Populating Static Cursors  Advantage SQL Engine |  |  |  |  |

Static cursors have been optimized to be dynamically populated. If an application executes a SELECT statement that results in a static query and then reads through the rowset, Advantage will populate the cursor as the client requests the data. Because of this optimized dynamic population, an application will experience a delay if it makes a request that causes the Advantage SQL engine to have to fully populate the cursor. Examples include AdsGotoBottom (Last) and AdsGetRecordCount (RecordCount). These operations will cause the static cursor to be fully populated, which, if unnecessary, will take extra processing time. The use of aggregate functions or rowset ordering (ORDER BY) may also cause static cursors to be fully populated before any data can be returned.
