---
title: Crystal Server Type
slug: crystal_server_type
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_server_type.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 4c7029e29cf5b41b19e3c5c19e5fb8b717b6cf0b
---

# Crystal Server Type

Server Type

Server Type

Crystal Reports

| Server Type  Crystal Reports |  |  |  |  |

The Advantage Crystal Reports driver uses remote server connections by default. If you try to use the driver and you do not have the Advantage Database Server installed, you will get 6060 or 6024 errors when trying to connect to your database.

To change the default server type, specify an ADS\_SERVER\_TYPE value in the "settings" section of the ads.ini file.

For example, to set the server type to local server, you would modify your ads.ini file to include the following:

[SETTINGS]

ADS\_SERVER\_TYPE = 1

See [ads.ini File Support](master_ads_ini_file_support.md) for details on ads.ini settings and valid values for the ADS\_SERVER\_TYPE setting.
