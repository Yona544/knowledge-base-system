---
title: Error 7085 Invalid Unc Server Name
slug: error_7085_invalid_unc_server_name
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7085_invalid_unc_server_name.htm
source: Advantage CHM
tags:
  - error
checksum: c6e613bbe82ee8bd5f14dfd034193924978362c4
---

# Error 7085 Invalid Unc Server Name

7085 Invalid UNC server name

7085 Invalid UNC server name

Advantage Error Guide

| 7085 Invalid UNC server name  Advantage Error Guide |  |  |  |  |

Remote Server

Problem: A UNC path passed to the server does not match the servers computer name.

Solution: This indicates an internal error. Contact Advantage [Technical Support](master_technical_support_u_s__and_canada.md).

Local Server

Problem: There was an error reading the UNC server name from the REPLACE\_UNC\_SERVER key in the ads.ini file. Either the ads.ini file could not be found or the server name specified was not found.

Solution: Verify the ads.ini file is in the search path and that an entry exists for the server used in the connection string.
