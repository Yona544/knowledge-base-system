---
title: Crystal Showing Deleted Dbf Records
slug: crystal_showing_deleted_dbf_records
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_showing_deleted_dbf_records.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 99ebf237ed0f41f4dc84d63b9a275e81ce7579b5
---

# Crystal Showing Deleted Dbf Records

Showing Deleted DBF Records

Showing Deleted DBF Records

Crystal Reports

| Showing Deleted DBF Records  Crystal Reports |  |  |  |  |

The Advantage Crystal Reports Driver filters out deleted DBF records by default. To force the driver to show deleted records, add the following two lines to your ads.ini file:

 [Crystal]

 ShowDeleted=1

If specified in the [Crystal] section of the ads.ini file, the setting will be global for use by all reports. If instead you would like to add a per-alias ShowDeleted setting, the following syntax can be used (and often will already exist in your ads.ini file, as this is the format the Advantage Data Architect uses to store additional alias information):

 

 [<YourAliasName>\_info]

 ShowDeleted=yes

Note when using a per-alias ShowDeleted setting, the strings "yes" and "no" are used, as opposed to 1 and 0 which are used in the global [Crystal] section.

Note This setting is only available in Crystal version 9 and newer.
