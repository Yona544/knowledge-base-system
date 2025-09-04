---
title: Crystal Collation
slug: crystal_collation
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_collation.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 6f7d41f7ab7995604366de8a606a2d1d6618ab16
---

# Crystal Collation

Collation

Collation

Crystal Reports

| Collation  Crystal Reports |  |  |  |  |

The Collation setting can be used to specify both a Character Type and the Unicode locale in a single setting. To specify a global collation for the Advantage Crystal Reports Driver to use, add the following two lines to your ads.ini file (specifying any valid character type and Unicode locale):

 

 [Crystal]

 Collation=ansi:en\_US

If specified in the [Crystal] section of the ads.ini file, the setting will be global for use by all reports. If instead you would like to add a per-alias setting, the following syntax can be used (and often will already exist in your ads.ini file, as this is the format the Advantage Data Architect uses to store additional alias information):

 

 [<YourAliasName>\_info]

 Collation=oem:de\_DE
