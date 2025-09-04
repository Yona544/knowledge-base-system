---
title: Error 7158 The Server Cannot D
slug: error_7158_the_server_cannot_d
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7158_the_server_cannot_d.htm
source: Advantage CHM
tags:
  - error
checksum: 28ea82ecc73eefbfe69041a99cb44d9e904119ae
---

# Error 7158 The Server Cannot D

error 7158 The server cannot determine the default ANSI/OEM Unicode collation locale

7158 The server cannot determine the default ANSI/OEM Unicode collation locale

Advantage Error Guide

| 7158 The server cannot determine the default ANSI/OEM Unicode collation locale  Advantage Error Guide |  |  |  |  |

The likely cause for this error is that an older version (pre 10.0 release) of the adscollate.adt is loaded by the servers. When Advantage database server is loaded, it will try to determine the Unicode collation locales correspond to the servers default ANSI/OEM character sets. This is done using look up in the adscollate.adt. If the look up failed to find the corresponding Unicode collation locales, this error will be returned when the server try to sort or compare Unicode characters for tables opened with the default ANSI/OEM collation.
