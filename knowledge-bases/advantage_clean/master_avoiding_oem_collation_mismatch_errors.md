---
title: Master Avoiding Oem Collation Mismatch Errors
slug: master_avoiding_oem_collation_mismatch_errors
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_avoiding_oem_collation_mismatch_errors.htm
source: Advantage CHM
tags:
  - master
checksum: 25274f4fff75cf442be1cd2ab479cc78c8386aec
---

# Master Avoiding Oem Collation Mismatch Errors

Avoiding OEM Collation Mismatch Errors

Avoiding OEM Collation Mismatch Errors

Troubleshooting

| Avoiding OEM Collation Mismatch Errors  Troubleshooting |  |  |  |  |

A single Advantage application can connect to multiple Advantage Database Servers, or one or more Advantage Database Servers and the Advantage Local Server. If such an application is using ANSI or OEM collation with non-USA collation sets, care must be taken to avoid a 5092 Collation Mismatch error. To avoid such an error, make sure the same OEM collation language is selected when installing the Advantage Database Server and the Advantage clients. The OEM collation language selected during an Advantage client install will be placed in the Advantage Local Server configuration file, ADSLOCAL.CFG.

Note If your application is connecting to a single Advantage Database Server, just the Advantage Local Server, or USA OEM collation language is always being used, no Collation Mismatch errors will occur.

 

Note If you change your OEM collation language from one language to another, you need to rebuild all of your index files.
