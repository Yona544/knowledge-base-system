---
title: Master Row Level Trigger Support
slug: master_row_level_trigger_support
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_row_level_trigger_support.htm
source: Advantage CHM
tags:
  - master
checksum: 233f1e4614cfff70f7ee56e77fa0c00e061abb04
---

# Master Row Level Trigger Support

Row Level Trigger Support

Row Level Trigger Support

Advantage Concepts

| Row Level Trigger Support  Advantage Concepts |  |  |  |  |

Advantage supports row-level triggers. Row-level triggers are fired once for each row that an update operation affects. For example, if a table contains multiple records with the deptnum field equal to 5, and the following SQL statement is executed:

DELETE FROM mytable WHERE deptnum = 5

a trigger will fire once for each row that is affected by the DELETE operation (each row in which deptnum is equal to 5).
