---
title: Devguide Updated Crystal Report Driver
slug: devguide_updated_crystal_report_driver
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_updated_crystal_report_driver.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2a268c5beb5ccfb3573379064f84d8b161d7441d
---

# Devguide Updated Crystal Report Driver

Updated Crystal Report Driver

     Updated Crystal Report Driver

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Updated Crystal Report Driver  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage 8's Crystal Report driver can now accept a handle to the client application's connection, permitting it to use the client's connection to the server. Previously, the Crystal Report driver established its own connection to the server, incurring the overhead of connecting and disconnecting. The enhancement not only improves performance, but also permits you to generate reports based on temporary tables available on the client connection.
