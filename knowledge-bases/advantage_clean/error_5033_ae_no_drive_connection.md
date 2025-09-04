---
title: Error 5033 Ae No Drive Connection
slug: error_5033_ae_no_drive_connection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5033_ae_no_drive_connection.htm
source: Advantage CHM
tags:
  - error
checksum: d9aa6c6e42c667dd21a7bf472ff99a21d5d041c8
---

# Error 5033 Ae No Drive Connection

5033 AE\_NO\_DRIVE\_CONNECTION

5033 AE\_NO\_DRIVE\_CONNECTION

Advantage Error Guide

| 5033 AE\_NO\_DRIVE\_CONNECTION  Advantage Error Guide |  |  |  |  |

No connected server was found for the given drive letter. This error may occur if the application's connect path to the database relies on a mapped drive letter. Verify that the workstation has the correct drive mapped to the server. For example, if the application's connect path is H:\data, verify that H:\ is mapped on the workstation. If using the Advantage Internet Server, add the appropriate drive letters to the [DRIVES] section of the ADS.INI file.
