---
title: Odbc Trim Trailing Spaces
slug: odbc_trim_trailing_spaces
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_trim_trailing_spaces.htm
source: Advantage CHM
tags:
  - odbc
checksum: b4e070b0748bd735e26972d85248848454a1799d
---

# Odbc Trim Trailing Spaces

Trim Trailing Spaces

Trim Trailing Spaces

| Trim Trailing Spaces |  |  |  |  |

By default, when character field data is retrieved, trailing spaces on the end of the field are returned to the application. For example, if a 20-byte character field has a value such as "xyz" with only 3 characters, it will be returned to the application with 17 spaces (0x20) on the end of the value. If the Trim Trailing Spaces option is turned on, then the trailing spaces will be removed from the value before it is returned to the application.
