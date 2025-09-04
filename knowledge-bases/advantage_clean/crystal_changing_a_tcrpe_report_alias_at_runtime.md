---
title: Crystal Changing A Tcrpe Report Alias At Runtime
slug: crystal_changing_a_tcrpe_report_alias_at_runtime
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_changing_a_tcrpe_report_alias_at_runtime.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 60e2a2e8a5d6a7711a2159ce05128cbaacfc1bc4
---

# Crystal Changing A Tcrpe Report Alias At Runtime

Changing a TCrpe Report Alias at Runtime

Changing a TCrpe Report Alias at Runtime

Crystal Reports

| Changing a TCrpe Report Alias at Runtime  Crystal Reports |  |  |  |  |

The following code is an example of how to change the alias a report is using at run-time when using Crystals Delphi/Kylix/C++Builder TCrpe component:

// show report with alias it was designed with

crpe1.DiscardSavedData;

crpe1.show;

 

// set a different alias

crpe1.closejob;

crpe1.Connect.servername := 'worktest';

 

// show the report with the new alias

crpe1.DiscardSavedData;

crpe1.show;
