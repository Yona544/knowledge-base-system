---
title: Crystal Report Distribution
slug: crystal_report_distribution
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_report_distribution.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 1dc7f4ad309d91f3d175e6b7b6173d9c3583c003
---

# Crystal Report Distribution

Report Distribution

Report Distribution

Crystal Reports

| Report Distribution  Crystal Reports |  |  |  |  |

The following Advantage-specific files must be included in your report distribution for all versions of Crystal Reports:

- ads.ini - this is the most important file to note, as Crystal will not detect this file as being necessary for the report, so you must manually add this file to your distribution.

- ace32.dll

- axcws32.dll (if using Advantage Database Server)

- adsloc32.dll (if using Advantage Local Server)

- adslocal.cfg (if using Advantage Local Server)

- adscollate.adt, adscollate.adm (if using a [dynamic collation](master_collation_support.md) with Advantage Local Server).

For Crystal Reports version 6, 7, or 8, the following Advantage-specific files must be included in your report distribution:

- p2sads.dll - Advantage Crystal Reports Driver

For Crystal Reports version 9 or newer, the following Advantage-specific files must be included in your report distribution:

- crdb\_ads.dll - Advantage Crystal Reports Driver

- crdb\_p2sads.dll - Only necessary if shipping reports that were first created with versions of Crystal Reports prior to version 9.

Note These files must be placed in the application folder or in the search path.
