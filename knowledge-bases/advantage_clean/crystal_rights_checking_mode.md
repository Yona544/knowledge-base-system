---
title: Crystal Rights Checking Mode
slug: crystal_rights_checking_mode
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_rights_checking_mode.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 2df7be42d4b2d73da962665de7f1070385564b28
---

# Crystal Rights Checking Mode

Rights Checking Mode

Rights Checking Mode

Crystal Reports

| Rights Checking Mode  Crystal Reports |  |  |  |  |

By default, the Advantage Crystal Reports Driver uses the ADS\_CHECKRIGHTS option for rights checking on all statements. To force the Advantage Crystal Reports Driver to use the ADS\_IGNORERIGHTS option, add the following two lines to your ads.ini file:

 [Crystal]

 RightsChecking=2 ; ADS\_CHECKRIGHTS=1 ADS\_IGNORERIGHTS=2

If specified in the [Crystal] section of the ads.ini file, the setting will be global for use by all reports. If instead you would like to add a per-alias Rights Checking Mode, the following syntax can be used (and often will already exist in your ads.ini file, as this is the format the Advantage Data Architect uses to store additional alias information):

 

 [<YourAliasName>\_info]

 SecurityMode=ignorerights

When using a per-alias Rights Checking Mode, the strings "ignorerights" and "checkrights" are used, as opposed to 1 and 2 which are used in the global [Crystal] section.

Beginning with version 10.0, the client no longer performs rights checking by default. See [Check Rights](master_check_rights.md).

 

Note By default, Crystal Reports attempts to verify table existence before it runs a report. If you change Advantage to ignore rights, and remove file system access to the tables, Crystal will return a "Table not Found" error. The report needs to be modified to disable the Crystal setting titled "Verify on First Refresh". To turn off this option, open the report and go to File->Report Options. In the options dialog, clear the option Verify on First Refresh, click OK, and save the report.
