---
title: Error 5168 Ae Info Auto Creation Occurred
slug: error_5168_ae_info_auto_creation_occurred
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5168_ae_info_auto_creation_occurred.htm
source: Advantage CHM
tags:
  - error
checksum: 916c0420c90b4a3c7a0653cea361ad453c18c20a
---

# Error 5168 Ae Info Auto Creation Occurred

5168 AE\_INFO\_AUTO\_CREATION\_OCCURRED

5168 AE\_INFO\_AUTO\_CREATION\_OCCURRED

Advantage Error Guide

| 5168 AE\_INFO\_AUTO\_CREATION\_OCCURRED  Advantage Error Guide |  |  |  |  |

This error code is never returned to the client. It will only appear in error logs should a dictionary tables auto-creation property be set to True and the tables file and/or index files not exist and require re-creation.

Note This code serves as verification that auto-creation successfully took place. It is a sign that auto-creation is working properly and to list any files that were re-created.

 

Note This code is preceded by several "File Not Found" error codes in the error log (7041 errors). This is normal behavior.
