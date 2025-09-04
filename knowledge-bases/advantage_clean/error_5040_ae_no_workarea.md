---
title: Error 5040 Ae No Workarea
slug: error_5040_ae_no_workarea
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5040_ae_no_workarea.htm
source: Advantage CHM
tags:
  - error
checksum: 5a4084aa1e299732d5df3fac99892f14ae3bff11
---

# Error 5040 Ae No Workarea

5040 AE\_NO\_WORKAREA

5040 AE\_NO\_WORKAREA

Advantage Error Guide

| 5040 AE\_NO\_WORKAREA  Advantage Error Guide |  |  |  |  |

This error is no longer applicable since the 6.1 release of Advantage clients. Prior to the 6.1 release, this error is returned when the maximum number of tables has been opened for this connection. The maximum number of tables open at any one time per connection prior to the 6.1 release is 255.

Try closing a table before opening another, or create another connection and open the tables on that connection.
