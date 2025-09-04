---
title: Master Use Of Deleted Byte
slug: master_use_of_deleted_byte
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_use_of_deleted_byte.htm
source: Advantage CHM
tags:
  - master
checksum: b991b3c1ebc8ba0080fbb4e83b0c289afc4c45a6
---

# Master Use Of Deleted Byte

Use of Deleted Byte

Use of Deleted Byte

Advantage Concepts

| Use of Deleted Byte  Advantage Concepts |  |  |  |  |

Advantage TPS, as a default, uses the "deleted" byte in a DBF table record to indicate that the record has an update or insert pending within a transaction. This does not affect the deletion status of the record. If you would like to keep the "deleted" byte from being temporarily altered, a one byte character field with the name "AXS\_TPS" can be added to any DBF table being used with TPS. The AXS\_TPS field would then be used by the Advantage TPS rather than the "deleted" byte.

Note Use of the "deleted" byte and the optional "AXS\_TPS" field only applies to DBF tables. Advantage proprietary ADT tables do not have the same concept of a "deleted" byte.
