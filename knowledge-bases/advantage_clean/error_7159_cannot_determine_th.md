---
title: Error 7159 Cannot Determine Th
slug: error_7159_cannot_determine_th
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7159_cannot_determine_th.htm
source: Advantage CHM
tags:
  - error
checksum: 52b8be26ff2062172be6b2755468bb06519e8494
---

# Error 7159 Cannot Determine Th

error 7159 Cannot determine the code page for the default ANSI/OEM character set

7159 Cannot determine the code page for the default ANSI/OEM character set

Advantage Error Guide

| 7159 Cannot determine the code page for the default ANSI/OEM character set  Advantage Error Guide |  |  |  |  |

The likely cause for this error is that an older version (pre 10.0 release) of the adscollate.adt is loaded by the server. When Advantage database server is loaded, it will try to determine the code pages of the servers default ANSI/OEM character sets. This is done using look up in the adscollate.adt. If the look up failed to find the corresponding code pages for the character sets, this error will be returned when a conversion between Unicode and code page characters is needed on a table opened with the default ANSI/OEM character type.
