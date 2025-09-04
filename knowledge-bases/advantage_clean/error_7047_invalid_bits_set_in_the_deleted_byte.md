---
title: Error 7047 Invalid Bits Set In The Deleted Byte
slug: error_7047_invalid_bits_set_in_the_deleted_byte
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7047_invalid_bits_set_in_the_deleted_byte.htm
source: Advantage CHM
tags:
  - error
checksum: 56a65e9271a3b8148753a7e0e964802eae062e4e
---

# Error 7047 Invalid Bits Set In The Deleted Byte

7047 Invalid bits set in the deleted byte

7047 Invalid bits set in the deleted byte

Advantage Error Guide

| 7047 Invalid bits set in the deleted byte  Advantage Error Guide |  |  |  |  |

Problem: The "deleted" byte, which is the first byte in a table record that is used to indicate whether the record is marked for deletion or not, has bits set that are invalid for that byte. The previous log file entry contains the record number of the record that has invalid bits in its "deleted" byte.

Solution: Clear the invalid bits in the "deleted" byte. Open the table exclusively via a non-Advantage driver. Then loop through all records in the table re-marking all records for deletion that are currently marked for deletion and recalling all records that are not currently marked for deletion.
