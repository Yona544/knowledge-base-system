---
title: Error 7111 The Temporary Table Is In Use
slug: error_7111_the_temporary_table_is_in_use
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7111_the_temporary_table_is_in_use.htm
source: Advantage CHM
tags:
  - error
checksum: aed7adfd60dbb21dceb2a6d06209ddd193a32289
---

# Error 7111 The Temporary Table Is In Use

7111 The temporary table is in use

7111 The temporary table is in use

Advantage Error Guide

| 7111 The temporary table is in use  Advantage Error Guide |  |  |  |  |

Problem: The temporary table is already in use. There are two possible causes for this error:

| a. | An attempt was made to open a temporary table as a regular table using the table path directly when the temporary table is already in use. Or |

| b. | An attempt was made to open a temporary table when the table has already been opened as a regular table using the table path directly. |

Solution: Avoid opening temporary tables as regular tables.
